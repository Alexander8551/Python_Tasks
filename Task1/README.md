# Task1
У вас есть 3 числа a, b, c создайте блок-схему, в которой вы проверяете, что a это положительное число, если оно положительное то вы находите максимальное число среди этих трех и возвращаете его, иначе вы возвращаете -1
Создайте функцию, для этого алгоритма. Число a должно вводится пользователем внутри функции, а b и c- аргументы функции. 

# Solution
![block_diagram](https://github.com/user-attachments/assets/ec412fac-d805-4e9f-b61e-e3289d7e0263)

```python
def find_max_or_negative_one(b, c):
    a = int(input("Введите число a: "))
    if a > 0:
        return max(a, b, c)
    else:
        return -1

result = find_max_or_negative_one(2, 3)
print(result)
```
