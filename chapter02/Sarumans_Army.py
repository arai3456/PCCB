def sarumans_army(N, R, X):
  mark = list()
  start = X[0]
  for i in range(N):
    if X[i] - start > R:
      mark.append(X[i-1])
      for j in range(i,N):
        if X[j] - X[i-1] > R:
          start = X[j]
          break
  if X[-1] - mark[-1] > R:
    mark.append(X[-1])

          
  return mark
   

if __name__ == '__main__':
  N = 6
  R = 10
  X = [1, 7, 15, 20, 30, 50]
  print(sarumans_army(N, R, X))
