import sqlite3

from constants.banco_dados import BANCO_DADOS_CARGAS_PENDENTES, TABELA_CARGAS_PENDENTES


def conectar_banco_dados_cargas_pendentes():
    return sqlite3.connect(BANCO_DADOS_CARGAS_PENDENTES)

def criar_tabela_cargas_pendentes():

    conexao = conectar_banco_dados_cargas_pendentes()
    cursor = conexao.cursor()

    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {TABELA_CARGAS_PENDENTES} (
        data TEXT,
        numero_carga VARCHAR(7),
        nota_fiscal VARCHAR(1),
        boleto VARCHAR(1),
        acerto VARCHAR(1),
        mapa VARCHAR(1),
        troca VARCHAR(1)
        )
        """
    )

    conexao.commit()
    conexao.close()
