n = 5
a = [2, 3, 4, 5 ,10]

ans = 0

for i in range(n):
  a_1 = a[i]
  for j in range(i + 1, n):
    a_2 = a[j]
    for k in range(j + 1, n):
      a_3 = a[k]
      triangle = [a_1, a_2, a_3]
      longest = max(triangle)
      length = sum(triangle)
      if longest < length - longest:
        ans = max(ans, length)
print(ans)
