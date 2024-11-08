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
