"""Потребно е да се закаже состанок во петок за Марија, Петар и Симона. Симона како менаџер мора да присуствува на
состанокот со најмалку уште една личност. Состанокот трае еден час, и може да се закаже во периодот од 12:00 до 20:00.
Почетокот на состанокот може да биде на секој час, односно состанокот може да почне во 12:00, но не во 12:05, 12:10 итн.
За секој од членовите дадени се времињата во кои се слободни:
Симона слободни термини: 13:00-15:00, 16:00-17:00, 19:00-20:00
Марија слободни термини: 14:00-16:00, 18:00-19:00
Петар слободни термини: 12:00-14:00, 16:00-20:00
Потребно е менаџерот Симона да ги добие сите можни почетни времиња за состанокот. Даден е почетен код со кој е креирана
класа за претставување на проблемот, на кој се додадени променливите. Потоа се повикува наоѓање на решение со BacktrackingSolver.
 Ваша задача е да ги додадете домените на променливите, како и да ги додадете ограничувањата (условите) на проблемот.
Потсетник: Во дадениот модул constraint веќе се имплементирани следните ограничувања како класи: AllDifferentConstraint,
 AllEqualConstraint, MaxSumConstraint, ExactSumConstraint,  MinSumConstraint, InSetConstraint, NotInSetConstraint, SomeInSetConstraint,  SomeNotInSetConstraint.
"""

from constraint import *


def check_simona(prisustvo, vreme):
    simona_slob_termini = [13, 14, 16, 19]
    if prisustvo == 1 and vreme in simona_slob_termini:
        return True
    return False


def check_marija(prisustvo, vreme):
    marija_slob_termini = [14, 15, 18]
    if prisustvo != 1 or vreme in marija_slob_termini:
        return True
    else:
        return False


def check_petar(prisustvo_petar, prisustvo_marija, vreme):
    petar_slob_termini = [12, 13, 16, 17, 18, 19]
    if prisustvo_petar != 1 or vreme in petar_slob_termini:
        if prisustvo_marija != prisustvo_petar:
            return True
    else:
        return False


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    marija_d = [0, 1]
    simona_d = [0, 1]  # mora da prisustvuva
    petar_d = [0, 1]
    vreme_s = [12, 13, 14, 15, 16, 17, 18, 19, 20]
    problem.addVariable("Marija_prisustvo", marija_d)
    problem.addVariable("Simona_prisustvo", simona_d)
    problem.addVariable("Petar_prisustvo", petar_d)
    problem.addVariable("vreme_sostanok", vreme_s)
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(check_simona, ("Simona_prisustvo", "vreme_sostanok"))
    problem.addConstraint(check_marija, ("Marija_prisustvo", "vreme_sostanok"))
    problem.addConstraint(check_petar, ("Petar_prisustvo", "Marija_prisustvo", "vreme_sostanok"))
    problem.addConstraint(SomeInSetConstraint({1}),
                          ["Marija_prisustvo", "Petar_prisustvo"])  # barem eden od niv treba da prisustvuva

    # ----------------------------------------------------

    solutions = problem.getSolutions()
    for solution in solutions:
        print("%s'Simona_prisustvo': %d, 'Marija_prisustvo': %d, 'Petar_prisustvo': %d, 'vreme_sostanok': %d%s" % (
            "{", solution['Simona_prisustvo'], solution['Marija_prisustvo'], solution['Petar_prisustvo'],
            solution['vreme_sostanok'], "}"))


"""
	
{'Simona_prisustvo': 1, 'Marija_prisustvo': 1, 'Petar_prisustvo': 0, 'vreme_sostanok': 14}
{'Simona_prisustvo': 1, 'Marija_prisustvo': 0, 'Petar_prisustvo': 1, 'vreme_sostanok': 19}
{'Simona_prisustvo': 1, 'Marija_prisustvo': 0, 'Petar_prisustvo': 1, 'vreme_sostanok': 16}
{'Simona_prisustvo': 1, 'Marija_prisustvo': 0, 'Petar_prisustvo': 1, 'vreme_sostanok': 13}
"""