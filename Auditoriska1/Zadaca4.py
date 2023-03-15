"""Напишете програма каде корисникот внесува број и на екран му се печати 'Paren' ако бројот е парен или 'Neparen'
ако бројот е непарен. Дополнително ако бројот е делив со 4 да се испечати 'Deliv so 4'

 Vnesete broj:
8
Paren
Deliv so 4"""
def parnost(br):
    if br%2==0:
        return "paren"
    elif br%2!=0:
        return "neparen"

if __name__== '__main__':
    print('Vnesete broj')
    vnes=int(input())
    izlez=parnost(vnes)
    print(izlez)
    if vnes%4==0:
        print("Deliv so 4")