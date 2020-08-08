# Makes the matrix from input
def make_matrix(rows):
	matrix = []
	for i in range(rows):
		row = [eval(x) for x in input().split()]
		matrix.append(row)
	return matrix


# Adds two matrices
def add_M():
	[m1, n1] = [int(i) for i in input("Enter size of first matrix:").split()]
	matrix_2 = make_matrix(m1)

	[m2, n2] = [int(i) for i in input("Enter size of second matrix:").split()]
	matrix_1 = make_matrix(m2)

	if (m1, n1) != (m2, n2):
		print("The operation cannot be performed.")

	else:
		print("The result is:")
		for i in range(m1):
			for j in range(n1):
				print(matrix_1[i][j] + matrix_2[i][j], end=" ")
			print("\n", end="")


# Multiplies a matrix by a scalar
def scalar_mult():
	[m, n] = [int(i) for i in input().split()]
	matrix = make_matrix(m)
	scalar = int(input())
	print("The result is:")
	for i in range(m):
		for j in range(n):
			matrix[i][j] = scalar * matrix[i][j]
	print("\n".join(' '.join(map(str, l)) for l in matrix))


# Multiplies two matrices
def matrix_multiplication():
	[m1, n1] = [int(i) for i in input("Enter size of first matrix:").split()]
	matrix_1 = make_matrix(m1)

	[m2, n2] = [int(i) for i in input("Enter size of second matrix:").split()]
	matrix_2 = make_matrix(m2)

	if n1 != m2:
		print("The operation cannot be performed.")
	else:
		print("The result is:")
		for i in range(m1):
			for k in range(n2):
				total = 0
				for j in range(n1):
					total += matrix_1[i][j] * matrix_2[j][k]
				print(round(total, 2), end=" ")
			print("\n", end="")


# Transposes a matrix
def transpose_matrix():
	print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
	choice = input("Your choice:")
	[m, n] = [int(i) for i in input("Enter matrix size:").split()]
	matrix = make_matrix(m)
	print("The result is:")
	if choice == "1":
		for i in range(m):
			for j in range(n):
				print(matrix[j][i], end=" ")
			print("\n", end="")
	elif choice == "2":
		for i in range(m):
			for j in range(n):
				print(matrix[n - 1 - j][m - 1 - i], end=" ")
			print("\n", end="")
	elif choice == "3":
		for i in range(m):
			for j in range(n):
				print(matrix[i][n - 1 - j], end=" ")
			print("\n", end="")
	else:
		for i in range(m):
			for j in range(n):
				print(matrix[m - 1 - i][j], end=" ")
			print("\n", end="")


def determinant(mat, n):
	temp = [0] * n
	total = 1
	det = 1
	for i in range(0, n):
		index = i  # initialize the index

		# finding the index which has non zero value
		while (mat[index][i] == 0 and index < n):
			index += 1

		if (index == n):  # if there is non zero element
			# the determinat of matrix as zero
			continue
		if (index != i):
			for j in range(0, n):
				mat[index][j], mat[i][j] = mat[i][j], mat[index][j]
			det = det * int(pow(-1, index - i))
		for j in range(0, n):
			temp[j] = mat[i][j]
		for j in range(i + 1, n):
			num1 = temp[i]  # value of diagonal element
			num2 = mat[j][i]  # value of next row element

			for k in range(0, n):
				# multiplying to make the diagonal
				# element and next row element equal

				mat[j][k] = (num1 * mat[j][k]) - (num2 * temp[k])

			total = total * num1  # Det(kA)=kDet(A);

	# mulitplying the diagonal elements to get determinant
	for i in range(0, n):
		det = det * mat[i][i]

	print(float(det / total))  # Det(kA)/k=Det(A);

	# mat = matrix_1
	# N = len(mat)


	# print('The result is :')
	# print(determinant(mat, N))

while True:
	print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
0. Exit""")

	choice = input("Your choice: ")

	if choice == '1':
		add_M()
	elif choice == '2':
		scalar_mult()
	elif choice == '3':
		matrix_multiplication()
	elif choice == '4':
		transpose_matrix()
	elif choice == '5':
		[m1, n1] = [int(i) for i in input("Enter matrix size:").split()]
		print('Enter matrix:')
		matrix_1 = make_matrix(m1)
		print('The result is:')
		determinant(matrix_1, len(matrix_1))
	else:
		break
