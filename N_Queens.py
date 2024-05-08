class N_Queens:
    def __init__(self,n):
        self.n = n
        self.board = [[0]*n for _ in range(n)]
        self.solutions = []

    def isSafe(self,row,col):
        for i in range(row):
            if self.board[i][col] == 1:
                return False
            if 0 <= col-row+i < self.n and self.board[i][col-row+i] == 1:
                return False
            if 0 <= col+row-i < self.n and self.board[i][col+row-i] == 1:
                return False
        return True    

    def backtracking(self, row=0):
        if row == self.n:
            self.solutions.append([row[:] for row in self.board])
            return True
        
        for col in range(self.n):
            if self.isSafe(row,col):
                self.board[row][col] = 1
                self.backtracking(row+1)
                self.board[row][col] = 0
    
    def print(self):
        for i,solution in enumerate(self.solutions):
            print(f"Solution {i+1}")
            for row in solution:
                print(" ".join("Q" if cell==1 else "-" for cell in row))
            print()

n_queens = N_Queens(4)
n_queens.backtracking()
print("Solutions : ")
n_queens.print()
