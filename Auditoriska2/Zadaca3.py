"""Задача 3 - Вгнездени list comprehension
Користејќи list comprehension дадена матрица составена од броеви да се промени секој елемент така што ќе се помножи со 2.
Секој елемент на матрицата се чита од тастатура така што прво се читаат N и M (број на редици и колони)
а потоа во секој ред се читаат елементите одделени со празно место

Пример влез: 4 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4

Излез: [[2, 4, 6, 8], [2, 4, 6, 8], [2, 4, 6, 8], [2, 4, 6, 8]]"""
if __name__=="__main__":
    n=int(input())
    m=int(input())
    matrica=[]
    for i in range(0,n):
        redica=[int(element) for element in input().split(" ")]  # citame elementite kako string, go delime stringot po prazno mesto i sekoj element od listata go konvertirame vo int
        matrica.append(redica)
    print(matrica)
    #rezultat=[elem*2 for red in matrica for elem in red] za lista
    rezultat= [[matrica[i][j] * 2 for j in range(0, m)] for i in range(0, n)]  # za lista od listi
    print(rezultat)
