from doctest import testmod

def nearest_low(x):
    power = 1
    low = pow(2, power)
    if x == low:
        return x
    elif low < x:
        while x > low:
            power += 1
            low = pow(2, power)
        return pow(2, power - 1)
    else:
        while low > x:
            power -= 1
            low = pow(2, power)
        return low

def nearest_high(x):
    power = 1
    high = pow(2, power)
    if x == high:
        return x
    elif high < x:
        while x > high:
            power += 1
            high = pow(2, power)
        return high
    else:
        while high > x:
            power -= 1
            high = pow(2, power)
        return pow(2, power + 1)

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

    low = nearest_low(x)
    high = nearest_high(x)
    
    if x == low:
        return x

    if abs(x - low) < abs(x - high):
        return float(low)
    else:
        return float(high)

    return power_of_two