import unittest
from matrix import Matrix, WrongMatrix

# https://github.com/HEEEjoO/kol1_gr1


class test_matrix(unittest.TestCase):

	def setUp(self):
		self.matrix = Matrix(1,2,3,4)


	def test_add_matrixes(self):
		self.assertEqual(Matrix(5,5,5,5), self.matrix + Matrix(4,3,2,1))


	def test_radd_right(self):
		self.assertEqual(Matrix(2,3,4,5),self.matrix+1)

	def test_radd_left(self):
		self.assertEqual(Matrix(2,3,4,5),1+self.matrix)

	def test_rsub_right(self):
		self.assertEqual(Matrix(0,1,2,3),self.matrix-1)

	def test_rsub_left(self):
		self.assertEqual(Matrix(0,1,2,3),1-self.matrix)


	def test_rmul_right(self):
		self.assertEqual(Matrix(9,9,21,21),self.matrix*3)

	def test_rmul_left(self):
		self.assertEqual(Matrix(9,9,21,21),3*self.matrix)

	def test_sub_matrixes(self):
		self.assertEqual(Matrix(0,0,0,0), self.matrix - Matrix(1,2,3,4))

	def test_mul_matrixes(self):
		self.assertEqual(Matrix(517,65,1467,153), self.matrix * Matrix(433,23,42,21))





if __name__ == "__main__":
	unittest.main()
