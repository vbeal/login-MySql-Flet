# models.py

# Importar módulos necessários do SQLAlchemy
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Importar a configuração da URI do banco de dados
from config import DATABASE_URI

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
    password = Column(String(50), nullable=False)  # Coluna password, não nulo

# Criar a tabela no banco de dados
Base.metadata.create_all(engine)

# Testar a conexão
if engine:
    print("Conexão bem-sucedida!")
else:
    print("Falha na conexão.")
