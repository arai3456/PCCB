
def partition_function(n, m, M):
  dp = list()
  for i in range(m+1):
    dp.append(list())
    for j in range(n+1):
      dp[i].append(0)
  dp[0][0] = 1
  for i in range (1,m+1):
    for j in range(n+1):
      if j - i >= 0:
        dp[i][j] = (dp[i-1][j] + dp[i][j - i]) % M
      else:
          dp[i][j] = dp[i-1][j]
  return dp[m][n]


if __name__ == '__main__':
  n = 4
  m = 3
  M = 10000

  print(partition_function(n, m, M))


