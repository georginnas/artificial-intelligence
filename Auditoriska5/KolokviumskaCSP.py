"""
Потребно е да се направи распоред на часови за една група студенти. Студентите слушаат 4 предмети: Вештачка интелигенција (AI), Машинско учење (ML), Роботика (R)
 и Биоинформатика (BI). За секој предмет треба да се закажат термини за предавања и вежби. Бројот на термини за предавања за секој предмет се прима на влез. Бројот н
 а термини за вежби е секогаш 1 (ако за тој предмет има вежби). Еден термин трае 2 часа. Почетокот на терминот може да биде на секој час, односно терминот може да почне во 12:00,
  но не во 12:05, 12:10 итн. За секој од предметите дадени се времињата во кои може да се одржат (дадено е времето на можен почеток на терминот):

Вештачка интелигенција (предавања): понеделник, среда, петок во 11:00 и 12:00 часот
Вештачка интелигенција (вежби): вторник и четврток во 10:00, 11:00, 12:00 и 13:00 часот
Машинско учење (предавања): понеделник, среда, петок во 12:00, 13:00 и 15:00 часот
Машинско учење (вежби): вторник и четврток во 11:00, 13:00 и 14:00 часот
Роботика (предавања): понеделник, среда, петок во 10:00, 11:00, 12:00, 13:00, 14:00 и 15:00 часот
Роботика (вежби): нема
Биоинформатика (предавања): понеделник, среда, петок во 10:00 и 11:00 часот
Биоинформатика (вежби): вторник и четврток во 10:00 и 11:00 часот
За термините важат следните ограничувања:

Не смее да има преклопување на термините
Предавањата и вежбите за Машинско учење мора да почнуваат во различно време (пр. ако има час во понделник кој почнува во 12 часот, тогаш не смее да има термин по Машинско учење кој почнува во 12 другите денови)
Доколу има повеќе часови по некој предмет, не мора час 1 да доаѓа пред час 2.

Даден е почетен код со кој е креирана класа за претставување на проблемот и домените на променливите. Потоа се повикува наоѓање на решение со BacktrackingSolver. Ваша задача е да ги дефинирате променливите, како и да ги додадете ограничувањата (условите) на проблемот.


"""

from constraint import *
def check_valid_all(termin1, termin2):

    day1=termin1[:3]
    day2=termin2[:3]

    hour1=termin1[-2:]
    hour2=termin2[-2:]


    if day1==day2 and abs(int(hour1)-int(hour2))<2: #imame preklopuvanje na termini
        return False
    return True
def check_valid_ml(termin1,termin2):

    hour1 = termin1[-2:]
    hour2 = termin2[-2:]

    if hour1==hour2:
        return False
    return True

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = input()
    casovi_ML = input()
    casovi_R = input()
    casovi_BI = input()

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Tuka dodadete gi promenlivite--------------------
    variables_all=[]
    variables_ml=[]

    #AI predavanja
    for i in range(int(casovi_AI)):
        problem.addVariable(f'AI_cas_{i+1}', AI_predavanja_domain)
        variables_all.append(f'AI_cas_{i+1}')

    # ML predavanja
    for i in range(int(casovi_ML)):
        problem.addVariable(f'ML_cas_{i + 1}', ML_predavanja_domain)
        variables_ml.append(f'ML_cas_{i + 1}')

    # R predavanja
    for i in range(int(casovi_R)):
        problem.addVariable(f'R_cas_{i + 1}', R_predavanja_domain)
        variables_all.append(f'R_cas_{i + 1}')
    # BI predavanja
    for i in range(int(casovi_BI)):
        problem.addVariable(f'BI_cas_{i + 1}', BI_predavanja_domain)
        variables_all.append(f'BI_cas_{i + 1}')

    #AI vezbi
    problem.addVariable(f'AI_vezbi',AI_vezbi_domain)
    variables_all.append('AI_vezbi')
    # ML vezbi
    problem.addVariable(f'ML_vezbi', ML_vezbi_domain)
    variables_ml.append(f'ML_vezbi')
    # BI vezbi
    problem.addVariable(f'BI_vezbi', BI_vezbi_domain)
    variables_all.append(f'BI_vezbi')
    # ---Tuka dodadete gi ogranichuvanjata----------------

    for i in range(len(variables_all)):
        for j in range(i+1, len(variables_all)):
            problem.addConstraint(check_valid_all, [variables_all[i], variables_all[j]])

    for i in range(len(variables_all)):
        for j in range(i + 1, len(variables_ml)):
            problem.addConstraint(check_valid_ml, [variables_ml[i], variables_ml[j]])


    solution = problem.getSolution()

    print(solution)