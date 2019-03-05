def mean(list):
  sum = 0

  for item in list:
    sum += item
  
  return sum / len(list)

def variance(list):
  return