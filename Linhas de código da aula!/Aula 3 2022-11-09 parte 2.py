#criação de funções lesgo

preco = 19.90

#Calcular 5% de imposto, guardar na variavel imposto e exibir na tela
imposto = preco * 0.05
print("Seu imposto é",imposto)

preco2 = 100
imposto = preco2 * 0.05
print("Seu outro imposto é",imposto)

#Criar uma função "calcular_imposto()", que calcula um imposto de 5% e retorna a quem pediu
def calcular_imposto(preco_produto): #utilizado para definir o nome e a funcionalidade de sua função.
  imposto = preco_produto * 0.05
  return imposto 

#Aqui é o uso... aqui é imposto a calcular
preco = float(input("Digite o preço do produto\n"))
imposto = calcular_imposto(preco)
print(imposto)

#Explicação de variável local x global
print(preco) #????
preco_produto = 100
print (preco_produto)

#agora calcular imposto a alíquota agora é 7%

valores = [1.99, 24.50, 78.27, 1515.5]
#se eu quiser calcular o imposto destes quatro valores e mostrar na tela é assim:
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto(valor)}")

