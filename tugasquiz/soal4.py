print ("operasi penjumlahan matriks ordo 2 x 2 ")

ordo1 = [
    [2, 4],
    [3, 1],
]

ordo2 = [
    [9, 5],
    [4, 2],
]
for x in range (0, len(ordo1)):
    for y in range (0, len(ordo1[0])):
        print (ordo1[x] [y] + ordo2[x] [y], end=' '),
    print(' ')