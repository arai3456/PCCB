def LCS(n, m, s, t):
  dp = list()
#5*5のテーブル作る
  for i in range(n + 1):
#空のリストを5個入れる
    dp.append(list())
    for j in range(m + 1):
#それぞれのリストに0を5個ずつ
      dp[i].append(0)
#テーブルの中身を2つずつ埋める
#dpのijは0から、sとtのijは'ab'から
  for i in range(0,n):
    for j in range(0, m):
#斜め下のsとtが同じだったら
      if s[i] == t[j]:
#斜め上の数字に1足す
        dp[i+1][j+1] = dp[i][j]+1
      else:
        　#ちがったら、iとjの次のやつ、jとiの次のやつが合ってるかみて、高い方を入れる
        dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
  return dp[n][m]

if __name__ == '__main__':
  n = 4
  m = 4
  s = 'abcd'
  t = 'becd'
  print(LCS(n, m, s, t))

