import random

def quickselect(l, k, time) :
  length = len(l)
  equal = 1
# Pick two random pivot elements from the list, each
# equally likely
  while(equal==1):
    randIndex1 = random.randint(0, length-1)
    randIndex2 = random.randint(0, length-1)
    if randIndex1 != randIndex2:
      equal = 0
    elif len(l) <= 1:
      return (l[randIndex1], time)
      
  pivot_1 = l[randIndex1]
  pivot_2 = l[randIndex2]

  if pivot_1 < pivot_2:
    a = pivot_1
    b = pivot_2
  elif pivot_1 > pivot_2:
    a = pivot_2
    b = pivot_1

  l_small = []
  l_mid = []
  l_big = []

  for i in range(length):
    if l[i] < a:
      l_small.append(l[i])
    elif l[i] > b:
      l_big.append(l[i])
    elif a < l[i] < b:
      l_mid.append(l[i])

  assert(length == len(l_small) + len(l_big) + len(l_mid) + 2)

  if len(l) - k + 1 <= len(l_small):
  # kth largest must be in l_small
    time += 1
    k_updated = k - len(l_mid) - len(l_big) - 2
    res = quickselect(l_small, k_updated, time)
    return res
  elif len(l_small) + len(l_mid) + 2 > len(l) - k + 1 > len(l_small) + 1:
  # kth largest must be in l_mid
    k_updated = k - len(l_big) - 1 
    time += 1
    res = quickselect(l_mid, k_updated, time)
    return res
  elif len(l) - k + 1 > len(l_small) + len(l_mid) + 2:
  # kth largest must be in l_big
    time += 1
    res = quickselect(l_big, k, time)
    return res
  else:
    if len(l_small) + len(l_mid) + 2 == len(l) - k + 1:
      return (b, time)
    else:
      return (a, time)

#Make your code return both the kth largest element and the number of calls to QUICK- SELECT (or its double-pivot variant) it took to find it.
calls = 0
for i in range(20000):
  a=[i for i in range(200)]
  tuble = quickselect(a, 10, 1)
  calls += tuble[1]
print("Average calls: ", calls/20000)