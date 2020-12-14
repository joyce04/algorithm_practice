import time
# given a sorted array, sum return true if there is a pair sum == sum 

# [1, 2, 3, 4], 8 False
# [1, 3, 4, 6], 10 True

# 1. nested loop to find matching pair
# 1-2, 1-3, 1-4
# 2-3, 2-4
# 3-4
def pair_match_sum(arr, sum_n):
  t1 = time.perf_counter()
  for i in range(len(arr)-1):
    for j in range(i, len(arr)):
      pair_sum = arr[i]+arr[j]
      if pair_sum == sum_n:
        return True
  t2 = time.perf_counter()
  print('time :' + str(t2-t1) + ' seconds')
  return False

print(pair_match_sum([1, 2, 3, 4], 8))
print(pair_match_sum([1, 3, 4, 6], 10))
print(pair_match_sum([1]*10000, 10))

# two anchors (i,j)
# [1', 2, 3, 4'], 8
# if sum bigger than 8 [1', 2, 3', 4]
# if sum smaller than 8 [1, 2', 3', 4]
# as long as i<j
def pair_match_sum1(arr, sum_n):
  t1 = time.perf_counter()
  i, j = 0, len(arr)-1
  while(i<j):
    pair_sum = arr[i]+arr[j]
    if pair_sum == sum_n:
      return True
    if pair_sum > sum_n:
      j -= 1
    elif pair_sum < sum_n:
      i += 1
  t2 = time.perf_counter()
  print('time :' + str(t2-t1) + ' seconds')
  return False

print(pair_match_sum1([1, 2, 3, 4], 8))
print(pair_match_sum1([1, 3, 4, 6], 10))

# if arr is not sorted
def pair_match_sum2(arr, sum_n):
  t1 = time.perf_counter()
  hash = {}
  for i in arr:
    if hash.get(sum_n-i):
      return True
    else:
      hash[i] = True
  t2 = time.perf_counter()
  print('time :' + str(t2-t1) + ' seconds')
  return False

print(pair_match_sum2([1, 2, 3, 4], 8))
print(pair_match_sum2([1, 3, 4, 6], 10))
