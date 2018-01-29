def LIS(n, a):
  dp = list()
  INF = 1000000000
  for i in range(n):
    dp.append(INF)
  for i in range(n):
    if a[i] < dp[0]:
      dp[0] = a[i]
    for j in range(n):
      if a[i] > dp[j] and a[i] < dp[j+1]:
        dp[j+1] = a[i]
  print(dp)
  ans = 0
  for i in range(n):
    if dp[i] != INF:
      ans += 1
  return ans

if __name__ == '__main__':
  n = 5
  a = [4,2,3,1,5]
  print(LIS(n,a))
