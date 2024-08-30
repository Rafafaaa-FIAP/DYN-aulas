class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return self.items.pop(0)
        raise IndexError('Queue from an empty queue')

    def size(self):
        return len(self.items)

    def front(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError('Consulting front of an empty queue')

    def __str__(self):
        if self.is_empty():
            return 'Queue: [Empty]'
        return f'Start -> {' -> '.join(map(str, self.items))} -> End'
