from hashlib import sha256


def key_cracking(hashed: str) -> str:
    pole = ""
    for i in range(16):
        pole += hashed[i]
    print(pole)
    print(pole.encode())


# Verejné testy:
print(key_cracking("a746222f09d85605c52d4e636788d6ffdc274698b98b8c5f3244c06958683a69"))  # snow
print(key_cracking("e6ad06ca7b0a33fbb0ea8d52e482eacca927a5735101bd2a0712d2f230233089"))  # iglu
