import re
import string
import emoji


def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.replace("_x000D_", " ")
    text = emoji.replace_emoji(text, replace="")
    text = re.sub(r"[:;][-~]?[)D(/\\|pP]", "", text)
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)
    text = re.sub(r"(\d+)\s+([^\d\s]+)", r"\1_\2", text)
    text = text.translate(
        str.maketrans({p: " " for p in string.punctuation if p != "_"})
    )
    return text


def normalize_repeated_chars(text):
    def remove_tail_repeat(word):
        return re.sub(r"(.)\1{1,}$", r"\1", word)

    return " ".join(remove_tail_repeat(word) for word in text.split())
