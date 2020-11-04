import numpy as np

def updateCurrCell(matrix, row, col, newMatrix, n):
    alive = 0
    for neighbourRow in range(3):
        for neighbourCol in range(3):
            if neighbourRow == 1 and neighbourCol == 1:
                continue;
            curr = row + neighbourRow - 1
            currNeighbourRow = ((curr % n) + n) % n
            curr = col + neighbourCol - 1
            currNeightbourCol = ((curr % n) + n) % n
            if matrix[currNeighbourRow, currNeightbourCol] == 1:
                alive+=1
    if alive < 2 or alive > 3:
        newMatrix[row, col] = 0
    if matrix[row, col] == 1 and alive >= 2 and alive <= 3:
        newMatrix[row, col] = 1
    if matrix[row, col] == 0 and alive == 3:
        newMatrix[row, col] = 1

def serial(n, iterations):
    listOfMatrix = []
    matrix = (np.random.rand(n**2).reshape(n, n) > 0.5).astype(np.int8)
    for numOfCicles in range(iterations):
        newMatrix = np.zeros((n, n))
        for row in range(n):
            for col in range(n):
                updateCurrCell(matrix, row, col, newMatrix, n)
        listOfMatrix.append(newMatrix)
        matrix = newMatrix
    return listOfMatrix