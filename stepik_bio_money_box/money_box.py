# -*- coding: UTF-8 -*-

class MoneyBox:
    def __init__(self, capacity: int):
        self.capacity = int(capacity)
        self.count = 0

    def can_add(self, v):
        return False if (self.count + v) > self.capacity else True

    def add(self, v):
        if self.can_add(v):
            self.count += v

if __name__ == "__main__":
    mb = MoneyBox(int(input("Введите емкость копилки: ")))
    while True:
        count = int(input("Введите количество монет для добавления: "))
        mb.add(count)