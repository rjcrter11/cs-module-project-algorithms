'''
Input: a List of integers
Returns: a List of integers
'''
# Assumptions:
# List wont be empty


def product_of_all_other_numbers(arr):
    # Loop through array, and multiply all nums
    # After, divide the product by each element to get the list
    product = 1
    for item in arr:
        product *= item

    divided_list = [product // i for i in arr]
    return divided_list


if __name__ == '__main__':
    # Use the main function to test your implementation
    # Simplest case:
    # arr = [2, 3, 4]  # expect 12, 8, 6
    arr = [1, 2, 3, 4, 5]
    #arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
