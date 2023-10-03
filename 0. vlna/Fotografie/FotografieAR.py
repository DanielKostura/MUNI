from typing import List

def is_face_on_photo(photo: List[List[str]]) -> bool:
    for i in range( len(photo) - 1 ):
        for j in range( len(photo[0]) - 1 ):
            face = ['f','a','c','e']
            if photo[i][j] in face: face.remove(photo[i][j])
            if photo[i][j + 1] in face: face.remove(photo[i][j + 1])
            if photo[i + 1][j] in face: face.remove(photo[i + 1][j])
            if photo[i + 1][j + 1] in face: face.remove(photo[i + 1][j + 1])
            
            if len(face) == 0:
                return True
    return False