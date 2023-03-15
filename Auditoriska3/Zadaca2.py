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
        #(x, y, (x_o1, y_o1, d_o1), (x_o2, y_o2, d_o2) - state
        successors = dict()
        man_x=state[0]
        man_y=state[1]
        obstacle_1=list(state[2])
        obstacle_2=list(state[3])

#PRVA PRECHKA
        if obstacle_1[2]==1: #up
            if obstacle_1[1]==self.grid_size[1]-1: #bidejki od 0 pocnuvaat zatoa do 5 maksimumot e a ne 6
                obstacle_1[2]=-1
                obstacle_1[1]-=1
            else:
                obstacle_1[1]+=1
        else: #down
            if obstacle_1[1]== 0:
                obstacle_1[2]=1
                obstacle_1[1]+=1
            else:
                obstacle_1[1]-=1
#VTORAPRECHKA
        if obstacle_2[2]==1: #up
            if obstacle_2[1]==self.grid_size[1]-1: #bidejki od 0 pocnuvaat zatoa do 5 maksimumot e a ne 6
                obstacle_2[2]=-1
                obstacle_2[1]-=1
            else:
                obstacle_2[1]+=1
        else: #down
            if obstacle_2[1]== 0:
                obstacle_2[2]=1
                obstacle_2[1]+=1
            else:
                obstacle_2[1]-=1
        obstacles=[(obstacle_1[0], obstacle_1[1]), (obstacle_2[0], obstacle_2[1])]
#CHOVEKOT
 # (x, y, (x_o1, y_o1, d_o1), (x_o2, y_o2, d_o2) - state
        #RIGHT x=x+1
        if man_x+1 <self.grid_size[0] and (man_x+1, man_y) not in obstacles:
            successors["Right"]=(man_x+1, man_y, (obstacle_1[0], obstacle_1[1], obstacle_1[2]), (obstacle_2[0], obstacle_2[1], obstacle_2[2]))
        #LEFT
        if man_x - 1 > 0 and (man_x - 1, man_y) not in obstacles:
            successors["Left"] = (man_x - 1, man_y, (obstacle_1[0], obstacle_1[1], obstacle_1[2]),
                                   (obstacle_2[0], obstacle_2[1], obstacle_2[2]))
        #UP
        if man_y+1 < self.grid_size[1] and (man_x, man_y+1) not in obstacles:
            successors["Up"] = (man_x , man_y+1, (obstacle_1[0], obstacle_1[1], obstacle_1[2]),
                                   (obstacle_2[0], obstacle_2[1], obstacle_2[2]))
        if man_y - 1 > 0 and (man_x, man_y - 1) not in obstacles:
            successors["Down"] = (man_x, man_y - 1, (obstacle_1[0], obstacle_1[1], obstacle_1[2]),
                                (obstacle_2[0], obstacle_2[1], obstacle_2[2]))
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
        #(g0, g1)
        # (x, y, (x_o1, y_o1, d_o1), (x_o2, y_o2, d_o2) - state
        return state[0]==self.goal[0] and state[1]==self.goal[1]


if __name__ == '__main__':
    goal_state=(7,4)
    initial_state=(0,2)
    obstacle1=(2,5,-1)
    obstacle2=(5,0,1)
    explorer=Explorer((initial_state[0], initial_state[1], obstacle1, obstacle2),goal_state)
    print(breadth_first_graph_search(explorer).solution()) #akciite da stigneme do celta
    #['Right', 'Up', 'Right', 'Right', 'Right', 'Up', 'Right', 'Right', 'Right']