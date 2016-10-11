#  Description: This program will prompt the user for the dimensions of a desired magic square. Using the function makeSquare(n), this program will create a n x n matrix that is a magic square. The magic square will then be printed with formatting and the matrix will be verified as a magic square.

# Populate a 2-D list with numbers from 1 to n2
def makeSquare (n):
	# Create list a that will be 2-D list representing magic square
	a = []

	# Convert a into n x n 2-D list filled with 0's
	for i in range (n):
		row = []
		for j in range (n):
			row.append(0)
		a.append(row)

	# Initialize variables i and j for row and column of magic square (start at location of 1)
	i = n - 1
	j = (n // 2)

	# Run through each number that will be added to magic square
	for k in range (1, n ** 2 + 1):
		# Wrap row value, i, if it is out of range of magic square
		if (i == n) and (j != n):
			i = 0
		# Wrap column value, j, if it is out of range of magic square
		if (j == n) and (i != n):
			j = 0
		# Correct i and j for case where previous k was added to lower right corner
		if (i == n) and (j == n):
			i = i - 2
			j = j - 1
		# Correct currnet i and j values if position is already filled
		if a[i][j] != 0:
			i = i - 2
			j = j - 1
		# Fill empty position with k value
		if a[i][j] == 0:
			a[i][j] = k
		# Increment i and j
		i += 1
		j += 1

	# Return magic square
	return a

# Print the magic square in a neat format where the numbers
# are right justified
def printSquare (magicSquare):
	# Run through each value of 2-D list
	for i in range (len(magicSquare)):
		for j in range (len(magicSquare[0])):
				# Print individual values as right-justified
				print(format(magicSquare[i][j], "3d"), end = ' ')
		# Print new line variable to begin printing next row of values
		print()

# Check that the 2-D list generated is indeed a magic square
def checkSquare (magicSquare):
	# Define variables to check the sums of magic square
	sum_row = 0
	sum_rows = []
	sum_col = 0
	sum_cols = []
	sum_UL_LR = 0
	sum_UR_LL = 0

	# Calculate the sum of individual rows
	for i in range(len(magicSquare)):
		for j in range(len(magicSquare[0])):
			sum_row += magicSquare[i][j]
		# Add a single row's sum to list of row sums
		sum_rows.append(sum_row)
		# Reset sum of individual row
		sum_row = 0
	# Check that each row's sum is equal
	sum_rows.sort()
	# Print sum of row if all rows' sums are equal
	if sum_rows[0] == sum_rows[-1]:
		print("Sum of row =", format(sum_rows[0], ".0f"))
	# Print error message if each row's sum is not equal to eachother
	else:
		print("Sum of rows do not match")

	# Calculate the sum of individual columns
	for j in range(len(magicSquare[0])):
		for i in range(len(magicSquare)):
			sum_col += magicSquare[i][j]
		# Add a single column's sum to list of column sums
		sum_cols.append(sum_col)
		# Reset sum of individual column
		sum_col = 0
	# Check that each column's sum is equal
	sum_cols.sort()
	# Print sum of column if all columns' sums are equal
	if sum_cols[0] == sum_cols[-1]:
		print("Sum of column =", format(sum_cols[0], ".0f"))
	# Print error message if each column's sum is not equal to eachother
	else:
		print("Sum of columns do not match")

	# Calculate and print sum of upper left to lower right diagonal
	for i in range(len(magicSquare)):
		sum_UL_LR += magicSquare[i][i]
	print("Sum diagonal (UL to LR) =", format(sum_UL_LR, ".0f"))

	# Calculate and print sum of upper right to lower left diagonal
	for i in range(len(magicSquare)):
		sum_UR_LL += magicSquare[i][-i - 1]
	print("Sum diagonal (UR to LL) =", format(sum_UR_LL, ".0f"))

def main():
	# Prompt user to enter desired dimensions of magic square
	n = int(input("Please enter an odd number: "))
	print()
	# Error check user's input
	while (n % 2 != 1) or (n < 3):
		n = int(input("Please enter an odd number: "))
		print()

	# Create magic square
	magicSquare = makeSquare(n)
	# Print header for magic square
	print("Here is a", n, "x", n, "magic square:")
	print()
	# Print magic square
	printSquare(magicSquare)
	print()
	# Verify that it is a magic square
	checkSquare(magicSquare)

main()