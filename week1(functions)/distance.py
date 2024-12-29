from math import sqrt
from operator import add, sub, mul
from doctest import testmod

def square(n):
    return n * n

def distance(x1, y1, x2, y2):
    """Calculates the Euclidian distance between two poings (x1, y1) and (x2, y2)

    >>> distance(1, 1, 1, 2)
    1.0
    >>> distance(1, 3, 1, 1)
    2.0
    >>> distance(1, 2, 3, 4)
    2.8284271247461903
    """

    return sqrt(add(square(sub(x1, x2)),square(sub(y1, y2))))

def distance3d(x1, y1, z1, x2, y2, z2):
    """Calculates the 3D Euclidian distance between two points (x1, y1, z1) and
    (x2, y2, z2).

    >>> distance3d(1, 1, 1, 1, 2, 1)
    1.0
    >>> distance3d(2, 3, 5, 5, 8, 3)
    6.164414002968976
    """
    "*** YOUR CODE HERE ***"
    return sqrt(add(add(square(sub(x2, x1)), square(sub(y2, y1))), square(sub(z2, z1))))

def harmonic(x, y):
    """Return the harmonic mean of x and y.

    >>> harmonic(2, 6)
    3.0
    >>> harmonic(1, 1)
    1.0
    >>> harmonic(2.5, 7.5)
    3.75

    """
    "*** YOUR CODE HERE ***"
    return 2 / (1 / x + 1 / y)

def last_square(x):
    """Return the largest perfect square less than X, where X>0.

    >>> last_square(10)
    9
    >>> last_square(39)
    36
    >>> last_square(100)
    81
    >>> result = last_square(2) # Return, don't print
    >>> result
    1


    """
    "*** YOUR CODE HERE ***"
    i = 1
    while i * i < x:
        i += 1
    j = mul(i - 1, i - 1)
    return j

def checkNum(low, high):
    """Return if there are number in the interval
    >>> checkNum(0, 0)
    False
    >>> checkNum(0, 5)
    True
    """
    if low == high or low > high:
        return False
    else:
        return True

def overlaps(low0, high0, low1, high1):
    """Return whether the open intervals (LOW0, HIGH0) and (LOW1, HIGH1)
    overlap.

    >>> overlaps(10, 15, 14, 16)
    True
    >>> overlaps(10, 15, 1, 5)
    False
    >>> overlaps(10, 10, 9, 11)
    False
    >>> result = overlaps(1, 5, 0, 3)  # Return, don't print
    >>> result
    True

    >>> [overlaps(a0, b0, a1, b1) for a0, b0, a1, b1 in
    ...       ( (1, 4, 2, 3), (1, 4, 0, 2), (1, 4, 3, 5), (0.1, 0.4, 0.2, 0.3),
    ...         (2, 3, 1, 4), (0, 2, 1, 4), (3, 5, 1, 4) )].count(False)
    0
    >>> [overlaps(a0, b0, a1, b1) for a0, b0, a1, b1 in
    ...       ( (1, 4, -1, 0), (1, 4, 5, 6), (1, 4, 4, 5), (1, 4, 0, 1),
    ...         (-1, 0, 1, 4), (5, 6, 1, 4), (4, 5, 1, 4), (0, 1, 1, 4),
    ...         (5, 5, 3, 6), (5, 3, 4, 6), (5, 5, 5, 5),
    ...         (3, 6, 5, 5), (4, 6, 5, 3), (0.3, 0.6, 0.5, 0.5) )].count(True)
    0
    """
    "*** YOUR CODE HERE ***"
    # checking if there are numbers in intervals
    if not checkNum(low0, high0) or not checkNum(low1, high1):
        return False

    # checking overlap
    if high1 <= low0 or high0 <= low1:
        return False
    else:
        return True
    
    # retrun low1 < min(high0, high1) > low0

def triangular_sum(n):
    """
    >>> t_sum = triangular_sum(5)
    1
    3
    6
    10
    15
    >>> t_sum
    35
    """
    "*** YOUR CODE HERE ***"
    i = 1
    j = 0
    while i <= n:
        k = (i + 1) * i // 2
        print(k)
        j += k
        i += 1
    return j

def same_hailstone(a, b):
    """Return whether a and b are both members of the same hailstone
    sequence.

    >>> same_hailstone(10, 16) # 10, 5, 16, 8, 4, 2, 1
    True
    >>> same_hailstone(16, 10) # order doesn't matter
    True
    >>> result = same_hailstone(3, 19) # return, don't print
    >>> result
    False

    """
    "*** YOUR CODE HERE ***"
    num = min(a, b)
    num2 = max(a, b)
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        if num == num2:
            return True
    return False

def nearest_two(x):
    """Return the power of two that is nearest to x.

    >>> nearest_two(8)    # 2 * 2 * 2 is 8
    8.0
    >>> nearest_two(11.5) # 11.5 is closer to 8 than 16
    8.0
    >>> nearest_two(14)   # 14 is closer to 16 than 8
    16.0
    >>> nearest_two(2015)
    2048.0
    >>> nearest_two(.1)
    0.125
    >>> nearest_two(0.75) # Tie between 1/2 and 1
    1.0
    >>> nearest_two(1.5)  # Tie between 1 and 2
    2.0

    """
    power_of_two = 1.0
    "*** YOUR CODE HERE ***"

    low = pow(2, power_of_two)
    while low < x:
        power_of_two += 1
        low = pow(q, power_of_two)
    
    return power_of_two
    

if __name__ == "__main__":
    testmod()
