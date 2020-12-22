# Load Factor = (n/k) Optimal Load factor = (2/3)
# n = max number of elements, k = bucket size
	

class HashTable:
  def __init__(self, size):
    self.size = size
    self.data = [[] for i in range(size)]
  
  def _hash_(self, key):
    hash = 0
    for ch in key:
      hash = (hash + ord(ch)) % self.size
    return hash
  
  def find_bucket(self, key):
    return self.data[self._hash_(key)]

  def set(self, key, val):
    bucket = self.find_bucket(key)
    for b in range(len(bucket)):
      if bucket[b][0] == key:
        bucket[b][1] = value
        return
    bucket.append([key, val])

  def get(self, key):
    bucket = self.find_bucket(key)
    for b in range(len(bucket)):
      if bucket[b][0] == key:
        return bucket[b][1]
    return None
  
  def delete(self, key):
    bucket = self.find_bucket(key)
    for b in range(len(bucket)):
      if bucket[b][0]==key:
        bucket.pop(b)
        return

  def keys(self):
    keys = []
    for i in range(self.size):
      if self.data[i]:
        keys.extend(list(map(lambda x: x[0], self.data[i])))
    return keys


hashtable = HashTable(3)

print('hash :', hashtable._hash_('grapes'))
print('hash :', hashtable._hash_('grapes1233'))
print('hash :', hashtable._hash_('pear'))

hashtable.set('grapes', 10000)
hashtable.set('apples', 50)
hashtable.set('basket', 12)
print('Data :', hashtable.data)

print('GET value : ', hashtable.get('grapes'))
hashtable.set('grapes1', 10000)
hashtable.set('grapes2', 10000)
hashtable.delete('basket')
print('Data :', hashtable.data)

print('keys :', hashtable.keys())