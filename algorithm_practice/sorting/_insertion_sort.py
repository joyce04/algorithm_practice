# if almost sorted or small data

def insertion_sort(num):
  for i in range(1, len(num)):
    for j in range(i):
      if num[j] > num[i]:
        num[i], num[j] = num[j], num[i]
  return num


num_list = [6, 5, 3, 1, 8, 7, 2, 4]
num_list2 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(insertion_sort(num_list))
print(insertion_sort(num_list2))