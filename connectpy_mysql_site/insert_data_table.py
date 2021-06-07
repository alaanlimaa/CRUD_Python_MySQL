import mysql.connector
connect = mysql.connector.connect(host='localhost', database='pesssoas', user='root', password='28101565')
if connect.is_connected():
    print(f'\033[1;32mConectado ao servidor MySQL versão {connect.get_server_info()}\033[m')
    print()
cursor = connect.cursor()
cont = 1
dados = []
while True:
    cpf = input(f'{cont}º Pessoa CPF = ')[:15]
    nome = input(f'{cont}º Pessoa Nome = ').title()[:20]
    sexo = ' '
    while sexo not in 'MF':
        sexo = input(f'{cont}º Pessoa Sexo [M/F] = ').strip().upper()[0]
    idade = input(f'{cont}º Pessoa Idade = ')[:3]
    cidade = input(f'{cont}º Pessoa Cidade = ').title()[:20]
    dadospessoa = (cpf, nome, sexo, idade, cidade)
    dados.append(dadospessoa)
    resp = input('Deseja continuar [S/N]: ').upper().strip()[0]
    while resp not in 'SN':
        resp = input('Deseja continuar [S/N]: ').upper().strip()[0]
    if resp == 'N':
        break
    cont += 1
for i in dados:
    cursor.execute(f'insert into dados_pessoas values {i}')
    connect.commit()
connect.close()
if connect.is_closed():
    print(f'\033[1;32mDados adcionados com sucesso no banco de dados MySQL versão {connect.get_server_info()}!\033[m')