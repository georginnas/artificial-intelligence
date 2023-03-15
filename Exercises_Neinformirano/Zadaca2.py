"""Црно - бело Problem 2 (0 / 0)
Предложете соодветна репрезентација и напишете ги потребните функции во Python за да се реши следниот проблем за кој една можна почетна состојба е прикажана на Слика 1:
Tабла со димензии N x N се состои од бели и црни полиња. Со избор (кликнување) на едно поле се прави промена на бојата на тоа поле и на сите негови непосредни соседи (горе, долу, лево и десно)
во спротивната боја, како што е прикажано на Слика 2. Целта е сите полиња на таблата да бидат обоени во црна боја. Потребно е проблемот да се реши во најмал број на потези т.е. со избирање (кликнување)
на најмал можен број на полиња."
За сите тест примери обликот на таблата е ист како на примерот даден на Слика 1. За секој тест пример се менува големината N на таблата, како и распоредот на црни и бели полиња на неа, соодветно.

Во рамки на почетниот код даден за задачата се вчитуваат влезните аргументи за секој тест пример. Во променливата n ја имате големината на таблата (бројот на редици односно колони); во променливата
fields ја имате бојата на сите полиња на таблата (по редослед: одлево - надесно, редица по редица, ако таблата ја гледате како матрица), каде 1 означува дека полето е обоено во црна, а 0 означува дека полето
е обоено во бела боја.

Изборот на полиња (потезите) потребно е да ги именувате на следниот начин:

x: redica, y: kolona

каде redica и kolona се редицата и колоната на избраното (кликнатото) поле (ако таблата ја гледате како матрица).

Вашиот код треба да има само еден повик на функција за приказ на стандарден излез (print) со кој ќе ја вратите секвенцата на потези која треба да се направи за да може сите полиња на таблата да бидат обоени
во црна боја. Треба да примените неинформирано пребарување. Врз основа на тест примерите треба самите да определите кое пребарување ќе го користите.
"""
from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


class CrnoBelo(Problem):
    def __init__(self,n, inital, goal=None):
        super().__init__(inital,goal)
        self.n=n

    def successor(self, state):
        successors=dict()
        #state [(0, 0, 0), (1, 0, 0), (1, 1, 0)]
        for i in range(self.n):
            for j in range(self.n):
                list_state=[list(row)for row in state]
                list_state[i][j]=0 if list_state[i][j]==1 else 1
                if i > 0: #LEVO
                    list_state[i - 1][j] = 0 if list_state[i - 1][j] == 1 else 1
                if i < self.n - 1: #DESNO
                    list_state[i + 1][j] = 0 if list_state[i + 1][j] == 1 else 1
                if j > 0: #GORE
                    list_state[i][j - 1] = 0 if list_state[i][j - 1] == 1 else 1
                if j < self.n - 1:  # DOLU
                    list_state[i][j + 1] = 0 if list_state[i][j + 1] == 1 else 1
                #['x: 0, y: 0', 'x: 0, y: 2', 'x: 1, y: 1', 'x: 2, y: 2']
                successors[f'x: {i}, y: {j}']=tuple([tuple(row) for row in list_state])

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return sum([item for row in state for item in row])==self.n*self.n #se pominuva [(0, 0, 0, 0), (1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 3, 3)] for row in state: (0, 0, 0, 0), a for item in row: 0
        # se sobiraat edinicite i toa treba da e ednakvo na polinjata vo matricata t.e n*n

if __name__ == '__main__':
    # vcituvanje na vleznite argumenti za test primerite
    n = int(input())
    fields = list(map(int, input().split(','))) #GO PRAVI SEKOJ BROJ INTEGER I GO SMESTUVA VO LISTATA
    #[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
    in_state=[tuple(fields[i:i+n])for i in range(0, len(fields), n)] #IZMINUVANJE NA LISTATA SO FOR OD 0 DO KRAJ SO CEKOR 3, VO 1 ITERACIJA i=0, [0:0+3], VO 2 ITERACIJA i=3, [3:3+3], VO 3 ITERACIJA i=6, [6, 6+3]
    #porkastruvanjeto ke bide torka!
    crnobelo=CrnoBelo(n, tuple(in_state))
    print(breadth_first_graph_search(crnobelo).solution())


