# import sys
# import re
#
# for line in sys.stdin:
#     content = line.rstrip()
#     r = re.sub(r'([a-z])\1+', r'\1', content)
#     print(r)

#
# import requests
# import re
# from urllib.parse import urlsplit
#
# link = input()
# r = requests.get(link)
# if r.status_code == 200:
#     _links = list(set(re.findall(r'href=[\'"]?([^\'" >]+)', str(r.content))))
#     for url in _links:
#         base_url = "{0.netloc}".format(urlsplit(url))
#         print(base_url)


# url = "http://stackoverflow.com/questions/9626535/get-domain-name-from-url"
# base_url = "{0.netloc}".format(urlsplit(url))
# print(base_url)
# link = input()
# b = input()
# counter = 0
# found = False
# links = {}
#
# r = requests.get(link)
# if r.status_code == 200:
#     _links = list(set(re.findall(r'href=[\'"]?([^\'" >]+)', str(r.content))))
#     counter += 1
#     if _links:
#         for link in _links:
#             r = requests.get(link)
#             if r.status_code == 200:
#                 __links = list(set(re.findall(r'href=[\'"]?([^\'" >]+)', str(r.content))))
#                 if b in __links:
#                     found = True
#                     break
#
#
# if found:
#     print("Yes")
# else:
#     print("No")

import csv
import operator
from datetime import datetime
def validate_date(d):
    try:
        datetime.strptime(d, r'%m/%d/%Y %H:%M:%S %p')
        return True
    except ValueError:
        return False

with open("Crimes1.csv") as f:
    reader = csv.reader(f)
    c = 0
    _dict = dict()
    for line in reader:
        if c == 0:
            c += 1
            continue

        # if validate_date(line[2]) and '2015' in line[2]:

        if line[5] not in _dict.keys():
            _dict[line[5]] = 1
        else:
            _dict[line[5]] += 1
__dict = sorted(_dict.items(), key=operator.itemgetter(1), reverse=True)
print(__dict)

# import requests
# import sys
# for line in sys.stdin:
#     number = line.rstrip()
#     link = "http://numbersapi.com/" + number + "/math?json=true"
#     r = requests.get(link)
#     if r.status_code == 200:
#         res = r.json()
#         if res["found"]:
#             print("Interesting")
#         else:
#             print("Boring")
