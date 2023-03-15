"""Дискови Problem 2 (0 / 0)
Предложете соодветна репрезентација и напишете ги потребните функции во Python за да се реши следниот проблем за кој една можна почетна
состојба е прикажана на Слика 1.

“На една лента составена од L полиња поставени се N дискови (N < L). Дисковите се меѓусебно различни и се нумерирани со целите броеви од
1 до N. На почетокот, дисковите се позиционирани во првите N полиња од лентата (гледајќи одлево - надесно), подредени во растечки редослед
според нивните редни броеви (Слика 1 - почетна состојба за N = 3 и L = 7). Потребно е дисковите да се доведат на крајот на лентата
(во последните N полиња од лентата, гледајќи одлево - надесно), при што ќе бидат подредени во опаѓачки редослед според нивните редни броеви
(како пример, на Слика 2 е прикажана целната состојба која што соодветствува на почетната состојба прикажана на Слика 1). Во еден потег,
еден диск може да се премести од полето во кое се наоѓа во соседно празно поле (лево или десно). Исто така, диск може да се премести и од
полето во кое се наоѓа -> преку едно поле (во лево или десно), но само ако притоа „прескокнатото“ поле содржи друг диск (на пример, може да
 се премести диск од првото во третото поле само ако третото поле е празно и второто поле содржи друг диск!). Не е дозволено дисковите да
 излегуваат од лентата. Потребно е проблемот да се реши во најмал број на потези.”

За сите тест примери изгледот на лентата е ист како на примерот даден на сликите. За сите тест примери распоредот на дисковите на почетокот
 е ист (како што беше објаснето погоре). За секој тест пример се менува бројот на дискови, а исто така се менува и димензијата на лентата.

Од стандарден влез се вчитуваат влезните аргументи за секој тест пример. Најпрво е даден бројот на дискови (N), а потоа се чита димензијата
на лентата (бројот на полиња од кои што е составена истата, L).

Движењата на дисковите потребно е да ги именувате на следниот начин:

D1: Disk i - за преместување на дискот i надесно во соседно празно поле, i = 1, 2, ..., N
D2: Disk i - за преместување на дискот i преку едно поле надесно, i = 1, 2, ..., N
L1: Disk i - за преместување на дискот i налево во соседно празно поле, i = 1, 2, ..., N
L2: Disk i - за преместување на дискот i преку едно поле налево, i = 1, 2, ..., N
Вашиот код треба да има само еден повик на функција за приказ на стандарден излез (print) со кој ќе ја вратите секвенцата
 на движења која треба да се направи за да може дисковите да се доведат на бараните позиции. Треба да примените неинформирано пребарување.
  Врз основа на тест примерите треба самите да определите кое пребарување ќе го користите.

НАПОМЕНА: Подреденоста на акциите во successor функција е важна кај неинформирано пребарување. Соодветно, за да се добие решението
кое се очекува во изгенерираните излези, редоследот треба да биде D1, D2, L1, L2, за секое од полињата во лентата последователно,
почнувајќи од почетокот. Доколку акциите не се подредени со истиот редослед, можно е да се најде исто оптимално решение со различна
патека."""
from searching_framework.utils import Problem
from searching_framework.uninformed_search import *
from searching_framework.informed_search import *

def D1(i, lista):
    lista_new=lista[:]
    if i < len(lista)-1 and lista[i+1]==0:
        lista_new[i+1]=lista[i]
        lista_new[i]=0
    return tuple(lista_new)

def D2(i, lista):
    lista_new=lista[:]
    if i+2 < len(lista) and lista[i+2]==0 and lista[i+1]!=0:
        lista_new[i+2]=lista[i]
        lista_new[i]=0
    return tuple(lista_new)

def L1(i, lista):
    lista_new=lista[:]
    if i > 0 and lista[i-1]==0:
        lista_new[i-1]=lista[i]
        lista_new[i]=0
    return tuple(lista_new)
def L2(i, lista):
    lista_new=lista[:]
    if i > 1 and lista[i-2]==0 and lista[i-1]!=0:
        lista_new[i-2]=lista[i]
        lista_new[i]=0
    return tuple(lista_new)

class Disk(Problem):
    def __init__(self, initial, goal):
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
        successors=dict()

        lista=list(state)

        for i in range(0, len(lista)):
            if lista[i]!=0:
                # D1
                new_state=D1(i, lista)
                if new_state!=state:
                    successors[f'D1: Disk {lista[i]}']=new_state
                # D2
                new_state = D2(i, lista)
                if new_state != state:
                    successors[f'D2: Disk {lista[i]}'] = new_state
                # L1
                new_state = L1(i, lista)
                if new_state != state:
                    successors[f'L1: Disk {lista[i]}'] = new_state
                # L2
                new_state = L2(i, lista)
                if new_state != state:
                    successors[f'L2: Disk {lista[i]}'] = new_state
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
        :return: резултантна состојба(
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
        return state==self.goal
    def h(self, node):
        state_l=list(node.state)
        goal_l=list(self.goal)
        value=0
        for x, y in zip(state_l,goal_l):
            if x != y and x!=0: # moze i samo value/2
                value+=1
        return value
"""
1 2 3 0 0 0 0 state
0 0 0 0 3 2 1 goal
so zip:
1 0
2 0
3 0
0 3
0 2
0 1
ova dava kolku ne se na mesto znaci ni vrakja 6 , a treba da ni vrati tri , zatoa sto tri elementi ne se na mesto nie nemame 6 elementi...
"""


if __name__=="__main__":
    diskovi=int(input())
    dolzina=int(input())

    lista=[]
    for i in range(1,diskovi+1):
        lista.append(i)
    for i in range(diskovi, dolzina):
        lista.append(0)
    l1=lista[:]
    lista.reverse()
    diskovi=Disk(tuple(l1), tuple(lista))
    print(astar_search(diskovi).solution())