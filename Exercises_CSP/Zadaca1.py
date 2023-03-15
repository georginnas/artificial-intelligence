"""
Дадена е nxn табла за шах. Треба да се постават n кралици на таблата така што ниедна кралица да не се напаѓа.
Кралиците може да се постават на било која позиција која сметаме дека е најсоодветна. Единственото ограничување е дека не
 треба да се напаѓаат. Можните придвижувања на кралицата ви се дадени на сликата подолу:
 На влез се прима бројот на кралици и димензии на таблата n. На излез треба да се испечати бројот на уникатни позиции
 на кои може да ги поставете кралиците со default Backtracking Solver ако бројот на кралици е помал или еднаков на 6. Во спротивно да се испечати само првото решение.

Потсетник: Во дадениот модул constraint веќе се имплементирани следните ограничувања како класи:  AllDifferentConstraint, AllEqualConstraint, MaxSumConstraint,
 ExactSumConstraint,  MinSumConstraint, InSetConstraint, NotInSetConstraint, SomeInSetConstraint,  SomeNotInSetConstraint.
"""

from constraint import *


def queens_attacking(q1, q2):
    if (abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])) or q1[0] == q2[0] or q1[1] == q2[1]:
        return False
    return True


if __name__ == '__main__':

    problem = Problem(BacktrackingSolver())

    n = int(input())

    queens = range(1, n+1)

    domains = []
    for i in range(0, n):
        for j in range(0, n):
            domains.append((i, j))

    domains = [(row, col) for row in range(0, n) for col in range(0, n)]

    problem.addVariables(queens[0:], domains)

    for queen1 in queens:
        for queen2 in queens:
            if queen1 < queen2:
                problem.addConstraint(queens_attacking, (queen1, queen2))



    if n <= 6:
        solutions = problem.getSolutions()
        print(len(solutions))
    else:
        solution = problem.getSolution()
        print(solution)

