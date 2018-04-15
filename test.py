import unittest
from matrix import Matrix, WrongMatrix

# https://github.com/HEEEjoO/kol1_gr1


class test_matrix(unittest.TestCase):

	def setUp(self):
		self.matrix = Matrix(1,2,3,4)
		self.matrix2 = Matrix(1,2,3,4,5,6,7,8,9)
		self.matrix3 = Matrix(3,4,5,6)
		self.matrix0 = Matrix()


	def test_init(self):
		self.assertEqual((self.matrix0).__str__(), 'Matrix 0x0:\n\n')


	def test_add_matrixes(self):
		self.assertRaises(WrongMatrix, Matrix.__add__, self.matrix, self.matrix2)

	
	def test_add_matrixes2(self):
		self.assertEqual(Matrix(5,5,5,5).__str__(), (self.matrix + Matrix(4,3,2,1)).__str__())


	def test_radd_number(self):
		self.assertEqual(Matrix(2,3,4,5).__str__(),(self.matrix + 1).__str__())


	def test_rsub(self):
		self.assertNotEqual(Matrix(0,1,2,10),self.matrix-1)


	def test_rmul_(self):
		self.assertEqual(Matrix(9,9,21,21).__str__(), (self.matrix*3).__str__())


	def test_sub(self):
		self.assertEqual(Matrix(0,1,2,3).__str__(), (1-self.matrix).__str__())
		self.assertRaisesRegex(WrongMatrix, "Wrong matrices. Must be the same size.", Matrix.__sub__, self.matrix, self.matrix2)


	def test_mul_matrixes(self):
		self.assertEqual(Matrix(517,65,1467,153).__str__(), (self.matrix * Matrix(433,23,42,21)).__str__())


	def test_zero_matrix(self):
		self.assertIn('0',(self.matrix*0).__str__())
		

	def test_str(self):
		self.assertIsInstance(self.matrix.__str__(), str)





if __name__ == "__main__":
	unittest.main()
