"""Напишете програма која бара од корисникот да внесе име и години и потоа пресметува во која година тој ќе има 100 години.
 Испечатете го неговото име и годината добиена.

Vnesete ime i godini:
Dimitar 23
Dimitar ke ima 100 godini vo 2097"""

def presmetaj(godini):
    return (100-int(godini))+2021

if __name__== '__main__':
    print('Vnesete ime i godini: ')
    vnes=input().split()
    god=presmetaj(vnes[1])
    print(f'{vnes[0]} kje ima 100 godini vo {god}')
