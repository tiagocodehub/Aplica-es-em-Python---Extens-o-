import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('salon.db')
cursor = conn.cursor()

# Criação das tabelas
cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT,
                    email TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS servicos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    preco REAL NOT NULL
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS agendamentos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cliente_id INTEGER,
                    servico_id INTEGER,
                    data TEXT,
                    hora TEXT,
                    FOREIGN KEY (cliente_id) REFERENCES clientes (id),
                    FOREIGN KEY (servico_id) REFERENCES servicos (id)
                )''')

print("Tabelas criadas com sucesso!")

# Fechar a conexão
conn.commit()
conn.close()

