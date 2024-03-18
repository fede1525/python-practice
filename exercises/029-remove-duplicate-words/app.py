def remove_duplicate_words(text):
    words = text.split()
    unique_words = set(words)
    sorted_words = sorted(unique_words)

    return " ".join(sorted_words)

