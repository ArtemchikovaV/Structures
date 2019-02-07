class Heap():
    # max heap
    def __init__(self):
        self.heap_list = [0]
        self.heap_size = 0

    def insert(self, value):
        if self.heap_size == 0:
            self.heap_list[0] = value
            self.heap_size += 1
            return

        self.heap_list.append(value)
        self.heap_size += 1
        self.liftUp(self.heap_size - 1)


    def liftUp(self, ind):
        if ind == 0:
            return
        if self.heap_list[ind] > self.heap_list[ind // 2]:
            self.heap_list[ind], self.heap_list[ind // 2] =\
                self.heap_list[ind // 2], self.heap_list[ind]

        self.liftUp(ind // 2)


    def liftDown(self, ind):

        if ind * 2 >= self.heap_size:
            return

        if self.heap_list[2 * ind] > self.heap_list[2 * ind + 1]:
            min_child_ind = 2 * ind + 1
        else:
            min_child_ind = 2 * ind

        if self.heap_list[ind] < self.heap_list[min_child_ind]:
            self.heap_list[ind], self.heap_list[min_child_ind] = \
                self.heap_list[min_child_ind], self.heap_list[ind]

        self.liftDown(min_child_ind * 2)



h = Heap()
h.insert(2)
h.insert(3)
h.insert(4)
h.insert(10)
h.insert(1)
print(h.heap_list)