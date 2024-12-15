# register_user.py

import bcrypt
from models import Usuario, session

def cadastrar_usuario(username, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    novo_usuario = Usuario(username=username, password=hashed_password.decode('utf-8'))
    session.add(novo_usuario)
    session.commit()
    print(f"Usuário {username} cadastrado com sucesso!")
