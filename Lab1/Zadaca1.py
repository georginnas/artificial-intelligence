"""Minesweeper Problem 2 (0 / 0)
Овој проблем се базира на играта Minesweeper.

Креирајте функција која како влез зема листа од # и -, каде што секој хаш знак (#) претставува мина,
а секоја цртичка (-) претставува поле без мина. Функцијата треба да враќа листа каде што секоја цртичка е заменета
со бројка која го претставува бројот на мини од најблиските полиња на моменталното поле
(хоризонтално, вертикално, и дијагонално). Листата која се враќа на излез креирајте ја со пристапот list comprehension.

Од стандарден влез е дадена големината на полето N (полето е со димензии NxN), како и репрезентацијата на полето со # и
-. Потребно е да направите репрезентација на полето преку листа од листи, каде што елементите се # и -.
Оваа листа е влез на претходно дефинираната функција, а излезот од функцијата е потребно да се испечати од стандарден влез.

Помош: влезот е зададен ред по ред за секоја редица во полето, додека индивидуалните елементи се одвоени со 3 празни места.
За да се одделат елементите со 3 празни места, може да ја искористите функцијата split() дефинирана на стрингови.
За печатење на излезот може да ја користите функцијата join() дефинирана на стрингови."""

if __name__=="__main__":
    n=int(input())
    matrica=[]

    for i in range(0,n):
        redica=[element for element in input().split("   ")]
        matrica.append(redica)
    print(matrica)
    changed = []
    for i in range(0, n):
        red = []
        for j in range(0, n):
            if matrica[i][j] == '#':
                red.append("#")
            elif j+1!=n and matrica[i][j + 1] == "#":  # desno
                red.append(1)
            elif j-1!=-1 and matrica[i][j - 1] == "#":  # levo
                red.append(1)
            elif i+1!=n and matrica[i + 1][j] == "#":   # nadolu
                red.append(1)
            elif i-1!=-1 and matrica[i - 1][j] == "#": # nagore
                red.append(1)
            elif j-1!=-1  and i-1!=-1 and matrica[i - 1][j - 1] == "#":  #doludesno
                red.append(1)
            elif j - 1 != -1 and i+1!=n and matrica[i + 1][j - 1] == "#":  #dolulevo
                red.append(1)
            elif j+1!=n and i-1!=-1 and matrica[i - 1][j + 1] == "#":  #goredesno
                red.append(1)
            elif j+1!=n and i+1!=n and matrica[i + 1][j + 1] == "#":  #gorelevo
                red.append(1)
            else:
                red.append(0)

        changed.append(red)


    print(changed)
