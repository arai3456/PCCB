def LCS(n, m, s, t):
  dp = list()
  for i in range(n + 1):
    dp.append(list())
    for j in range(m + 1):
      dp[i].append(0)
  for i in range(0,n):
    for j in range(0, m):
      if s[i] == t[j]:
        dp[i+1][j+1] = dp[i][j]+1
      else:
        dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
  return dp[n][m]

if __name__ == '__main__':
  n = 4
  m = 4
  s = 'abcd'
  t = 'becd'
  print(LCS(n, m, s, t))

