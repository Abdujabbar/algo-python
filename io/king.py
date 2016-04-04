

a1 = int(input()) - 1
a2 = int(input()) - 1
b1 = int(input()) - 1
b2 = int(input()) - 1

arr = [[0 for x in range(8)] for x in range(8)] 


arr[a1][a2] = 1
arr[b1][b2] = 1


if a1 + 1 == b1 or a2 + 1 == b2 or a1 - 1 == b1 or a2 - 1 == b2 or\
b1 + 1 == a1 or b2 + 1 == a2 or b1 - 1 == a1 or b2 - 1 == a2:
    print("YES")
else:
    _diff = 1
    if a1 + _diff < 8 and a2 + _diff < 8 and arr[a1 + _diff][a2 + _diff] == 1:
        print("YES")
    elif a1 + _diff < 8 and a2 - _diff >= 0 and arr[a1 + _diff][a2 - _diff] == 1:
        print("YES")
    elif a1 - _diff >= 0 and a2 + _diff < 8 and arr[a1 - _diff][a2 + _diff] == 1:
        print("YES")
    elif a1 - _diff >= 0 and a2 - _diff >= 0 and arr[a1 - _diff][a2 - _diff] == 1:
        print("YES")
    else:
        print("NO")