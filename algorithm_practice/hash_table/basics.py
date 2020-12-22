# python : hash table = dictionary
# by key
# insert O(1)
# lookup O(1)
# delete O(1)
# search O(1)
# can be slow keys
# trade off (fast access for more memory)

user = {'age':54, 
      'name':'kylie',
      'magic':True,
      'scream': lambda: print('ahhhhhhhh!')}

print(user['age'])
user['scream']()
