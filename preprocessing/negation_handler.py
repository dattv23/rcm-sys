def process_negations(text, negation_prefixes, negative_indicators):
    words = text.split()
    result = []
    i = 0
    while i < len(words):
        if i + 2 < len(words) and words[i] == "không" and words[i + 1] == "có":
            result.append(f"{words[i]}_{words[i+1]}_{words[i+2]}")
            i += 3
        elif (
            i + 2 < len(words)
            and words[i] in negation_prefixes
            and words[i + 1] in negative_indicators
        ):
            result.append(f"{words[i]}_{words[i+1]}_{words[i+2]}")
            i += 3
        elif i + 1 < len(words) and words[i] in negation_prefixes:
            result.append(f"{words[i]}_{words[i+1]}")
            i += 2
        elif i + 1 < len(words) and words[i] in negative_indicators:
            result.append(f"{words[i]}_{words[i+1]}")
            i += 2
        else:
            result.append(words[i])
            i += 1
    return " ".join(result)
