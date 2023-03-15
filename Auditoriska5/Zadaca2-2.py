"""
Пример 2 - Топови
• Дадена ни е 8x8 табла за шах. Треба да
се постават 8 топови на таблата така
што ниеден топ да не се напаѓа.
Топовите може да се постават на било
која позиција која сметаме дека е
најсоодветна. Единственото
ограничување е дека не треба да се
напаѓаат.
Пример 2: Декларирај множество
променливи, домен и ограничувања
Ако не сакаме топовите да се напаѓаат
треба нивната редица и колона да биде
различна
• Секој топ постави го во различна колона
и стави ги редиците како променливи.
Треба да одлучиме во која редица ќе го
поставиме секој топ. (може и обратно –
постави ги во различни редици и стави
колони како променливи)
• Променливи: rook1, rook2,…rook8
• Домени: 𝐷𝑖 = {0,1,2, … 7}

"""

#USTE PODOBRENO RESENIE





from constraint import *

if __name__=="__main__":
    problem=Problem()
    domain = range(0,8) #vo koja redica treba da se naoga sekoj od topovite

    rooks=range(0,8) #vo koja kolona se naoga sekoja od topovite

    problem.addVariables(rooks,domain)

    problem.addConstraint(AllDifferentConstraint(), rooks)
    print(problem.getSolution())
    print(problem.getSolutions())
