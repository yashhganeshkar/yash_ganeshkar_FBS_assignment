
# Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number.

def find_triplets(nums, target):
    nums.sort()
    triplets = set()

    n = len(nums)
    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == target:
                triplet = (nums[i], nums[left], nums[right])
                triplets.add(triplet)
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1

    for triplet in triplets:
        print(triplet)

    return list(triplets)

numbers = [1, 2, -1, 0, -2, 1, -1, 2]
target = 0

find_triplets(numbers, target)
