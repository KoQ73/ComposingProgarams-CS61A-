def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result is None  # No return value
    True
    """
    "*** YOUR CODE HERE ***"
    k = 1
    while k < n + 1:
        check_print(k)
        k = k + 1

def check_print(k):
    if k % 3 == 0 and k % 5 == 0:
        print("fizzbuzz")
    elif k % 3 == 0:
        print("fizz")
    elif k % 5 == 0:
        print("buzz")
    else:
        print(k)
