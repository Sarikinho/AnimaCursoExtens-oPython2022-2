#Comando input():quero permitir que o usuario digite algo
nome = str(input("Digita seu nome:\n"))

#Exibir na tela o nome e pedir a idade e exibir a idade
print("Olá",(nome),", quantos anos você tem?")
idade = int(input())

#Ainda não foi dado, só um teste mesmo
if idade > 18:
  print("Você é maior de idade")
else:
  print("Você é menor de idade")

#Dobrei o int (18)
dobro = idade * 2
print (f"\nO dobro da sua idade é {int(dobro)}")

#Agora sim a Estrutura condicional - If (Se) e Else (Então)
diferença = 18 - idade 

if int(idade) < 18:
  print ("Faltam", abs(diferença), "anos pra você completar a maior idade")
else:
  print ("Fazem", abs(diferença),"anos que você atingiu a maior idade")
# abs = Número em módulo


genero = input("Qual o seu gênero?\na) Masculino\nb) Fêminino\nc) Nenhum dos dois\n").title()
 
if genero == "A":
  print ("Olá moço!")
  gen = "Masculino"
elif genero == "B": 
  print ("Olá moça!")
  gen = "Feminino"
elif genero == "C": 
  print ("Olá pessoa!")
  gen = "Indefinido"
print ("\nForam coletadas as seguintes informações:\nNome:",nome,"\nIdade:",idade, "\nGênero:",gen)