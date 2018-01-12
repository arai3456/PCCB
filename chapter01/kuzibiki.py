
def kuzibiki(n, m, k_):
  Flag = False
  for i in range(n):
    for j in range(n):
      for k in range(n):
        for l in range(n):
          if sum([k_[i], k_[j], k_[k], k_[l]]) == m:
            Flag = True
  if Flag == True:
    return "Yes"
  else:
    return "No"

if __name__ == '__main__':
  n = 3
  m = 10
  k_ = [1, 3, 5]

  print(kuzibiki(n, m, k_))
