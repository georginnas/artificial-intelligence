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
from constraint import *
#(row, column)
#domenot se site mozni polinja na tablata
def not_attacking(rook1, rook2): #(i1,j1) (i2,j2)
    return rook1[0]!=rook2[0] and rook1[1]!=rook2[1]

if __name__=="__main__":
    problem=Problem()
    domain=[(i,j) for i in range(0,8) for j in range(0,8)]
    print(domain)
    rooks= range(1,9)


    problem.addVariables(rooks,domain)

    for rook1 in rooks:
        for rook2 in rooks:
            if rook1!=rook2:
                problem.addConstraint(not_attacking, (rook1,rook2))

    print(problem.getSolutions())
