# Binary Heap 
# lookup O(n)
# insert, delete O(log n) -- 마지막 leaf에 추가후 bubble swith로 올라감

# max heap : higher value for parents -- priority queue
# min heap

# priority queue in python 
# heapq
import heapq as hq

h = []
hq.heappush(h, (5, 'write code'))
hq.heappush(h, (7, 'release product'))
hq.heappush(h, (1, 'write spec'))
hq.heappush(h, (3, 'create tests'))
print(hq.heappop(h))
print(h)