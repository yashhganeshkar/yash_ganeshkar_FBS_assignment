
# Write a Python program to find all the anagrams and group them
# together from a given list of strings.

from collections import defaultdict

def group_anagrams(words):
    anagram_dict = defaultdict(list)

    for word in words:
        key = ''.join(sorted(word))
        anagram_dict[key].append(word)

    grouped_anagrams = list(anagram_dict.values())

    for group in grouped_anagrams:
        print(group)

    return grouped_anagrams


words = ["listen", "silent", "enlist", "hello", "below", "elbow", "bored", "robed"]
group_anagrams(words)
