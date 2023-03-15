"""Совршен број Problem 2 (0 / 0)
Да се дефинира функција sovrshen_broj(), која на влез прима еден аргумент – природен број,
а како резултат враќа вредност True ако бројот е совршен, односно False ако бројот не е совршен. За еден природен број
n велиме дека е _совршен_ ако тој е еднаков на збирот од неговите делители (не земајќи го во предвид и самиот број
n како делител).

Пример. 6 е совршен број, бидејќи негови делители се 1, 2 и 3, и 6 == 1 + 2 + 3

Од стандарден влез да се прочита еден природен број и да се повика претходно дефинираната функција sovrshen_broj()
за прочитаниот број. На стандарден излез да се отпечати соодветна порака (“Brojot e sovrshen” или “Brojot ne e sovrshen”)."""


def sovrshen_broj(br):
    sum=0
    for i in range(br-1, 0, -1): #tretiot parametar e cekor
        if br%i==0:
            sum+=i
    if br==sum:
        return True
    else:
        return False

if __name__ == "__main__":
    broj = eval(input())
    if sovrshen_broj(broj)== True:
        print(f'Brojot {broj} e sovrshen broj')
    else:
        print(f'Brojot {broj} ne e sovrshen broj')
