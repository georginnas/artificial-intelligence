"""Напишете програма која од листа на броеви (на пример, a=[5, 10, 15, 20])
 ќе направи нова листа од само првиот и последниот елемент. За вежбање кодот поставете го во функција."""
def elementi(li):
    li1=[]
    li1.append(li[0])
    li1.append(li[-1])
    return li1
if __name__=='__main__':
    print("Vnesi broj na dolzina na lista")
    n=int(input())
    li=[]
    for i in range(0,n):
        li.append(int(input()))
    print(elementi(li))
