import itertools
import json
from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path

from buildable_dataclasses.hashcached_data.hashcached_data import HashCachedData
from misc_python_utils.beartypes import NeList
from misc_python_utils.dict_utils import get_val_from_nested_dict
from misc_python_utils.file_utils.readwrite_files import read_lines, write_lines
from misc_python_utils.prefix_suffix import PrefixSuffix
from misc_python_utils.slugification import CasedNameSlug
from tqdm import tqdm


@dataclass
class RglobRawCorpus(HashCachedData):
    corpus_dir: str = "some-dir"
    file_pattern: str = "file-pattern"
    cache_base: PrefixSuffix  # better no default here = field(default_factory=lambda: BASE_PATHES["lm_data"])
    upsample_factor: int = 1
    limit: int | None = None
    name: CasedNameSlug = field(init=False)

    def __post_init__(self):
        self.name = Path(self.corpus_dir).stem

    @property
    def corpus_filepath(self) -> str:
        return f"{self.cache_dir}/raw_corpus.txt.gz"

    def get_raw_text_fun(self, line: str) -> str:  # noqa: PLR6301
        return line

    def _build_cache(self) -> None:
        counter = [0]

        def count_lines(l: str) -> str:
            counter[0] += 1  # TODO this is ugly!
            return l

        files = self._get_files()
        print(f"{self.name} found {len(files)} files: {files=}")  # noqa: T201
        lines_g = (line for file in files for line in read_lines(file))
        lines_g = (
            count_lines(self.get_raw_text_fun(line))
            for line in itertools.islice(lines_g, self.limit)
        )
        write_lines(
            self.corpus_filepath,
            tqdm(lines_g, f"{self.name} is writing lines"),
        )
        assert counter[0] > 0, f"{self.name} got zero lines!"

    def _get_files(self) -> NeList[str]:
        assert Path(self.corpus_dir).is_dir(), f"{self.corpus_dir=}"
        return [str(f) for f in Path(self.corpus_dir).rglob(self.file_pattern)]

    def __iter__(self) -> Iterator[str]:
        for _ in range(self.upsample_factor):
            yield from read_lines(self.corpus_filepath)


@dataclass
class RglobRawCorpusFromDicts(RglobRawCorpus):
    dict_path: str = "key_a.key_b.key_c"

    def get_raw_text_fun(self, line: str) -> str:
        o = get_val_from_nested_dict(json.loads(line), self.dict_path.split("."))
        assert isinstance(o, str)
        return o
