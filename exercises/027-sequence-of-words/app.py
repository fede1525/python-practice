def sequence_of_words(words):
    words_list = words.split(",")
    sorted_words = sorted(words_list)
    output = ", ".join(sorted_words)

    return output

print(sequence_of_words("hello, world, goodbye, everyone"))
