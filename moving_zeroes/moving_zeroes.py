'''
Input: a List of integers
Returns: a List of integers
'''
# Assumptions:
# Order of non zero integers doesn't matter
# Array contains at least one 0 and one non zero integer


def moving_zeroes(arr):
    # init two empty lists to hold 0's and non zero ints
    nons = []
    zeros = []
    # for loop to check if value is zero or non zero
    for item in arr:
        if item == 0:
            zeros.append(item)
        else:
            nons.append(item)
    # concat lists, w/ non zero list first
    arr = nons + zeros
    # return concatenated list
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    # Simplest case:
    #arr = [0, 3]
    # =======
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
