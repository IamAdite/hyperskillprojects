A = []
r1 = [int(x) for x in input("Enter matrix size:").split(" ")]
print("Enter matrix:")
for i in range(r1[0]):
    A.append([int(x) for x in input().split(" ")])

mode = input("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
C = []
for i in range(len(A)):
    C.append([])
    for j in range(len(A[0])):
        C[i].append(0)
if mode == "1":
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[j][i] = A[i][j]

elif mode == "2":
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[-j][i] = A[i][j]

elif mode == "3":
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][-j] = A[i][j]

else:
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[-i][j] = A[i][j]

for i in range(len(C)):
    print(*C[i], sep=' ')
