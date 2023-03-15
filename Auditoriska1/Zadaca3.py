"""Напишете програма која на влез прима два броја и проверува дали првиот број е делив со вториот.
Да се испечати 'Deliv' ако е делив.

Vnesete dva broj:
125
5
Deliv"""

def delivost(br1, br2):
    if br1%br2==0:
        return "deliv"
    elif br1%br2!=0:
        return "ne e deliv"

if __name__== '__main__':
    print('Vnesete dva broja')
    br1=int(input())
    br2=int(input())
    izlez=delivost(br1, br2)
    print(izlez)





