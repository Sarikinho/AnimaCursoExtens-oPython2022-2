# Pede o nome do aluno e sua nota (0 a 10), se ele tirou nota boa (o famoso 10), FRASE MOTIVACIONAL
nome = input("Qual o seu nome?\n")
nota = float(input(f"{nome}, quanto você tirou na prova final do curso de Python?\n"))

if nota == 10:
  print ("\nParabéns!")
elif nota == 0: 
  print ("\nTa de sacanagem???")
elif nota > 10 or nota < 0:
  print("Como????????")
else:
  print ("\nMelhore, na proxima quero 10!")



