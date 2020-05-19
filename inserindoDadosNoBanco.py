import MySQLdb
import from tkinter import messagebox

try:
    valor1 = "Valor1"
    valor2 = "Valor2"

    # cursorVar É A VARIÁVEL QUE VOCÊ DEFINIU NA CONEXÃO DO SEU BANCO: cursorVar = mysqlVar.cursor()
    # O SQL E ONDE ESTÁ (%s,%s)É ONDE SERÃO ADICIONADOS OS VALORES QUE VOCÊ DEFINIR..
    # QUE PODEM VIR DE CAMPOS DE TEXTOS OU OUTROS LOCAS. NO EXEMPLO EU USEI 2 VARIAVEIS  
    cursorVar.execute("INSERT INTO nomeDaTabela (campo1,campo2) VALUES (%s,%s)",(valor1, valor2))
    messagebox.showinfo("CONEXÃO", "CADASTRO REALIZADO COM SUCESSO")

    # SALVA AS ALTERAÇÕES FEITAS NO BANCO
    # IMPORTANTE CHAMAR ELE SEMPRE APÓS CADA TRANSAÇÃO PARA CONFIRMAR 
    mysqlVar.commit()
       
except:
    messagebox.showerror("CONEXÃO", "NÃO FOI POSSÍVEL CADASTRAR OS DADOS")
        
            