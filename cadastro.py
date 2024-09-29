import sqlite3

# Função para adicionar um cliente
def adicionar_cliente(nome, telefone, email):
    conn = sqlite3.connect('salon.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nome, telefone, email) VALUES (?, ?, ?)", (nome, telefone, email))
    conn.commit()
    conn.close()
    print("Cliente cadastrado com sucesso!")

# Função para adicionar um serviço
def adicionar_servico(nome, preco):
    conn = sqlite3.connect('salon.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO servicos (nome, preco) VALUES (?, ?)", (nome, preco))
    conn.commit()
    conn.close()
    print("Serviço cadastrado com sucesso!")

# Função para agendar um serviço
def agendar_servico(cliente_id, servico_id, data, hora):
    conn = sqlite3.connect('salon.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO agendamentos (cliente_id, servico_id, data, hora) VALUES (?, ?, ?, ?)", (cliente_id, servico_id, data, hora))
    conn.commit()
    conn.close()
    print("Serviço agendado com sucesso!")

# Função para visualizar todos os clientes
def ver_clientes():
    conn = sqlite3.connect('salon.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Telefone: {cliente[2]} | Email: {cliente[3]}")
    conn.close()

# Função para visualizar todos os serviços
def ver_servicos():
    conn = sqlite3.connect('salon.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM servicos")
    servicos = cursor.fetchall()
    for servico in servicos:
        print(f"ID: {servico[0]} | Serviço: {servico[1]} | Preço: R$ {servico[2]:.2f}")
    conn.close()

# Função para visualizar agendamentos
def ver_agendamentos():
    conn = sqlite3.connect('salon.db')
    cursor = conn.cursor()
    query = '''SELECT ag.id, c.nome, s.nome, ag.data, ag.hora 
               FROM agendamentos ag
               JOIN clientes c ON ag.cliente_id = c.id
               JOIN servicos s ON ag.servico_id = s.id'''
    cursor.execute(query)
    agendamentos = cursor.fetchall()
    for agendamento in agendamentos:
        print(f"ID: {agendamento[0]} | Cliente: {agendamento[1]} | Serviço: {agendamento[2]} | Data: {agendamento[3]} | Hora: {agendamento[4]}")
    conn.close()
