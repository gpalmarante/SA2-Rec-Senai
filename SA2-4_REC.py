def checkInput(prompt):
  result = input(prompt)
  if not result.strip():
      result = 0
  return result
under = "_"
print("Desenhar uma linha!")
n = int(checkInput("Digite o comprimento da linha : "))

line = under*n
print(under*n)