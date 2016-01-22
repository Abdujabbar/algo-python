from random import randint


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

a = [randint(-100, 100) for x in range(4)]
print(a)
quick_sort(a, 0, len(a) - 1)
print(a)
print(is_sorted(a))


