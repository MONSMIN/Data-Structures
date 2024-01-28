def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    iterations = 0
    upper_bound = arr[-1]

    while low <= high:
        mid = (low + high) // 2
        iterations += 1

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            upper_bound = arr[mid]
            high = mid - 1
        else:
            return iterations, arr[mid]

    return iterations, upper_bound


sorted_array = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
target_value = 6.5

result = binary_search(sorted_array, target_value)
print(f"Кількість ітерацій: {result[0]}")
print(f"Верхня межа: {result[1]}")
