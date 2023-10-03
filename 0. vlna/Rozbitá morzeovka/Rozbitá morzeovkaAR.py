import string

translation_dict = dict([('a', '.-'), ('b', '-...'), ('c', '-.-.'), ('d', '-..'), ('e', '.'), ('f', '..-.'), ('g', '--.'), ('h', '....'), ('i', '..'), ('j', '.---'), ('k', '-.-'), ('l', '.-..'), ('m', '--'), ('n', '-.'), ('o', '---'), ('p', '.--.'), ('q', '--.-'), ('r', '.-.'), ('s', '...'), ('t', '-'), ('u', '..-'), ('v', '...-'), ('w', '.--'), ('x', '-..-'), ('y', '-.--'), ('z', '--..'), (' ', ''), ('/', '-..-.'), ('-', '-....-'), ('.', '.-.-.-'), (',', '--..--'), (' ', ''), ("1", ".----"), ("2", "..---"), ("3", "...--"), ("4", "....-"), ("5", "....."), ("6", "-...."), ("7", "--..."), ("8", "---.."), ("9", "----."), ("0", "-----")])

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
    morse_text += "//"
    return morse_text

def decode(morse_text: str) -> str:
    morse_array = morse_text.split("/")
    plain_text = ""
    for i in range(len(morse_array)):
        current_element = morse_array[i]
        if len(current_element) == 0:
            plain_text += " "
        else:
            plain_text += morse[current_element]
    plain_text = plain_text[:-3]
    return plain_text

assert decode(encode(string.ascii_lowercase)).strip() == string.ascii_lowercase, "[!] Error on basic alphabet translation"
test_strings = ["", "karlik jede na dovolenou", "ready player one", "xkcd.com/1700", "xkcd.com/1739", "xkcd.com/323", "xkcd.com/376", "www.boredpanda.com/i-make-dark-and-amusing-comics-about-my-life-to-express-myself-14", "its not a bug, its a feature", "never gonna give you up, never gonna let you down, never gonna run around and desert you, never gonna make you cry, never gonna say goodbye, never gonna tell a lie and hurt you"]
for x in test_strings:
    assert decode(encode(x)).strip() == x, "[!] Error on test string " + x
    print("[~]", decode(encode(x)))