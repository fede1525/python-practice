def compute_word_frequency(text):
    words = [word.lower().strip(".,?:;!") for word in text.split()]

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    sorted_words = sorted(word_counts.items())

    for word, count in sorted_words:
        print(f"{word}: {count}")

