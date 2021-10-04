from time import sleep
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="registros_py"
)
cursor = db.cursor()

def titulo(txt):
    txt=str(txt)
    print("=-="*20)
    print(f"{txt.title() :>30}")
    print("=-="*20)

def adicao_usuarios():
    
    name = str(input("nome: "))
    email = str(input("email: "))
    senha = str(input("senha: "))
    sql = "INSERT INTO pessoas_cadastradas (nome,email,senha) VALUES(%s,%s,%s)"
    val =(name,email,senha)
    cursor.execute(sql,val)
    db.commit()



def mostrartabela():
    cursor.execute('SELECT * FROM pessoas_cadastradas')
    data = (cursor.fetchall())
    for identificacao in data:
         print(f"{identificacao[0]:<5}|{identificacao[1]:<50}|{identificacao[2]:<50}|{identificacao[3]:<50}")
        

def excluircadastros():
    id_pessoa = input(str("Digite o id_pessoa para remover o cadastro: "))
    cursor.execute(f"DELETE FROM pessoas_cadastradas WHERE id_pessoa = {id_pessoa} ")
    db.commit()
    print("Cadastro excluido com sucesso!")
    sleep(3)