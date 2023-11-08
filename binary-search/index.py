import time, random

def binary_search(list, item): #? o argumento lista precisa ser uma lista ordenada de itens 
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (low + high) // 2

        if list[mid] == item:
            return mid
        elif list[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1


my_list = list(range(1, 10000001))
target = random.randint(1, 10000001)

print("Starting to search for a item using binary search")

binary_start_timer = time.time()
result = binary_search(my_list, target)
binary_end_timer = time.time()

binary_elapsed_time = binary_end_timer - binary_start_timer

print(f"Element {target} found at index {result} in {binary_elapsed_time} seconds using binary_seach()")

print("Starting to search for a item using list.index()")

index_start_timer = time.time()
result = my_list.index(target)
index_end_timer = time.time()

index_elapsed_time = index_end_timer - index_start_timer

print(f"Element {target} found at index {result} in {index_elapsed_time} seconds using list.index()")
