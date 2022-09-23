def find_sum(number):
    sum = 0
    for i in range(0, number, 3):
        if i % 3 == 0:
            sum += i
    for j in range(0, number, 5):
        if j % 5 == 0 and not j % 3 == 0:
            sum += j
    return sum
print(find_sum(1000))
