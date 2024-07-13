from collections import Counter
from dataclasses import dataclass
from functools import partial

from buildable_dataclasses.buildable_container import BuildableContainer
from buildable_dataclasses.hashcached_data.hashcached_data import HashCachedData
from misc_python_utils.file_utils.readwrite_files import write_lines
from misc_python_utils.prefix_suffix import PrefixSuffix
from python_text_cleaning.character_mappings.text_cleaning import TextCleaner
from tqdm import tqdm

from building_kenlms.rglob_corpus import RglobRawCorpus

TYPICAL_NUM_NGRAMS_OF_KENLM = 5


@dataclass(kw_only=True)
class WordBasedLMCorpus(HashCachedData):
    name: str
    raw_corpora: BuildableContainer[RglobRawCorpus]
    transcript_cleaner: TextCleaner
    cache_base: PrefixSuffix  # better no default here! = field(default_factory=lambda: BASE_PATHES["lm_data"])

    @property
    def corpus_filepath(self) -> str:
        return f"{self.cache_dir}/processed.txt.gz"

    @property
    def word_counts_filepath(self) -> str:
        return f"{self.cache_dir}/word_counts.txt"

    def process_line(self, l: str, counter: Counter[str]) -> str | None:
        s = self.transcript_cleaner(l)
        return spacesplit_tokenize_and_tokencounting(s, counter)

    def _build_cache(self) -> None:
        lines_g = tqdm(
            (line for corpus in self.raw_corpora for line in corpus),
            desc="raw-lines",
            position=0,
        )

        counter = Counter[str]()

        write_lines(
            self.corpus_filepath,
            tqdm(  # pyright: ignore [reportArgumentType]
                filter(
                    lambda x: x is not None,
                    map(partial(self.process_line, counter=counter), lines_g),
                ),
                desc=f"{self.name} is writing processed and filtered lines",
                position=1,
            ),
        )
        wordcounts: dict[str, int] = dict(
            sorted(counter.items(), key=lambda kv: -kv[1]),
        )
        assert len(wordcounts) > 0, f"{self.name} contains no words!"
        write_lines(
            self.word_counts_filepath,
            (f"{word}\t{count}" for word, count in wordcounts.items()),
        )


def spacesplit_tokenize_and_tokencounting(
    line: str,
    counter: Counter[str],
) -> str | None:
    text = line.replace("\n", "").replace("\r", "")
    tokens = text.split(" ")  # TODO: proper tokenization!? why space?
    if len(text) >= TYPICAL_NUM_NGRAMS_OF_KENLM:
        counter.update(tokens)
    else:
        text = None

    return text
