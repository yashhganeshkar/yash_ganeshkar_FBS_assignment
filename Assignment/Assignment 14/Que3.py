
# Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.

li1 = ["Yashh", "Ganeshkar", "Yashh", "Tejas", "Rajkumar", "Ganeshkar"]

words = []

for i in li1:
    words.extend(i.split())

unique_words = set(words)

for i in unique_words:
    print(f"Frequency of {i} is {words.count(i)}")