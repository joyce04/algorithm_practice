# given an array of intergers : nums and an integer : target
# return indices of two numbers such that they add up to target
# each input would have one solution

# [2, 7, 11, 15], 9 => [0, 1]

def two_sum(nums, target):
  complementary_nums = {}
  for i in range(len(nums)):
    compl_n = target-nums[i]
    if complementary_nums.get(compl_n) != None:
      return [complementary_nums[compl_n], i]
    else:
      complementary_nums[nums[i]] = i

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))