# merge 2 sorted arrays
# [0, 3, 4, 31], [4, 6, 30] => [0, 3, 4, 4, 30, 31]

def merge(array1, array2):
  # check data types
  if type(array1)!=list or type(array2)!=list:
    raise Exception('array type not list')
  if len(array1) == 0:
    return array2
  if len(array2) ==0:
    return array1

  merged = []
  i = j = 0
  while(i < len(array1) and j < len(array2)):
    if array1[i] < array2[j]:
      merged.append(array1[i])
      i += 1
    else:
      merged.append(array2[j])
      j += 1
    
  return merged+array1[i:]+array2[j:]
  
  
print(merge([0, 3, 4, 31], [4, 6, 30]))
print(merge([4, 6, 30], [0, 3, 4, 31]))
print(merge([4, 6, 30], [0, 3, 4, 31, 32, 50]))
print(merge([4, 6, 30, 51], [0, 3, 4, 31, 32, 50]))
print(merge([4, 6, 30, 51], []))
print(merge([], [4, 6, 30, 51]))
merge(None, None)