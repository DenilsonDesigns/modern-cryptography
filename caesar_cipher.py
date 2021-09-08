def generate_key(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    cnt = 0
    for char in letters:
        key[char] = letters[(cnt + n) % len(letters)]
        cnt += 1
    return key


def get_descryption_key(key):
    dkey = {}
    for c in key:
        dkey[key[c]] = c
    return dkey


def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher


# This is done by your enemy:
key = generate_key(3)
print(key)
message = "YOU ARE AWESOME"
cipher = encrypt(key, message)

# This is us breaking the cipher:
# print(cipher)
for i in range(26):
    dkey = generate_key(i)
    message = encrypt(dkey, cipher)
    print(26-i, message)
