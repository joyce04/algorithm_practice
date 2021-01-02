# bubble sort
# insertion sort : mostly sorted or small
# selection sort

# divide and conquer
# merge sort : probably best(worst case) -- space complexity O(n)
# quick sort : depend on pivot
# heap sort : https://brilliant.org/wiki/heap-sort/#citation-1

# https://www.toptal.com/developers/sorting-algorithms
# https://www.youtube.com/user/AlgoRythmics/videos

letters = ['a', 'd', 'b', 'r', 'e']
nums = [1, 33, 23, 4, 5]
print(sorted(letters))
print(sorted(nums))
nums.sort()
print(nums)


# python sorted : timsort (hybrid of merge and insertion sort)


import locale
# locale.resetlocale

list_of_strings = ['Hola', 'Sí', 'Adiós', 'Gracias']
list_of_strings.sort()
print(list_of_strings)
print(sorted(list_of_strings, key=locale.strxfrm))

# 1. sort 10 places by distance : insertion sort
# 2. ebay sort listing by curren bid amount : radix or counting [num in range]
# 3. sport scores on ESPN : merge sort(if memory is sufficient) or quick
# 4. massive dataset(can't fit to memory) : heap sort
# 5. almost sorted review data : insertion
# 6. temperatue records for the past 50 years : heap / quick
# 7. user name db random : merge sort(if memory is sufficient), quick
