def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    a=data[0]
    k=1
    b=len(data)
    while k<b:
        if a<data[k]:
            a=data[k]
        k=k+1
    b=data[0]
    k=1
    while k<b:
        if b>data[k]:
            b=data[k]
        k=k+1    
    return a+b
print(find_max_min_sum([1, 2, 3, 4, 5]))