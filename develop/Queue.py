import array

class Queue :
    def __init__(self, max_size) :
        assert max_size > 0
        self.max = max_size
        self.size = 0
        self.head = 0
        self.tail = 0
        self.data = array.array('i', range(max_size))
    
    def empty(self) :
        return self.size == 0

    def full(self) :
        return self.size == self.max
    
    def enqueue(self, x) :
        if(not self.full()) :
            self.data[self.tail] = x
            self.tail += 1
            self.size += 1
            if(self.tail == self.max) :
                self.tail = 0
            print('Data successfully added : ' + str(x))
        else :
            print('Queue is full. Cannot add!!!')

    def dequeue(self) :
        if(not self.empty()) :
            x = self.data[self.head]
            self.head += 1
            self.size -= 1
            if(self.head == self.max) :
                self.head = 0
            print('Data returned successfully : ' + str(x))
            return x
        else :
            print('Queue is empty. Hence dequeue fails')
