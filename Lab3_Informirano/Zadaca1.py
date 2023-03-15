"""Pacman Problem 1 (0 / 0)
Предложете соодветна репрезентација на играта Pacman и напишете ги потребните функции во Python за да се реши следниот
проблем за кој една можна почетна состојба е прикажана на Слика 1:
Во табла со димензии 10x10 се наоѓа човече. Човечето може да се придвижува на кое било соседно поле хоризонтално или вертикално,
доколку на соодветната позиција не постои пречка. Потребно е човечето да ги изеде сите точки поставени во таблата. Во даден момент можни
се четири акции на движење на човечето: продолжи право, продолжи назад, сврти лево и сврти десно. На Слика 2 се прикажани можните движења
на човечето за две насоки, каде што со сина боја е обележана новата позиција добиена со акцијата продолжи право, продолжи назад со црвена
боја, сврти лево со сива боја и сврти десно со зелена боја. Потребно е проблемот да се реши во најмал број на потези.
За сите тест примери изгледот и големината на таблата се исти како на примерот даден на Слика 1. За сите тест примери позициите на пречките се исти.
За секој тест пример почетната позиција на човечето се менува, а исто така се менуваат и позиците на точките.

Од стандарден влез се читаат почетните x и y координати во кои на почетокот се наоѓа човечето (ако таблата ја гледате во
стандардниот координатен систем). Следно се чита насоката кон која е поставен играчот ('istok', 'zapad', 'sever', 'jug'). Потоа
се чита број на точки во таблата, по што во секој нов ред се читаат x и y координатите на точките во таблата (ако таблата ја гледате во
стандардниот координатен систем).

Движењата на човечето потребно е да ги именувате на следниот начин:

ProdolzhiPravo - за придвижување на човечето за едно поле нанапред
ProdolzhiNazad - за придвижување на човечето за едно поле наназад
SvrtiLevo - за придвижување на човечето за едно поле налево
SvrtiDesno - за придвижување на човечето за едно поле надесно
Вашиот код треба да има само еден повик на функција за приказ на стандарден излез (print) со кој ќе ја вратите секвенцата
на движења која човечето треба да ја направи за да може од својата почетна позиција да стигне до позицијата на куќичката.
Треба да примените неинформирано пребарување. Врз основа на тест примерите треба самите да определите кое пребарување ќе го користите.

НАПОМЕНА: Подреденоста на акциите во successor функција е важна кај неинформирано пребарување. Соодветно, за да се добие решението кое
се очекува во изгенерираните излези, редоследот треба да биде ProdolzhiPravo, ProdolzhiNazad, SvrtiLevo, SvrtiDesno. Доколку акциите не
се подредени со истиот редослед, можно е да се најде исто оптимално решение со различна патека.

Your solution:Programming language: Python36
1

gegekj
Full Screen F11heigth: A- A A+Select a theme:
default
Sample input
0
0
istok
5
2,6
4,0
6,5
8,2
8,3
Sample output
['ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiNazad', 'ProdolzhiPravo', 'SvrtiDesno',
'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiNazad', 'ProdolzhiPravo',
'SvrtiLevo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiLevo', 'ProdolzhiNazad', 'ProdolzhiPravo', 'SvrtiLevo',
'ProdolzhiPravo', 'SvrtiDesno']
"""


"""
Дефинирање на класа за структурата на проблемот кој ќе го решаваме со пребарување.
Класата Problem е апстрактна класа од која правиме наследување за дефинирање на основните 
карактеристики на секој проблем што сакаме да го решиме
"""
from searching_framework.utils import Problem
from searching_framework.uninformed_search import *
from searching_framework.informed_search import *

def pac_up(x, y, obstacles):
    if y<9 and (x,y+1) not in obstacles:
        y+=1
    return y
def pac_down(x, y, obstacles):
    if y>0 and (x,y-1) not in obstacles:
        y-=1
    return y
def pac_left(x, y, obstacles):
    if x>0 and (x-1,y) not in obstacles:
        x-=1
    return x
def pac_right(x, y, obstacles):
    if x<9 and (x+1,y) not in obstacles:
        x+=1
    return x

class Pacman(Problem):

    def __init__(self, obstacles, initial, goal=None):
        super().__init__(initial, goal)
        self.obstacles = obstacles
        self.grid_size = [10, 10] #ova se dopishuva ako odnapred znaeme koja ke ni bide goleminata na tablata

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
        successors=dict()
        pac_x=state[0]
        pac_y=state[1]
        direction=state[2]
        food_list=state[3]

        if direction=='istok':
            x_new=pac_right(pac_x,pac_y,self.obstacles)
            if x_new!=pac_x:
                successors["ProdolzhiPravo"]=(x_new, pac_y, 'istok', tuple([food for food in food_list if (x_new, pac_y) != (food[0], food[1])]))

            x_new = pac_left(pac_x, pac_y, self.obstacles)
            if x_new != pac_x:
                successors["ProdolzhiNazad"] = (x_new, pac_y, 'zapad', tuple([food for food in food_list if (x_new, pac_y) != (food[0], food[1])]))

            y_new = pac_up(pac_x, pac_y, self.obstacles)
            if y_new != pac_y:
                successors["SvrtiLevo"] = (pac_x, y_new, 'sever', tuple([food for food in food_list if (pac_x, y_new) != (food[0], food[1])]))

            y_new = pac_down(pac_x, pac_y, self.obstacles)
            if y_new != pac_y:
                successors["SvrtiDesno"] = (pac_x, y_new, 'jug', tuple([food for food in food_list if (pac_x, y_new) != (food[0], food[1])]))


        if direction =="zapad":
            x_new = pac_left(pac_x, pac_y, self.obstacles)
            if x_new != pac_x:
                successors["ProdolzhiPravo"] = (x_new, pac_y, 'zapad', tuple([food for food in food_list if (x_new, pac_y) != (food[0], food[1])]))

            x_new = pac_right(pac_x, pac_y, self.obstacles)
            if x_new != pac_x:
                successors["ProdolzhiNazad"] = (x_new, pac_y, 'istok', tuple([food for food in food_list if (x_new, pac_y) != (food[0], food[1])]))

            y_new = pac_down(pac_x, pac_y, self.obstacles)
            if y_new != pac_y:
                successors["SvrtiLevo"] = (pac_x, y_new, 'jug', tuple([food for food in food_list if (pac_x, y_new) != (food[0], food[1])]))

            y_new = pac_up(pac_x, pac_y, self.obstacles)
            if y_new != pac_y:
                successors["SvrtiDesno"] = (pac_x, y_new, 'sever', tuple([food for food in food_list if (pac_x, y_new) != (food[0], food[1])]))

        if direction=="sever":
            y_new = pac_up(pac_x, pac_y, self.obstacles)
            if y_new != pac_y:
                successors["ProdolzhiPravo"] = (pac_x, y_new, 'sever',tuple([food for food in food_list if (pac_x, y_new) != (food[0], food[1])]))

            y_new = pac_down(pac_x, pac_y, self.obstacles)
            if y_new != pac_y:
                successors["ProdolzhiNazad"] = (pac_x, y_new, 'jug', tuple([food for food in food_list if (pac_x, y_new) != (food[0], food[1])]))

            x_new = pac_left(pac_x, pac_y, self.obstacles)
            if x_new != pac_x:
                successors["SvrtiLevo"] = (x_new, pac_y, 'zapad', tuple([food for food in food_list if (x_new, pac_y) != (food[0], food[1])]))

            x_new = pac_right(pac_x, pac_y, self.obstacles)
            if x_new != pac_x:
                successors["SvrtiDesno"] = (x_new, pac_y, 'istok', tuple([food for food in food_list if (x_new, pac_y) != (food[0], food[1])]))


        if direction=="jug":
            y_new = pac_down(pac_x, pac_y, self.obstacles)
            if y_new != pac_y:
                successors["ProdolzhiPravo"] = (pac_x, y_new, 'jug', tuple([food for food in food_list if (pac_x, y_new) != (food[0], food[1])]))

            y_new = pac_up(pac_x, pac_y, self.obstacles)
            if y_new != pac_y:
                successors["ProdolzhiNazad"] = (pac_x, y_new, 'sever', tuple([food for food in food_list if (pac_x, y_new) != (food[0], food[1])]))

            x_new = pac_right(pac_x, pac_y, self.obstacles)
            if x_new != pac_x:
                successors["SvrtiLevo"] = (x_new, pac_y, 'istok', tuple([food for food in food_list if (x_new, pac_y) != (food[0], food[1])]))

            x_new = pac_left(pac_x, pac_y, self.obstacles)
            if x_new != pac_x:
                successors["SvrtiDesno"] = (x_new, pac_y, 'zapad', tuple([food for food in food_list if (x_new, pac_y) != (food[0], food[1])]))

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

        return len(state[-1])==0
    @staticmethod
    def md(x1, y1, x2, y2):
        return abs(x1-x2)+abs(y1-y2)
    def h(self, node):
        pac_x= node.state[0]
        pac_y =node.state[1]
        food_list = list(node.state[3])
        flag=1
        max=0
        for food in food_list:
            val = self.md(pac_x, pac_y, food[0], food[1])
            if flag==1:
                max=val
                flag=0
            if val>=max:
                max=val
        return max

    """  @staticmethod TOCNO E I OVA
    def md(x1, y1, x2, y2):
        return abs(x1-x2)+abs(y1-y2)
    def h(self, node):
        pac_x= node.state[0]
        pac_y =node.state[1]
        food_list = list(node.state[3])
        flag=1
        min=0
        for food in food_list:
            val = self.md(pac_x, pac_y, food[0], food[1])
            if flag==1:
                min=val
                flag=0
            if val<=min:
                min=val
        return min"""



if __name__=="__main__":
    obstacle_list=((0,6), (0,8), (0,9), (1,2), (1,3), (1,4), (1,9), (2,9), (3,6), (3,9), (4,1), (4,5), (4,6), (4,7), (5,1), (5,6), (6,0), (6,1), (6,2), (6,9), (8,1), (8,4), (8,7), (8,8), (9,4), (9,7), (9,8))
    pac_x=int(input())
    pac_y=int(input())
    direction=input()
    n=int(input())
    food_list=[]
    for i in range(0,n):
        broevi=input().split(",")
        lista=[int(broevi[0]), int(broevi[1])]
        br=tuple(lista)
        food_list.append(br)
    pacman=Pacman(obstacle_list,(pac_x, pac_y, direction, tuple(food_list)))
    print(astar_search(pacman).solution())

"""
['ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiNazad', 'ProdolzhiPravo', 'SvrtiDesno', 'ProdolzhiPravo', 'ProdolzhiPravo',
 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiNazad', 'ProdolzhiPravo', 'SvrtiLevo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiLevo', 'SvrtiDesno',
  'SvrtiDesno', 'ProdolzhiPravo', 'SvrtiLevo', 'ProdolzhiPravo', 'SvrtiDesno']"""
