class SparseMatrix:
    def __init__(self, matrix_file_path):
        # Load the matrix from the file
        self.matrix, self._shape = self.load_matrix(matrix_file_path)
        print(f"Loaded matrix from {matrix_file_path} with shape {self._shape}")

    def load_matrix(self, matrix_file_path):
        # Implement the logic to load the matrix from the file
        matrix = []
        rows, cols = 0, 0
        try:
            with open(matrix_file_path, 'r') as file:
                for line in file:
                    if line.startswith('rows='):
                        rows = int(line.split('=')[1])
                    elif line.startswith('cols='):
                        cols = int(line.split('=')[1])
                    elif line.strip() and not line.startswith('#') and '=' not in line:
                        # Handle tuples or other non-integer data
                        try:
                            matrix.append(list(map(int, line.strip('(),\n').split(','))))
                        except ValueError as e:
                            raise ValueError(f"Error parsing matrix file: {e}")
        except ValueError as e:
            raise ValueError(f"Error parsing matrix file: {e}")
        return matrix, (rows, cols)

    @property
    def shape(self):
        return self._shape

    def add(self, other):
        # Implement the logic to add two matrices
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same dimensions for addition")
        result = [[0] * self._shape[1] for _ in range(self._shape[0])]
        for i, j, val in self.matrix:
            result[i][j] += val
        for i, j, val in other.matrix:
            result[i][j] += val
        return SparseMatrix.from_matrix(result)

    def subtract(self, other):
        # Implement the logic to subtract two matrices
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same dimensions for subtraction")
        result = [[0] * self._shape[1] for _ in range(self._shape[0])]
        for i, j, val in self.matrix:
            result[i][j] += val
        for i, j, val in other.matrix:
            result[i][j] -= val
        return SparseMatrix.from_matrix(result)

    def multiply(self, other):
        # Implement the logic to multiply two matrices
        if self._shape[1] != other._shape[0]:
            raise ValueError("Matrices cannot be multiplied due to incompatible dimensions")
        result = [[0] * other._shape[1] for _ in range(self._shape[0])]
        for i, j, val in self.matrix:
            for k in range(other._shape[1]):
                result[i][k] += val * other.matrix[j][k]
        return SparseMatrix.from_matrix(result)

    def print_readable(self):
        # Implement the logic to print the matrix in a readable format
        for row in self.matrix:
            print(' '.join(map(str, row)))

    @classmethod
    def from_matrix(cls, matrix):
        instance = cls.__new__(cls)
        instance.matrix = matrix
        instance._shape = (len(matrix), len(matrix[0]) if matrix else 0)
        return instance