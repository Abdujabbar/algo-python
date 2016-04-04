""" http://informatics.mccme.ru/mod/statements/view3.php?id=276&chapterid=256#1 """ 

a1 = int(input()) - 1
a2 = int(input()) - 1
b1 = int(input()) - 1
b2 = int(input()) - 1
arr = [[0 for x in range(8)] for x in range(8)] 

arr[a1][a2] = 1
arr[b1][b2] = 1
is_head = False


if a1 == b1 or a2 == b2:
    print("YES")
else:
    _diff = abs(a1 - b1) if abs(a1 - b1) > abs(a2 - b2) else abs(a2 - b2)
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


      
#print(arr)

#is_head = False

#for i in range(a1, 9):
#    for j in range(a2, 9):
#        if arr[i - 1][j - 1] == 1:
#            is_head = True

#for x in arr:
#    print(x)
	
#if is_head:
#    print("YES")
#else:
#    print("NO")
