""" http://informatics.mccme.ru/mod/statements/view3.php?id=276&chapterid=253#1 """
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


year = int(input())

if is_leap(year):
    print("YES")
else:
    print("NO")


