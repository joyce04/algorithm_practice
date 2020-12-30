class Stack:
  def __init__(self):
    self.array = []
    self.length = 0
  
  def peek(self):
    if self.length == 0:
      return
    return self.array[self.length -1]

  def push(self, value):
    self.array.append(value)
    self.length += 1
  
  # def left_shift(self): #queue
  #   for i in range(1, len(self.array)):
  #     self.array[i-1] = self.array[i]
  #   del self.array[i]

  def pop(self):
    if self.length == 0:
      return
    last = self.array[self.length -1]
    del self.array[self.length -1]
    self.length -= 1
    return last   

  def print(self):
    print(self.array)


mystack = Stack()
mystack.push('google')
mystack.push('youtube')
mystack.push('udemy')
mystack.push('google')
print(mystack.length)
mystack.print()

print(mystack.peek())
print(mystack.pop())
print(mystack.length)
mystack.print()

print(mystack.pop())
print(mystack.length)
mystack.print()