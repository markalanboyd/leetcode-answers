str1 = "ABCDEF"
str2 = "ABC"


def find_repeating_substring(s: str) -> str:
    temp = (s + s)[1:-1]
    position = temp.find(s)
    if position != -1:
        return s[: position + 1]
    return s


def divide_strings(str1: str, str2: str) -> str:
    if set(str1) != set(str2):
        return ""
    len_str1 = len(str1)
    len_str2 = len(str2)
    longer, shorter = (str1, str2) if len_str1 > len_str2 else (str2, str1)
    if shorter in longer:
        return find_repeating_substring(shorter)
    return ""


answer = divide_strings(str1, str2)
print(answer)
