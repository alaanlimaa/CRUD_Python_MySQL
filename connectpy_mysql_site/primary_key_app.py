import mysql.connector
connect = mysql.connector.connect(host='localhost', database='pessoas',user='root', password='*****')
if connect.is_connected():
    print(f'\033[1;32mConectado ao servidor MySQL versão {connect.get_server_info()}\033[m')
cursor = connect.cursor()
cursor.execute('alter table dados_pessoas add primary key (n_cpf)')
connect.commit()
connect.close()


