from app.database.db import getConnection
from app.model.v_producao_model import vProducaoLeiteAnimal

# Função para listar a produção de todos os animais
def listar_produção ():
    conn = getConnection()
    cur = conn.cursor()

    sql = """
    SELECT 
        a.id_animal, a.nome_animal, a.especie, 
        a.raca, a.total_ordenhas, a.total_litros_produzidos
    FROM v_producao_leite_por_animal a
    """

    try:
        cur.execute(sql)
        rows = cur.fetchall()
    finally:
        cur.close()
        conn.close()

    return [
        vProducaoLeiteAnimal (
            id_animal=f[0],
            nome_animal=f[1],
            especie=f[2],
            raca=f[3],
            total_ordenhas= f[4],
            total_litros_produzidos=f[5]
        ) for f in rows
    ]

# Função para buscar a produção pelo id do animal
def resumo_producao (id: int):
    conn = getConnection()
    cur = conn.cursor()

    sql = """
    SELECT 
        a.id_animal, a.nome_animal, a.especie, 
        a.raca, a.total_ordenhas, a.total_litros_produzidos
    FROM v_producao_leite_por_animal a
    WHERE a.id_animal = %s
    """

    try:
        cur.execute(sql, (id,))
        row = cur.fetchone()
    finally:
        cur.close()
        conn.close()

    if row:
        return vProducaoLeiteAnimal (
                id_animal=row[0],
                nome_animal=row[1],
                especie=row[2],
                raca=row[3],
                total_ordenhas= row[4],
                total_litros_produzidos=row[5]
        )
    return None
