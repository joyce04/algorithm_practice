# bubble sort
#  6, 5, 3, 1, 8, 7, 2, 4
#  5, 6, 3, 1, 8, 7, 2, 4
#  5, 3, 6, 1, 8, 7, 2, 4
#  5, 3, 1, 6, 8, 7, 2, 4 -- iteration 계속

def bubble_sort(num_list):
  for i in range(len(num_list)):
    for j in range(1, len(num_list)):
      if num_list[j-1] > num_list[j]:
        # python!! swap with a single line of code
        num_list[j], num_list[j-1] = num_list[j-1], num_list[j]
  return num_list

num_list = [6, 5, 3, 1, 8, 7, 2, 4]
num_list2 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(bubble_sort(num_list))
print(bubble_sort(num_list2))



flist = []
for i in range(3):
  flist.append(lambda: i)

print([f() for f in flist])