def process_special_word(text, special_word=""):
    new_text = ""
    text_lst = text.split()
    i = 0
    if special_word in text_lst:
        while i <= len(text_lst) - 1:
            word = text_lst[i]
            if word == special_word:
                next_idx = i + 1
                if next_idx <= len(text_lst) - 1:
                    word = word + "_" + text_lst[next_idx]
                i = next_idx + 1
            else:
                i = i + 1
            new_text = new_text + word + " "
    else:
        new_text = text
    return new_text.strip()
