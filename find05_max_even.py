def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    a=data[0]
    k=1
    b=len(data)
    while k<b:
        if a<data[k] and data[k]%2==0:
            a=data[k]
        k=k+1
    return a
print(find_max_even([12, 2, 5, 2, 7, 16, 9, 13]))
