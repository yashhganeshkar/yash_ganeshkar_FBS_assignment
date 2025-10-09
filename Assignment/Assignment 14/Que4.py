
# Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

li = [2, 4, 3, 5, 7, 8, -1]

target = 7

pairs = []

seen = set()

for num in li:
    complementry = target - num
    if(complementry in seen):
        pairs.append((complementry, num))
    seen.add(num)

print(pairs)