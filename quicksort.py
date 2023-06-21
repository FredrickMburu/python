import time
import random

start_time = time.time()

def quicksort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quicksort(items_lower) + [pivot] + quicksort(items_greater)

# Adjust the size of the array
array_size = 10000

# Generate an array with random elements
my_array = [random.randint(1, 100) for _ in range(array_size)]

print("Original array:", my_array)
sorted_array = quicksort(my_array)
print("Sorted array:", sorted_array)

end_time = time.time()
elapsed_time = end_time - start_time
print("Time taken:", elapsed_time, "seconds")
