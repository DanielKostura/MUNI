from math import sqrt

###################################################################################
########################################ZLE########################################
###################################################################################

# Tuto funkci implementuj.
def count(data, num):
    kniznica = {}
    for i in range(len(data)):
        if data[i][num] in kniznica.keys():
            kniznica[data[i][num]] += 1
        else:
            kniznica[data[i][num]] = 1

    return kniznica

def corr_coef(data: list[tuple[float, float]]) -> float:
    n = len(data)
    kx = count(data, 0)
    ky = count(data, 1)
    
    #citatel
    ex = 0
    for key in kx.keys():
        ex += key * kx[key]/n
    ey = 0
    for key in ky.keys():
        ey += key * ky[key]/n

    cxy = 0
    for i in range(n):
        cxy += (data[i][0]-ex) * (data[i][1]-ey)
    cxy /= 4

    #menovatel
    dx = 0
    for key in kx.keys():
        dx += (key-ex)**2 * kx[key]/n
    
    dy = 0
    for key in ky.keys():
        dy += (key-ey)**2 * ky[key]/n
    
    return cxy/(sqrt(dx)*sqrt(dy))
    

# Testy:
d = [(0,0), (0,0.5), (1,0.5), (4,2)]
data1 = [
    (0, 0), (1, -1), (1, 1)
]

data2 = [
    (0, 0), (1, 1), (2, -2), (3, 3), (4, -4)
]

data3 = [
    (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
    (0, 0.5), (0, 0.5), (0, 0.5), (0, 0.5), (0, 0.5),
    (1, 0.5), (1, 0.5), (1, 0.5), (1, 0.5), (1, 0.5),
    (4, 2), (4, 2), (4, 2), (4, 2), (4, 2)
    ]

data4 = [
    (0, 0), (1, 0.5), (4, 2)
    ]


print(corr_coef(data1))  # 0.0
print(corr_coef(data2))  # -0.3511234415883917
print(corr_coef(data3))  # 0.9658242787731629
print(corr_coef(data4))  # 1.0