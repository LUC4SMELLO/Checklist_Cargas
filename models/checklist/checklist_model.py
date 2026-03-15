from typing import Literal

from database.banco_dados_cargas import conectar_banco_dados_cargas
from constants.banco_dados import TABELA_CARGAS


class ChecklistModel:
    def __init__(self):
        pass

    def inserir_carga(self, dados: dict):

        conexao = None
        try:
            conexao = conectar_banco_dados_cargas()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                INSERT INTO {TABELA_CARGAS} (
                data,
                numero_carga,
                nota_fiscal,
                boleto,
                acerto,
                mapa,
                troca,
                problema,
                status
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                    (
                        dados["data"],
                        dados["numero_carga"],
                        dados["nota_fiscal"],
                        dados["boleto"],
                        dados["acerto"],
                        dados["mapa"],
                        dados["troca"],
                        dados["problema"],
                        "pendente"
                    )
            )

            conexao.commit()

        except Exception as erro:
            print("Erro ao inserir carga: ", erro)
            return []

        finally:
            if conexao:
                conexao.close()

    def editar_carga(self, dados: dict):
        
        conexao = None
        try:
            conexao = conectar_banco_dados_cargas()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                UPDATE {TABELA_CARGAS}
                SET nota_fiscal = ?,
                boleto = ?,
                acerto = ?,
                mapa = ?,
                troca = ?,
                problema = ?
                WHERE numero_carga = ?
                """,
                    (
                        dados["nota_fiscal"],
                        dados["boleto"],
                        dados["acerto"],
                        dados["mapa"],
                        dados["troca"],
                        dados["problema"],
                        dados["numero_carga"]
                    )
            )

            conexao.commit()

        except Exception as erro:
            print("Erro ao editar carga: ", erro)
            return []

        finally:
            if conexao:
                conexao.close()

    def excluir_carga(self, dados: dict):

        conexao = None
        try:
            conexao = conectar_banco_dados_cargas()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                DELETE FROM {TABELA_CARGAS}
                WHERE numero_carga = ?
                """,
                    (
                        dados["numero_carga"],
                    )
            )

            conexao.commit()

        except Exception as erro:
            print("Erro ao excluir carga: ", erro)
            return []

        finally:
            if conexao:
                conexao.close()

    def concluir_carga(self, dados: dict):

        conexao = None
        try:
            conexao = conectar_banco_dados_cargas()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                UPDATE {TABELA_CARGAS}
                SET status = ?
                WHERE numero_carga = ?
                """,
                    (
                        "concluido",
                        dados["numero_carga"]
                    )
            )

            conexao.commit()
    
        except Exception as erro:
            print("Erro ao concluir carga: ", erro)
            return []
    
        finally:
            if conexao:
                conexao.close()

    def carregar_cargas(self, tipo_carga: Literal["pendente", "concluido"]):

        conexao = None
        try:
            conexao = conectar_banco_dados_cargas()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                SELECT
                    numero_carga,
                    nota_fiscal,
                    boleto,
                    acerto,
                    mapa,
                    troca,
                    problema
                FROM {TABELA_CARGAS}
                WHERE status = ?
                """,
                    (
                        tipo_carga,
                    )
            )

            colunas = [desc[0] for desc in cursor.description]
            registros = [dict(zip(colunas, row)) for row in cursor.fetchall()]

            return registros
        
        except Exception as erro:
            print("Erro ao carregar cargas pendentes: ", erro)
            return ["erro caralho"]
        
        finally:
            if conexao:
                conexao.close()
