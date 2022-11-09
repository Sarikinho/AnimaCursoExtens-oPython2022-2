print("Início de aula 3 (09/11/2022)")

contador = 1

# Exibir de 1 até 10 repetidamente
while(contador <= 10):
  print (contador)
  contador = contador+1

# Laço for (python for = for each)
fruta = "goiaba"
print (fruta)

fruta1 = "laranja"
fruta2 = "maçã"
fruta3 = "uva"

#Lista
frutas = ["laranja", "maçã", "uva"]

#mostra todas
print (frutas)

#quero exibir apenas a 3a. furta (uva)
print(frutas[0])
print(frutas[1])
print(frutas[2])

#exibir quantas frutas tem na minha lista?
print (len(frutas)) #length = tamanho

#Quero incluir uma fruta nova
frutas.append("manga")

print(len(frutas)) #lenght = tamanho
print(frutas)

print (frutas[0])
print (frutas[1])
print (frutas[2])
print (frutas[3])
#print (frutas[4])

i=0
while(i<len(frutas)):
  print(frutas[i])
  i = i + 1