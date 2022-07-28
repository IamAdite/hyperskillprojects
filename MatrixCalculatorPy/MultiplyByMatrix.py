A = []
B = []
C = []
r1 = [int(x) for x in input().split(" ")]
for i in range(r1[0]):
    A.append([int(x) for x in input().split(" ")])
r2 = [int(x) for x in input().split(" ")]
for i in range(r2[0]):
    B.append([int(x) for x in input().split(" ")])
for i in range(r1[0]):
    C.append([])
    for j in range(r2[1]):
        C[i].append(0)
if r1[0] == r2[1]:
    for i in range(r1[0]):
        for j in range(r2[1]):
            for x in range(r2[0]):
                C[i][j] += A[i][x] * B[x][j]
    for i in range(r1[0]):
        print(*C[i], sep=' ')
else:
    print('ERROR')
