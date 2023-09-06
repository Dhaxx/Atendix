import random
import base64
import hashlib

def gera_hash(senha):
    # Gerando o Salt
    numero_aleatorio = random.randint(0, 2**32 - 1)
    bytes_aleatorios = numero_aleatorio.to_bytes(4, byteorder='big')
    salt = base64.b64encode(bytes_aleatorios).decode('utf-8')

    #Gerando o Hash com salt
    senha_com_salt = senha + salt
    hash_obj = hashlib.sha256()
    hash_obj.update(senha_com_salt.encode('utf-8'))
    hash_result = hash_obj.hexdigest()
    return {
        salt,
        hash_result}

def valida_hash(senha, salt):
    senha_com_salt = senha + salt
    hash_obj = hashlib.sha256()
    hash_obj.update(senha_com_salt.encode('utf-8'))
    hash_result = hash_obj.hexdigest()
    return hash_result