import mysql.connector
connect = mysql.connector.connect(host='localhost', database='pesssoas', user='root', password='28101565')
if connect.is_connected():
    print(f'\033[1;32mConectado ao servidor MySQL versão {connect.get_server_info()}\033[m')
    print()
cursor = connect.cursor()
cursor.execute('select c_nome from dados_pessoas')
colum = cursor.fetchall()
colum.sort()
for i in colum:
    print(i[0])