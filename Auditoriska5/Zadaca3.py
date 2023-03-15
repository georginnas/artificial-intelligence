"""
Пример 3 – Магичен квадрат
• Магичен квaдрат е nxn квадратна матрица (каде n е
бројот на ќелии на секоја страна) пополнет со
различни природни броеви во ранг 1,2,….,n2 така
што секоја ќелија содржи различен број и сумата
на секој ред, колона и дијагонала е иста. Сумата се
нарекува магична константа или магична сума на
магичниот квадрат.
• Даден ни е 4x4 магичен квадрат. Треба да ги
пополниме ќелиите со различни природни броеви
во ранг 1,2,…,16 така што секоја ќелија ќе содржи
различен број и сумата на секој ред, колона и
дијагонала ќе биде 34.
Пример 3: Декларирај множество
променливи, домен и ограничувања
16 позиции кои треба да бидат
пополнети со 16 различни вредности
• Променливи:
position1,position2,….,position16
• Домени: 𝐷𝑖 = {1,2, … .16} за секоја
променлива
"""

from constraint import *

if __name__=="__main__":
    problem=Problem()

    variables=range(0,16)

    domain= range(1,17)

    problem.addVariables(variables,domain)

    problem.addConstraint(AllDifferentConstraint(), variables) #sekoe od polinjata treba da dobie razlicna vrednost od domenot

    """
    0  1  2  3 
    4  5  6  7
    8  9  10 11
    12 13 14 15
    """
    #REDICA
    for row in range(4): #kolona
        problem.addConstraint(ExactSumConstraint(34),[row * 4 + i for i in range(4)]) #redica

    #KOLONA
    for col in range(4): #redica col=0-> [0+4*0, 0+4*1, 0+4*2, 0+4*3]= [0,4,8,12]
        problem.addConstraint(ExactSumConstraint(34), [col + 4 *i for i in range(4)]) #kolona

    problem.addConstraint(ExactSumConstraint(34), range(0,16,5)) # ja zemame dijagonalata pocnuvame od 0, 0+5=5 pozicija, posle 5+5=10 i 10+5=15 t.e so cekor 5!
    problem.addConstraint(ExactSumConstraint(34), range(3,13,3)) #ovaa e drugata dijagonala
    # mora krajnoto da bide 13 i 16 za da vleze i posledniot broj

    print(problem.getSolution())