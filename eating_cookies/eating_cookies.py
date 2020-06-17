'''
Input: an integer
Returns: an integer
'''
# Assumptions:
# Good candidate for recursion
#


def eating_cookies(n):
    # Use recursion a la fibonacci
    # Set base cases w/ 3 down

    # base cases:
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    # Recursion w/ 3 values
    return eating_cookies(n - 1) + eating_cookies(n-2) + eating_cookies(n-3)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 6

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
