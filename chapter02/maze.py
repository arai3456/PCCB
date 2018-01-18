def bfs(N, M, INF, maze):
  que_list = list()
  d = list()
  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1]
  for i in range(len(maze)):
    for j in range(len(maze[i])):
      if maze[i][j] == 'S':
        sx = i
        sy = j
      elif maze[i][j] == 'G':
        gx = i
        gy = j

#最初に全部INFにする
  for i in range(N):
    d.append(list())
    for j in range(M):
      d[i].append(INF)
      d[i][j] = INF
  que_list.append([sx,sy])
  d[sx][sy] = 0

  while que_list != []:
    p = que_list.pop(0)
    if p[0] == gx and p[1] == gy:
      break
    for i in range(4):
      nx = p[0] + dx[i]
      ny = p[1] + dy[i]
      if 0 <= nx and nx < N and 0 <= ny and ny < M and maze[nx][ny] != '#' and d[nx][ny] == INF:
#一個移動したらプラス1する
        que_list.append([nx, ny])
        d[nx][ny] = d[p[0]][p[1]] + 1
  return d[gx][gy]


if __name__ == '__main__':
  N = 10
  M = 10
  INF = 100000000
  maze = [
      ['#', 'S', '#', '#', '#', '#', '#', '#', '.', '#'],
      ['.', '.', '.', '.', '.', '.', '#', '.', '.', '#'],
      ['.', '#', '.', '#', '#', '.', '#', '#', '.', '#'],
      ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
      ['#', '#', '.', '#', '#', '.', '#', '#', '#', '#'],
      ['.', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
      ['.', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
      ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
      ['.', '#', '#', '#', '#', '.', '#', '#', '#', '.'],
      ['.', '.', '.', '.', '#', '.', '.', '.', 'G', '#'],
      ]
  print(bfs(N, M, INF, maze))
