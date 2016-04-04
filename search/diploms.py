""" http://informatics.mccme.ru/mod/statements/view.php?id=1966 """

w, h, n = [int(x) for x in input().split()]

minSide = min(w, h)
maxSide = max(w, h) * n




while minSide < maxSide:
    m = (minSide + maxSide)//2
    j = (int(m / w)) * (int(m / h))
    if j < n:
        minSide = m + 1
    else:
        maxSide = m

print(minSide)

