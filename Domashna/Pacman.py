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
        # ((0, 2, 'jug'), (2, 5, 'zapad'), (4, 0, 'sever'), (8, 1))
        succ=dict()
        pac1,pac2,pac3,ghost=state
        old_state=state


        #GHOST
        new_ghost=(ghost[0]-1,ghost[1])
        if ghost[0]-1 >=0 and (ghost[0]-1,ghost[1]) not in self.obstacles:
            new_state=(pac1,pac2,pac3,new_ghost)
            if new_state!=old_state:
                succ["LevoGhost"]=new_state

        new_ghost = (ghost[0] + 1, ghost[1])
        if ghost[0] + 1 < self.grid_size[1] and (ghost[0] + 1, ghost[1]) not in self.obstacles:
            new_state = (pac1, pac2, pac3, new_ghost)
            if new_state != old_state:
                succ["DesnoGhost"] = new_state

        new_ghost = (ghost[0], ghost[1]+1)
        if ghost[1] + 1 < self.grid_size[0] and (ghost[0], ghost[1]+1) not in self.obstacles:
            new_state = (pac1, pac2, pac3, new_ghost)
            if new_state != old_state:
                succ["GoreGhost"] = new_state


        new_ghost = (ghost[0], ghost[1]-1)
        if ghost[1] - 1 >= 0 and (ghost[0], ghost[1]-1) not in self.obstacles:
            new_state = (pac1, pac2, pac3, new_ghost)
            if new_state != old_state:
                succ["DoluGhost"] = new_state


        #PAC1---------------------------------------------------------------------------------------------------------
        #GORE
        if pac1[2]=="sever":
            new_pac=(pac1[0],pac1[1],'zapad')
            new_state=(new_pac,pac2,pac3,ghost)
            if new_state!=old_state:
                succ["Zavrti se levo PAC1"]=new_state

            new_pac = (pac1[0], pac1[1], 'istok')
            new_state = (new_pac, pac2, pac3, ghost)
            if new_state != old_state:
                succ["Zavrti se desno PAC1"] = new_state

            new_pac=(pac1[0], pac1[1]+1, 'sever')
            if pac1[1]+1<self.grid_size[0] and (pac1[0],pac1[1]+1) not in self.obstacles:
                new_state=(new_pac,pac2,pac3,ghost)
                if new_state!=old_state:
                    succ["Pridvizi se napred PAC1"]=new_state

            new_state=(pac1,pac2,pac3,ghost)
            succ["Stop PAC1"]=new_state
        # DOLU
        if pac1[2] == "jug":

            new_pac = (pac1[0], pac1[1], 'istok')
            new_state = (new_pac, pac2, pac3, ghost)
            if new_state != old_state:
                succ["Zavrti se levo PAC1"] = new_state

            new_pac = (pac1[0], pac1[1], 'zapad')
            new_state = (new_pac, pac2, pac3, ghost)
            if new_state != old_state:
                succ["Zavrti se desno PAC1"] = new_state

            new_pac = (pac1[0], pac1[1] - 1, 'jug')
            if pac1[1] - 1 >= 0 and (pac1[0], pac1[1] - 1) not in self.obstacles:
                new_state = (new_pac, pac2, pac3, ghost)
                if new_state != old_state:
                    succ["Pridvizi se napred PAC1"] = new_state
            new_state = (pac1, pac2, pac3, ghost)
            succ["Stop PAC1"] = new_state
        # LEVO
        if pac1[2] == "zapad":

            new_pac = (pac1[0], pac1[1], 'jug')
            new_state = (new_pac, pac2, pac3, ghost)
            if new_state != old_state:
                succ["Zavrti se levo PAC1"] = new_state

            new_pac = (pac1[0], pac1[1], 'sever')
            new_state = (new_pac, pac2, pac3, ghost)
            if new_state != old_state:
                succ["Zavrti se desno PAC1"] = new_state

            new_pac = (pac1[0]-1, pac1[1], 'zapad')
            if pac1[0] - 1 >= 0 and (pac1[0]-1, pac1[1]) not in self.obstacles:
                new_state = (new_pac, pac2, pac3, ghost)
                if new_state != old_state:
                    succ["Pridvizi se napred PAC1"] = new_state

            new_state = (pac1, pac2, pac3, ghost)
            succ["Stop PAC1"] = new_state
        # DESNO
        if pac1[2] == "istok":

            new_pac = (pac1[0], pac1[1], 'sever')
            new_state = (new_pac, pac2, pac3, ghost)
            if new_state != old_state:
                succ["Zavrti se levo PAC1"] = new_state

            new_pac = (pac1[0], pac1[1], 'jug')
            new_state = (new_pac, pac2, pac3, ghost)
            if new_state != old_state:
                succ["Zavrti se desno PAC1"] = new_state

            new_pac = (pac1[0] + 1, pac1[1], 'istok')
            if pac1[0] + 1 < self.grid_size[1] and (pac1[0] + 1, pac1[1]) not in self.obstacles:
                new_state = (new_pac, pac2, pac3, ghost)
                if new_state != old_state:
                    succ["Pridvizi se napred PAC1"] = new_state

            new_state = (pac1, pac2, pac3, ghost)
            succ["Stop PAC1"] = new_state

        # PAC2----------------------------------------------------------------------------------------
        # GORE
        if pac2[2] == "sever":
            new_pac = (pac2[0], pac2[1], 'zapad')
            new_state = (pac1, new_pac, pac3, ghost)
            if new_state != old_state:
                succ["Zavrti se levo PAC2"] = new_state

            new_pac = (pac2[0], pac2[1], 'istok')
            new_state = (pac1, new_pac, pac3, ghost)
            if new_state != old_state:
                succ["Zavrti se desno PAC2"] = new_state

            new_pac = (pac2[0], pac2[1] + 1, 'sever')
            if pac2[1] + 1 < self.grid_size[0] and (pac2[0], pac2[1] + 1) not in self.obstacles:
                new_state = (pac1, new_pac, pac3, ghost)
                if new_state != old_state:
                    succ["Pridvizi se napred PAC2"] = new_state

            new_state = (pac1, pac2, pac3, ghost)
            succ["Stop PAC2"] = new_state
        # DOLU
        if pac2[2] == "jug":

            new_pac = (pac2[0], pac2[1], 'istok')
            new_state = (pac1, new_pac, pac3, ghost)
            if new_state != old_state:
                succ["Zavrti se levo PAC2"] = new_state

            new_pac = (pac2[0], pac2[1], 'zapad')
            new_state = (pac1, new_pac, pac3, ghost)
            if new_state != old_state:
                succ["Zavrti se desno PAC2"] = new_state

            new_pac = (pac2[0], pac2[1] - 1, 'jug')
            if pac2[1] - 1 >= 0 and (pac2[0], pac2[1] - 1) not in self.obstacles:
                new_state = (pac1, new_pac, pac3, ghost)
                if new_state != old_state:
                    succ["Pridvizi se napred PAC2"] = new_state
            new_state = (pac1, pac2, pac3, ghost)
            succ["Stop PAC2"] = new_state
        # LEVO
        if pac2[2] == "zapad":

            new_pac = (pac2[0], pac2[1], 'jug')
            new_state = (pac1, new_pac, pac3, ghost)
            if new_state != old_state:
                succ["Zavrti se levo PAC2"] = new_state

            new_pac = (pac2[0], pac2[1], 'sever')
            new_state = (pac1, new_pac, pac3, ghost)
            if new_state != old_state:
                succ["Zavrti se desno PAC2"] = new_state

            new_pac = (pac2[0] - 1, pac2[1], 'zapad')
            if pac2[0] - 1 >= 0 and (pac2[0] - 1, pac2[1]) not in self.obstacles:
                new_state = (pac1, new_pac, pac3, ghost)
                if new_state != old_state:
                    succ["Pridvizi se napred PAC2"] = new_state

            new_state = (pac1, pac2, pac3, ghost)
            succ["Stop PAC2"] = new_state
        # DESNO
        if pac2[2] == "istok":

            new_pac = (pac2[0], pac2[1], 'sever')
            new_state = (pac1, new_pac, pac3, ghost)
            if new_state != old_state:
                succ["Zavrti se levo PAC2"] = new_state

            new_pac = (pac2[0], pac2[1], 'jug')
            new_state = (pac1, new_pac, pac3, ghost)
            if new_state != old_state:
                succ["Zavrti se desno PAC2"] = new_state

            new_pac = (pac2[0] + 1, pac2[1], 'istok')
            if pac2[0] + 1 < self.grid_size[1] and (pac2[0] + 1, pac2[1]) not in self.obstacles:
                new_state = (pac1, new_pac, pac3, ghost)
                if new_state != old_state:
                    succ["Pridvizi se napred PAC2"] = new_state

            new_state = (pac1, pac2, pac3, ghost)
            succ["Stop PAC2"] = new_state

        # PAC3----------------------------------------------------------------------------------------------------------
        # GORE
        if pac3[2] == "sever":
            new_pac = (pac3[0], pac3[1], 'zapad')
            new_state = (pac1, pac2, new_pac, ghost)
            if new_state != old_state:
                succ["Zavrti se levo PAC3"] = new_state

            new_pac = (pac3[0], pac3[1], 'istok')
            new_state = (pac1, pac2, new_pac, ghost)
            if new_state != old_state:
                succ["Zavrti se desno PAC3"] = new_state

            new_pac = (pac3[0], pac3[1] + 1, 'sever')
            if pac3[1] + 1 < self.grid_size[0] and (pac3[0], pac3[1] + 1) not in self.obstacles:
                new_state = (pac1, pac2, new_pac, ghost)
                if new_state != old_state:
                    succ["Pridvizi se napred PAC3"] = new_state

            new_state = (pac1, pac2, pac3, ghost)
            succ["Stop PAC3"] = new_state
        # DOLU
        if pac3[2] == "jug":

            new_pac = (pac3[0], pac3[1], 'istok')
            new_state = (pac1, pac2, new_pac, ghost)
            if new_state != old_state:
                succ["Zavrti se levo PAC3"] = new_state

            new_pac = (pac3[0], pac3[1], 'zapad')
            new_state = (pac1, pac2, new_pac, ghost)
            if new_state != old_state:
                succ["Zavrti se desno PAC3"] = new_state

            new_pac = (pac3[0], pac3[1] - 1, 'jug')
            if pac3[1] - 1 >= 0 and (pac3[0], pac3[1] - 1) not in self.obstacles:
                new_state = (pac1, pac2, new_pac, ghost)
                if new_state != old_state:
                    succ["Pridvizi se napred PAC3"] = new_state
            new_state = (pac1, pac2, pac3, ghost)
            succ["Stop PAC3"] = new_state
        # LEVO
        if pac3[2] == "zapad":

            new_pac = (pac3[0], pac3[1], 'jug')
            new_state = (pac1, pac2, new_pac, ghost)
            if new_state != old_state:
                succ["Zavrti se levo PAC3"] = new_state

            new_pac = (pac3[0], pac3[1], 'sever')
            new_state = (pac1, pac2, new_pac, ghost)
            if new_state != old_state:
                succ["Zavrti se desno PAC3"] = new_state

            new_pac = (pac3[0] - 1, pac3[1], 'zapad')
            if pac3[0] - 1 >= 0 and (pac3[0] - 1, pac3[1]) not in self.obstacles:
                new_state = (pac1, pac2, new_pac, ghost)
                if new_state != old_state:
                    succ["Pridvizi se napred PAC3"] = new_state

            new_state = (pac1, pac2, pac3, ghost)
            succ["Stop PAC3"] = new_state
        # DESNO
        if pac3[2] == "istok":

            new_pac = (pac3[0], pac3[1], 'sever')
            new_state = (pac1, pac2, new_pac, ghost)
            if new_state != old_state:
                succ["Zavrti se levo PAC3"] = new_state

            new_pac = (pac3[0], pac3[1], 'jug')
            new_state = (pac1, pac2, new_pac, ghost)
            if new_state != old_state:
                succ["Zavrti se desno PAC3"] = new_state

            new_pac = (pac3[0] + 1, pac3[1], 'istok')
            if pac3[0] + 1 < self.grid_size[1] and (pac3[0] + 1, pac3[1]) not in self.obstacles:
                new_state = (pac1, pac2, new_pac, ghost)
                if new_state != old_state:
                    succ["Pridvizi se napred PAC3"] = new_state

            new_state = (pac1, pac2, pac3, ghost)
            succ["Stop PAC3"] = new_state
        print(succ)
        return succ

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
        pac2=state[1]
        pac3=state[2]
        ghost=state[1]
        pac11=(pac1[0],pac1[1])
        pac22=(pac2[0],pac2[1])
        pac33=(pac3[0],pac3[1])

        return pac11==pac22==pac33==ghost


if __name__=="__main__":
    obstacle_list=((0,3), (0,5), (3,0), (3,3), (4,3), (4,4), (5,3), (6,0), (6,3), (6,4), (8,5))
    grid_size=[6,9]
    agents=[(0,2,'jug'), (2,5,'zapad'), (4,0,'sever'),(8,1)]
    pacman=Pacman(obstacle_list,grid_size,tuple(agents))
    print(breadth_first_graph_search(pacman).solution())


