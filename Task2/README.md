# Task2
Создайте алгоритм сортировки массива, который не указан в лекции и опишите его блок-схемой. 
Затем создайте его на python и сравните скорость сортировки этого алгоритма и сортировки пузырьком.
Сравнивайте на массиве размером в 1 000 000 элементов. 

# Solution
## Быстрая сортировка (Quick Sort)
В среднем имеет сложность O(n log n).
![block_diagram](https://github.com/user-attachments/assets/9e3ce3b3-e43e-49eb-b2cb-150a71b3fc1f)

### Сравнение времени сортировки на массиве размером в 1 000 000 элементов:
- *Время быстрой сортировки:* 0.5223546028137207 секунд
- *Время сортировки пузырьком:* 29 часов 33 минуты (расчетное)

Для тестирования сортировки пузырьком на больших массивах добавлен прогресс сортировки.
```python
import random
import time

# Реализация быстрой сортировки
def quick_sort(arr):
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr[len(arr) // 2]  # Выбор среднего элемента в качестве опорного
		less = [x for x in arr if x < pivot] # Элементы, меньше опорного
		equal = [x for x in arr if x == pivot] # Элементы, равные опорному
		greater = [x for x in arr if x > pivot] # Элементы, больше опорного
		return quick_sort(less) + equal + quick_sort(greater)
		
# Реализация сортировки пузырьком
def bubble_sort(arr):
	n = len(arr)
	start_time = time.time()  # Начало замера времени
	for i in range(n):  # Проходим по всему массиву
		# Вычисляем процент завершения
		progress = (i / (n - 1)) * 100
		elapsed_time = time.time() - start_time  # Время, прошедшее с начала
		print(f"Прогресс: {progress:.2f}%, Время: {elapsed_time:.2f} секунд", end='\r')
		for j in range(0, n-i-1):  # Проходим по массиву до последнего неотсортированного элемента
			if arr[j] > arr[j+1]:
				# Если текущий элемент больше следующего, меняем их местами
				arr[j], arr[j+1] = arr[j+1], arr[j]
	print(f"Прогресс: 100.00%, Время: {elapsed_time:.2f} секунд")  # Завершаем вывод прогресса
	return arr

# Генерация случайного массива из 1 000 000 элементов
array = [random.randint(0, 100) for _ in range(1000000)]

# Сортировка и замер времени для быстрой сортировки
start_time = time.time()
quick_sorted_array = quick_sort(array)
quick_sort_time = time.time() - start_time
print(f"Время быстрой сортировки: {quick_sort_time} секунд")

# Сортировка и замер времени для сортировки пузырьком
start_time = time.time()
bubble_sorted_array = bubble_sort(array)
bubble_sort_time = time.time() - start_time
print(f"Время сортировки пузырьком: {bubble_sort_time} секунд")
```
