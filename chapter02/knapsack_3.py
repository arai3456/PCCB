def knapsack(n, w, v, W):
  # make dp_table
  dp = list()
  INF = 1000000000
  max_v = 8

  for i in range(n + 1):
    dp.append(list())
    for j in range(max_v):
      dp[i].append(INF)
  dp[0][0] = 0
  for i in range(n):
    #jは価値
    for j in range(max_v):
      if j < v[i]:
        dp[i + 1][j] = dp[i][j]
      else:
        dp[i + 1][j] = min(dp[i][j], dp[i][j - v[i]] + w[i])
  res = 0
  for i in range(max_v):
    if dp[n][i] <= W:
      res = i
  print(*dp, sep='\n')
  return res



  

if __name__ == '__main__':
  n = 4
#w=weight, v=value
  w = [2, 1, 3, 2]
  v = [3, 2, 4, 2]
  W = 5
  print(knapsack(n, w, v, W))
