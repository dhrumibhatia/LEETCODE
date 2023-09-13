# 1572. Matrix Diagonal Sum
mat = [ [1,2,3],
        [4,5,6],
        [7,8,9] ]


def diagonalSum(mat):
        if len(mat) == 1:
            return mat[0][0]
        else:
            n = len(mat)
            dia1 = sum(mat[i][i] for i in range(n))
            dia2 = sum(mat[i][n - 1 - i] for i in range(n))
            if len(mat) %2!=0: #to avoid odd matrix which will count mid elemnts twice
                return dia1 + dia2 - mat[int(n/2)][int(n/2)]
            return dia1 + dia2
