import numpy as np

# implement this
def bgr_to_cmy(bgr_image):
    pass


# test
bgr_img = np.array([[[255,255,0],[150,50,0],[96,69,180]]])
print(bgr_to_cmy(bgr_img))
# [[[255   0   0]
#   [255 205 105]
#   [ 75 186 159]]]