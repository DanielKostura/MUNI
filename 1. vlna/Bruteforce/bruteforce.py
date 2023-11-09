from hashlib import sha256

abeceda = ["a", "b", "c", "d","e" ,"f" ,"g" ,"h" ,"i" ,"j" ,"k","l" ,"m" ,"n" ,"o", "p" ,"q" ,"r" ,"s" ,"t" ,"u","v" ,"w","x","y" ,"z"]

def key_cracking(hashed: str) -> str:
    for i in range(len(abeceda)):
        for j in range(len(abeceda)):
            for k in range(len(abeceda)):
                for l in range(len(abeceda)):
                    slovo = abeceda[i] + abeceda[j] + abeceda[k] + abeceda[l]
                    if sha256( slovo.encode() ).hexdigest() == hashed:
                        return slovo


# Verejné testy:
print(key_cracking("a746222f09d85605c52d4e636788d6ffdc274698b98b8c5f3244c06958683a69"))  # snow
print(key_cracking("e6ad06ca7b0a33fbb0ea8d52e482eacca927a5735101bd2a0712d2f230233089"))  # iglu
