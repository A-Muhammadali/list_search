def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    a=1
    k=0
    b=len(data)
    while k<b:
        if data.count(data[k])>a:
            a=data.count(data[k])
        k=k+1
    return a
print(find_max_count([12, 2, 5, 2, 7, 9, 1,1,1]))