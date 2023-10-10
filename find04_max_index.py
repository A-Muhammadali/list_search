def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    a=data[0]
    k=1
    b=len(data)
    while k<b:
        if a<data[k]:
            a=data[k]
        k=k+1
    return data.index(a)
print(find_max_index([12, 2, 5, 2, 7, 9, 13]))