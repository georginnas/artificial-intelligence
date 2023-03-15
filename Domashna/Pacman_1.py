from searching_framework.utils import Problem
from searching_framework.uninformed_search import *
from searching_framework.informed_search import *



class Pacman(Problem):

    def __init__(self, obstacles, grid_size, initial, goal=None):
        super().__init__(initial, goal)
        self.obstacles = obstacles
        self.grid_size =grid_size

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
        # ((0, 2, 'jug'),(8, 1))
        succ=dict()
        pac1,new_ghost=state
        ghost=state[1]
        old_state=state

        #PAC1---------------------------------------------------------------------------------------------------------
        #GORE
        if pac1[2]=="sever":
            new_pac=(pac1[0],pac1[1],'zapad')
            new_state=(new_pac,new_ghost)
            if new_state!=old_state:
                succ["Zavrti se levo PAC1"]=new_state

            new_pac = (pac1[0], pac1[1], 'istok')
            new_state = (new_pac, new_ghost)
            if new_state != old_state:
                succ["Zavrti se desno PAC1"] = new_state

            new_pac=(pac1[0], pac1[1]+1, 'sever')
            if pac1[1]+1<self.grid_size[0] and (pac1[0],pac1[1]+1) not in self.obstacles:
                new_state=(new_pac,new_ghost)
                if new_state!=old_state:
                    if new_pac==new_ghost:
                        succ["Go unishtuvam duhot"]=new_state
                    else:
                        succ["Pridvizi se napred PAC1"]=new_state

            new_state=(pac1,new_ghost)
            succ["Stop PAC1"]=new_state
        # DOLU
        if pac1[2] == "jug":

            new_pac = (pac1[0], pac1[1], 'istok')
            new_state = (new_pac, new_ghost)
            if new_state != old_state:
                succ["Zavrti se levo PAC1"] = new_state

            new_pac = (pac1[0], pac1[1], 'zapad')
            new_state = (new_pac, new_ghost)
            if new_state != old_state:
                succ["Zavrti se desno PAC1"] = new_state

            new_pac = (pac1[0], pac1[1] - 1, 'jug')
            if pac1[1] - 1 >= 0 and (pac1[0], pac1[1] - 1) not in self.obstacles:
                new_state = (new_pac, new_ghost)
                if new_state != old_state:
                    if new_pac==new_ghost:
                        succ["Go unishtuvam duhot"]=new_state
                    else:
                        succ["Pridvizi se napred PAC1"] = new_state
            new_state = (pac1, new_ghost)
            succ["Stop PAC1"] = new_state
        # LEVO
        if pac1[2] == "zapad":

            new_pac = (pac1[0], pac1[1], 'jug')
            new_state = (new_pac, new_ghost)
            if new_state != old_state:
                succ["Zavrti se levo PAC1"] = new_state

            new_pac = (pac1[0], pac1[1], 'sever')
            new_state = (new_pac,  new_ghost)
            if new_state != old_state:
                succ["Zavrti se desno PAC1"] = new_state

            new_pac = (pac1[0]-1, pac1[1], 'zapad')
            if pac1[0] - 1 >= 0 and (pac1[0]-1, pac1[1]) not in self.obstacles:
                new_state = (new_pac,  new_ghost)
                if new_state != old_state:
                    if new_pac==new_ghost:
                        succ["Go unishtuvam duhot"]=new_state
                    else:
                        succ["Pridvizi se napred PAC1"] = new_state

            new_state = (pac1, new_ghost)
            succ["Stop PAC1"] = new_state
        # DESNO
        if pac1[2] == "istok":

            new_pac = (pac1[0], pac1[1], 'sever')
            new_state = (new_pac, new_ghost)
            if new_state != old_state:
                succ["Zavrti se levo PAC1"] = new_state

            new_pac = (pac1[0], pac1[1], 'jug')
            new_state = (new_pac,new_ghost)
            if new_state != old_state:
                succ["Zavrti se desno PAC1"] = new_state

            new_pac = (pac1[0] + 1, pac1[1], 'istok')
            if pac1[0] + 1 < self.grid_size[1] and (pac1[0] + 1, pac1[1]) not in self.obstacles:
                new_state = (new_pac, new_ghost)
                if new_state != old_state:
                    if new_pac==new_ghost:
                        succ["Go unishtuvam duhot"]=new_state
                    else:
                        succ["Pridvizi se napred PAC1"] = new_state

            new_state = (pac1,new_ghost)
            succ["Stop PAC1"] = new_state

        return succ







        new_ghost=(ghost[0]-1,ghost[1])
        if ghost[0]-1 >=0 and (ghost[0]-1,ghost[1]) not in self.obstacles:
            new_state=(pac1,new_ghost)
            if new_state!=old_state:
                succ["LevoGhost"]=new_state

        new_ghost = (ghost[0] + 1, ghost[1])
        if ghost[0] + 1 < self.grid_size[1] and (ghost[0] + 1, ghost[1]) not in self.obstacles:
            new_state = (pac1, new_ghost)
            if new_state != old_state:
                succ["DesnoGhost"] = new_state

        new_ghost = (ghost[0], ghost[1]+1)
        if ghost[1] + 1 < self.grid_size[0] and (ghost[0], ghost[1]+1) not in self.obstacles:
            new_state = (pac1,new_ghost)
            if new_state != old_state:
                succ["GoreGhost"] = new_state


        new_ghost = (ghost[0], ghost[1]-1)
        if ghost[1] - 1 >= 0 and (ghost[0], ghost[1]-1) not in self.obstacles:
            new_state = (pac1 ,new_ghost)
            if new_state != old_state:
                succ["DoluGhost"] = new_state



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
        pac1=state[0]
        ghost=state[1]
        pac11=(pac1[0],pac1[1])

        return pac11==ghost


if __name__=="__main__":
    obstacle_list=((0,3), (0,5), (3,0), (3,3), (4,3), (4,4), (5,3), (6,0), (6,3), (6,4), (8,5))
    grid_size=[6,9]
    agents=[(0,2,'jug'),(8,1)]
    pacman=Pacman()
    print(breadth_first_graph_search(pacman).solution())
    print(depth_first_graph_search(pacman).solution())


