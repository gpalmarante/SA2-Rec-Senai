lst = []
n = 4
def Soma(L):
    Som=0
    for i in L:
        Som = Som + i
    return Som

print("Calcular media de 4 numeros:") 
print("Digite 4 numeros")

for i in range(0, n):
    nota = int(input("Digite um Numero:"))
 
    lst.append(nota) 
m = Soma(lst)
media = m / n
if media >= 1:
    print("Media dos valor positiva = +" + str(media))
else:
    print("Media dos valor Negativa = " + str(media))