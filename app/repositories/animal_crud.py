from app.database.db import getConnection
from app.model.animal_model import Animal


# Função para listar todos os animais
def listar_animais ():
    conn = getConnection()
    cur = conn.cursor()

    sql = """
    SELECT 
        a.id_animal, a.id_fazenda, a.id_raca, 
        a.nome, a.sexo, a.data_nasc, a.peso, a.status_saude, a.fase_vida
    FROM animal a
    """

    try:
        cur.execute(sql)
        rows = cur.fetchall()
    finally:
        cur.close()
        conn.close()

    return [
        Animal (
            id_animal=a[0],
            id_fazenda=a[1],
            id_raca=a[2],
            nome=a[3],
            sexo=a[4],
            data_nasc= str(a[5]) if a[5] else None,
            peso=a[6],
            status_saude=a[7],
            fase_vida=a[8]
        ) for a in rows
    ]


# Função para adicionar um novo animal no banco
def criar_animal (animal: Animal):
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

    except Exception:
        conn.rollback()  # Desfaz a operação no banco
        raise

    finally:
        cur.close()
        conn.close()
        
    return {"msg": "Animal criado com sucesso"}




