import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234567',
    database='Python',
)
cursor = conexao.cursor()

nome = "Monitor"
valor = 1200

comando = f'INSERT INTO Vendas (NomeProduto, valor) VALUES ("{nome}",{valor})'
cursor.execute(comando)
comando = 'SELECT * FROM VENDAS'
cursor.execute(comando)
#conexao.commit()
resultado = cursor.fetchall()
print(resultado)

cursor.close()
conexao.close()