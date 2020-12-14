class Array:
  def __init__(self):
    self.length = 0
    self.data = {}

  def get(self, index):
    return self.data[index]

  def push(self, item):
    self.data[self.length] = item
    self.length += 1

  def pop(self):
    last_item = self.data[self.length-1]
    del self.data[self.length-1]
    self.length -= 1
    return last_item
  
  def __shift_left__(self, index):
    for i in range(index, self.length-1):
      self.data[i] = self.data[i+1]
    del self.data[self.length-1] # remove last item

  def delete(self, index):
    delete_item = self.data[index]
    self.__shift_left__(index)
    self.length -= 1

  def __shift_right__(self, index):
    for i in range(self.length-1, index-1, -1):
      self.data[i+1] = self.data[i]

  def insert(self, index, item):
    if index >= self.length:
      self.push(item)
    else:
      self.__shift_right__(index)
      self.data[index] = item
    self.length += 1    


array = Array()
array.push('hi')
array.push('you')
print(array.data)
print(array.length)

array.pop()
print(array.data)
print(array.length)

array.push('hello')
array.push('world')
array.delete(0)
print(array.data)
print(array.length)

array.insert(0, 'first')
array.insert(1, 'second')
array.insert(0, 'x')
print(array.data)
print(array.length)
