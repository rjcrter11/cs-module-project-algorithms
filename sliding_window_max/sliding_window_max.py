'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):

    n = len(nums)
    # store max value in result array
    result = []
    # Nested Loop
    # Outer loop to go through start index to kth
    for i in range(n - k+1):
        max_val = nums[i]
        # Inner loop for k iterations
        for j in range(i, i + k):
            # check for values larger than max_val
            if max_val < nums[j]:
                max_val = nums[j]
        # Append those values to result array
        result.append(max_val)
    # return result array
    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    # arr = [1, 3, -1, -3, 5, 3, 6, 7]
    # k = 3
    '''
    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7      3
    1 [3  -1  -3] 5  3  6  7       3
    1  3 [-1  -3  5] 3  6  7       5
    1  3  -1 [-3  5  3] 6  7       5
    1  3  -1  -3 [5  3  6] 7       6
    1  3  -1  -3  5 [3  6  7]      7

    '''


# print(
#     f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
