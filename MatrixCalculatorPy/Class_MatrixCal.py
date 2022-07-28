class MatrixCal:
    def __init__(self):
        pass

    def Add(self, A, B):
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
                self.A[i][j] *= self.const
        return A

    def MultByMatrix(self, A, B):
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
        for row in (A[:i] + A[i+1:]):
            return [row[:j] + row[j+1:]]

    def Det(self, A, total=0):
        indices = list(range(len(A)))
        if len(A) == 1 and len(A[0]) == 1:
            print(A[0][0])
        else:
            if len(A) == 2 and len(A[0]) == 2:
                val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
                return val

            for fc in indices:
                As = A.copy()
                As = As[1:]
                height = len(As)

                for i in range(height):
                    As[i] = As[i][0:fc] + As[i][fc+1:]

                sign = (-1) ** (fc % 2)
                sub_det = self.Det(As)
                total += sign * A[0][fc] * sub_det

            return total
