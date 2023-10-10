def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    a=data[0]
    k=1
    b=len(data)
    while k<b:
        if a<data[k]:
            a=data[k]
        k=k+1
    return a
print(find_max([12, 2, 5, 2, 7, 9, 13]))
    