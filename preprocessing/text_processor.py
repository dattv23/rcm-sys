from .cleaner import clean_text, normalize_repeated_chars
from .teencode import load_teencode_dict, normalize_teencode
from .phrase_normalization import (
    load_phrase_normalization_dict,
    normalize_phrases_in_text,
)
from .stopwords import load_stopwords, remove_stopwords
from .negation_handler import process_negations
from .special_word_handler import process_special_word
from .tokenizer import tokenize


class TextProcessor:
    def __init__(self, teencode_path, stopword_path, phrase_mapping_path):
        self.teencode_dict = load_teencode_dict(teencode_path)
        self.stopwords = load_stopwords(stopword_path)
        self.phrase_rules = load_phrase_normalization_dict(phrase_mapping_path)
        self.negation_prefixes = {"không", "chưa", "chẳng", "chớ", "chả", "đừng"}
        self.negative_indicators = {"bị", "nên", "được", "đáng", "thiếu", "mất"}

    def preprocess(self, text):
        text = clean_text(text)
        text = normalize_teencode(text, self.teencode_dict)
        text = normalize_repeated_chars(text)
        text = normalize_phrases_in_text(text, self.phrase_rules)
        text = tokenize(text)
        text = process_negations(text, self.negation_prefixes, self.negative_indicators)
        text = remove_stopwords(text, self.stopwords)
        for word in ["giao_hàng", "giao", "bao", "bọc", "bao_bọc", "đóng_gói"]:
            text = process_special_word(text, special_word=word)
        return text
