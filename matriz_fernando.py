M = [[1,2,3],
    [4,5,6],
    [7,8,9]]

H = [[9,8,7],
    [6,5,4],
    [3,2,1]]

for i in range(len(M)):
    for j in range(len( M[i] )):
        print(M[i][j] * H[i][j])