
def kuzibiki(n, k_, w):
  for i in k_:
    for j in k_:
      for k in k_:
        x = w - sum([i, j, k])
        k_2 = k_
        if last_kuzibiki(x, k_2):
          return True
  return False

def last_kuzibiki(x, k_2):
  while len(k_2) != 0:
    m = int(len(k_2) / 2)
    if k_2[m] == x:
      return True
    elif x < k_2[m]:
      k_2 = k_2[:m]
    elif x > k_2[m]:
      k_2 = k_2[m + 1:]
  return False

if __name__ == '__main__':
  n = 10
  k_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  w = 10
  
  if kuzibiki(n, k_, w):
    print("Yes")
  else:
    print("No")


