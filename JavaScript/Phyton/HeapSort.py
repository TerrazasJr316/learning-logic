import heapq

def heapq_sort(arr):
    heapq.heapify(arr)
    result = []
    while arr:
        result.append(heapq.heappop(arr))
    return result

arr = [60, 20, 40, 70, 30, 10]
print("Input Array: ", arr)
print("Sorted Array: ", heapq_sort(arr))