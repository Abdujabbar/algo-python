import os
_list = os.walk('main')
_results = set()
for x in _list:
    for xx in range(1, len(x)):
        for t in x[xx]:

            if t[-3:] == '.py':
                _results.add(x[0])
                break
target = open('results.txt', 'w')
for x in sorted(_results):
    target.write(x + '\n')


