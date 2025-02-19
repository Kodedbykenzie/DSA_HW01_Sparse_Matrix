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
    except Exception as e:
        print(f"Error loading matrices: {e}")
        sys.exit(1)
    
    # Print the shapes of the matrices for debugging
    print(f"Matrix 1 shape: {matrix1.shape}")
    print(f"Matrix 2 shape: {matrix2.shape}")

    # Check if matrices have the same dimensions for addition and subtraction
    if operation in ["add", "subtract"] and matrix1.shape != matrix2.shape:
        print("Error: Matrices must have the same dimensions for this operation.")
        sys.exit(1)

    # Check if matrices have compatible dimensions for multiplication
    if operation == "multiply" and matrix1.shape[1] != matrix2.shape[0]:
        print("Error: Matrices cannot be multiplied due to incompatible dimensions.")
        sys.exit(1)

    result = None  # ✅ Initialize result
    try:
        if operation == "add":
            result = matrix1.add(matrix2)
        elif operation == "subtract":
            result = matrix1.subtract(matrix2)
        elif operation == "multiply":
            result = matrix1.multiply(matrix2)
        else:
            print("Invalid operation")
            sys.exit()

        if result:  # ✅ Check if result is assigned
            result.print_readable()
        else:
            print("Operation could not be performed due to an error.")

    except Exception as e:
        print(f"Unexpected error: {e}")  # ✅ Better error handling

if __name__ == "__main__":
    main()