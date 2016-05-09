import json
import operator


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


_input = input()
j = json.loads(_input)
_dict = dict()
for i in j:
    _dict[i['name']] = set()

for i in j:
    for item in i['parents']:
        _dict[item].add(i['name'])


__dict = sorted(_dict, key=operator.itemgetter(0))
for v in __dict:
    print(v + " : " + str(len(dfs(_dict, v))))
