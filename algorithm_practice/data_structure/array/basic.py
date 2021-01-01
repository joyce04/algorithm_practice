# lookup O(1)
# push O(1)
# insert O(n)
# delete O(n)

strings = ['a', 'b', 'c', 'd']
# 32bit system ) 4*4 = 16 bytes of storage

print(strings[2])

# push append
strings.append('e')
print(strings)

# pop
strings.pop()
print(strings)

# insert
strings.insert(0, 'x')
print(strings)
