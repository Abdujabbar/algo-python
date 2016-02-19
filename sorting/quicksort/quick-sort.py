from random import randint
import time

def partition(a, lo, hi):
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] <= pivot:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[hi], a[i] = a[i], a[hi]
    return i


def quick_sort(a, lo, hi):
    if hi < lo:
        return
    p = partition(a, lo, hi)
    quick_sort(a, lo, p - 1)
    quick_sort(a, p + 1, hi)


def is_sorted(a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True

a = [randint(0, 10**5) for x in range(10**5)]
b = [randint(0, 10**5) for x in range(10**5)]
# print(a)
start_time = time.time()
quick_sort(a, 0, len(a) - 1)
print("--- %s seconds ---" % (time.time() - start_time))
print(is_sorted(a))
start_time = time.time()
sorted(b)
print("--- %s seconds ---" % (time.time() - start_time))
# print(a)
print(is_sorted(b))


