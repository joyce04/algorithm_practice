# linked list
# contains value , pointer to next
# prepand, append O(1)
# lookup O(n)
# insert O(n)
# delete O(n)

class Node:
  def __init__(self, value, prev, next):
    self.value = value
    self.prev = prev
    self.next = next

class DoubleLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def append(self, value):
    if self.length ==0: #new
      node = Node(value, None, None)
      self.head = node
      self.tail = node
    else:
      node = Node(value, self.tail, None)
      self.tail.next = node
      self.tail = node
    self.length += 1
  
  def prepend(self, value):
    node = Node(value, None, self.head)
    self.head.prev = node
    self.head = node
    self.length += 1
  
  def traverse_to(self, index):
    cur_node = self.head
    for i in range(index-1):
      cur_node = cur_node.next
    return cur_node
  
  def insert(self, index, value):
    if index == 0:
      self.prepend(value)
    elif self.length < index:
      self.append(value)
    else:
      prev_node = self.traverse_to(index)
      next_node = prev_node.next
      node = Node(value, prev_node, next_node)
      prev_node.next = node
      next_node.prev = node
      self.length +=1
  
  def remove(self, index):
    if self.length > index:
      prev_node = self.traverse_to(index-1)
      cur_node = prev_node.next
      next_node = cur_node.next
      prev_node.next = next_node
      next_node.prev = prev_node
      del cur_node
      self.length -= 1

  def print(self, reverse=False):
    if reverse:
      cur_node = self.tail
      while cur_node != None:
        print(cur_node.value , end = ' <- ')
        cur_node = cur_node.prev
      print()
    else:
      cur_node = self.head
      while cur_node != None:
        print(cur_node.value , end = ' -> ')
        cur_node = cur_node.next
      print()


my_linked_list = DoubleLinkedList()
my_linked_list.append(10)
my_linked_list.append(5)
my_linked_list.prepend(16)
my_linked_list.insert(2, 99)
my_linked_list.insert(0, 9)
my_linked_list.insert(22, 69)
print(my_linked_list.length) 
my_linked_list.print() #9, 16, 10, 99, 5, 
my_linked_list.print(True) 

my_linked_list.remove(1)
print(my_linked_list.length)
my_linked_list.print() #9, 10, 99, 5, 
my_linked_list.print(True) 
