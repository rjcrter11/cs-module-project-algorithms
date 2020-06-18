'''
Input: a List of integers
Returns: a List of integers
'''
# Assumptions:
# Order of non zero integers doesn't matter
# Array contains at least one 0 and one non zero integer


# def moving_zeroes(arr):
#     # init two empty lists to hold 0's and non zero ints
#     nons = []
#     zeros = []
#     # for loop to check if value is zero or non zero
#     for item in arr:
#         if item == 0:
#             zeros.append(item)
#         else:
#             nons.append(item)
#     # concat lists, w/ non zero list first
#     arr = nons + zeros
#     # return concatenated list
#     return arr


'''
what if we had a pointer at the beginning and one at the end
and they moved towards eachother in the middle?

if the left pointer sees a zero and right pointer sees a 
non zero, swap

if the left sees a non zero increment
if the right sees a zero increment
'''


def moving_zeroes(arr):
    # left pointer at the beginning
    # right pointer at the end
    left = 0
    right = len(arr)-1
    # loop until left and right pointers meet or right pointer passes the left pointer
    # right pointer is less than left pointer
    while left <= right:
        # swap situation
        # left sees zero and right sees non zero
        # swap the items
        # increment left
        # decrement right
        if arr[left] == 0:
            arr[left], arr[left+1] = arr[left+1], arr[left]
            left += 1
        else:
            left += 1
        if arr[right] != 0:
            arr[right - 1], arr[right] = arr[right], arr[right-1]
            right -= 1
        else:
            right -= 1
        # non swap situation
            # if left sees non zero
            # increment left
            # if right sees zero
            # decrement right

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    # Simplest case:
    #arr = [0, 3]
    # =======
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
    #print(f"The resulting of moving_zeroes is: {moving_zeroes_optimized(arr)}")
