"""Проблем: Два сада
 Дадени се два сада J0 и J1, со капацитети C0 и C1 литри, соодветно. Да се доведат до состојба во која J0 има G0 литри,
 J1 има G1 литри.
• Акции:
 Испразни кој било од садовите
 Претури течност од еден во друг сад, со тоа што не може да се
надмине капацитетот на садот
 Наполни кој било од садовите (за дома)
Торка (X, Y) која означува дека J0 содржи X литри, а J1
содржи Y литри. Опционална вредност ‘*’, која означува дека е
небитно колку литри има во садот.
• Цел: Предефинираната состојба до која сакаме да стигнеме.
Ако нѐ интересира само едниот сад, за другиот можеме да
ставиме ‘*’."""

from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

class Container(Problem):
    def __init__(self,capacities,inital, goal=None):
        super().__init__(inital,goal)
        self.capacities=capacities
    def successor(self, state):
        #state=(j0,j1)
        successors =dict()
        j0,j1=state #kolku ima vo momentot
        c0, c1=self.capacities #max

        if j0>0:
            successors["Isprazni go sadot J0"]=(0,j1) # se ispraznuva j0 a j1 si ostanuva isto
        if j1>0:
            successors["Isprazni go sadot J1"]=(j0,0)
        if j0>0 and j1<c1: #c1-j1>0 shto e isto!
            delta=min(c1-j1,j0)
            successors["Preturi od J0 vo J1"]=(j0-delta, j1+delta)
        if j1>0 and j0<c0:
            delta=min(c0-j0,j1)
            successors["Preturi od J1 vo J0"]=(j0+delta, j1-delta)

        return successors
    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        return state==self.goal

if __name__=="__main__":
    container=Container([20,20],(10,6), (16,0))

    result=breadth_first_graph_search(container)
    print(result.solution()) #niza na akcii
    print(result.solve()) #lista na sostojbi

    result = depth_first_graph_search(container)
    print(result.solution())  # niza na akcii
    print(result.solve())  # lista na sostojbi


"""

class Container(Problem):
    def __init__(self, capacities, initial, goal=None):
        super().__init__(initial, goal)
        self.capacities = capacities

    def successor(self, state):
        За дадена состојба, врати речник од парови {акција : состојба}
        достапни од оваа состојба. Ако има многу следбеници, употребете
        итератор кој би ги генерирал следбениците еден по еден, наместо да
        ги генерирате сите одеднаш.
        :param state: дадена состојба
        :return:  речник од парови {акција : состојба} достапни од оваа
                  состојба
        :rtype: dict
        
        successors = dict()

        j0, j1 = state
        c0, c1 = self.capacities

        if j0 > 0:
            successors['Isprazni go sadot J0'] = (0, j1)

        if j1 > 0:
            successors['Isprazni go sadot J1'] = (j0, 0)

        if j0 > 0 and j1 < c1:
            delta = min(c1 - j1, j0)
            successors['Preturi od J0 vo J1'] = (j0 - delta, j1 + delta)

        if j1 > 0 and j0 < c0:
            delta = min(c0 - j0, j1)
            successors['Preturi od J1 vo J0'] = (j0 + delta, j1 - delta)

        return successors

    def actions(self, state):
        За дадена состојба state, врати листа од сите акции што може да
        се применат над таа состојба
        :param state: дадена состојба
        :return: листа на акции
        :rtype: list
        
        return self.successor(state).keys()

    def result(self, state, action):
        За дадена состојба state и акција action, врати ја состојбата
        што се добива со примена на акцијата над состојбата
        :param state: дадена состојба
        :param action: дадена акција
        :return: резултантна состојба
        
        return self.successor(state)[action]

    def goal_test(self, state):
        Врати True ако state е целна состојба. Даденава имплементација
        на методот директно ја споредува state со self.goal, како што е
        специфицирана во конструкторот. Имплементирајте го овој метод ако
        проверката со една целна состојба self.goal не е доволна.
        :param state: дадена состојба
        :return: дали дадената состојба е целна состојба
        :rtype: bool
        
        return state == self.goal


if __name__ == '__main__':
    container = Container([15, 5], (5, 5), (10, 0))

    result = breadth_first_graph_search(container)
    print(result.solution())
    print(result.solve())

    result = depth_first_graph_search(container)
    print(result.solution())
    print(result.solve())
    """