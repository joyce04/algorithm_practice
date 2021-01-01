# linear data structure

# stack LIFO (last in first out) --- arrays or linked list
# lookup O(n) pop,push,peek O(1)

# queue FIFO (first in first out) --- linked list (since array requires shifting for queue)
# lookup O(n) enqueue,dequeue,peek O(1)

class Node:
  def __init__(self, value, next):
    self.value = value
    self.next = next

class Stack:
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0
  
  def peek(self):
    if self.length == 0:
      return
    return self.top.value

  def push(self, value):
    if self.length ==0:
      node = Node(value, None)
      self.top = node
      self.bottom = node
    else:
      prev_top = self.top
      node = Node(value, prev_top)
      self.top = node
    self.length += 1
      
  def pop(self):
    if self.length == 0:
      return
    if self.top == self.bottom:
      self.bottom = None
    prev_top = self.top
    self.top = prev_top.next
    self.length -= 1
    return prev_top.value

  def print(self):
    cur_node = self.top
    while cur_node!=None:
      print(cur_node.value, end='->')
      cur_node = cur_node.next
    print()
    


mystack = Stack()
mystack.push('youtube')
mystack.push('udemy')
mystack.push('google')
mystack.print()

print(mystack.peek())
print(mystack.pop())
mystack.print()

print(mystack.pop())
mystack.print()

print('last item')
print(mystack.pop())
mystack.print()