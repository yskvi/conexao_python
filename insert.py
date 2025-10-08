import mysql.connector
# conexao com o banco de dados db_nota
conexao = mysql.connector.connect(host='localhost', database= 'db_nota', user= 'root', password= 'root')

nr_cnpj = (input('digite sua cnpj: '))
nm_razao_social = (input('digite sua razão social: '))
nm_pais = (input('digite o nome do seu pais: '))
nm_email = (input('digite seu email: '))

insert_cliente = f"insert into tb_cliente values ('{nr_cnpj}' , '{nm_razao_social}' , '{nm_pais}' , '{nm_email}');"


# comandos para executar dentro do banco de dados
cursor = conexao.cursor()
cursor.execute(f'{insert_cliente}')
conexao.commit()
print('Inserido com sucesso')