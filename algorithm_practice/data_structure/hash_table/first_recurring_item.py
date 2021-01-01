# given an array return the first recurring item
# input = [2, 4, 1, 2, 3, 5, 1, 2, 4]
# return 2

def first_recurring_bf(arr):
  for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
      if arr[i]==arr[j]:
        return arr[i]
  return None

def first_recurring(arr):
  unique_items = {}
  for i in range(len(arr)):
    if unique_items.get(arr[i]):
      return arr[i]
    else:
      unique_items[arr[i]] = True
  return None

print(first_recurring_bf([2, 4, 1, 2, 3, 5, 1, 2, 4])) #2
print(first_recurring_bf([2, 1, 1, 2, 3, 5, 1, 2, 4])) #1
print(first_recurring_bf([2, 3, 4, 5])) # none

print(first_recurring([2, 4, 1, 2, 3, 5, 1, 2, 4])) #2
print(first_recurring([2, 1, 1, 2, 3, 5, 1, 2, 4])) #1
print(first_recurring([2, 3, 4, 5])) # none

# answer differ for first_recurring_bf and first_recurring
print(first_recurring([2, 5, 5, 2, 3, 5, 1, 2, 4])) # 2loop => 2


    