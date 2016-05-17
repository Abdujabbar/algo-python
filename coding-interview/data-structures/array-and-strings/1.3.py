
def remove_duplicates(str):
    str = list(str)
    i = 1
    tail = 1
    while i < len(str):
        j = 0
        while j < tail and str[i] != str[j]:
            j += 1
        if j == tail:
            str[tail] = str[i]
            tail += 1
        i += 1

    return str[:tail]


s = input()
print(remove_duplicates(s))
