minhaMatriz = [[1,2,3], [4,5,6], [7,8,9]]

print(minhaMatriz)

for i in range(0,3):
    print(minhaMatriz[i])

minhaMatriz[0][0] = 200
minhaMatriz[1][1] = 300
minhaMatriz[2][2] = 400

for i in range(0,3):
    print(minhaMatriz[i])