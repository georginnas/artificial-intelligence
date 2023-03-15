"""Задача 1 - Swap на елементи во листа од торки
Да се напише функција која за дадена листа од торки во облик [('a', 1), ('b', 2), ('c', 3)]
ќе направи swap на елементите во торките така што елементот на позиција 0 ќе биде елемент на позиција 1 и обратно.
Да се користи list comprehension. Пример влез: [('a', 1), ('b', 2), ('c', 3)]

Пример излез: [(1, 'a'), (2, 'b'), (3, 'c')]"""
def swap (x,y):
    return y,x
if __name__=="__main__":
    print("Vnesi broj na torki") #VNES ZA VAKOV VID NA ZADACA
    n=int(input())
    li=[]
    changed=[]
    for i in range(n):
        li.append(tuple(input()))
    for (x,y) in li:
        changed.append((x,int(y))) #changed.append((int(y), x)) # bez list comprehension
    print([swap(x,y) for (x,y) in li])
