def solve(n, a, m, K):
  dp = list()
  for i in range(K + 1):
    dp.append(-1)
  dp[0] = 0
  for i in range(n):
    for j in range(K + 1):
      #i-1までの数字で作れてるとき
      if dp[j] >= 0:
        dp[j] = m[i]
        # 見てる数字(a[i])より作りたい数字(j)が小さいときと、dp[j - a[i]] <= 0 (数字が残ってるとき) 
      elif j < a[i] or dp[j - a[i]] <= 0:
        dp[j] = -1
      else:
        #余の数を消費してjが作れるとき
        dp[j] = dp[j - a[i]] - 1
  print(dp)
  if dp[K] >= 0:
    print('Yes')
  else:
    print('No')

if __name__ == '__main__':
  n = 3
  a = [3,5,8]
  m = [3,2,2]
  K = 17

  solve(n, a, m, K)


