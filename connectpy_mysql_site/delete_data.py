import mysql.connector
connect = mysql.connector.connect(host='localhost', database='pessoas', user='root', password='*****')
if connect.is_connected():
    print(f'\033[1;32mConectado ao servidor MySQL versão {connect.get_server_info()}\033[m')
    print()
cursor = connect.cursor()
try:
    cursor.execute('delete from dados_pessoas where n_cpf = "498798652351324"')
    connect.commit()
except:
    print('\033[1;31mERRO! Verifique o código digitado.\033[m')
connect.close()
if connect.is_closed():
    print(f'\033[1;32mDados adcionados com sucesso no banco de dados MySQL versão {connect.get_server_info()}!\033[m')
