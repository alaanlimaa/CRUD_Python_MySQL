import mysql.connector
connect = mysql.connector.connect(host='localhost', user='root', password='*****')
if connect.is_connected():
    print(f'\033[1;32mConectado ao servidor MySQL versão {connect.get_server_info()}\033[m')
cursor = connect.cursor()
cursor.execute('create database pessoas')
connect.close()
if connect.is_closed():
    print(f'\033[1;32mConexão ao servidor MySQL versão {connect.get_server_info()} encerrada!\033[m')
    print(f'\033[1;32mBanco de dados criado com sucesso!\033[m')
