# Populate a 2-D list with numbers from 1 to n2
def makeSquare ( n ):
	# empty 2-D list filled with 0's
	empty_square = [];
	empty_row = [];
	for i in range (0, n):
		for j in range (0, n):
			empty_row.append(0);
		empty_square.append(empty_row);
		empty_row = [];
	return empty_square;


	square = [];
	new_row = [];
	# Cycle through all numbers from 1 to n**2
	for i in range(0, n**2):
		for j in range(1, n + 1):
			new_row.append((i*n) + j);
		square.append(new_row);
		new_row = [];
	return square;

# Print the magic square in a neat format where the numbers
# are right justified
def printSquare ( magicSquare ):
	return

# Check that the 2-D list generated is indeed a magic square
def checkSquare ( magicSquare ):
	return

def main():
	# Prompt the user to enter an odd number 3 or greater
	userNum = int(input("Enter an odd number greater than or equal to 3: "))
	print(makeSquare(userNum))

	# Check the user input

	# Create the magic square

	# Print the magic square

	# Verify that it is a magic square

main()