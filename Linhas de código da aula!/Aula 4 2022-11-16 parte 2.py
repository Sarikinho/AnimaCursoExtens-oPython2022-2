#1o. passo: importar a biblioteca sqlite3
import sqlite3

#2o. passo: Vamos estabelecer uma conexão com o banco
conexao = sqlite3.connect("dc_universe.db")

#3o. passo: Criar um objeto do tipo cursor
cursor = conexao.cursor()

#4o. passo: Comando SQL do banco
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)')"

#5o. passo: Executar o comando SQL
cursor.execute(sql)

#6o. passo: Confirmar o INSERT com commit() e fechar o banco
conexao.commit()
conexao.close()