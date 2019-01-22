"""Queue structure"""

class Queue:
    def __init__(self):
        self.sequence = []

    def dequeue(self):
        """pop, popleft"""
        return self.sequence.pop()

    def enqueue(self, data):
        """push"""
        self.sequence.insert(0, data)

    def isEmpty(self):
        return self.sequence == []

    def isInQueue(self, data):
        return data in self.sequence

    def clear(self):
        self.__init__()

    def __str__(self):
        result = "["
        for i in range(len(self.sequence)):
            if i == len(self.sequence) - 1:
                result += str(self.sequence[i]) + "]\n"
            else:
                result += str(self.sequence[i]) + ", "

        return result

q = Queue()
q.enqueue(4)
q.enqueue(7)
q.enqueue(1)
print(q)

print(q.dequeue())
print(q)
print(q.isInQueue(7))