#いるところがwだったら.に置き換える
def dfs(x, y):
  field[x][y] = '.'
  #最初にxの移動範囲決める
  for dx in range(-1, 2):
#次にyの移動範囲決める
    for dy in range(-1, 2):
      nx = x + dx
      ny = y + dy
      if 0 <= nx and nx < n and 0 <= ny and ny < m and field[nx][ny] =='W':
        dfs(nx, ny)

def lake_count(n, m, field):
  res = 0
  for i in range(n):
    for j in range(m):
      if field[i][j] == 'W':
        dfs(i, j)
        res += 1
  return res



if __name__ == "__main__":
  field = [
    ['W', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', '.'],
    ['.', 'W', 'W', 'W', '.', '.', '.', '.', '.', 'W', 'W', 'W'],
    ['.', '.', '.', '.', 'W', 'W', '.', '.', '.', 'W', 'W', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', '.', '.'],
    ['.', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', '.', '.'],
    ['.', 'W', '.', 'W', '.', '.', '.', '.', '.', 'W', 'W', '.'],
    ['W', '.', 'W', '.', 'W', '.', '.', '.', '.', '.', 'W', '.'],
    ['.', 'W', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', '.'],
    ['.', '.', 'W', '.', '.', '.', '.', '.', '.', '.', 'W', '.'],
    ]
  n = 10
  m = 12

  print(lake_count(n, m, field))
