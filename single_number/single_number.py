'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


# Assumptions:
# Array will not be empty
# There is always one odd number out
# Every other number shows up exactly twice


# def single_number(arr):
#     # For loop to iterate through list
#     for item in arr:
#         # If statement to check if current item == 1 or 2
#         if arr.count(item) == 1:
#             # Return if current item == 1
#             return item


def single_number(nums):
    # keep track of times item occurs in input
    counts = {}

    for num in nums:
        # if item in counts
        if num in counts:
            # remove items
            del counts[num]
        # otherwise
        else:
            # add item
            counts[num] = 1

    for k, v in counts.items():  # O(n)
        if v == 1:
            return k


if __name__ == '__main__':
    # Use the main function to test your implementation
    # Simplest possible case:
    # arr = [1, 1, 2]
    # arr = [1, 1, 3, 2, 2]
    # =======
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
    #print(f"The odd-number-out is {single_number_optimized(arr)}")
