L =  [5, 7, 2, 9, 4, 1, 3]

A = ' '.join(" ".join(str(x) for x in L))
print ("Lista L = " + A)
print ("O tamanho da lista = " + str(len(L)))
def Tamanho(List):
    Cont= 0
    for i in List:
        Cont += 1
    return Cont
print("O tamanho da lista = " +str(Tamanho(L)))       

print("O maior Valor da lista = "+ str(max(L)))
def MaxValor():
    Max=0
    for i in L:
        if (Max < i):
            Max = i
    print("O maior Valor da lista = " + str(Max))  
MaxValor() 

print ("O menor Valor da lista = "+ str(min(L)))
def MinValor():
    Min=L[0]
    for i in L:
        if (Min > i):
            Min = i
    print("O maior Valor da lista = " + str(Min))  
MinValor() 

print ("A soma dos Valores da lista = "+ str(sum(L)))

def Soma():
    Som=0
    for i in L:
        Som = Som + i
    print ("A soma dos Valores da lista = "+ str(Som))
Soma()

L.sort(reverse = False)
print ("A lista em ordem crescente = "+ str(L))
def OrdCre():
    for i in range(0,Tamanho(L)):
        for j in range(i+1,Tamanho(L)):
            if L[i] > L[j]:
                    L[i], L[j] = L[j], L[i]
    print ("A lista em ordem crescente = "+ str(L)) 
OrdCre()          
L.sort(reverse = True)
print ("A lista em ordem decrescente = "+ str(L))
def OrdDec():
    for i in range(0,Tamanho(L)):
        for j in range(i+1,Tamanho(L)):
            if L[i] < L[j]:
                    L[i], L[j] = L[j], L[i]
    print ("A lista em ordem Decrescente = "+ str(L)) 
OrdDec() 