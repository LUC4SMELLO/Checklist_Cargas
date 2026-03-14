import sqlite3

from constants.banco_dados import BANCO_DADOS_CARGAS_CONCLUIDAS, TABELA_CARGAS_CONCLUIDAS


def conectar_banco_dados_cargas_concluidas():
    return sqlite3.connect(BANCO_DADOS_CARGAS_CONCLUIDAS)

def criar_tabela_cargas_concluidas():

    conexao = conectar_banco_dados_cargas_concluidas()
    cursor = conexao.cursor()

    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {TABELA_CARGAS_CONCLUIDAS} (
        data TEXT,
        numero_carga VARCHAR(7),
        nota_fiscal VARCHAR(1),
        boleto VARCHAR(1),
        acerto VARCHAR(1),
        mapa VARCHAR(1),
        troca VARCHAR(1),
        problema VARCHAR(1)
        )
        """
    )

    conexao.commit()
    conexao.close()
