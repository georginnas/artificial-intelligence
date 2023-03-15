"""Таблица на квадрати, кубови и корени Problem 3 (0 / 0)
Да се направи таблица на степени, кубови и квадратни корени заокружени на 5 децимали на броевите од m до n,
така што резултатот ќе се чува во речник на кој клучот е самиот број, а вредноста е торка од облик
(квадрат, куб, корен заокружен на 5 децимали). Пр:

{1 : (1,1,1), 2 : (4,8,1.1412), …}

Потоа да се искористи речникот така што за прочитан број од стандардниот влез ќе се испечати торката
која е соодветна на бројот (клучот) или да се испечати “nema podatoci” доколку прочитаниот број е надвор од интервалот.
Исто така, треба да се испечати и сортирана листа од паровите вредности на добиениот речник, во зависност од m и n.

Забелешка: Може да се користи наредбата: sorted(tablica.items()) За заокружување може да се користи функцијата: round(x, 5)"""
import math
def presmetaj(broj):
    stepen=broj*broj
    kub=broj*broj*broj
    koren=math.sqrt(broj)
    koren=round(koren, 5)
    tu=(stepen,kub,koren)
    return tu

if __name__ == "__main__":
    m = int(input())
    n = int(input())
    x = int(input())
    # vasiot kod pisuvajte go tuka
    if m<n:
        tablica = {}
        j=0
        for i in range(m,n+1,+1):
            tablica[i]=tuple(presmetaj(i))
        print(tablica)
        if x in tablica.keys():
            print(x, tablica[x])
        else:
            print("nema podatoci")
            print("[]")
    else:
        print("nema podatoci")
        print("[]")