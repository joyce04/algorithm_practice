class Node:
  def __init__(self, value, next):
    self.value = value
    self.next = next
  
class Queue:
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0
  
  def peek(self):
    if self.length==0:
      return None
    return self.first.value
  
  def enqueue(self, value):
    if self.length == 0:
      node = Node(value, None)
      self.first = node
      self.last = node
    else:
      prev_last = self.last
      node = Node(value, None)
      prev_last.next = node
      self.last = node
    self.length += 1
  
  def dequque(self):
    if self.length == 0:
      return None
    elif self.length == 1:
      self.last = None
    first = self.first
    self.first = self.first.next
    return first.value
  
  def print(self):
    cur_node = self.first
    while cur_node!=None:
      print(cur_node.value, end='->')
      cur_node = cur_node.next
    print()


myqueue = Queue()
print(myqueue.peek())
myqueue.enqueue('Joy')
myqueue.enqueue('Matt')
myqueue.enqueue('Pavel')
myqueue.enqueue('Samir')
myqueue.print()

print(myqueue.dequque())
myqueue.print()

print(myqueue.peek())
print(myqueue.dequque())
myqueue.print()

print(myqueue.dequque())
myqueue.print()

print('last item')
print(myqueue.dequque())
myqueue.print()