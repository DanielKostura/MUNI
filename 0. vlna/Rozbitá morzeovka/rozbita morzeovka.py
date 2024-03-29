import string

translation_dict = dict([('a', '.-'), ('b', '-...'), ('c', '-.-.'), ('d', '-..'), ('e', '.'), ('f', '..-.'), ('g', '--.'), ('h', '....'), ('i', '..'), ('j', '.---'), ('k', '-.-'), ('l', '.-..'), ('m', '--'), ('n', '-.'), ('o', '---'), ('p', '.--.'), ('q', '--.-'), ('r', '.-.'), ('s', '...'), ('t', '-'), ('u', '..-'), ('v', '...-'), ('w', '.--'), ('x', '-..-'), ('y', '-.--'), ('z', '--..'), (' ', ''), ('/', '-..-.'), ('-', '-....-'), ('.', '.-.-.-'), (',', '--..--'), ("1", ".----"), ("2", "..---"), ("3", "...--"), ("4", "....-"), ("5", "....."), ("6", "-...."), ("7", "--..."), ("8", "---.."), ("9", "----."), ("0", "-----")])

alphabet = {}
morse = {}

for key, value in translation_dict.items():
    alphabet[key] = value
    morse[value] = key

def encode(plaintext: str) -> str:
    plaintext = plaintext.lower()
    morse_text = ""
    for char in plaintext:
        morse_text += alphabet[char] + "/"

    if plaintext[-1] != " ":
        morse_text = morse_text[:-1]

    morse_text += "///"
    return morse_text

def decode(morse_text: str) -> str:
    morse_array = morse_text.split("/")
    plain_text = ""
    for i in range(len(morse_array)):
        current_element = morse_array[i]
        plain_text += morse[current_element]
    plain_text = plain_text[:-3]
    return plain_text

print(decode(encode("Najit vsechny bugy je casto problem")))
print(decode(encode("Uspet neni lehke, ale je to sladka tecka.")))
print(decode(encode("Do translation dict jsou pridany vsechny specialni znaky a cisla, ktera budete potrebovat. To stejne nerikam o malych pismenech.")))
print(encode("ab c")) # .-/-...//-.-.///

