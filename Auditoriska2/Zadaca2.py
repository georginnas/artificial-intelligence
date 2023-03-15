"""Задача 2 - Движење на агенти
Да се дефинира класа за Агент кој ја чува својата позиција (координати x и y) во некој простор.
Да се дефинира метод кој го означува движењето на агентот во просторот. Потоа да се дефинираат агенти кои имплементираат
специфично движење (лево, десно, горе, долу). Извршете 5 движења за секој од агентите и испечатете ја позицијата на агентот
во секој чекор.
"""
class Agent:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __repr__(self):
        return f'Position: ({self.x}, {self.y})' #PRINTANJE

    def move(self):
        pass

class UpAgent(Agent):
    def __init__(self,x,y):
        super().__init__(x,y)

    def move(self):
        self.y += 1
class DownAgent(Agent):
    def __init__(self,x,y):
        super().__init__(x,y)

    def move(self):
        self.y -= 1
class LeftAgent(Agent):
    def __init__(self,x,y):
        super().__init__(x,y)

    def move(self):
        self.x -= 1
class RightAgent(Agent):
    def __init__(self,x,y):
        super().__init__(x,y)

    def move(self):
        self.x += 1


if __name__=="__main__":
    la=LeftAgent(3,4)
    for i in range(5):
        la.move()
        print(f'Step: {i}, {la}')
    ra = RightAgent(-2, 3)
    for i in range(5):
        ra.move()
        print(f'Step: {i}, {ra}')
    ua = UpAgent(-2, -3)
    for i in range(5):
        ua.move()
        print(f'Step: {i}, {ua}')
    da = DownAgent(2, 3)
    for i in range(5):
        da.move()
        print(f'Step: {i}, {da}')