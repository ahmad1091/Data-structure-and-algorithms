# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.
def nullifyRow(matrix,row):
    for i in range(len(matrix)):
        matrix[raw][i] = 0

def nullifyCol(matrix,col):
    for i in range(len(matrix)):
        matrix[i][col] = 0

def setZeros(matrix List[List[]])-> List[List[]]:
    row = [False] * len(matrix)
    col = [False] * len(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = 0
                col[j] =0 
            
        for i in range(len(matrix)):
            if(row[i]= 0):
                nullifyRow(matrix, i)

        for j in range(len(matrix[0])):
            if(col[j]= 0):
                nullifyCol(matrix, j)

    return matrix

print(setZeros())