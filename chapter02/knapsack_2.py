def knapsack(n, w, v, W):
  # make dp_table
  dp = list()
  for i in range(n + 1):
    dp.append(list())
    for j in range(W + 1):
      dp[i].append(0)
  for i in range(n):
    for j in range(W+1):
      if j < w[i]:
        dp[i + 1][j] = dp[i][j]
      else:
        dp[i + 1][j] = max(dp[i][j], dp[i + 1][j - w[i]] + v[i])
  print(*dp, sep="\n")
  return dp[n][W]


  

if __name__ == '__main__':
  n = 3
#w=weight, v=value
  w = [3, 4, 2]
  v = [4, 5, 3]
  W = 7
  print(knapsack(n, w, v, W))
