def knapsack(n, w, v, W):
  # make dp_table
  dp = list()
  for i in range(n + 1):
    dp.append(list())
    for j in range(W + 1):
      dp[i].append(0)
  #iは深さ（逆から見る）
  for i in range(n-1,-1,-1):
    #jは重さ
    for j in range(W+1):
    #持ってる重さより加える重さの方が大きかったら
      if j < w[i]:
        #valueはそのまま（何も加えない）
        dp[i][j] = dp[i + 1][j]
#なにも加えないver.と加えるver.(持ってる重さから加える重さを引いて、加える価値を足す)あるとき
#比較
      else:
        dp[i][j] = max(dp[i + 1][j], dp[i + 1][j - w[i]] + v[i])
  return dp[0][W]



  

if __name__ == '__main__':
  n = 4
#w=weight, v=value
  w = [2, 1, 3, 2]
  v = [3, 2, 4, 2]
  W = 5
  print(knapsack(n, w, v, W))
