import logging
from typing import List
import fast_langdetect
from lingua import LanguageDetectorBuilder
from wordfreq import word_frequency

from ..model import LangSectionType
from ..split.utils import contains_ja


all_detector = (
    LanguageDetectorBuilder.from_all_languages()
    .with_preloaded_language_models()
    .build()
)


logger = logging.getLogger(__name__)


def fast_lang_detect(text: str) -> str:
    result = str(fast_langdetect.detect(text, low_memory=False)["lang"])
    result = result.lower()
    return result


def lingua_lang_detect_all(text: str) -> str:
    language = all_detector.detect_language_of(text=text)
    if language is None:
        return "x"
    return language.iso_code_639_1.name.lower()


# For example '衬衫' cannot be detected by `langdetect`, and `fast_langdetect` will detect it as 'en'
def detect_lang_combined(text: str, lang_section_type: LangSectionType) -> str:
    if lang_section_type is LangSectionType.ZH_JA:
        if contains_ja(text):
            return "ja"
        return fast_lang_detect(text)
    return fast_lang_detect(text)


def possible_detection_list(text) -> List[str]:
    languages = []
    languages.append(fast_lang_detect(text))
    languages.append(lingua_lang_detect_all(text))
    return languages


def _detect_word_freq_in_lang(word: str, lang: str) -> float:
    return word_frequency(word=word, lang=lang)


def is_word_freq_higher_in_ja(word: str) -> bool:
    word_freq_ja = _detect_word_freq_in_lang(word=word, lang="ja")
    word_freq_zh = _detect_word_freq_in_lang(word=word, lang="zh")
    # 0.8 means either is more frequently used in Japanese or in both language the word is frequently used
    return (word_freq_ja / word_freq_zh) > 0.8
