def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    k = 2
    while n % k != 0 and n > 2:   
        print(k)
        k = k + 1
    return k == n