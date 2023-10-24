import cx_Oracle

# Configuração da conexão
dsn = cx_Oracle.makedsn('oracle.fiap.com.br', '1521', service_name='ORCL')
user = 'rm99627'
password = '051298'

# Estabeleça uma conexão
conn = cx_Oracle.connect(user=user, password=password, dsn=dsn)

# Crie um cursor para executar consultas SQL
cursor = conn.cursor()

# Consulta SQL
sql = "SELECT * FROM sua_tabela"

# Executa a consulta
cursor.execute(sql)

# Recupera os resultados
for row in cursor:
    print(row)  # Isso imprimirá cada linha da consulta

# Feche o cursor e a conexão quando terminar
cursor.close()
conn.close()
