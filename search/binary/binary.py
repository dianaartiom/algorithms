
# difine an array of sorted elements
array = [1, 4, 5, 7, 8, 9]

# binary search
def binary_search(_list, item):
    if len(_list) == 0:
        return False
    else:
        midpoint = len(_list)//2
        if _list[midpoint] == item:
            return True
        else:
            if item < _list[midpoint]:
                return binary_search(_list[:midpoint], item)
            else:
                return binary_search(_list[midpoint+1:], item)

print(binary_search(array, 8))
print(binary_search(array, 9))
print(binary_search(array, 7))
print(binary_search(array, 5))
print(binary_search(array, 4))
print(binary_search(array, 1))
print(binary_search(array, 2))
print(binary_search(array, 87))
