
def ant(L, n, x):
  ant_max = 0
  ant_min = 0
  for i in range(n):
    Left = x[i]
    Right = L-x[i]
    if Right > Left:
      i_max = Right
      i_min = Left
    else:
      i_max = Left
      i_min = Right
    ant_max = max(i_max, ant_max)
    ant_min = max(i_min, ant_min)
  return ant_max, ant_min

if __name__ == '__main__':

  L = 10
  n = 3
  x = [2, 6, 7]

  ant_max, ant_min = ant(L, n, x)
  print('max:{0}, min:{1}'.format(ant_max, ant_min))


