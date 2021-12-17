def is_prime(x):
    res = True
    count = int(x ** (1 / 2)) + 1
    if count <= 2:
        count = 3
    if x == 1 or x == 0:
        return "No"
    elif x == 2:
        return "Yes"
    else:
        for i in range(2, count):
            if x % i == 0:
                res = False
                return "No"
        if res:
            return "Yes"
number = int(input())
print (is_prime(number))
