class SparseMatrix:
    def __init__(self, matrix_file=None, rows=0, cols=0):
        self.rows = rows
        self.cols = cols
        self.data = {}  # Dictionary to store nonzero values {(row, col): value}

        if matrix_file:
            self.load_from_file(matrix_file)

    def load_from_file(self, matrix_file):
        """Loads a sparse matrix from a file"""
        try:
            with open(matrix_file, 'r') as file:
                lines = file.readlines()

                # Read matrix dimensions.
                self.rows = int(lines[0].strip().split('=')[1])
                self.cols = int(lines[1].strip().split('=')[1])

                # Read nonzero values.
                for line in lines[2:]:
                    line = line.strip()
                    if not line:
                        continue  # Ignore empty lines
                    if not line.startswith('(') or not line.endswith(')'):
                        raise ValueError("Input file has wrong format")

                    try:
                        row, col, value = map(int, line[1:-1].split(','))
                        self.data[(row, col)] = value
                    except ValueError:
                        raise ValueError("Input file has wrong format")

        except FileNotFoundError:
            print(f"Error: File {matrix_file} not found.")

    def getElement(self, row, col):
        """Retrieves an element from the matrix"""
        return self.data.get((row, col), 0)

    def setElement(self, row, col, value):
        """Sets an element in the matrix"""
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]  # Remove zero values to save space

    def __add__(self, other):
        """Performs matrix addition"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match for addition")

        result = SparseMatrix(rows=self.rows, cols=self.cols)
        result.data = self.data.copy()

        # Add nonzero elements of the other matrix
        for (row, col), value in other.data.items():
            if (row, col) in result.data:
                result.data[(row, col)] += value  # Add values for matching coordinates
            else:
                result.data[(row, col)] = value  # Insert new nonzero values

        return result

    def __sub__(self, other):
        """Performs matrix subtraction"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match for subtraction")

        result = SparseMatrix(rows=self.rows, cols=self.cols)
        result.data = self.data.copy()

        # Subtract nonzero elements of the other matrix
        for (row, col), value in other.data.items():
            if (row, col) in result.data:
                result.data[(row, col)] -= value  # Subtract values for matching coordinates
            else:
                result.data[(row, col)] = -value  # Insert negative values for missing coordinates

        return result

    def __mul__(self, other):
        """Performs matrix multiplication"""
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions do not allow multiplication")

        result = SparseMatrix(rows=self.rows, cols=other.cols)

        # Iterate through rows of self and columns of other matrix
        for (row1, col1), value1 in self.data.items():
            for (row2, col2), value2 in other.data.items():
                if col1 == row2:  # Check if column of first matches row of second matrix
                    result_value = value1 * value2
                    if (row1, col2) in result.data:
                        result.data[(row1, col2)] += result_value
                    else:
                        result.data[(row1, col2)] = result_value

        return result

    def print_readable(self):
        """Prints the matrix in a readable format"""
        for row in range(self.rows):
            row_data = []
            for col in range(self.cols):
                row_data.append(str(self.getElement(row, col)))
            print(' '.join(row_data))


def main():
    # Get matrix file paths
    matrix_file1 = input("Enter the first matrix file path: ")
    matrix_file2 = input("Enter the second matrix file path: ")

    try:
        # Load matrices
        matrix1 = SparseMatrix(matrix_file=matrix_file1)
        matrix2 = SparseMatrix(matrix_file=matrix_file2)

        # Print matrices (for testing)
        print("Matrix 1:")
        matrix1.print_readable()
        print("Matrix 2:")
        matrix2.print_readable()

        # Prompt user for operation
        operation = input("Enter operation (Add, Subtract, Multiply): ").strip().lower()

        result = None  # Initialize result

        if operation == "add":
            result = matrix1 + matrix2
        elif operation == "subtract":
            result = matrix1 - matrix2
        elif operation == "multiply":
            result = matrix1 * matrix2
        else:
            print("Invalid operation")
            return

        if result:
            print(f"Matrix {operation.capitalize()} Result:")
            result.print_readable()
        else:
            print("Operation could not be performed due to an error.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()