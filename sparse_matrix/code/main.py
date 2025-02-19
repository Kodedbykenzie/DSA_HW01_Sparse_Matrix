from sparse_matrix import SparseMatrix

# File paths for matrix input files
matrix_1_path = '/Users/User/DSA_HW01_Sparse_Matrix/sparse_matrix/sample_input/matrixfile1.txt'
matrix_2_path = '/Users/User/DSA_HW01_Sparse_Matrix/sparse_matrix/sample_input/matrixfile3.txt'


def main():
    import sys

    # Prompt user for operation
    operation = input("Enter operation (Add, Subtract, Multiply): ").strip().lower()

    # Try to load matrices with exception handling
    try:
        matrix1 = SparseMatrix(matrix_file_path=matrix_1_path)
        matrix2 = SparseMatrix(matrix_file_path=matrix_2_path)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error in matrix format: {e}")
        sys.exit(1)

    # Perform the requested operation
    try:
        if operation == "add":
            result = matrix1.add(matrix2)
        elif operation == "subtract":
            result = matrix1.subtract(matrix2)
        elif operation == "multiply":
            result = matrix1.multiply(matrix2)
        else:
            print("Invalid operation. Please enter 'Add', 'Subtract', or 'Multiply'.")
            sys.exit(1)

        # Print result
        print("\nResult:")
        result.print_readable()
    except ValueError as e:
        print(f"Error during operation: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
