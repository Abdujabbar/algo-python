from random import randint
import time

inv = 0

def merge_sort(a):
    if len(a) <= 1:
        return a
    m = int(len(a) / 2)
    left = a[:m]
    right = a[m:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    global inv
    result = []
    i = 0
    j = 0
    for t in range(len(left) + len(right)):
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                inv += len(left) - i
                j += 1
        elif i < len(left):
            result.append(left[i])
            i += 1
        elif j < len(right):
            result.append(right[j])
            j += 1
    return result

aa = merge_sort(a)

print(inv)