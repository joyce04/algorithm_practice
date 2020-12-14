# import datetime as d
import time

#  O(n)
# nemo = ['nemo']
# large_names = ['nemo']*100000
# # print(large_names)

# def find_nemo(names):
#   # t1 = d.datetime.now().timestamp()
#   t1 = time.perf_counter()
#   for n in names:
#     if n=='nemo':
#       print('found')
#       break
#   # t2 = d.datetime.now().timestamp()
#   t2 = time.perf_counter()

#   print('time :' + str(t2-t1) + ' seconds')

# find_nemo(large_names)


# O(n^2)
# if two separate boxes O(n*m)
# input_boxes = [1,2,3,4,5]

# def log_all_pairs(boxes):
#   logs = []
#   for i in range(len(boxes)):
#     # for j in range(i, len(boxes)):
#     for j in range(len(boxes)):
#       logs.append([boxes[i], boxes[j]])
#   print(logs)

# log_all_pairs(input_boxes)


# drop non-dominant term

# O(n!)
