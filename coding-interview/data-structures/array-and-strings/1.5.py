
def replace_spaces(s):
    r = ''
    for i in s:
        if i == ' ':
            r += '%20'
        else:
            r += i
    return r

print(replace_spaces("hello w  o rl d"))
