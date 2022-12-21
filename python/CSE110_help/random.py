def make_square(tuple1):
    dict1 = {}
    for val1 in range(tuple1[0],tuple1[1]+1):
        dict1[val1] = val1**2
    return dict1

print(make_square((5,9)))