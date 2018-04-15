from matrix import Matrix, WrongMatrix

matrix_2x2 = Matrix(1,2,3,4)
print (matrix_2x2)

matrix_2x2_result = matrix_2x2 + Matrix(4,3,2,1)
print (matrix_2x2_result)
matrix_2x2_result = matrix_2x2 + 1
print (matrix_2x2_result)
matrix_2x2_result = 1 + matrix_2x2
print (matrix_2x2_result)

matrix_2x2_result = matrix_2x2 - Matrix(1,2,3,4)
print (matrix_2x2_result)
matrix_2x2_result = matrix_2x2 - 1
print (matrix_2x2_result)
matrix_2x2_result = 1 - matrix_2x2
print (matrix_2x2_result)

matrix_2x2_result = matrix_2x2 * Matrix(433,23,42,21)
print (matrix_2x2_result)
matrix_2x2_result = matrix_2x2 * 3
print (matrix_2x2_result)
matrix_2x2_result = 3 * matrix_2x2
print (matrix_2x2_result)


matrix0 = Matrix()
print(matrix0)
