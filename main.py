#Comando input():quero permitir que o usuario digite algo
nome = str(input("Digita seu nome:\n"))

#Exibir na tela o nome e pedir a idade e exibir a idade
print("Olá",(nome),", quantos anos você tem?")
idade = int(input())

print ("\nForam coletadas as seguintes informações:\nNome:",nome,"\nIdade:",idade)

#Ainda não foi dado, só um teste mesmo
if idade > 18:
  print("Você é maior de idade")
else:
  print("Você é menor de idade")

#Dobrei o int (18)
dobro = idade * 2
print (f"O dobro da sua idade é {int(dobro)}")