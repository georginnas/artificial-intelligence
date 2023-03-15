"""Gradebook Problem 1 (1 / 94)
Дефинирајте речник students во кој ќе се чуваат информации за предметите кои ги полагале студентите.
Од стандарден влез се читаат информации за име, презиме, број на индекс, предмет, поени од теоретски дел,
поени од практичен дел и поени од лабораториски вежби. Може да се вчитаат информации за неограничен број студенти.
Вчитувањето информации завршува кога ќе се прочита клучниот збор end. Пополнете го речникот students со вчитаните информации.

Потоа, за секој од студентите да се испечати името и презимето, и оцената за секој од предметите кои ги има полагано.

Оцената се пресметува на следниот начин:

[0, 50] - 5

(50, 60] - 6

(60, 70] - 7

(70, 80] - 8

(80, 90] - 9

(90, 100] - 10"""
def suma_kolokviumi(poeni1,poeni2,poeni3):
    suma=poeni1+poeni2+poeni3
    if suma<51:
        return 5
    elif suma>50 and suma<61:
        return 6
    elif suma>60 and suma<71:
        return 7
    elif suma>70 and suma<81:
        return 8
    elif suma>80 and suma<91:
        return 9
    elif suma>90:
        return 10
if __name__ == "__main__":
    while True:
        if input()=="end":
            break
        student=input().split(",")
        r={}
        ime = str(student[0])
        prezime =str(student[1])
        brindeks =int(student[2])
        predmet =str(student[3])
        poeniteo =int(student[4])
        poenipra =int(student[5])
        poenilab=int(student[6])
        r = {"ime": ime, "prezime": prezime, "indeks": brindeks, "predmet": predmet,"poeniteo": poeniteo, "poenipra": poenipra,"poenilab": poenilab}
        print("Student: " +ime+" "+prezime)
        print("\t"+"\t"+predmet+": "+str(suma_kolokviumi(poeniteo, poenipra, poenilab)))
