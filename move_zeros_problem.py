def move_zeros(lst):
    length, counter = len(lst), 0
    while counter < len(lst):
        if lst[counter] == 0:
            lst = lst[:counter] + lst[counter+1:]
        else:
            counter += 1
    return lst + [0 for _ in range(length-counter)]

print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
print(move_zeros([])
