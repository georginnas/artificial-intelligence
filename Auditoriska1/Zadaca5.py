"""Во оваа задача се чуваат родендените на пријатели, кои треба да се пронајдат според имињата на пријателите.
Креирајте речник (dictionary) со имиња и родендени. Потоа, додадете функционалност со која од стандарден влез
се чита име на пријател, и вратете го неговиот роденден (односно испечатете го на стандарден излез). Интеракцијата на
програмата треба да изгледа како:

Dobredojdovte do rechnikot za rodendeni. Nie gi znaeme rodendenite na:
Ana
Marija
Stefan
Aleksandar
Koj rodenden e potrebno da se prebara?
Marija
 Rodendenot na Marija e na 01/17/1991"""
if __name__== '__main__':
    recnik = {
        'Marija': '01/17/1991',
        'Ana': '02/17/1991',
        'Stefan': '03/17/1991',
        'Aleksandar': '01/17/199'
    }
    print("Dobredojdovte do rechnikot za rodendeni. Nie gi znaeme rodendenite na:")
    print('\n'.join(recnik.keys())) #ili ' ' za prazno mesto
    print("Koj rodenden e potrebno da se prebara?")
    ime=input()
    print(f'Rodendenot na {ime} e na {recnik[ime]}')


