import mysql.connector

conexao = mysql.connector.connect(host='localhost', database= 'db_nota', user= 'root', password= 'root')

# if conexao.is_connected():
# db_info = conexao.get_server_info()
# print(f'conectado ao servidor {db_info}')
# cursor = conexao.cursor()
# cursor.execute('Select database();')
# linha = cursor.fetchone()
# print (f'Conectado ao bando de dados, {linha}')

criar_tabela= """create table tb_cliente(
                    nr_cpnj char(14) primary key,
                    nm_razao_social varchar(35) not null,
                    nm_pais varchar(28),
                    nm_email varchar(40) not null
);
create table tb_produto(
 cd_produto int auto_increment primary key,
 nm_produto varchar(25) not null,
 vl_produto decimal(5,2) not null
 );
 
 create table tb_nota(
  cd_nota int auto_increment primary key,
  dt_emissao date not null,
  dt_envio date not null
  vl_total decimal (6,2)
  fk_br_cnpj(14),
  foreign key (fk_nr_cpnj) references tb_cliente (nr_cnpj)
 );

                """

cursor = conexao.cursor()
cursor.execute(f'{criar_tabela}')
print(f'Tabela criada com sucesso ')

