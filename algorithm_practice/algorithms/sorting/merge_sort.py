# O(n log n)
# divide and conquer

def merge(left, right):
  result = []
  left_index, right_index = 0, 0
  while(left_index < len(left) and right_index < len(right)):
    if left[left_index] < right[right_index]:
      result.append(left[left_index])
      left_index += 1
    else:
      result.append(right[right_index])
      right_index += 1
  return result + left[left_index:] + right[right_index:]


def merge_sort(num):
  if len(num) < 2:
    return num
  mid = len(num) // 2
  return merge(merge_sort(num[:mid]), merge_sort(num[mid:]))



num_list = [6, 5, 3, 1, 8, 7, 2, 4]
num_list2 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(merge_sort(num_list))
print(merge_sort(num_list2))