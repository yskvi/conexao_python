import mysql.connector
# conexao com o banco de dados db_nota
conexao = mysql.connector.connect(host='localhost', database= 'db_nota', user= 'root', password= 'root')

nr_cnpj = (input('digite sua cnpj: '))
nm_razao_social = (input('digite o nome novo: '))

update_cliente = f"update tb_cliente set nm_razao_social = '{nm_razao_social}' where nr_cnpj = '{nr_cnpj}';"


# comandos para executar dentro do banco de dados
cursor = conexao.cursor()
cursor.execute(f'{update_cliente}')
conexao.commit()
print('atualizado com sucesso')