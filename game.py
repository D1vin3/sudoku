import time
m = 9
grid = open('matrix.txt').readlines()
for i in range(m):
    grid[i] = list(map(int, grid[i].split(" ")))

def run():
    print_matrix(solve(grid))

def row_col_check(row, col, grid):
    values = set(range(1,10))
    for i in range(m):
        if grid[row][i] in values:
            values.remove(grid[row][i])
        if grid[i][col] in values:
            values.remove(grid[i][col])
    r = row//3
    c = col//3
    for ii in range(3*r, 3*r+3):
        for jj in range(3*c, 3*c+3):
            if grid[ii][jj] in values:
                values.remove(grid[ii][jj])
    return values
  
def find_zero(grid):
    for i in range(m):
        for j in range(m):
            if grid[i][j]==0:
                return i,j
    return False, False

def solve(grid):
    i,j = find_zero(grid) 
    if type(i)!=int:
        return grid

    values = row_col_check(i, j, grid)
    for val in values:
        grid[i][j] = val 
        if solve(grid):
            return grid
        grid[i][j] = 0

def print_matrix(matrix):
    for i in range(m):
        for j in range(m):
            print(matrix[i][j],end='')
            if (j+1)%3==0:
                print('|',end=' ')
        print()
        if (i+1)%3==0 and j==8 and i!=8:
            print('--------------')
    return matrix

started_time = time.time()
run()
finished_time = time.time()
print("Sudoku solved in " , (finished_time-started_time))
