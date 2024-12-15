# models.py

import os
import bcrypt  # Importar bcrypt para hash de senha
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import DATABASE_URI

# Imprimir variáveis de ambiente para depuração
print("DB_USER:", os.getenv('DB_USER'))
print("DB_PASSWORD:", os.getenv('DB_PASSWORD'))
print("DB_HOST:", os.getenv('DB_HOST'))
print("DB_PORT:", os.getenv('DB_PORT'))
print("DB_NAME:", os.getenv('DB_NAME'))

# Criar uma instância do engine para conexão com o banco de dados
engine = create_engine(DATABASE_URI, echo=True)

# Criar uma sessão de conexão com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Base para a criação de tabelas
Base = declarative_base()

# Definir o modelo Usuario
class Usuario(Base):
    __tablename__ = 'usuarios'  # Nome da tabela no banco de dados
    id = Column(Integer, primary_key=True)  # Coluna ID, chave primária
    username = Column(String(50), unique=True, nullable=False)  # Coluna username, único e não nulo
    password = Column(String(60), nullable=False)  # Coluna password, não nulo (tamanho ajustado para hash)

# Criar a tabela no banco de dados
Base.metadata.create_all(engine)

# Função para cadastrar novo usuário com senha hash
def cadastrar_usuario(username, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    novo_usuario = Usuario(username=username, password=hashed_password.decode('utf-8'))
    session.add(novo_usuario)
    session.commit()
    print(f"Usuário {username} cadastrado com sucesso!")

# Testar a conexão
if __name__ == "__main__":
    # Cadastrar um novo usuário para teste
    cadastrar_usuario("usuario_teste", "senha_teste")
    print("Conexão bem-sucedida!")
