"""Дадена е сложувалка 3x3, на која има полиња со броеви од 1
до 8 и едно празно поле. Празното поле е обележано со ‘*’
Проблемот е како да се стигне од некоја почетна распределба
на полињата до некоја посакувана, на пример:
Акции: акциите ќе ги разгледуваме како придвижување на
празното поле, па можни акции се:
• Горе
• Долу
• Лево
• Десно
• При дефинирањето на акциите, мора да се внимава дали
тие воопшто можат да се преземат во дадената
сложувалка.
Состојбата ќе ја дефинираме како стринг кој ќе има 9 знаци
(по еден за секое бројче, плус ‘*’).
• Притоа, стрингот ќе се пополнува со изминување на
сложувалката од првиот кон третиот ред, од лево кон десно.
• Пример: состојбата за почетната сложувалка е „*32415678“, а
за финалната сложувалка е „*12345678“.
Примери за хевристика
1. Број на полиња кои не се на вистинското место
2. Менхетен растојание до целната состојба
Менхетен растојание
• За да можеме да го дефинираме растојанието,
потребно е да дефинираме координатен систем
• Почетокот на координатниот систем е поставен во
долниот лев агол на сложувалката
• Дефинираме речник за координатите на секое
поле од сложувалката.
• Дефинираме функција која пресметува Менхетн
растојание за сложувалката.
• Оваа функција на влез прима два цели броеви,
кои одговараат на две полиња на кои се наоѓаат
броевите за кои треба да пресметаме растојание

"""
from searching_framework.utils import Problem
from searching_framework.informed_search import greedy_best_first_graph_search, astar_search, \
    recursive_best_first_search


class Puzzle(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def successor(self, state):
        """
        state = '*32415678'
                0 1 2
                3 4 5
                6 7 8
        """
        succ = {}

        ind=state.index("*")

        #Gore i-3, i
        if ind >= 3:
            tmp=list(state)
            tmp[ind], tmp[ind-3]=tmp[ind-3], tmp[ind]
            new_state="".join(tmp)
            succ["Gore"]=new_state
        #Dole i+3, i
        if ind < 6:
            tmp=list(state)
            tmp[ind], tmp[ind+3]=tmp[ind+3], tmp[ind]
            new_state="".join(tmp)
            succ["Dole"]=new_state
        #Levo
        if ind%3!=0 :
            tmp=list(state)
            tmp[ind], tmp[ind-1]=tmp[ind-1], tmp[ind]
            new_state="".join(tmp)
            succ["Levo"]=new_state
        #Desno
        if ind%3!=2 :
            tmp=list(state)
            tmp[ind], tmp[ind+1]=tmp[ind+1], tmp[ind]
            new_state="".join(tmp)
            succ["Desno"]=new_state


        return succ

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        #BROJ NA POLINJA KOI NE SE NA VISTINSKO MESTO
        counter = 0 #ke broime kolku polinja ne se na vistinskoto mesto
        """
        a=[1,2,3] b=[a,b,c]
        zip(a,b)=[(1,a), (2,b), (3,c)]
        *32415678', '*12345678'
        (*,*), (3,1), (2,2)... 
        """
        for x, y in zip(node.state, self.goal):
            if x!=y:
                counter+=1

        return counter


if __name__ == '__main__':
    puzzle = Puzzle('*32415678', '*12345678')
    print(greedy_best_first_graph_search(puzzle).solution())
    print(greedy_best_first_graph_search(puzzle).solve())
    print(astar_search(puzzle).solve())
    print(recursive_best_first_search(puzzle).solve())