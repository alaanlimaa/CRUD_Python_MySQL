import mysql.connector
connect = mysql.connector.connect(host='localhost', database='pessoas',user='root', password='****')
if connect.is_connected():
    print(f'\033[1;32mConectado ao servidor MySQL versão {connect.get_server_info()}\033[m')
    cursor = connect.cursor()
    cursor.execute('create table dados_pessoas ( n_cpf varchar(15) not null, c_nome varchar(20), '
                   'c_sexo varchar(01), c_idade varchar(03), c_cidade varchar(20));')
    connect.close()
    if connect.is_closed():
        print(f'\033[1;32mConexão ao servidor MySQL versão {connect.get_server_info()}\033[m')

