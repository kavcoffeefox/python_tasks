# -*- coding: UTF-8 -*-
from functools import reduce

class Buffer:
    def __init__(self):
        self.buffer = list()

    def add(self, *a):
        for i in a:
            self.buffer.append(i)

            if len(self.buffer) == 5:
                print(reduce(lambda x,y: x + y, self.buffer))
                self.buffer.clear()

    def get_current_part(self):
        return self.buffer


if __name__ == "__main__":
    buf = Buffer()
    buf.add(1,1,1)
    buf.add(2)
    buf.add(1,2,3,4,5,6,7)
    print(buf.get_current_part())