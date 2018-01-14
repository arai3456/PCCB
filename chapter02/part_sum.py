
def dfs(i, sum_a, n, k, a):
    if i == n:
      return sum_a == k
    if dfs(i + 1, sum_a, n, k, a) :
      return True

    if dfs(i + 1, sum_a + a[i], n, k, a):
      return True

    return False

if __name__ == "__main__":
  n = 4
  a = [1,2,4,7]
  k = 13
  sum_a = 0
  i = 0
  if dfs(i, sum_a, n, k, a):
    print("Yes")
  else:
    print("No")


