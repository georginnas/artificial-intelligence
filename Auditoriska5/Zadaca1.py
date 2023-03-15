"""
Пример 1 – Боење на мапа
Дадена ни е мапата на Австралија и
треба да ја обоиме со три бои: сина,
зелена и црвена. Соседните региони не
смее да имаат иста боја. Секој регион
може да има една од трите бои
Пример 1: Декларирај множество
променливи, домен и ограничувања
Променливи: WA, NT, Q, NSW, V, SA, T
• Домени: 𝐷𝑖 = {𝑟𝑒𝑑, 𝑔𝑟𝑒𝑒𝑛, 𝑏𝑙𝑢𝑒}
• Ограничувања: соседните региони мора да имаат различни бои
• пр., WA ≠ NT
"""
from constraint import*
def different(a,b):
    return a!=b
if __name__=="__main__":
    problem=Problem()

    variables=["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    domain=["red", "green", "blue"]

    problem.addVariables(variables, domain)

    problem.addConstraint(different, ("WA", "NT"))
    problem.addConstraint(different, ("WA", "SA"))
    problem.addConstraint(different, ("SA", "NT"))
    problem.addConstraint(different, ("Q", "NT"))
    problem.addConstraint(different, ("SA", "Q"))
    problem.addConstraint(different, ("NSW", "Q"))
    problem.addConstraint(different, ("NSW", "SA"))
    problem.addConstraint(different, ("NSW", "V"))
    problem.addConstraint(different, ("SA", "V"))

    solutions=problem.getSolutions() #site resenija

    print(solutions)

    solution = problem.getSolution() #edno resenie
    print(solution)
