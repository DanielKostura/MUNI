def encode(n: int, plain_text: str) -> str:     # vraci ciphertext typu String
    slovo = ""

    while len(plain_text) >= n:
        for i in range(n-1, -1, -1):
            slovo += plain_text[i]
        plain_text = plain_text[n:]
    for i in range(len(plain_text)-1, -1, -1):
        slovo += plain_text[i]
    return slovo

def decode(n: int, cipher_text: str) -> str:    # vraci plaintext typu String
    slovo = ""

    while len(cipher_text) >= n:
        for i in range(n-1, -1, -1):
            slovo += cipher_text[i]
        cipher_text = cipher_text[n:]
    for i in range(len(cipher_text)-1, -1, -1):
        slovo += cipher_text[i]
    return slovo


print(encode(3, "Ahoj"))    # ohAj
print(encode(2, "Ahoj"))    # hAjo
print(encode(10, "Ahoj"))   # johA
print(encode(3, "12345"))   # 32154
print(encode(5, "komunikace"))  # numokecaki
print(decode(2, "hAjo"))    # Ahoj
print(decode(5, "rgorpavomain"))    # programovani
print(decode(3, encode(3, "Karlik a Los Karlos komunikuji sifrovane"))) # Karlik a Los Karlos komunikuji sifrovane