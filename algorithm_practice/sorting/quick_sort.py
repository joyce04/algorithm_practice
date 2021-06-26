# pivot item -> less than pivot to left and bigger than pivot to right 
# -> same to smaller array by divide and conquer

def partition(num, pivot, left, right):
  pivot_val = num[pivot]
  partition_index = left

  for i in range(left+1, right):
    if num[i] < pivot_val:
      num[i], num[partition_index] = num[partition_index], num[i]
      partition_index += 1
  
  num[right], num[partition_index] = num[partition_index], num[right]
  return partition_index

def quick_sort(num, left, right):
  if left < right:
    pivot = right
    partition_index = partition(num, pivot, left, right)

    quick_sort(num, left, partition_index-1)
    quick_sort(num, partition_index+1, right)
  return num


num_list = [6, 5, 3, 1, 8, 7, 2, 4]
num_list2 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(quick_sort(num_list, 0, len(num_list)-1))
print(quick_sort(num_list2, 0, len(num_list2)-1))