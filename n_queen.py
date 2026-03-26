def is_safe(board, row, col, n):
    
    for i in range(col):
        if board[row][i] == 1:
            return False


    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

   
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, n, solutions):
    if col >= n:
      
        solution = []
        for i in range(n):
            row_str = ""
            for j in range(n):
                row_str += "Q " if board[i][j] == 1 else ". "
            solution.append(row_str)
        solutions.append(solution)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_n_queens_util(board, col + 1, n, solutions) or res
            board[i][col] = 0 #

    return res

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    
    solve_n_queens_util(board, 0, n, solutions)
    
    if not solutions:
        print("Solution does not exist")
        return
        
    print(f"Found {len(solutions)} solutions for {n}-Queens.")
    for idx, sol in enumerate(solutions):
        print(f"\nSolution {idx + 1}:")
        for row in sol:
            print(row)

if __name__ == "__main__":
    n = 4 
    solve_n_queens(n)