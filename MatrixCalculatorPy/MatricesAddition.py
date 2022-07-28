A = []
B = []
C = []
r1 = [int(x) for x in input().split(" ")]
for i in range(r1[0]):
    A.append([int(x) for x in input().split(" ")])
r2 = [int(x) for x in input().split(" ")]
for i in range(r2[0]):
    B.append([int(x) for x in input().split(" ")])
if r1[0] == r2[0] and r1[1] == r2[1]:
    for i in range(r1[0]):
        C.append([])
        for j in range(r2[1]):
            C[i].append(A[i][j] + B[i][j])
    for i in range(r1[0]):
        print(*C[i], sep=' ')
else:
    print('ERROR')
