def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    a=data[0]
    k=1
    b=len(data)
    while k<b:
        if a>data[k]:
            a=data[k]
        k=k+1
    return data.count(a)
print(find_min_count([12, 2, 5, 2,2, 7, 16, 9, 13]))
