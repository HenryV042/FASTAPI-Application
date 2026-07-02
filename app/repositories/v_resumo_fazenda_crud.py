from app.database.db import getConnection
from app.model.v_resumo_fazenda_model import vResumoFazenda

# Função para listar o resumo das fazendas
def listar_resumo ():
    conn = getConnection()
    cur = conn.cursor()

    sql = """
    SELECT 
        f.id_fazenda, f.nome_fazenda, f.nome_produtor, 
        f.area_hectares, f.total_animais, f.total_investido
    FROM v_resumo_fazendas f
    """

    try:
        cur.execute(sql)
        rows = cur.fetchall()
    finally:
        cur.close()
        conn.close()

    return [
        vResumoFazenda (
            id_fazenda=f[0],
            nome_fazenda=f[1],
            nome_produtor=f[2],
            area_hectares=f[3],
            total_animais= f[4],
            total_investido=f[5]
        ) for f in rows
    ]

# Função para buscar o resumo pelo id da fazenda
def resumo_fazenda (id: int):
    conn = getConnection()
    cur = conn.cursor()

    sql = """
    SELECT 
        f.id_fazenda, f.nome_fazenda, f.nome_produtor, 
        f.area_hectares, f.total_animais, f.total_investido
    FROM v_resumo_fazendas f
    WHERE f.id_fazenda = %s
    """

    try:
        cur.execute(sql, (id,))
        row = cur.fetchone()
    finally:
        cur.close()
        conn.close()

    if row:
        return vResumoFazenda (
            id_fazenda=row[0],
            nome_fazenda=row[1],
            nome_produtor=row[2],
            area_hectares=row[3],
            total_animais= row[4],
            total_investido=row[5],
        )
    return None
