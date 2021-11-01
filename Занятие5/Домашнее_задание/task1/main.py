if __name__ == "__main__":

    matrix = []

    for row in range(1, 10):
        for col in range(1, 10):
            matrix[row][col] = row * col

    print(matrix)