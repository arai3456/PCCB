def coin(coins, C, A):
  ans = 0
  for c in reversed(coins):
    for i in range(C[c]):
      if A >= c:
        A = A - c
        ans += 1
  return ans

if __name__ == '__main__':
  coins = [1, 5, 10, 50, 100, 500]
  C ={1: 3, 5 : 2, 10: 1, 50 : 3, 100 :0, 500 : 2}
  A = 620

  print(coin(coins, C, A))

