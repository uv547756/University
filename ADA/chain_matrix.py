import sys
def matrixChainOrder(p, n):
    m = [[0 for x in range(n)] for x in range(n)]
    
    for i in range(1, n):
        m[i][i] = 0

    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q

    return m[1][n - 1]

if __name__ == "__main__":
    # Taking the number of matrices as input
    num_matrices = int(input("Enter the number of matrices (at least 4): "))
    
    if num_matrices < 4:
        print("The number of matrices must be at least 4.")
        sys.exit()

    # Taking the dimensions as input
    print("Enter the dimensions of the matrices:")
    p = []
    for i in range(num_matrices + 1):
        dimension = int(input(f"Dimension {i + 1}: "))
        p.append(dimension)

    n = len(p)
    
    # Calculating the minimum cost of matrix chain multiplication
    min_cost = matrixChainOrder(p, n)

    print(f"The minimum number of multiplications needed is {min_cost}")
