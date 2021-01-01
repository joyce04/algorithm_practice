class Node:
  def __init__(self, value, prev, next):
    self.value = value
    self.prev = prev
    self.next = next

class Stack:
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0
  
  def peek(self):
    if self.length == 0:
      return
    return self.bottom.value

  def push(self, value):
    if self.length ==0:
      node = Node(value, None, None)
      self.top = node
      self.bottom = node
    else:
      prev_botton = self.bottom
      node = Node(value, prev_botton, None)
      prev_botton.next = node
      self.bottom = node
    self.length += 1
      
  def pop(self):
    if self.length == 0:
      return
    if self.length ==1:
      self.top = None

    last = self.bottom
    prev = last.prev
    prev.next = None
    self.bottom = prev
    self.length -= 1
    return last.value
    

  def print(self):
    cur_node = self.top
    while cur_node!=None:
      print(cur_node.value, end='->')
      cur_node = cur_node.next
    print()
    


mystack = Stack()
mystack.push('google')
mystack.push('youtube')
mystack.push('udemy')
mystack.push('google')
mystack.print()

print(mystack.peek())
print(mystack.pop())
mystack.print()