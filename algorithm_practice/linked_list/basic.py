# linked list
# contains value , pointer to next
# prepand, append O(1)
# lookup O(n)
# insert O(n)
# delete O(n)

class Node:
  def __init__(self, value, next):
    self.value = value
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def append(self, value):
    node = Node(value, None)
    if self.length ==0: #new
      self.head = node
      self.tail = node
    else:
      self.tail.next = node
      self.tail = node
    self.length += 1
  
  def prepend(self, value):
    node = Node(value, self.head)
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
      cur_node = self.traverse_to(index)
      node = Node(value, cur_node.next)
      cur_node.next = node
      self.length +=1
  
  def remove(self, index):
    if self.length > index:
      prev_node = self.traverse_to(index-1)
      cur_node = prev_node.next
      prev_node.next = cur_node.next
      del cur_node
      self.length -= 1
  
  def print(self):
    cur_node = self.head
    while cur_node != None:
      print(cur_node.value , end = ' -> ')
      cur_node = cur_node.next
    print()


my_linked_list = LinkedList()
my_linked_list.append(10)
my_linked_list.append(5)
my_linked_list.prepend(16)
my_linked_list.insert(2, 99)
my_linked_list.insert(0, 9)
my_linked_list.insert(22, 69)
print(my_linked_list.length) 
my_linked_list.print() #9, 16, 10, 99, 5, 

my_linked_list.remove(1)
print(my_linked_list.length)
my_linked_list.print() #9, 10, 99, 5, 