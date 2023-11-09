from hashlib import sha256

def increment(key: str) -> str:
    """
    :param key: klúč
    :return: nasledujúci klúč v legikografickom poradí
    """
    key = list(key)
    for i in range(len(key) - 1, -1, -1):
        if key[i] != "z":
            key[i] = chr(ord(key[i]) + 1)
            break
        else:
            key[i] = "a"
    return "".join(key)


def key_cracking(hashed: str) -> str:
    """
    :param hash: zahashované heslo zložené z 4
    znakov malých písmen anglickej abecedy
    :return: originálne heslo
    """
    key = "a" * 4
    while sha256(key.encode()).hexdigest() != hashed:
        key = increment(key)
    return key