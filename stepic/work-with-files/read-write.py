
with open("passwords.txt", "r") as ps:
    _lines = ps.read()

_lines = reversed(_lines.split('\n'))
target = open('output.txt', "w")
for _line in _lines:
    # print(_line)
    target.write(_line + '\n')
