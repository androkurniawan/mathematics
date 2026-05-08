def quick_sort(list_to_sort):
    if len(list_to_sort) <= 1:
        return list_to_sort
    
    lower = []
    higher = []
    
    pivot = list_to_sort.pop(0)
    equal = [pivot]
    
    for item in list_to_sort:
        if item < pivot:
            lower.append(item)
        elif item > pivot:
            higher.append(item)
        else:
            equal.append(item)
    
    return quick_sort(lower) + equal + quick_sort(higher)


# Contoh penggunaan
data = [3, 6, 8, 10, 1, 2, 1]
print(quick_sort(data))  # Output: [1, 1, 2, 3, 6, 8, 10]