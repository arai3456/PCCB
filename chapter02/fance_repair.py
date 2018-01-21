

def fance_repair(X):
  ans = 0
  while len(X) != 1:
    # まず、Xを短い順にソートする
    X = sorted(X)
    #X1とX2をくっつける
    t = X[0] + X[1]
    #ansにt(X1 + X2)を足す
    ans += t
    # X を短くする(list)
    X.pop(0)
    X[0] = t
  return ans

if __name__ == '__main__':
  N = 3
  X = [8, 5, 8]
  print(fance_repair(X))
