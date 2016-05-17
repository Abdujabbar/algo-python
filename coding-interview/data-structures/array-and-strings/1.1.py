

def is_unique_chars(str):
    ll = len(str)
    _dict = dict()
    for i in range(ll):
        if str[i] in _dict.keys():
            return False
        _dict[str[i]] = True

    return True

s = list(input())

print(is_unique_chars(s))


