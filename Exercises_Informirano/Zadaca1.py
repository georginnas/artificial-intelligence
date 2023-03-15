"""Подвижни препреки Problem 3 (0 / 0)
Предложете соодветна репрезентација и напишете ги потребните функции во Python за да се реши следниот проблем за кој една можна почетна состојба е прикажана на слика 1:
"Потребно е човечето безбедно да дојде до куќичката. Човечето може да се придвижува на кое било соседно поле хоризонтално или вертикално. Пречките 1, 2 и 3 се подвижни,
при што пречката 1 се движи хоризонтално, пречката 2 се движи дијагонално, а пречката 3 се движи вертикално. Секоја од пречките се придвижува за едно поле во соодветниот
правец и насока со секое придвижување на човечето. Притоа пречката 1 на почетокот се движи во лево, пречката 2 на почетокот се движи горе-десно и пречката 3 на почетокот се движи
nадолу (пример за положбата на пречките после едно придвижување на човечето е прикажан на слика 2). Кога некоја пречка ќе дојде до крајот на таблата при што повеќе не може да се движи
во насоката во која се движела, го менува движењето во спротивната насока. Доколку човечето и која било од пречките се најдат на исто поле - човечето ќе биде уништено."
Слика 2

За сите тест примери изгледот и големината на таблата се исти како на примерот даден на сликите. За сите тест примери почетните положби, правец и насока на движење за препреките се исти.
За секој тест пример почетната позиција на човечето се менува, а исто така се менува и позицијата на куќичката.

Во рамки на почетниот код даден за задачата се вчитуваат влезните аргументи за секој тест пример. Во променливите man_x и man_y ги имате x и y координатите во кои на почетокот се наоѓа човечето
(ако таблата ја гледате во стандардниот координатен систем). Во променливите house_x и house_y ги имате x и y координатите во кои се наоѓа куќичката (ако таблата ја гледате во стандардниот координатен систем).

Движењата на човечето потребно е да ги именувате на следниот начин:

Desno - за придвижување на човечето за едно поле надесно
Levo - за придвижување на човечето за едно поле налево
Gore - за придвижување на човечето за едно поле нагоре
Dolu - за придвижување на човечето за едно поле надолу
Вашиот код треба да има само еден повик на функција за приказ на стандарден излез (print) со кој ќе ја вратите секвенцата на движења која човечето треба да ја направи за да може од својата почетна позиција
 да стигне до позицијата на куќичката. Треба да примените неинформирано пребарување. Врз основа на тест примерите треба самите да определите кое пребарување ќе го користите.
"""

from searching_framework.utils import Problem
from searching_framework.uninformed_search import *
from searching_framework.informed_search import *

def updateO1(obstacle1):
    obstacle1_new=[list(obstacle1[0]), list(obstacle1[1])]
    k1=obstacle1_new[0]
    k2=obstacle1_new[1]
    d=obstacle1[2]

    if d==-1: #odi levo
        if k1[0]==0:
            d=1
            k1[0]+=1
            k2[0]+=1
        else:
            k1[0]-=1
            k2[0]-=1
    else: #d==1
        if k2[0]==5:
            d=-1
            k1[0]-=1
            k2[0]-=1
        else:
            k1[0]+=1
            k2[0]+=1
    n_state=((k1[0],k1[1]),(k2[0],k2[1]),d)
    return n_state

def updateO2(obstacle2):
    obstacle2_new = [list(obstacle2[0]), list(obstacle2[1]),list(obstacle2[2]), list(obstacle2[3])]
    k1=obstacle2_new[0]
    k2=obstacle2_new[1]
    k3=obstacle2_new[2]
    k4=obstacle2_new[3]
    d=obstacle2[4]

    if d==1: #desnogore
        if k4[0]==5 and k4[1]==5 and k1[0]==4 and k1[1]==4:
            d=-1
            k1[0]-=1
            k1[1]-=1
            k2[0]-=1
            k2[1]-=1
            k3[0]-=1
            k3[1]-=1
            k4[0]-=1
            k4[1]-=1
        else:
            k1[0] += 1
            k1[1] += 1
            k2[0] += 1
            k2[1] += 1
            k3[0] += 1
            k3[1] += 1
            k4[0] += 1
            k4[1] += 1
    else: #levodolu
        if k1[0]==0 and k1[1]==0 and k4[1]==1 and k4[0]==1:
            d=1
            k1[0] += 1
            k1[1] += 1
            k2[0] += 1
            k2[1] += 1
            k3[0] += 1
            k3[1] += 1
            k4[0] += 1
            k4[1] += 1
        else:
            k1[0] -= 1
            k1[1] -= 1
            k2[0] -= 1
            k2[1] -= 1
            k3[0] -= 1
            k3[1] -= 1
            k4[0] -= 1
            k4[1] -= 1
    n_state = ((k1[0], k1[1]), (k2[0], k2[1]),(k3[0], k3[1]), (k4[0], k4[1]), d)
    return n_state

def updateO3(obstacle3):
    obstacle3_new = [list(obstacle3[0]), list(obstacle3[1])]
    k1 = obstacle3_new[0]
    k2 = obstacle3_new[1]
    d = obstacle3[2]

    if d == 1:  # odi gore
        if k2[1]==5:
            d = -1
            k1[1] -=1
            k2[1]-=1
        else:
            k1[1] += 1
            k2[1] += 1
    else:  # d odi dolu
        if k1[1]==0:
            d = 1
            k1[1] += 1
            k2[1] += 1
        else:
            k1[1] -= 1
            k2[1] -= 1

    n_state = ((k1[0], k1[1]), (k2[0], k2[1]), d)
    return n_state

class Explorer(Problem):

    def __init__(self, static_obstacles, initial, goal):
        super().__init__(initial, goal)
        self.static_obstacles=static_obstacles


    def successor(self, state):
        """За дадена состојба, врати речник од парови {акција : состојба}
        достапни од оваа состојба. Ако има многу следбеници, употребете
        итератор кој би ги генерирал следбениците еден по еден, наместо да
        ги генерирате сите одеднаш.
        :param state: дадена состојба
        :return:  речник од парови {акција : состојба} достапни од оваа
                  состојба
        :rtype: dict
        """
        # (x, y, obstacle1, obstacle2, obstacle3)
        #(x, y, (x_o1, y_o1, d_o1), (x_o2, y_o2, d_o2) - state
        successors = dict()
        man_x=state[0]
        man_y=state[1]
        obstacle1=list(state[2])
        obstacle2=list(state[3])
        obstacle3=list(state[4])
        obstacle1_new=updateO1(obstacle1)
        obstacle2_new=updateO2(obstacle2)
        obstacle3_new=updateO3(obstacle3)
        obstacle11_new = (obstacle1_new[0], obstacle1_new[1])
        obstacle22_new = (obstacle2_new[0], obstacle2_new[1], obstacle2_new[2], obstacle2_new[3])
        obstacle33_new = (obstacle3_new[0],obstacle3_new[1])


        # (x, y, (((k1), (k2), d), ((k1),(k2),(k3),(k4), d), ((k1),(k2),d))) - state
        #RIGHT
        if man_x+1<=10 and (man_x+1,man_y) not in self.static_obstacles and (man_x+1,man_y) not in obstacle11_new and (man_x+1,man_y) not in obstacle22_new and (man_x+1,man_y) not in obstacle33_new:
            successors["Right"]=(man_x+1, man_y, tuple(obstacle1_new), tuple(obstacle2_new), tuple(obstacle3_new))
        #LEFT
        if man_x-1>=0 and (man_x-1,man_y) not in self.static_obstacles and (man_x-1,man_y) not in obstacle11_new and (man_x-1,man_y) not in obstacle22_new and (man_x-1,man_y) not in obstacle33_new:
            successors["Left"]=(man_x-1, man_y,  tuple(obstacle1_new), tuple(obstacle2_new), tuple(obstacle3_new))
        #UP
        if man_y + 1 <= 10 and (man_x, man_y+1) not in self.static_obstacles and (man_x, man_y+1) not in obstacle11_new and (man_x, man_y+1) not in obstacle22_new and (man_x, man_y+1) not in obstacle33_new:
            successors["Up"] = (man_x, man_y+1, tuple(obstacle1_new), tuple(obstacle2_new), tuple(obstacle3_new))
        #DOWN
        if man_y - 1 >= 0 and (man_x, man_y - 1) not in self.static_obstacles and (man_x, man_y - 1) not in obstacle11_new and (man_x, man_y - 1) not in obstacle22_new and (man_x, man_y - 1) not in obstacle33_new:
                successors["Down"] = (man_x, man_y - 1, tuple(obstacle1_new), tuple(obstacle2_new), tuple(obstacle3_new))

        return successors


    def actions(self, state):
        """За дадена состојба state, врати листа од сите акции што може да
        се применат над таа состојба
        :param state: дадена состојба
        :return: листа на акции
        :rtype: list
        """
        return self.successor(state).keys()

    def result(self, state, action):
        """За дадена состојба state и акција action, врати ја состојбата
        што се добива со примена на акцијата над состојбата
        :param state: дадена состојба
        :param action: дадена акција
        :return: резултантна состојба
        """
        return self.successor(state)[action]

    def goal_test(self, state):
        """Врати True ако state е целна состојба. Даденава имплементација
        на методот директно ја споредува state со self.goal, како што е
        специфицирана во конструкторот. Имплементирајте го овој метод ако
        проверката со една целна состојба self.goal не е доволна.
        :param state: дадена состојба
        :return: дали дадената состојба е целна состојба
        :rtype: bool
        """


        return state[0]==self.goal[0] and state[1]==self.goal[1]

    @staticmethod
    def mhd(man_x, man_y, house_x, house_y):
        return abs(man_x-house_x)+abs(man_y-house_y)

    def h(self, node):
        man_x=node.state[0]
        man_y=node.state[1]
        house_x=self.goal[0]
        house_y=self.goal[1]
        val=self.mhd(man_x,man_y,house_x,house_y)
        return val



if __name__ == '__main__':
    static_obstacles=((6,6), (6,7), (6,8), (6,9), (6,10),(7,6), (7,7), (7,8), (7,9), (7,10),(8,6), (8,7), (8,8), (8,9), (8,10),(9,6), (9,7), (9,8), (9,9), (9,10),(10,6), (10,7), (10,8), (10,9), (10,10))
    man_x=int(input())
    man_y=int(input())
    house_x=int(input())
    house_y=int(input())
    obstacle1=((2,8),(3,8),-1)
    obstacle2=((2,2),(3,2),(2,3),(3,3),1)
    obstacle3=((8,2),(8,3),-1)
    goal_state=(house_x,house_y)
    # (x, y, obstacle1, obstacle2, obstacle3)
    # (x, y, (((k1), (k2), d), ((k1),(k2),(k3),(k4), d), ((k1),(k2),d))) - state
    explorer=Explorer(static_obstacles,(man_x, man_y, obstacle1,obstacle2,obstacle3),goal_state)
    print(astar_search(explorer).solution())


