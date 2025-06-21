import csv
import re


def load_phrase_normalization_dict(path):
    rules = {}
    with open(path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Phrase"] and row["Normalized"]:
                rules[row["Phrase"].strip()] = row["Normalized"].strip()
    return rules


def normalize_phrases_in_text(text, phrase_rules):
    for phrase, normalized in sorted(
        phrase_rules.items(), key=lambda x: len(x[0]), reverse=True
    ):
        text = re.sub(rf"\b{re.escape(phrase)}\b", normalized, text)
    return text
