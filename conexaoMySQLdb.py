"""CRIA UMA CONEXÃO COM O BANCO DE DADOS MySQLdb"""
import MySQLdb
 
try:
    mysqlVar = 0
    mysqlVar = MySQLdb.connect(host="localhost",    # seu host
                                    user="usuario",      # seu user
                                    passwd="senha", # sua senha
                                    db="database")  # nome da sua database
    cursorVar = mysqlVar.cursor()
    print("RODOU")
except:
    print("NÃO FOI POSSÍVEL CONECTAR COM O BANCO DE DADOS.")

