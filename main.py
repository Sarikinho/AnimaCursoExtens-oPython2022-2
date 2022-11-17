import aula4p3 as a43

conexao, cursor = a43.conectar()

nome = input("Digite o nome do herói/vilão:\n")
nome_civil = input("Digite o nome civil do herói/vilão (nome real):\n")
tipo = input ("Tecle 1 para Herói(na) ou 2 para Vilã(o):\n")

#Consulta para o valor máximo usado no banco
sql = "SELECT MAX(pessoa_id)+1 FROM pessoas"
cursor.execute(sql)
pessoa_id = cursor.fetchone()[0] #O [0] pode ser posto aq

if tipo == "1":
  tipo = "Herói(na)"
elif tipo == "2":
  tipo = "Vilã(o)"
sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ('{pessoa_id}', '{nome}', '{nome_civil}', '{tipo}')"

cursor.execute(sql)
conexao.commit()
conexao.close()