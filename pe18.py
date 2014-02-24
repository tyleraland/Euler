file = open("pe18-input")
t = [[int(num) for num in line.strip().split(' ')] for line in file]  # i,j indicate row,col respectively

for row in reversed(range(0,len(t)-1)): # Traverse triangle bottom-up; skip bottom
    for col in range(0,row+1): # Note: row >= col, and ...
        t[row][col] += max(t[row+1][col], t[row+1][col+1])
print(t[0][0])
