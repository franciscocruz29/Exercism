# 1. Understand the problem

# What are the inputs?
# word: string
# candidates: list of strings

# What are the outputs?
# The anagram list is the subset of the candidate list that are anagrams of the target (in any order) - list of strings

# What are the requirements?
# Given a target word and a list of candidate words, this exercise requests the anagram list: the subset of the candidates that are anagrams of the target.

# What are the rules?
# An anagram is a rearrangement of letters to form a new word
# A word is not its own anagram
# Lowercase and uppercase characters are equivalent

# 2. Examples

# word = "diaper"
# candidates = ["hello", "world", "zombies", "pants"]
# expected = []

# word = "BANANA"
# candidates = ["BANANA"]
# expected = []

# word = "solemn"
# candidates = ["lemons", "cherry", "melons"]
# expected = ["lemons", "melons"]

# word = "nose"
# candidates = ["Eons", "ONES"]
# expected = ["Eons", "ONES"]

# word = "Orchestra"
# candidates = ["cashregister", "Carthorse", "radishes"]
# expected = ["Carthorse"]


# 3. Steps for converting input to output (Algorithm)

# 1. Define the is_anagram function:
# a. Convert both input words to lowercase.
# b. If the lowercase versions of the input words are equal, return False (words cannot be anagrams of themselves).
# c. Sort the characters in each lowercase word.
# d. Compare the sorted words. If they are equal, return True. Otherwise, return False.

# 2. Implement the find_anagrams function:
# a. Create an empty list called anagram_list to store the anagrams found.
# b. Iterate through the candidates list.
# c. For each candidate, check if it is an anagram of the target word using the is_anagram function.
# d. If it is an anagram, append the candidate to the anagram_list.
# e. After iterating through all candidates, return the anagram_list as the output.

# 4. Implementation


def is_anagram(word1: str, word2: str) -> bool:
    word1 = word1.lower()
    word2 = word2.lower()

    if word1 == word2:
        return False

    return sorted(word1) == sorted(word2)


def find_anagrams(word: str, candidates: list) -> list:
    anagram_list = []

    for candidate in candidates:
        if is_anagram(word, candidate):
            anagram_list.append(candidate)

    return anagram_list

# 5. Refactored version:

# A refactored version of the code that uses list comprehensions and simplifies the is_anagram function


def is_anagram(word1: str, word2: str) -> bool:
    lower_word1, lower_word2 = word1.lower(), word2.lower()
    return lower_word1 != lower_word2 and sorted(lower_word1) == sorted(lower_word2)


def find_anagrams(word: str, candidates: list) -> list:
    return [candidate for candidate in candidates if is_anagram(word, candidate)]
