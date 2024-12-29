def wears_jacket_with_if(temp, raining):
    """
    Check wheter Jack will wear the jacket

    temp -- current temperature
    raining -- True if it's raining and False otherwise

    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    return raining or temp < 60