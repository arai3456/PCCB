def best_cow_line(n, S):
  T = list() 
  for i in range(n):
    print(S ,T, i)
    if S[0] < S[-1]:
      T.append(S[0])
      S = S[1:]
    elif S[0] == S[-1]:
      rs = S[::-1]
      if S > rs:
        T.append(S[-1])
        S = S[:-1]
      else:
        T.append(S[0])
        S = S[1:]
    else:
      T.append(S[-1])
      S = S[:-1]
  return T


if __name__ == '__main__':
  n = 6
  S = 'ACDBCB'
  print(''.join(best_cow_line(n, S)))
