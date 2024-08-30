class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue_front(self, item):
        self.items.insert(0, item)

    def enqueue_rear(self, item):
        self.items.append(item)

    def dequeue_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError('Deque is empty')

    def dequeue_rear(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError('Deque is empty')

    def size(self):
        return len(self.items)

    def peek_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError('Deque is empty')

    def peek_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError('Deque is empty')

