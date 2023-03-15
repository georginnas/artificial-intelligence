"""
N-Коњи Problem 1 (3 / 13)
Дадена е NxN табла за шах. Треба да се постават n коњи на таблата така што ниеден коњ да не се напаѓа.
Коњите може да се постават на било која позиција која сметаме дека е најсоодветна. Единственото ограничување
е дека не треба да се напаѓаат. Движењето на коњот е прикажано на сликата подолу:
На влез се прима бројот на коњи и димензии на таблата n. На излез треба да се испечати бројот на решенија кои ви ги
 дава решението со default Backtracking Solver ако бројот на коњи е помал или еднаков на 4. Во спротивно да се испечати само првото решение.

Забелешка: Не е задолжително да ви поминуваат последните три тест примери за задачата да биде точна. Зависи како сте ги поставиле условите.

"""
from constraint import *

def konji_ogranicuvanje(k1, k2):
    if k1[0] == k2[0] and k1[1] == k2[1]:
        return False
    if k1[0] - 2 == k2[0] and k1[1] - 1 == k2[1]:
        return False
    if k1[0] - 2 == k2[0] and k1[1] + 1 == k2[1]:
        return False
    if k1[0] - 1 == k2[0] and k1[1] - 2 == k2[1]:
        return False
    if k1[0] - 1 == k2[0] and k1[1] + 2 == k2[1]:
        return False
    if k1[0] + 1 == k2[0] and k1[1] - 2 == k2[1]:
        return False
    if k1[0] + 1 == k2[0] and k1[1] + 2 == k2[1]:
        return False
    if k1[0] + 2 == k2[0] and k1[1] - 1 == k2[1]:
        return False
    if k1[0] + 2 == k2[0] and k1[1] + 1 == k2[1]:
        return False
    return True

if __name__ == "__main__":

    problem = Problem()

    n = int(input())

    variables = range(0, n)
    domains = []
    for i in range(0, n):
        for j in range(0, n):
            domains.append((i, j))
    domains = [(row, col) for row in range(0, n) for col in range(0, n)]

    problem.addVariables(variables, domains)

    for konj1 in variables:
        for konj2 in variables:
            if konj1 < konj2:
                problem.addConstraint(konji_ogranicuvanje, (konj1, konj2))

    if n <= 4:
        solutions = problem.getSolutions()
        print(len(solutions))
    else:
        solution = problem.getSolution()
        print(solution)