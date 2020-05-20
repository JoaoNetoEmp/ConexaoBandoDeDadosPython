
import MySQLdb
from tkinter import messagebox

try:
    valor1 = "NovoValor1"
    valor2 = "NovoValor2"
    valor3 = "NovoValor3"
    valor4 = 1

    # cursorVar É A VARIÁVEL QUE VOCÊ DEFINIU NA CONEXÃO DO SEU BANCO: cursorVar = mysqlVar.cursor()
    # O SQL E ONDE ESTÁ %s É ONDE SERÃO ATUALIZADO OS VALORES QUE VOCÊ DEFINIR.. EXCETO NO ID
    # O ID É A REFERÊNCIA DO CADASTRO QUE O BD TERÁ PARA ATUALIZARR OS VALORES
    cursorVar.execute("""UPDATE estudante SET Campo1 = %s, Campo2 = %s, Campo3 = %s WHERE ID = %s""",(valor1, valor2, valor3, valor4))
    messagebox.showinfo("CONEXÃO","ATUALIZADO COM SUCESSO")

    # CONFIRMA A TRANSAÇÃO
    # myswlVar É A VARIAVEL QUE VOCÊ DEFINIU NA HORA DE CRIAR A CONEXÃO COM O BANCO
    mysqlVar.commit()

except:
    messagebox.showerror("CONEXÃO","ERRO AO ATUALIZAR")

