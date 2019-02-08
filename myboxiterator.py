class MyBoxIterator:
    def __init__(self, p):
        self.p = p
        self.ind = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind < len(self.p):
            item = self.p[self.ind]
            self.ind += 1
            return item
        else:
            raise StopIteration
