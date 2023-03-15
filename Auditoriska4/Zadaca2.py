"""
Предложете соодветна репрезентација и напишете ги потребните функции во Python за да се реши следниот проблем за кој една можна почетна состојба е прикажана на сликата
Потребно е човечето безбедно да дојде до куќичката. Човечето може да се придвижува на кое било соседно поле хоризонтално или вертикално. Пречките 1 и 2 се подвижни, при
што и двете пречки се движат вертикално. Секоја од пречките се придвижува за едно поле во соодветниот правец и насока со секое придвижување на човечето.

Притоа, пречката 1 на почетокот се движи надолу, додека пречката 2 на почетокот се движи нагоре. Пример за положбата на пречките после едно придвижување на човечето надесно
 е прикажан на десната слика.
Кога некоја пречка ќе дојде до крајот на таблата при што повеќе не може да се движи во насоката во која се движела, го менува движењето во спротивната насока. Доколку човечето
и која било од пречките се најдат на исто поле човечето ќе биде уништено.

За сите тест примери изгледот и големината на таблата се исти како на примерот даден на сликите. За сите тест примери почетните положби, правец и насока на движење за препреките
 се исти. За секој тест пример почетната позиција на човечето се менува, а исто така се менува и позицијата на куќичката.

Во рамки на почетниот код даден за задачата се вчитуваат влезните аргументи за секој тест пример.

Движењата на човечето потребно е да ги именувате на следниот начин:

Right - за придвижување на човечето за едно поле надесно
Left - за придвижување на човечето за едно поле налево
Up - за придвижување на човечето за едно поле нагоре
Down - за придвижување на човечето за едно поле надолу
Вашиот код треба да има само еден повик на функција за приказ на стандарден излез (print) со кој ќе ја вратите секвенцата на движења која човечето треба да ја направи за да може од
својата почетна позиција да стигне до позицијата на куќичката.

Треба да примените информирано пребарување. За имплементација на хевристичката функција треба да користите Менхетен растојание.


"""

"""Предложете соодветна репрезентација и напишете ги
потребните функции во Python за да се реши следниот
проблем за кој една можна почетна состојба е прикажана на
сликата.
Потребно е човечето безбедно да дојде до куќичката.
Човечето може да се придвижува на кое било соседно поле
хоризонтално или вертикално.
• Пречките 1 и 2 се подвижни, при што и двете пречки се
движат вертикално. Секоја од пречките се придвижува за едно
поле во соодветниот правец и насока со секое придвижување
на човечето.
• Притоа, пречката 1 на почетокот се движи надолу, додека
пречката 2 на почетокот се движи нагоре. Пример за
положбата на пречките после едно придвижување на човечето
надесно е прикажан на десната слика.
Кога некоја пречка ќе дојде до крајот на таблата при што повеќе не
може да се движи во насоката во која се движела, го менува
движењето во спротивната насока.
• Доколку човечето и која било од пречките се најдат на исто поле
човечето ќе биде уништено.
• За сите тест примери изгледот и големината на таблата се исти
како на примерот даден на сликите. За сите тест примери
почетните положби, правец и насока на движење за препреките се
исти. За секој тест пример почетната позиција на човечето се
менува, а исто така се менува и позицијата на куќичката.
• Во рамки на почетниот код даден за задачата се вчитуваат
влезните аргументи за секој тест пример.
Движењата на човечето потребно е да ги именувате на
следниот начин:
• Right - за придвижување на човечето за едно поле надесно
• Left - за придвижување на човечето за едно поле налево
• Up - за придвижување на човечето за едно поле нагоре
• Down - за придвижување на човечето за едно поле надолу
Вашиот код треба да има само еден повик на функција за
приказ на стандарден излез (print) со кој ќе ја вратите
секвенцата на движења која човечето треба да ја направи за
да може од својата почетна позиција да стигне до позицијата
на куќичката.
• Треба да примените неинформирано пребарување. Врз
основа на тест примерите треба самите да определите кое
пребарување ќе го користите."""
from searching_framework.utils import Problem
from searching_framework.uninformed_search import *
from searching_framework.informed_search import *

def obstacle_up(obstacle):
    x, y, d=obstacle
    if y<5:
        y+=1
    else:
        d*=(-1)
        y-=1
    new_obstacle=(x,y,d)
    return new_obstacle
def obstacle_down(obstacle):
    x, y, d = obstacle
    if y > 0:
        y -= 1
    else:
        d=d*(-1)
        y+=1
    new_obstacle = (x, y, d)
    return new_obstacle

def man_up(x, y, obstacles):
    if y+1 <6  and (x, y+1) not in obstacles:
        y+=1
    new_man=(x,y)
    return new_man
def man_down(x, y, obstacles):
    if y-1 > 0 and (x, y-1) not in obstacles:
        y -= 1
    new_man = (x, y)
    return new_man
def man_left(x, y, obstacles):
    if x-1 > 0 and (x-1, y) not in obstacles:
        x -= 1
    new_man = (x, y)
    return new_man
def man_right(x,y, obstacles):
    if x + 1 < 8 and (x+1, y) not in obstacles: #MOZNO E TUKA DA IMAM GRESKA ZOSTO NEMAM X+1
        x += 1
    new_man = (x, y)
    return new_man

class Explorer(Problem):

    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.grid_size = [8, 6] #ova se dopishuva ako odnapred znaeme koja ke ni bide goleminata na tablata

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
        #(man_x, man_y,(2, 5, -1), (5, 0, 1)
        successors = dict()
        man_x=state[0]
        man_y=state[1]
        man=(man_x,man_y)
        obstacle1=list(state[2])
        obstacle2=list(state[3])
        #PRVA PRECHKA
        if obstacle1[2]==1:
            new_obstacle1=obstacle_up(obstacle1)
        else:
            new_obstacle1=obstacle_down(obstacle1)
        #VTORA PRECHKA
        if obstacle2[2]==1:
            new_obstacle2=obstacle_up(obstacle2)
        else:
            new_obstacle2=obstacle_down(obstacle2)

        obstacles=[(new_obstacle1[0], new_obstacle1[1]), (new_obstacle2[0], new_obstacle2[1])]

        #CHOVEKOT

        #right
        new_man=man_right(man_x, man_y, obstacles)
        if man!=new_man:
            successors["Right"]=(new_man[0], new_man[1], tuple(new_obstacle1), tuple(new_obstacle2))
        # left
        new_man = man_left(man_x, man_y, obstacles)
        if man != new_man:
            successors["Left"] = (new_man[0], new_man[1], tuple(new_obstacle1), tuple(new_obstacle2))
        # up
        new_man = man_up(man_x, man_y, obstacles)
        if man != new_man:
            successors["Up"] = (new_man[0], new_man[1], tuple(new_obstacle1), tuple(new_obstacle2))
        # down
        new_man = man_down(man_x, man_y, obstacles)
        if man != new_man:
            successors["Down"] = (new_man[0], new_man[1], tuple(new_obstacle1), tuple(new_obstacle2))
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
        #(man_x, man_y,(2, 5, -1), (5, 0, 1)
        return state[0]==self.goal[0] and state[1]==self.goal[1]

    def h(self, node):
        x_man=node.state[0]
        y_man=node.state[1]
        x_house=self.goal[0]
        y_house=self.goal[1]
        return abs(x_man-x_house)+abs(y_man-y_house)



if __name__ == '__main__':
    man_x = int(input())
    man_y = int(input())
    house_x = int(input())
    house_y = int(input())

    house = [house_x, house_y]

    explorer=Explorer((man_x, man_y,(2, 5, -1), (5, 0, 1)), house)
    print(breadth_first_graph_search(explorer).solution()) #akciite da stigneme do celta
    print(astar_search(explorer).solution())
