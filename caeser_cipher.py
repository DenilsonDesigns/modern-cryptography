def generate_key(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    cnt = 0
    for char in letters:
        key[char] = letters[(cnt + n) % len(letters)]
        cnt += 1
    return key


def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher


key = generate_key(3)
print(key)
message = "YOU ARE AWESOME"
cipher = encrypt(key, message)
print(cipher)
