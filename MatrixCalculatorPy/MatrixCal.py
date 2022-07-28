class MatrixCal:
    def __init__(self):
        pass

    def Add(self, A, B):
        self.A = A
        self.B = B
        C = []
        if len(A) == len(B) and len(A[1]) == len(B[1]):
            for i in range(len(A)):
                C.append([])
                for j in range(len(B[0])):
                    C[i].append(self.A[i][j] + self.B[i][j])
            return C

        else:
            print('The operation cannot be performed.')

    def MultByConst(self, A, const):
        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] *= const
        return A

    def MultByMatrix(self,A, B):
        C = []
        for i in range(len(A)):
            C.append([])
            for j in range(len(B[0])):
                C[i].append(0)
        if len(A[0]) == len(B):
            for i in range(len(A)):
                for j in range(len(B[0])):
                    for x in range(len(B)):
                        C[i][j] += A[i][x] * B[x][j]
            return C

        else:
            print("The operation cannot be performed.")

    def Transpose(self, A, mode):
        C = []
        for i in range(len(A)):
            C.append([])
            for j in range(len(A[0])):
                C[i].append(0)

        if mode == 1:
            for i in range(len(A)):
                for j in range(len(A[0])):
                    C[j][i] = A[i][j]

        elif mode == 2:
            for i in range(len(A)):
                A[i] = A[i][::-1]
            for i in range(len(A)):
                for j in range(len(A[0])):
                    C[j][i] = A[i][j]
            for i in range(len(C)):
                C[i] = C[i][::-1]

        elif mode == 3:
            for i in range(len(A)):
                C[i] = A[i][::-1]

        else:
            C = A[::-1]
        return C

    def Minor(self, A, i, j):
        return [row[:j] + row[j+1:] for row in (A[:i]+A[i+1:])]

    def Det(self, A):
        if len(A) == 1:
            return A[0][0]
        elif len(A) == 2:
            return A[0][0] * A[1][1] - A[0][1] * A[1][0]

        determinant = 0
        for c in range(len(A)):
            determinant += ((-1)**c) * A[0][c] * self.Det(self.Minor(A, 0, c))
        return determinant

    def Inverse(self, A):
        determinant = self.Det(A)
        #special case for 2x2 matrix:
        if determinant == 0:
            return 'NaN'
        if len(A) == 2:
            return [[A[1][1] / determinant, -1 * A[0][1]/determinant],
                    [-1 * A[1][0] / determinant, A[0][0] / determinant]]

        cofactors = []
        for r in range(len(A)):
            cofactorRow = []
            for c in range(len(A)):
                minor = self.Minor(A,r,c)
                cofactorRow.append(((-1)**(r+c)) * self.Det(minor))
            cofactors.append(cofactorRow)
        cofactors = self.Transpose(cofactors, 1)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c]/determinant
        return cofactors


while True:
    print('1. Add matrices \n2. Multiply matrix by a constant \n3. Multiply matrices \n4. Transpose matrix \n5. Calculate a determinant \n6. Inverse matrix \n0. Exit')
    n = input('Your choice: ')
    if n == '1':
        A = []
        B = []
        r1 = [int(x) for x in input('Enter size of first matrix: ').split(" ")]
        print('Enter first matrix:')
        for i in range(r1[0]):
            A.append([float(x) for x in input().split(" ")])
        r2 = [int(x) for x in input('Enter size of second matrix: ').split(" ")]
        print('Enter second matrix:')
        for i in range(r2[0]):
            B.append([float(x) for x in input().split(" ")])

        res = MatrixCal().Add(A, B)

        print('The result is:')
        for i in res:
            print(*i, sep=' ')

    elif n == '2':

        A = []
        r1 = [int(x) for x in input('Enter size of matrix: ').split(" ")]
        print('Enter matrix: ')
        for i in range(r1[0]):
            A.append([int(x) for x in input().split(" ")])
        Const = int(input('Enter constant: '))

        res = MatrixCal().MultByConst(A, Const)

        print('The result is:')
        for i in res:
            print(*i, sep=' ')

    elif n == '3':
        A = []
        B = []
        r1 = [int(x) for x in input('Enter size of first matrix: ').split(" ")]
        print('Enter first matrix: ')
        for i in range(r1[0]):
            A.append([float(x) for x in input().split(" ")])
        r2 = [int(x) for x in input('Enter size of second matrix: ').split(" ")]
        print('Enter second matrix: ')
        for i in range(r2[0]):
            B.append([float(x) for x in input().split(" ")])

        res = MatrixCal().MultByMatrix(A, B)

        print('The result is:')
        for i in res:
            print(*i, sep=' ')

    elif n == '4':
        print("1. Main diagonal \n2. Side diagonal \n3. Vertical line \n4. Horizontal line")
        mode = int(input("Your choice: "))

        A = []
        r1 = [int(x) for x in input("Enter matrix size:").split(" ")]
        print("Enter matrix:")
        for i in range(r1[0]):
            A.append([float(x) for x in input().split(" ")])

        res = MatrixCal().Transpose(A, mode)

        print('The result is:')
        for i in res:
            print(*i, sep=' ')

    elif n == '5':
        A = []
        r1 = [int(x) for x in input('Enter matrix size: ').split(" ")]
        print('Enter matrix: ')
        for i in range(r1[0]):
            A.append([float(x) for x in input().split(" ")])

        print('The result is:')
        print(MatrixCal().Det(A))

    elif n == '6':
        A = []
        r1 = [int(x) for x in input('Enter matrix size: ').split(" ")]
        print('Enter  matrix: ')
        for i in range(r1[0]):
            A.append([float(x) for x in input().split(" ")])

        if MatrixCal().Det(A) == 0:
            print("This matrix doesn't have an inverse.")
        else:
            res = MatrixCal().Inverse(A)
            print('The result is: ')
            for i in range(len(res)):
                for j in range(len(res[0])):
                    res[i][j] = round(res[i][j], 3)

            for i in res:
                print(*i, sep=' ')

    elif n == '7':
        A = []
        r1 = [int(x) for x in input('Enter matrix size: ').split(" ")]
        i, j = input('Enter indicies: ').split()
        i = int(i)
        j = int(j)
        print('Enter  matrix: ')
        for i in range(r1[0]):
            A.append([float(x) for x in input().split(" ")])

        res = MatrixCal().Minor(A, i, j)
        print('The result is: ')
        for i in range(len(res)):
            print(*res, sep=' ')

    elif n == '0':
        break
