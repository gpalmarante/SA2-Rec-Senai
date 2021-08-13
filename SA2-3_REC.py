def checkInput(prompt):
  result = input(prompt)
  if not result.strip():
      result = 0
  return result

def Soma(L):
    Som=0
    for i in L:
        Som = Som + i
    return Som

def MaxValor(L):
    Max=0
    for i in L:
        if (Max < i):
            Max = i
    return Max

def MinValor(L):
    Min=L[0]
    for i in L:
        if (Min > i):
            Min = i
    return Min   


lst = []
n = 20

print("Calcular media de 20 numeros:") 
print("Digite 1 numeros")
for i in range(0, n):
    
    nota = int(checkInput("Digite o Numero "+str(i+1)+" da lista : "))
    
    lst.append(nota) 
    
m = Soma(lst)
media = m / n
print ("A media dos valores e : "+str(media))
print ("O maior valor :" + str(MaxValor(lst)))
print ("O menor valor :" + str(MinValor(lst)))
