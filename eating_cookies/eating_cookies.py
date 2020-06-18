'''
Input: an integer
Returns: an integer
'''
# Assumptions:
# Good candidate for recursion


def eating_cookies(n, cache=None):
    # Use recursion a la fibonacci
    # Set base cases
    # Set up cache for larg inputs

    # base cases:
    if n < 0:
        # negative numbers means we didnt find one of the ways
        return 0
    if n == 0:
        # getting to 0 means we found a way to eat our cookies
        return 1

    # if cache is None
        # create the cache
    if cache is None:
        cache = {}
    # check if cache exists
    # check if n is in cache
        # return cache[n]
    if cache and cache[n]:
        return cache[n]

    cache[n] = eating_cookies(
        n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
