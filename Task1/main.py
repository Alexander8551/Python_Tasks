def find_max_or_negative_one(b, c):
    a = int(input("Введите число a: "))
    if a > 0:
        return max(a, b, c)
    else:
        return -1

result = find_max_or_negative_one(2, 3)
print(result)
