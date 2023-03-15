from searching_framework.utils import Problem
from searching_framework.informed_search import astar_search

def valid(state):
    farmer, volk, jare, zelka=state

    if volk==jare and farmer!= volk:
        return False
    if jare==zelka and farmer!=jare:
        return False
    return True

class Farmer(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def successor(self, state):
        #(farmer, volk, jare, zelka) (e, e, e, e)
        successors={}
        farmer, volk, jare, zelka = state
        #FARMER SE PRENESUVA SEBE SI
        farmer_new="e" if farmer=="w" else "w"
        state_new=farmer_new, volk, jare, zelka
        if valid(state_new):
            successors["Farmer nosi farmer"]=state_new
        #FARMER PRENESUVA VOLK
        if farmer==volk:
            volk_new="e" if farmer=="w" else "w"
            state_new=farmer_new, volk_new, jare, zelka
            if valid(state_new):
                successors["Farmer nosi volk"]=state_new
        #FARMER PRENESUVA JARE
        if farmer==jare:
            jare_new="e" if farmer=="w" else "w"
            state_new=farmer_new, volk, jare_new, zelka
            if valid(state_new):
                successors["Farmer nosi jare"]=state_new
        #FARMER PRANESUVA ZELKA
        if farmer==zelka:
            zelka_new="e" if farmer=="w" else "w"
            state_new=farmer_new, volk, jare, zelka_new
            if valid(state_new):
                successors["Farmer nosi zelka"]=state_new
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        state=node.state
        goal=self.goal

        value=0

        for x, y in zip(state, goal):
            if x!=y:
                value+=1
        return value




if __name__ == '__main__':
    initial_state = ('e', 'e', 'e', 'e')
    goal_state = ('w', 'w', 'w', 'w')

    farmer = Farmer(initial_state, goal_state)
    print(astar_search(farmer).solution())