# select sort

def selection_sort(num):
  for i in range(len(num)):
    min_index = i
    for j in range(i+1, len(num)):
      if num[min_index] > num[j]:
        min_index = j

    num[i] , num[min_index] = num[min_index] , num[i]
  return num





num_list = [6, 5, 3, 1, 8, 7, 2, 4]
num_list2 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(selection_sort(num_list))
print(selection_sort(num_list2))