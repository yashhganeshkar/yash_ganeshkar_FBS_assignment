
# Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set.


def max_product_pair(numbers):
    unique_numbers = list(set(numbers))
    

    if len(unique_numbers) < 2:
        print("Not enough unique numbers to form a pair.")
        return None


    unique_numbers.sort()

    product1 = unique_numbers[-1] * unique_numbers[-2]  
    product2 = unique_numbers[0] * unique_numbers[1]    

    if product1 >= product2:
        result = (unique_numbers[-2], unique_numbers[-1])
        max_product = product1
    else:
        result = (unique_numbers[0], unique_numbers[1])
        max_product = product2

    print(f"The pair with the maximum product is: {result}")
    print(f"The maximum product is: {max_product}")
    return result, max_product


numbers = [3, 5, -10, -20, 5, 3, 8]
max_product_pair(numbers)
