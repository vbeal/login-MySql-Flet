# models.py

import os
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
    password = Column(String(128), nullable=False)  # Coluna password, não nulo (tamanho ajustado para hash)

# Criar a tabela no banco de dados
Base.metadata.create_all(engine)

# Testar a conexão
if __name__ == "__main__":
    print("Conexão bem-sucedida!")
