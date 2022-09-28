# I'm going to use Dynamic Programming

def findEvenFibSum():
    table = [0 for i in range(34)]
    table[0], table[1] = 0, 1
    for i in range(2, 34):
        table[i] = table[i-1]+table[i-2]
    sum = 0
    for fibNumber in table:
        if fibNumber % 2 == 0:
            sum += fibNumber
    return sum
print(findEvenFibSum())
