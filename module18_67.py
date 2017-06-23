from functools import partial
def parse_triangle(s):
  return list(map(lambda l: list(map(int,l.split(' '))),s.strip().split('\n')))
def best_path(t):
  for i,line in enumerate(t):
    if i==0:
      new_best = line
    else:
      new_best = [0]*len(line)
      for j,v in enumerate(line):
        new_best[j] = max(best[j] if j<len(best) else 0,best[j-1] if j-1>=0 else 0)+line[j]
    best = new_best
    print(best)
  return max(best)

def best_path_from_string(s):
  return best_path(parse_triangle(s))
