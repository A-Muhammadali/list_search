def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    a=data[0]
    k=1
    b=len(data)
    while k<b:
        if a>data[k] and data[k]%2==1:
            a=data[k]
        k=k+1
    return a
print(find_min_odd([12, 2, 5, 2, 7, 16, 9, 13]))

