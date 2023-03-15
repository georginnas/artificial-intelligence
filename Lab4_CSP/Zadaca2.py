"""Потребно е да составите тим кој се состои од 1 тим лидер и 5 членови. Членовите се избираат од множество на N1 можни членови.
 Тим лидерот се избира од множество на N2 можни тим лидери. Притоа, секој член и тим лидер има одредена тежина (реална вредност помеѓу 0 и 100).
 Ваша задача е да креирате оптимален тим. Оптимален тим е тимот чија сума на тежини е највисока. Дополнително, сумата не треба да биде поголема од 100.
  Не е можно еден тим лидер или еден член да се избере повеќе од еднаш.

Од стандарден влез се чита бројот на можни членови, а потоа се читаат информации за секој член во следниот формат „тежина име“.
Потоа, се чита бројот на можни тим лидери и информациите за секој тим лидер во следниот формат „тежина име“.

На стандарден излез да се испечати вкупната сума за формираниот тим. Потоа да се испечатат тим лидерот и членовите на тимот.

For example:"""
from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    var_participants=[]
    for l in range(5):
        var_participants.append(f'Participant {l+1}')
    var_teaml = ["Leader"]
    dom_participants = []
    dom_teaml = []
    n=int(input())
    particip=dict()
    for i in range(0,n):
        line=input().split(" ")
        variable=line[1]
        domain=line[0]
        particip[variable]=float(domain)
        dom_participants.append(float(domain))
    m=int(input())
    lead=dict()
    for j in range(0,m):
        line = input().split(" ")
        variable = line[1]
        domain = line[0]
        lead[variable]=float(domain)
        dom_teaml.append(float(domain))

    problem.addVariables(var_teaml,dom_teaml)
    problem.addVariables(var_participants, dom_participants)
    problem.addConstraint(AllDifferentConstraint())
    problem.addConstraint(MaxSumConstraint(100.0))


    solutions=dict()
    max=0.0
    team=[]
    for solution in problem.getSolutions():
        weight = 0.0
        for value in solution.values():
            weight+=value
        if weight>max:
            max=weight
            team=[value for value in solution.values()]


    leader=team[0]
    print(f'Total score: {round(max, 1)}')
    n_leader=""
    for key, value in lead.items():
        if leader == value:
            n_leader=key
    print(f'Team leader: {n_leader}')
    del team[0]
    i=0
    for player in team:
        for key, value in particip.items():
            if player == value:
                print(f'Participant {i+1}: {key}')
                i=i+1

#Posledniot test primer spored mene ne e tocen

"""
10
31.3 A
28.4 B
26.1 C
24.2 D
21.8 E
20.3 F
15.5 G
14.1 H
12.5 I
11.5 J
5
32.2 K
27.4 L
24.6 M
14.9 N
13.2 O

--------------
10
31.3 P
28.4 Q
26.1 R
24.2 S
21.8 T
20.3 U
15.5 V
14.1 W
12.5 X
11.5 Y
5
6.5 Z
7.8 A
8.7 B
10.1 C
12.6 D
----------
10
31.3 E
28.4 F
26.1 G
24.2 H
21.8 I
8.2 J
9.3 K
9.9 L
10.3 M
10.4 N
5
32.2 O
27.4 P
24.6 Q
14.9 R
13.2 S
------------
9
31.3 T
6.0 U
7.7 V
7.9 W
20.3 X
15.5 Y
14.1 Z
10.3 A
10.4 B
4
32.2 C
27.4 D
24.6 E
13.2 F
------------
7
31.3 G
28.4 H
26.1 I
24.2 J
21.8 K
8.2 L
9.3 M
6
6.5 N
7.8 O
8.7 P
27.4 Q
24.6 R
13.2 S
"""