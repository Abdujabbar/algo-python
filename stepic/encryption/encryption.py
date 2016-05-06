import simplecrypt

with open("passwords.txt", "r") as ps:
    _passwords = ps.read()
with open("encrypted.bin", "rb") as inp:
    _input = inp.read()

for _pass in _passwords.split('\n'):
    # print(_pass)
    try:
        encrypted = simplecrypt.decrypt(_pass, _input)
        print(encrypted)
        print(_pass)
    except simplecrypt.DecryptionException:
        pass


