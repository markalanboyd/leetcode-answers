# Intuition

[View post on Leetcode](https://leetcode.com/problems/merge-strings-alternately/solutions/4263719/try-to-merge-strings-alternately/)

To merge two strings alternately, we can iterate through both strings simultaneously, appending one character from each string at a time to a new string. If one string is longer than the other, we continue iterating through the longer string until all characters are exhausted.

# Approach
The approach is straightforward:
- Determine the length of the longer string to know how many iterations are needed.
- Use a loop to iterate up to the length of the longer string.
- In each iteration, append the current character from each string to a new list if the character exists.
- Use try-except to handle the case when we go beyond the length of the shorter string.
- After the loop, join the list of characters into a string and return it.

# Complexity
- Time complexity: \(O(n)\) where \(n\) is the length of the longer string, as we iterate through both strings at most once.
- Space complexity: \(O(n)\) for the output list, where \(n\) is the combined length of both strings, which is the maximum possible size of the merged string.

# Critique
Using exceptions for control flow isn't the best approach because it's computationally expensive. Checking to see if the index of the longer word has exceeded the shorter one is better practice.

```python
for i in range(len_longest):
    if i < len(word1):
        chars_list.append(word1[i])
    if i < len(word2):
        chars_list.append(word2[i])
```

# Code
```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
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
```