from app.database.db import getConnection
from app.model.animal_model import Animal

# Função para adicionar um novo animal no banco
def criar_animal(animal: Animal):
    conn = getConnection()
    cur = conn.cursor()
    
    sql = """
    INSERT INTO animal (id_animal, id_fazenda, id_raca, nome, sexo, data_nasc, peso, status_saude, fase_vida) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    try:
        cur.execute(sql, (
            animal.id_animal,
            animal.id_fazenda,
            animal.id_raca,
            animal.nome,
            animal.sexo,
            animal.data_nasc,
            animal.peso,
            animal.status_saude,
            animal.fase_vida
        ))
        conn.commit()
    finally:
        cur.close()
        conn.close()
        
    return {"msg": "Animal criado com sucesso"}
