class Board:
    def __init__(self):
        self.elems = []

    def to_queue(self, item):
        return self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def __repr__(self):
        return str(self.elems)


in_work = Board()
rework = Board()
finish = Board()

in_work.to_queue('task1')
in_work.to_queue('task2')
in_work.to_queue('task3')
in_work.to_queue('task4')

rework.to_queue(in_work.from_queue())
rework.to_queue(in_work.from_queue())


finish.to_queue(rework.from_queue())
finish.to_queue(in_work.from_queue())

print('задачи в работе', in_work)
print('задачи на доработке', rework)
print('задачи на выполнены', finish)
