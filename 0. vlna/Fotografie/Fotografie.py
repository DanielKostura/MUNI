from typing import List


def is_face_on_photo(photo: List[List[str]]) -> bool:
    letters = ["f", "a", "c", "e"]
    for i in range(len(photo) - 1):
        for j in range(len(photo[i]) - 1):  # -1 aby to nebolo out of range
            if photo[i][j] in letters:
                array = [photo[i][j], photo[i][j+1], photo[i+1][j], photo[i+1][j+1]]
                if letters[0] in array and letters[1] in array and letters[2] in array and letters[3] in array:
                    return True
    return False

# Veřejné testy:
print(is_face_on_photo([['f', 'a'], ['c', 'e']]))  # True
print(is_face_on_photo([['f', 'a', 'c', 'e']]))  # False
print(is_face_on_photo([['e', 'c', 'x'], ['a', 'f', 'x'], ['x', 'x', 'x']]))  # True
print(is_face_on_photo([['f', 'f', 'x'], ['a', 'a', 'x'], ['x', 'x', 'x']]))  # False
