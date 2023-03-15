"""
Задача 3 - Ѕвезди
Предложете соодветна репрезентација и напишете ги потребните функции во Python за да се реши следниот проблем за кој
една можна почетна состојба е прикажана на сликата.
На шаховска табла 8x8 поставени се еден коњ, еден ловец и три ѕвезди. Движењето на коњите на шаховската табла е во облик
на буквата Г: притоа, од дадена позиција можни се 8 позиции до кои даден коњ може да се придвижи, како што е прикажано на
сликата (1 = горе + горе + лево, 2 = горе + горе + десно, 3 = десно + десно + горе, 4 = десно + десно + долу, 5 = долу + +
долу + десно, 6 = долу + долу + лево, 7 = лево + лево + долу, 8 = лево + лево + горе)
Движењето на ловците на таблата е по дијагонала. Ловецот прикажан на сликата може да се придвижи на кое било од полињата
означени со X.
Целта на играта е да се соберат сите три ѕвезди. Една ѕвезда се собира доколку некоја од фигурите застане на истото поле
каде што се наоѓа и ѕвездата.

Притоа, не е дозволено двете фигури да бидат позиционирани на истото поле и не е дозволено фигурите да излегуваат од
таблата. Фигурите меѓусебно не се напаѓаат. Движењето на фигурите е произволно, т.е. во кој било момент може да се придвижи
која било од двете фигури. Потребно е проблемот да се реши во најмал број на потези.

За сите тест примери изгледот и големината на таблата се исти како на примерот даден на сликата. За секој тест пример
положбите на ѕвездите се различни. Исто така, за секој тест пример се менуваат и почетните позиции на коњот и ловецот,
соодветно. Во рамки на почетниот код даден за задачата се вчитуваат влезните аргументи за секој тест пример.

Движењата на коњот потребно е да ги именувате на следниот начин:

K1 - за придвижување од тип 1 (горе + лево)
K2 - за придвижување од тип 2 (горе + десно)
K3 - за придвижување од тип 3 (десно + горе)
K4 - за придвижување од тип 4 (десно + долу)
K5 - за придвижување од тип 5 (долу + десно)
K6 - за придвижување од тип 6 (долу + лево)
K7 - за придвижување од тип 7 (лево + долу)
K8 - за придвижување од тип 8 (лево + горе)
Движењата на ловецот потребно е да ги именувате на следниот начин:

B1 - за придвижување од тип 1 (движење за едно поле во насока горе-лево)
B2 - за придвижување од тип 2 (движење за едно поле во насока горе-десно)
B3 - за придвижување од тип 3 (движење за едно поле во насока долу-лево)
B4 - за придвижување од тип 4 (движење за едно поле во насока долу-десно)
Вашиот код треба да има само еден повик на функција за приказ на стандарден излез (print) со кој ќе ја вратите
секвенцата на движења која треба да се направи за да може фигурите да ги соберат сите три ѕвезди. Треба да примените
неинформирано пребарување. Врз основа на тест примерите треба самите да определите кое пребарување ќе го користите.
"""
from searching_framework.utils import Problem
from searching_framework.uninformed_search import *
            #KNIGHT
def k1(x, y, b_x, b_y): #up up left
    # y+2; x-1
    if 0 < x - 1 < 8 and 0 < y + 2 < 8 and [x-1, y+2]!=[b_x, b_y]:
        x-=1
        y+=2
    return x, y

def k2(x, y, b_x, b_y): #up up right
    # y+2; x+1
    if 0 < x + 1 < 8 and 0 < y + 2 < 8 and [x+1, y+2]!=[b_x, b_y]:
        x+=1
        y+=2
    return x, y

def k3(x, y, b_x, b_y): #right right up
    # y+1; x+2
    if 0 < x + 2 < 8 and 0 < y + 1 < 8 and [x+2, y+1]!=[b_x, b_y]:
        x+=2
        y+=1
    return x, y

def k4(x, y, b_x, b_y): #right right down
    # y-1; x+2
    if 0 < x + 2 < 8 and 0 < y - 1 < 8 and [x+2, y-1]!=[b_x, b_y]:
        x+=2
        y-=1
    return x, y

def k5(x, y, b_x, b_y): #down down right
    # y-2; x+1
    if 0 < x + 1 < 8 and 0 < y - 2 < 8 and [x+1, y-2]!=[b_x, b_y]:
        x+=1
        y-=2
    return x, y

def k6(x, y, b_x, b_y): #down down left
    # y-2; x-1
    if 0 < x - 1 < 8 and 0 < y - 2 < 8 and [x-1, y-2]!=[b_x, b_y]:
        x-=1
        y-=2
    return x, y

def k7(x, y, b_x, b_y): #left left down
    # y-1; x-2
    if 0 < x - 2 < 8 and 0 < y - 1 < 8 and [x-2, y-1]!=[b_x, b_y]:
        x-=2
        y-=1
    return x, y

def k8(x, y, b_x, b_y): #left left up
    # y+1; x-2
    if 0 < x - 2 < 8 and 0 < y + 1 < 8 and [x-2, y+1]!=[b_x, b_y]:
        x-=2
        y+=1
    return x, y

        #BISHOP
def b1(x, y, k_x, k_y): #up left
    # x-1;  y+1
    if 0 < x-1 < 8 and 0 < y+1 < 8 and [x-1, y+1] != [k_x, k_y]:
        x-=1
        y+=1
    return x, y

def b2(x, y, k_x, k_y): #up right
    # x+1;  y+1
    if 0 < x+1 < 8 and 0 < y+1 < 8 and [x+1, y+1] != [k_x, k_y]:
        x+=1
        y+=1
    return x, y

def b3(x, y, k_x, k_y): #down left
    # x-1;  y-1
    if 0 < x-1 < 8 and 0 < y-1 < 8 and [x-1, y-1] != [k_x, k_y]:
        x-=1
        y-=1
    return x, y

def b4(x, y, k_x, k_y): #down right
    # x+1;  y-1
    if 0 < x+1 < 8 and 0 < y-1 < 8 and [x+1, y-1] != [k_x, k_y]:
        x+=1
        y-=1
    return x, y


class Stars(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.grid_size=[8,8]

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
        successors = dict()
        #(kx, ky, bx, by, ((star1_x, star1_y), ...)

        knight_x=state[0]
        knight_y=state[1]

        bishop_x=state[2]
        bishop_y=state[3]

        star_pos=state[4]

        nex_x, new_y=k1(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [nex_x, new_y]:
            successors["K1"]=(nex_x, new_y, bishop_x, bishop_y, tuple([s for s in star_pos if (nex_x, new_y) != (s[0], s[1])]))

        nex_x, new_y = k2(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [nex_x, new_y]:
            successors["K2"] = (nex_x, new_y, bishop_x, bishop_y, tuple([s for s in star_pos if (nex_x, new_y) != (s[0], s[1])]))

        nex_x, new_y = k3(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [nex_x, new_y]:
            successors["K3"] = (nex_x, new_y, bishop_x, bishop_y, tuple([s for s in star_pos if (nex_x, new_y) != (s[0], s[1])]))

        nex_x, new_y = k4(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [nex_x, new_y]:
            successors["K4"] = (nex_x, new_y, bishop_x, bishop_y, tuple([s for s in star_pos if (nex_x, new_y) != (s[0], s[1])]))

        nex_x, new_y = k5(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [nex_x, new_y]:
            successors["K5"] = (nex_x, new_y, bishop_x, bishop_y, tuple([s for s in star_pos if (nex_x, new_y) != (s[0], s[1])]))

        nex_x, new_y = k6(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [nex_x, new_y]:
            successors["K6"] = (nex_x, new_y, bishop_x, bishop_y, tuple([s for s in star_pos if (nex_x, new_y) != (s[0], s[1])]))

        nex_x, new_y = k7(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [nex_x, new_y]:
            successors["K7"] = (nex_x, new_y, bishop_x, bishop_y, tuple([s for s in star_pos if (nex_x, new_y) != (s[0], s[1])]))

        nex_x, new_y = k8(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [nex_x, new_y]:
            successors["K8"] = (nex_x, new_y, bishop_x, bishop_y, tuple([s for s in star_pos if (nex_x, new_y) != (s[0], s[1])]))

        nex_x, new_y=b1(bishop_x, bishop_y, knight_x, knight_y)
        if[bishop_x, bishop_y] != [nex_x, new_y]:
            successors["B1"]=(knight_x, knight_y, nex_x, new_y, tuple([s for s in star_pos if (nex_x, new_y)!= (s[0], s[1])]))

        nex_x, new_y = b2(bishop_x, bishop_y, knight_x, knight_y)
        if [bishop_x, bishop_y] != [nex_x, new_y]:
            successors["B2"] = (
            knight_x, knight_y, nex_x, new_y, tuple([s for s in star_pos if (nex_x, new_y) != (s[0], s[1])]))

        nex_x, new_y = b3(bishop_x, bishop_y, knight_x, knight_y)
        if [bishop_x, bishop_y] != [nex_x, new_y]:
            successors["B3"] = (
            knight_x, knight_y, nex_x, new_y, tuple([s for s in star_pos if (nex_x, new_y) != (s[0], s[1])]))
        nex_x, new_y = b4(bishop_x, bishop_y, knight_x, knight_y)
        if [bishop_x, bishop_y] != [nex_x, new_y]:
            successors["B4"] = (
            knight_x, knight_y, nex_x, new_y, tuple([s for s in star_pos if (nex_x, new_y) != (s[0], s[1])]))


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
        #(kx, ky, bx, by, stars)
        return len(state[4]) == 0


if __name__ == '__main__':
    knight =[2,5]
    bishop = [5,1]
    stars_positions=((1,1), (4,3), (6,6))
    stars=Stars((knight[0], knight[1], bishop[0], bishop[1], stars_positions))
