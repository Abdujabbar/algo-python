

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

s1 = "alam"
s2 = "lama"

print(is_anagram(s1, s2))

