def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Последние i элементов уже отсортированы
        for j in range(0, n-i-1):
            # Если текущий элемент больше следующего, поменять их местами
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Пример использования функции
if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    print("Неотсортированный список:", unsorted_list)
    sorted_list = bubble_sort(unsorted_list)
    print("Отсортированный список:", sorted_list)
