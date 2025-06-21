import csv
import string


def load_teencode_dict(path):
    with open(path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return {row["Teencode"]: row["Meaning"] for row in reader}


def normalize_teencode(text, teencode_dict):
    words = text.split()
    converted_words = []
    for word in words:
        core = word.strip(string.punctuation)
        if core in teencode_dict:
            new_word = word.replace(core, teencode_dict[core]).replace(" ", "_")
            converted_words.append(new_word)
        else:
            converted_words.append(word)
    return " ".join(converted_words)
