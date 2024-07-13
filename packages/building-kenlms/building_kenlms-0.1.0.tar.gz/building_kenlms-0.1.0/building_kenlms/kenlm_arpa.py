# based on: https://github.com/mozilla/DeepSpeech/blob/master/data/lm/generate_lm.py

import os
import shutil
import subprocess  # noqa: S404
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Annotated

from beartype.vale import Is
from buildable_dataclasses.hashcached_data.hashcached_data import HashCachedData
from misc_python_utils.beartypes import NeStr
from misc_python_utils.file_utils.readwrite_files import read_lines
from misc_python_utils.prefix_suffix import PrefixSuffix
from misc_python_utils.slugification import CasedNameSlug

from building_kenlms.word_based_text_corpus import WordBasedLMCorpus


@dataclass(kw_only=True)
class ArpaArgs:
    order: int = 3
    max_memory: str = "80%"
    prune: str = "0|8|9"
    kenlm_bin: str = "/opt/kenlm/bin"
    vocab_size: int | None = None


arpa_suffixes = [".arpa.gz", ".arpa", ".gz"]  # TODO: WTF! who calls a arpa "lm.gz"?
ArpaFile = Annotated[
    str,
    Is[lambda s: any(s.endswith(suffix) for suffix in arpa_suffixes)],
]


@dataclass(kw_only=True)
class GotArpaFile:
    name: NeStr
    arpa_filepath: ArpaFile = field(init=False)


@dataclass(kw_only=True)
class AnArpaFile(GotArpaFile):
    arpa_filepath: ArpaFile = field(init=True)
    name: NeStr = field(init=False)

    def __post_init__(self) -> None:
        self.name = Path(self.arpa_filepath).name


@dataclass(kw_only=True)
class ArpaBuilder(HashCachedData, GotArpaFile):
    arpa_args: ArpaArgs
    corpus: WordBasedLMCorpus
    cache_base: (
        PrefixSuffix  # = field(default_factory=lambda: BASE_PATHES["lm_models"])
    )

    name: CasedNameSlug = field(init=False)

    def __post_init__(self):
        self.name = f"arpa-{self.corpus.name}"

    @property
    def arpa_filepath(self) -> str:
        return f"{self.cache_dir}/lm.arpa"

    def _build_cache(self) -> None:
        corpus_file, word_counts_file = (
            self.corpus.corpus_filepath,
            self.corpus.word_counts_filepath,
        )
        vocab_str = "\n".join(
            l.split("\t")[0]
            for l in read_lines(word_counts_file, limit=self.arpa_args.vocab_size)
        )

        build_kenlm_arpa(
            self.arpa_args,
            str(self.cache_dir),
            self.arpa_filepath,
            corpus_file,
            vocab_str,
        )
        assert Path(self.arpa_filepath).is_file(), f"could build {self.arpa_filepath=}"


def build_kenlm_arpa(
    args: ArpaArgs,
    output_dir: str,
    arpa_file: str,
    text_file: str,
    vocab_str: str | None = None,
) -> None:
    print("\nCreating ARPA file ...")  # noqa: T201
    os.makedirs(output_dir, exist_ok=True)  # noqa: PTH103
    subargs = [
        os.path.join(args.kenlm_bin, "lmplz"),  # noqa: PTH118
        "--order",
        str(args.order),
        "--temp_prefix",
        output_dir,
        "--memory",
        args.max_memory,
        "--text",
        text_file,
        "--arpa",
        arpa_file,
        "--prune",
        *args.prune.split("|"),
        "--skip_symbols",
        "--discount_fallback",
    ]
    subprocess.check_call(subargs, stdout=sys.stdout, stderr=sys.stdout)  # noqa: S603

    if vocab_str is not None:
        # Filter LM using vocabulary of top-k words
        print("\nFiltering ARPA file using vocabulary of top-k words ...")  # noqa: T201
        arpa_file_unfiltered = f"{output_dir}/lm_unfiltered.arpa"
        shutil.copy(arpa_file, arpa_file_unfiltered)

        subprocess.run(  # noqa: S603
            [  # noqa: S603
                os.path.join(args.kenlm_bin, "filter"),  # noqa: PTH118
                "single",
                f"model:{arpa_file_unfiltered}",
                arpa_file,
            ],
            input=vocab_str.encode("utf-8"),
            check=True,
        )
