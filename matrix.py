from math import sqrt
import numbers


class WrongMatrix(Exception):
	pass

class Matrix:
	def __init__(self, *rows):
		if sqrt(len(rows)).is_integer():
			self.rows = rows
			self.dimnision = int (sqrt(len(rows)))
			self.index = [[i,self.rows[i]] for i in range(len(self.rows))]
		else:
			raise WrongMatrix('Wrong numbers. Matrix must be size NxN.')


	def __add__(self, series_of_numbrs_or_matrix):
		if isinstance(series_of_numbrs_or_matrix, numbers.Integral):
			new_matrix = [series_of_numbrs_or_matrix for i in self.rows]
			k = Matrix(*new_matrix)
			return self + k
		if series_of_numbrs_or_matrix.dimnision != self.dimnision:
			raise WrongMatrix ("Wrong matrices. Must be the same size.")	
		new_matrix = []
		for i in range(len(self.rows)):
			new_matrix.append(self.index[i][1] + series_of_numbrs_or_matrix.index[i][1])
		return Matrix(*new_matrix)

	def __radd__ (self, numbers):
		return self.__add__(numbers)


	def __sub__(self, series_of_numbrs_or_matrix):
		if isinstance(series_of_numbrs_or_matrix, numbers.Integral):
			new_matrix = [series_of_numbrs_or_matrix for i in self.rows]
			k = Matrix(*new_matrix)
			return self - k
		if series_of_numbrs_or_matrix.dimnision != self.dimnision:
			raise WrongMatrix ("Wrong matrices. Must be the same size.")
		new_matrix = []
		for i in range(len(self.rows)):
			new_matrix.append(self.index[i][1] - series_of_numbrs_or_matrix.index[i][1])
		return Matrix(*new_matrix)

	def __rsub__ (self, numbers):
		return self.__sub__(numbers)


	def __mul__(self, series_of_numbrs_or_matrix):
		if isinstance(series_of_numbrs_or_matrix, numbers.Integral):
			new_matrix = [series_of_numbrs_or_matrix for i in self.rows]
			k = Matrix(*new_matrix)
			return self * k	
			for i in range(self.size):
				for j in range(self.size):
					self.rows[i][j] *= series_of_numbrs_or_matrix
		if series_of_numbrs_or_matrix.dimnision != self.dimnision:
			raise WrongMatrix ("Wrong matrices.")
		new_matrix = []
		for i in range(self.dimnision):
			for j in range(self.dimnision):
				s = 0
				for k in range(self.dimnision):
					s += self.index[i*self.dimnision+k][1] * series_of_numbrs_or_matrix.index[k*self.dimnision+j][1]
				new_matrix.append(s)
		return Matrix(*new_matrix)

	def __rmul__ (self, numbers):
		return self.__mul__(numbers)


	def __str__(self):
		return 'Matrix ' + str(self.dimnision) + 'x' + str(self.dimnision) + ':\n' +'\n'.join(' '.join(['{:6}'.format(self.index[j+i*self.dimnision][1]) for j in range(self.dimnision)]) for i in range(self.dimnision)) + '\n'
	


if __name__ == "__main__":
	print("matrix.py is being run directly")
