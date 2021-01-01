# https://leetcode.com/problems/implement-queue-using-stacks/description/#
# Implement a first in first out (FIFO) queue using only two stacks. 


class MyQueue:
  def __init__(self):
      """
      Initialize your data structure here.
      """
      self.s1 = []
      self.s2 = []
      self.length = 0
      

  def push(self, x: int) -> None:
      """
      Push element x to the back of queue.
      """
      length = self.length
      for i in range(length):
        self.s2.append(self.s1.pop())
      self.s1.append(x)
      for i in range(length):
        self.s1.append(self.s2.pop())
      self.length += 1   
      

  def pop(self) -> int:
      """
      Removes the element from in front of queue and returns that element.
      """
      if self.length > 0:
        self.length -= 1
        first = self.s1.pop()
        return first
      else:
        return None
      

  def peek(self) -> int:
      """
      Get the front element.
      """
      if self.length > 0:
        return self.s1[self.length-1]
      return None
      

  def empty(self) -> bool:
      """
      Returns whether the queue is empty.
      """
      if self.length == 0:
        return True
      else:
        return False

        
myq = MyQueue()
myq.push(1)
myq.push(2)
print(myq.s1)
print(myq.s2)

print(myq.peek())
print(myq.pop())
print(myq.s1)
print(myq.s2)
