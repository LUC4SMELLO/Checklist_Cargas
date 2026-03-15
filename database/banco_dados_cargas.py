import sqlite3

from constants.banco_dados import BANCO_DADOS_CARGAS, TABELA_CARGAS


def conectar_banco_dados_cargas():
    return sqlite3.connect(BANCO_DADOS_CARGAS)

def criar_tabela_cargas():

    conexao = conectar_banco_dados_cargas()
    cursor = conexao.cursor()

    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {TABELA_CARGAS} (
        data TEXT,
        numero_carga INTEGER,
        nota_fiscal INTEGER,
        boleto INTEGER,
        acerto INTEGER,
        mapa INTEGER,
        troca INTEGER,
        problema INTEGER,
        status TEXT
        )
        """
    )

    conexao.commit()
    conexao.close()
