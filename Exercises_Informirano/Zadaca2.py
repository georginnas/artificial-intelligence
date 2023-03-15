"""
Истражувач во граф Problem 4 (0 / 0)
Предложете соодветна репрезентација и напишете ги потребните функции во Python за да се реши следниот проблем за кој една можна почетна состојба е прикажана на Слика 1:
Слика 1

“Даден е графот со 16 јазли (крукчиња) прикажан на Слика 1. Играчот може да ја започне играта со позиционирање на кое било од крукчињата означени со X. Играчот може да се
 придвижи од крукчето на кое тековно се наоѓа до некое друго крукче ако постои врска помеѓу нив. Играчот собира ѕвезда ако застане на крукче на кое се наоѓа ѕвездата. Целта
 на играчот е да ги собере сите ѕвезди и притоа важи дека било која врска може да се помине само еднаш (може да сметате дека откако врската ќе биде помината - истата исчезнува)
 . Потребно е проблемот да се реши во најмал број на потези.”

За сите тест примери димензиите и структурата на графот се исти како на примерот даден на сликата. За сите тест примери крукчињата означени со X се исти. За секој тест пример се
менува почетната позиција на играчот, а исто така се менуваат и позициите на ѕвездите. Крукчињата се нумерирани со целите броеви од 1 до 16, одлево - надесно и одгоре - надолу.
 Ова значи дека крукчињата со X секогаш ги имаат редните броеви 6, 7, 10 и 11, соодветно (види ја Слика 1).

Во рамки на почетниот код даден за задачата се вчитуваат влезните аргументи за секој тест пример. Во променливата player_position го имате редниот број на крукчето во кое на почетокот
се наоѓа играчот (некој од целите броеви 6, 7, 10 или 11); во променливата star_one_position го имате редниот број на крукчето во кое се наоѓа првата ѕвезда; во променливата star_two_
position го имате редниот број на крукчето во кое се наоѓа втората ѕвезда.

Движењата на играчот потребно е да ги именувате на следниот начин:

Gore - за придвижување на играчот нагоре кон соседно крукче (крукче до кое постои врска)
Dolu - за придвижување на играчот надолу кон соседно крукче (крукче до кое постои врска)
Levo - за придвижување на играчот налево кон соседно крукче (крукче до кое постои врска)
Desno - за придвижување на играчот надесно кон соседно крукче (крукче до кое постои врска)
DoluDesno - за придвижување на играчот долу-десно кон соседно крукче (крукче до кое постои врска)
GoreLevo - зза придвижување на играчот горе-лево кон соседно крукче (крукче до кое постои врска)
Вашиот код треба да има само еден повик на функција за приказ на стандарден излез (print) со кој ќе ја вратите секвенцата на движења која играчот треба да ја направи за да ги собере двете ѕвезди.
Треба да примените неинформирано пребарување. Врз основа на тест примерите треба самите да определите кое пребарување ќе го користите.


"""

from searching_framework.utils import Problem
from searching_framework.uninformed_search import *
from searching_framework.informed_search import *
from math import *

class Explorer(Problem):
    coordinates={1: (0,3), 2: (1,3), 3: (2,3), 4: (3,3), 5: (0,2), 6: (1,2), 7: (2,2), 8:(3,2), 9:  (0,1), 10: (1,1), 11: (2,1), 12: (3,1), 13: (0,0), 14: (1,0), 15: (2,0), 16: (3,0)}

    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)


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
        # (x, (stars), (links))
        successors = dict()
        player=state[0]
        links=list(state[1])
        stars = list(state[2])

        # DOLUDESNO
        if player + 5 < 17 and (player, player + 5) in links:
            nl1 = tuple([link for link in links if (player, player + 5) != link])
            nl2 = tuple([link for link in list(nl1) if (player + 5, player) != link])
            successors["DoluDesno"] = (player + 5, nl2, tuple([s for s in stars if player + 5 != s]))
        # GORELEVO
        if player - 5 > 0 and (player, player - 5) in links:
            nl1 = tuple([link for link in links if (player, player - 5) != link])
            nl2 = tuple([link for link in list(nl1) if (player - 5, player) != link])
            successors["GoreLevo"] = (player - 5, nl2, tuple([s for s in stars if player - 5 != s]))
        # LEVO
        if player - 1 > 0 and (player, player - 1) in links:
            nl1 = tuple([link for link in links if (player, player - 1) != link])
            nl2 = tuple([link for link in list(nl1) if (player - 1, player) != link])
            successors["Levo"] = (player - 1, nl2, tuple([s for s in stars if player - 1 != s]))
        # DESNO
        if player + 1 < 17 and (player, player + 1) in links:
            nl1 = tuple([link for link in links if (player, player + 1) != link])
            nl2 = tuple([link for link in list(nl1) if (player + 1, player) != link])
            successors["Desno"] = (player + 1, nl2, tuple([s for s in stars if player + 1 != s]))
        #GORE
        if player-4 > 0 and (player, player-4) in links:
            nl1=tuple([link for link in links if (player, player-4) != link])
            nl2=tuple([link for link in list(nl1) if (player-4, player) != link])
            successors["Gore"]=(player-4, nl2, tuple([s for s in stars if player-4 != s]))
        #DOLU
        if player + 4 < 17 and (player, player + 4) in links:
            nl1 = tuple([link for link in links if (player, player + 4) != link])
            nl2 = tuple([link for link in list(nl1) if (player + 4, player) != link])
            successors["Dolu"] = (player + 4, nl2, tuple([s for s in stars if player + 4 != s]))

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


        return len(state[2])==0

    @staticmethod
    def ed(p_pos, s_pos):
        x1,y1=Explorer.coordinates[p_pos]
        x2,y2=Explorer.coordinates[s_pos]
        razlika1=x1-x2
        razlika2=y1-y2
        pow1=pow(razlika1,2)
        pow2=pow(razlika2,2)
        zbir=pow1+pow2
        return sqrt(zbir)
    def h(self, node):
        p_pos=node.state[0]
        stars=node.state[2]

        max=0
        for star in stars:
            val=self.ed(p_pos,star)
            if val>=max:
                max=val
        return max



if __name__ == '__main__':
    player_position = int(input())
    star_one_position = int(input())
    star_two_position = int(input())
    stars=(star_one_position, star_two_position)
    links=((1,2), (1,5), (2,6), (3,7), (3,4), (4,8), (5,6), (6,10), (6,7), (7,11), (7,8), (9,10), (9,13), (10,14), (10,11), (11,15), (11,12), (12,16), (13,14), (15,16), (6,11),(2,1), (5,1), (6,2), (7,3), (4,3), (8,4), (6,5), (10,6),
           (7,6), (11,7), (8,7), (10,9), (13,9), (14,10),(11,10), (15, 11), (12,11), (16,12), (14,13),(16,15), (11,6))
    explorer=Explorer((player_position,links,stars))
    print(astar_search(explorer).solution())