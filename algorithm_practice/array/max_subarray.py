# given an integer array nums, find the continguous subarray with the largest sum and return its sum
# nums : [-2, 1, -3, 4, -1, 2, 1, -5, 4] => 6

def max_subarray(nums):
  if len(nums)<2:
    return nums[0]
  
  maxsum = cursum = nums[0]
  for i in range(1, len(nums)):
    cursum = max(nums[i], cursum + nums[i])
    maxsum = max(maxsum, cursum)
  
  return maxsum

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])) #6