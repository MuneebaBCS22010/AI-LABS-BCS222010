# Stack Implementation using Python
stack_data = []
stack_data.append('X')
stack_data.append('Y')
stack_data.append('Z')
print("Current Stack:", stack_data)
removed = stack_data.pop()
print("Removed from stack:", removed)
removed = stack_data.pop()
print("Removed from stack:", removed)

if stack_data:
    top_item = stack_data[-1]
    print("Element at Top:", top_item)
else:
    print("Stack is Empty")

is_empty_stack = len(stack_data) == 0
print("Is stack empty?", is_empty_stack)

# Stack size
print("Stack size:", len(stack_data))


# Queue Implementation using Python
queue_data = []

queue_data.append('P')
queue_data.append('Q')
queue_data.append('R')
print("\nCurrent Queue:", queue_data)

removed_item = queue_data.pop(0)
print("Element removed from queue:", removed_item)
if queue_data:
    print("Front of queue:", queue_data[0])
else:
    print("Queue is empty")

print("Queue empty?", len(queue_data) == 0)

# Queue size
print("Queue length:", len(queue_data))


# Binary Search Algorithm
def search_binary(array, key):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == key:
            return mid
        elif array[mid] > key:
            right = mid - 1
        else:
            left = mid + 1

    return -1

# Sample sorted list and target value
numbers = [5, 11, 19, 26, 33, 47, 59, 71, 88]
search_value = 47

found_index = search_binary(numbers, search_value)

# Output the result
if found_index != -1:
    print("\nValue found at index:", found_index)
else:
    print("\nValue not present in the list.")
