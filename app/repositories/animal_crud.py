from app.database.db import getConnection
from app.model.animal_model import Animal, AnimalUpdate
from fastapi import HTTPException

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

# Função para buscar um animal pelo id
def buscar_animal (id: int):
    conn = getConnection()
    cur = conn.cursor()

    sql = """
    SELECT 
        a.id_animal, a.id_fazenda, a.id_raca, 
        a.nome, a.sexo, a.data_nasc, a.peso, a.status_saude, a.fase_vida
    FROM animal a
    WHERE a.id_animal = %s
    """

    try:
        cur.execute(sql, (id,))
        row = cur.fetchone()
    finally:
        cur.close()
        conn.close()

    if row:
        return Animal ( 
                id_animal=row[0],
                id_fazenda=row[1],
                id_raca=row[2],
                nome=row[3],
                sexo=row[4],
                data_nasc= str(row[5]) if row[5] else None,
                peso=row[6],
                status_saude=row[7],
                fase_vida=row[8]
            )
    return None

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

# Função que atualiza o animal a partir do id
def atualizar_animal (id: int, animal: AnimalUpdate):
    conn = getConnection()
    cur = conn.cursor()

    sql = """
    SELECT 
        a.id_animal
    FROM animal a
    WHERE a.id_animal = %s
    """

    cur.execute(sql, (id,))
    row = cur.fetchone()
    
    if not row:
        cur.close()
        conn.close()
        raise HTTPException(404, f"Animal não encontrado")
    
    fields = []
    values = []

    for campo, valor in animal.dict(exclude_unset=True).items():
        fields.append(f"{campo}=%s")
        values.append(valor)
    values.append(id)
    
    if not fields:
        cur.close()
        conn.close()
        raise HTTPException(400, f"Nenhum campo informado na atualização")
    
    try:
        sql = f"UPDATE animal SET {', '.join(fields)} WHERE id_animal=%s"
        cur.execute(sql, values)
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise 
    finally:
        cur.close()
        conn.close()
    return {"msg":"Animal atualizado com sucesso"}
    
# Função que deleta o animal a partir do id
def deletar_animal (id: int):
    conn = getConnection()
    cur = conn.cursor()

    sql = """
    DELETE FROM animal a
    WHERE a.id_animal = %s
    """
    try:
        cur.execute(sql, (id,))
        conn.commit
    except Exception as e:
        raise e
    finally:
        cur.close()
        conn.close()
    return {"msg":"Animal deletado com sucesso"}
