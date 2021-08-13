def checkInput(prompt):
  result = input(prompt)
  if not result.strip():
      result = 0
  return result
print("Coverte horas em minutos! ")

h = int(checkInput("Digite quantas HORAS : "))
mn = 60
m = h * mn * mn

print(str(h)+"Horas é igual a "+str(m)+" segundos")
