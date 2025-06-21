def load_stopwords(path):
    with open(path, "r", encoding="utf-8") as f:
        return set(line.strip().lower() for line in f if line.strip())


def remove_stopwords(text, stopwords):
    words = text.split()
    result = []
    i = 0
    while i < len(words):
        if i < len(words) - 1 and f"{words[i]}_{words[i+1]}" in stopwords:
            i += 2
            continue
        if words[i] not in stopwords:
            result.append(words[i])
        i += 1
    return " ".join(result)
