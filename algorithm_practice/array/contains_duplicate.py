# https://leetcode.com/problems/contains-duplicate/description/
# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

def contain_duplicate(arr):
  if len(arr)<2:
    return False

  prev_vals = {}
  for i in range(len(arr)):
    if prev_vals.get(arr[i]):
      return True
    else:
      prev_vals[arr[i]]= True
  return False

def contain_duplicate_set(arr):
  if len(arr)<2:
    return False
  return len(arr) != len(set(arr))

print(contain_duplicate([1,2,3,1]))
print(contain_duplicate([1,2,3,4]))
print(contain_duplicate_set([1,1,1,3,3,4,3,2,4,2]))