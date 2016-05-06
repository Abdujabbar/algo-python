import datetime

y, m, d = [int(x) for x in input().split()]
n = int(input())

dd = datetime.date(y, m, d)
r = dd + datetime.timedelta(days=n)
print(r.year, r.month, r.day)






