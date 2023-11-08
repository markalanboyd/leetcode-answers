word1 = "abc"
word2 = "pqrasdf"


def merge_words(word1: str, word2: str) -> str:
    len_longest = max(len(word1), len(word2))
    chars_list = []

    for i in range(len_longest):
        try:
            chars_list.append(word1[i])
        except IndexError:
            pass
        try:
            chars_list.append(word2[i])
        except IndexError:
            pass

    return "".join(chars_list)


print(merge_words(word1, word2))
