"""create linked list structure"""

class Node:
    """class for node of list"""
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    """"class for linked list"""
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def add(self, x):
        if self.length == 0:
            self.first = self.last = Node(x, None)
        else:
            self.last.next = self.last = Node(x, None)

        self.length += 1
    
    def __str__(self):
        """"magic method for list printing"""
        if self.length == 0:
            return '[]'

        current = self.first
        out_list = '['
        count = 0
        while(current!= None):
            if count == self.length - 1:
                out_list += str(current.value) + ']\n'
            else:
                out_list += str(current.value) + ', '
            current = current.next
            count += 1
            
        return out_list
        
#___________________________________________________
"""addition functions not natural for sortet list"""
      def pop(self, index):
        current = self.first
        if index == 0:
            self.first = current.next
            self.length -= 1
            return

        for i in range(index - 1):
            current = current.next

        current.next = current.next.next
        self.length -= 1
 
    def insert(self, index, x):
        if index == 0:
            self.first = Node(x, self.first)
            self.length += 1
            return 

        current = self.first
        for i in range(index - 1):
            current = current.next

        prev_next = current.next
        current.next = current = Node(x, prev_next)
        self.length += 1

    def clear(self):
        self.__init__()

l = LinkedList()
A = [1, 3, 5, 3, 7, 7, 9]
for a in A:
    l.add(a)
print(l)
l.pop(0)
l.pop(l.length - 1)
print(l)
l.insert(0, 10)
print(l)
