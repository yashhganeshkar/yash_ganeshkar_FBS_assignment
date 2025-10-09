
# Write a Python program to find the longest common prefix of all strings. Use the Python set.

def longest_common_prefix(strings):
    if not strings:
        return ""
    min_length = len(strings)
    for word in strings:
        if len(word) < min_length:
            min_length = len(word)
    for i in range(min_length):
        chars = set()
        for word in strings:
            chars.add(word[i])
        if len(chars) > 1:
            return strings[:i]
    return strings[:min_length]

li = ["flower", "flow", "flight"]

print(longest_common_prefix(li))