import numpy as np

# Túto funkciu implementujte
def rm_edge(ft_arr: np.ndarray, n: int):
    for i in range(n):
        for j in range(i, len(ft_arr)-i):
            ft_arr[j, i] = 0 # vlavo
            ft_arr[j, len(ft_arr[0])-i-1] = 0 # vpravo

        for j in range(i, len(ft_arr[0])-i):
            ft_arr[i, j] = 0 # hore
            ft_arr[len(ft_arr)-i-1, j] = 0 #dole
            
    
    pix = 0 
    for i in range(len(ft_arr)):
        for j in range(len(ft_arr[i])):
            if ft_arr[i, j] == 0:
                pix += 1

    return ft_arr

# Testy:
arr = np.array([[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]])

print(rm_edge(arr, 1))

print()
arr = np.array([[1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1]])

print(rm_edge(arr, 1))

print()
arr = np.array([[1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1]])

print(rm_edge(arr, 1))