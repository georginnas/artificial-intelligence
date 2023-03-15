"""
SOLITER
Предложете соодветна репрезентација и напишете ги потребните функции во Python за да се реши следниот проблем за кој една можна почетна состојба е прикажана на следната слика.
На табла со димензии N x N, каде N > 3 е непарен природен број, поставени се топчиња. Некои од полињата се неупотребливи т.е. во нив никогаш не може да се поставуваат топчиња
 (на Слика 1 ваквите полиња се обоени со црна боја). Топчињата не се разликуваат помеѓу себе. Со избор (кликнување) на кое било топче може да се направи преместување на тоа топче од полето
 во кое се наоѓа -> преку едно поле (во една од шесте насоки: горе-десно, горе-лево, долу-десно, долу-лево, лево или десно), но само ако „прескокнатото“ поле содржи друго топче и полето до
 „прескокнатото“ поле (во соодветната насока) е слободно. Притоа, „прескокнатото“ топче исчезнува т.е се отстранува од таблата. На пример, со кликнување на топчето кое се наоѓа во петтата редица и
  третата колона на таблата прикажана на Слика 1, топчето кое се наоѓа во полето горе-лево од него ќе исчезне, а кликнатото топче ќе се позиционира во полето што се наоѓа во третата редица и првата колона (види ја Слика 2!).
Не е дозволено топчињата да излегуваат од таблата. Целта е на таблата да остане точно едно топче кое ќе биде позиционирано во централното поле во првата редица, како што е прикажано на Слика 3. Потребно е проблемот да се реши
 во најмал број на потези т.е. со избирање (кликнување) на најмал можен број на топчиња.
"""

from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

def gore_levo(ball, lista_balls, n, obstacles):
    x,y=ball
    li=[]
    if x-1>=0 and y+1<=n and (x-1, y+1) in lista_balls and x-2>=0 and y+2<=n and (x-2, y+2) not in obstacles and (x-2, y+2) not in lista_balls :
        li=[(i,j) for (i,j) in lista_balls if (i,j)!=(x,y) and (i,j)!=(x-1,y+1)]
        li.append((x-2, y+2))
    return li
def gore_desno(ball, lista_balls, n, obstacles):
    x,y=ball
    li=[]
    if x+1<=n and y+1<=n and (x+1, y+1) in lista_balls and x+2<=n and y+2<=n and (x+2, y+2) not in obstacles and (x+2, y+2) not in lista_balls :
        li=[(i,j) for (i,j) in lista_balls if (i,j)!=(x,y) and (i,j)!=(x+1,y+1)]
        li.append((x+2, y+2))
    return li
def dolu_levo(ball, lista_balls, n, obstacles):
    x,y=ball
    li=[]
    if x-1>=0 and y-1>=0 and (x-1, y-1) in lista_balls and x-2>=0 and y-2>=0 and (x-2, y-2) not in obstacles and (x-2, y-2) not in lista_balls :
        li=[(i,j) for (i,j) in lista_balls if (i,j)!=(x,y) and (i,j)!=(x-1,y-1)]
        li.append((x-2, y-2))
    return li
def dolu_desno(ball, lista_balls, n, obstacles):
    x,y=ball
    li=[]
    if x+1<=n and y-1>=0 and (x+1, y-1) in lista_balls and x+2<=n and y-2>=0 and (x+2, y-2) not in obstacles and (x+2, y-2) not in lista_balls :
        li=[(i,j) for (i,j) in lista_balls if (i,j)!=(x,y) and (i,j)!=(x+1,y-1)]
        li.append((x+2, y-2))
    return li
def levo(ball, lista_balls, n, obstacles):
    x,y=ball
    li=[]
    if x-1>=0 and (x-1, y) in lista_balls and x-2>=0 and (x-2, y) not in obstacles and (x-2, y) not in lista_balls :
        li=[(i,j) for (i,j) in lista_balls if (i,j)!=(x,y) and (i,j)!=(x-1,y)]
        li.append((x-2, y))
    return li
def desno(ball, lista_balls, n, obstacles):
    x,y=ball
    li=[]
    if x+1<=n and (x+1, y) in lista_balls and x+2<=n and (x+2, y) not in obstacles and (x+2, y) not in lista_balls :
        li=[(i,j) for (i,j) in lista_balls if (i,j)!=(x,y) and (i,j)!=(x+1,y)]
        li.append((x+2, y))
    return li

class Soliter(Problem):
    def __init__(self, obstacles, n, initial, goal):
        super().__init__(initial,goal)
        self.obstacles=obstacles
        self.n=n

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
        succ={}
        lista_balls=list(state)

        for ball in lista_balls:
            li=lista_balls[:]
            #GORE_LEVO
            new_lista=gore_levo(ball,li,self.n,self.obstacles)
            if lista_balls !=new_lista:
                succ[f'Gore Levo: (x={ball[0]},y={ball[1]})']=tuple(new_lista)
            #GORE_DESNO
            new_lista = gore_desno(ball, li, self.n, self.obstacles)
            if lista_balls != new_lista:
                succ[f'Gore Desno: (x={ball[0]},y={ball[1]})'] = tuple(new_lista)
            #DOLU_LEVO
            new_lista = dolu_levo(ball, li, self.n, self.obstacles)
            if lista_balls != new_lista:
                succ[f'Dolu Levo: (x={ball[0]},y={ball[1]})'] = tuple(new_lista)
            #DOLU_DESNO
            new_lista = dolu_desno(ball, li, self.n, self.obstacles)
            if lista_balls != new_lista:
                succ[f'Dolu Desno: (x={ball[0]},y={ball[1]})'] = tuple(new_lista)
            #LEVO
            new_lista = levo(ball, li, self.n, self.obstacles)
            if lista_balls != new_lista:
                succ[f'Levo: (x={ball[0]},y={ball[1]})'] = tuple(new_lista)
            #DESNO
            new_lista = desno(ball, li, self.n, self.obstacles)
            if lista_balls != new_lista:
                succ[f'Desno: (x={ball[0]},y={ball[1]})'] = tuple(new_lista)
        return succ

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        points=list(state)
        if(len(points)==1):
            if (state[0][0],state[0][1])==(goal[0],goal[1]):
                return True
        return False

if __name__ == "__main__":
    n=int(input())
    m=int(input())
    topki=[]
    for i in range(m):
        topki.append(tuple(input().split(",")))
    k=int(input())
    prepreki=[]
    for j in range(k):
        prepreki.append(tuple(input().split(",")))
    balls=[(int(x),int(y)) for x,y in topki]
    obstacles=[(int(x),int(y)) for x,y in prepreki]
    goal=(n//2,n-1)
    soliter=Soliter(tuple(obstacles),n,(tuple(balls)),tuple(goal))
    print(breadth_first_graph_search(soliter).solution())
