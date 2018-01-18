def job(n, s, t):
  job_list = sorted(list(zip(t,s)))
  select_job_list = list()
  for i in range(n):
    if i == 0:
      select_job_list.append(job_list[i])
    if job_list[i][1] >= select_job_list[-1][0]:
      select_job_list.append(job_list[i])
  return select_job_list    
    
if __name__ == '__main__':
  n = 5
  s = [1, 2, 4, 6, 8]
  t = [3, 5, 7, 9, 10]
  print(len(job(n, s, t)))
