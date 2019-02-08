from myboxiterator import MyBoxIterator

class MyBox():
    def __init__(self):
        self.points = list()

    def __len__(self):
        return len(self.points)

    def add(self, point):
        self.points.append(point)

    def remove(self, point):
        assert point in self.points
        ind = self.points.index(point)
        return self.points.pop(ind)

    def __contains__(self, point):
        return point in self.points

    def __iter__(self):
        return MyBoxIterator(self.points)
