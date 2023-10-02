#!/usr/bin/python3

def list_intersection_3(l1, l2, l3):
    array = []
    for word in l1:
        if word in l2 and word in l3:
            array.append(word)

    return array


# ukázka zavolání funkce

def main():
    animals = ['kočka', 'pes']
    rhyme = ['pes', 'les', 'mez', 'ves', 'dnes']
    song = ['skákal', 'pes', 'přes', 'oves']

    for spy in list_intersection_3(animals, rhyme, song):
        print(spy)

if __name__ == '__main__':
    main()