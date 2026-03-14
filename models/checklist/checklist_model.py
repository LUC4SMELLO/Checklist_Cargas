from database.banco_dados_cargas_pendentes import conectar_banco_dados_cargas_pendentes
from constants.banco_dados import TABELA_CARGAS_PENDENTES

from database.banco_dados_cargas_concluidas import conectar_banco_dados_cargas_concluidas
from constants.banco_dados import TABELA_CARGAS_CONCLUIDAS


class ChecklistModel:
    def __init__(self):
        pass

    # -------------------------------------
    #           CARGAS PENDENTES
    # -------------------------------------

    def inserir_carga_pendente(self, dados: dict):

        conexao = None
        try:
            conexao = conectar_banco_dados_cargas_pendentes()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                INSERT INTO {TABELA_CARGAS_PENDENTES} (
                data,
                numero_carga,
                nota_fiscal,
                boleto,
                acerto,
                mapa,
                troca,
                problema
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                    (
                        dados["data"],
                        dados["numero_carga"],
                        dados["nota_fiscal"],
                        dados["boleto"],
                        dados["acerto"],
                        dados["mapa"],
                        dados["troca"],
                        dados["problema"]
                    )
            )

            conexao.commit()

        except Exception as erro:
            print("Erro ao inserir carga pendente: ", erro)
            return []

        finally:
            if conexao:
                conexao.close()

    def editar_carga_pendente(self, dados: dict):
        
        conexao = None
        try:
            conexao = conectar_banco_dados_cargas_pendentes()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                UPDATE {TABELA_CARGAS_PENDENTES}
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
            print("Erro ao editar carga pendente: ", erro)
            return []

        finally:
            if conexao:
                conexao.close()

    def excluir_carga_pendente(self, dados: dict):

        conexao = None
        try:
            conexao = conectar_banco_dados_cargas_pendentes()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                DELETE FROM {TABELA_CARGAS_PENDENTES}
                WHERE numero_carga = ?
                """,
                    (
                        dados["numero_carga"],
                    )
            )

            conexao.commit()

        except Exception as erro:
            print("Erro ao excluir carga pendente: ", erro)
            return []

        finally:
            if conexao:
                conexao.close()

    def carregar_cargas_pendentes(self):

        conexao = None
        try:
            conexao = conectar_banco_dados_cargas_pendentes()
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
                FROM {TABELA_CARGAS_PENDENTES}
                """
            )

            colunas = [desc[0] for desc in cursor.description]
            registros = [dict(zip(colunas, row)) for row in cursor.fetchall()]

            return registros
        
        except Exception as erro:
            print("Erro ao carregar cargas pendentes: ", erro)
            return []
        
        finally:
            if conexao:
                conexao.close()


    # -------------------------------------
    #           CARGAS CONCLUÍDAS
    # -------------------------------------

    def inserir_carga_concluida(self, dados: dict):

        conexao = None
        try:
            conexao = conectar_banco_dados_cargas_concluidas()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                INSERT INTO {TABELA_CARGAS_CONCLUIDAS} (
                data,
                numero_carga,
                nota_fiscal,
                boleto,
                acerto,
                mapa,
                troca,
                problema
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                    (
                        dados["data"],
                        dados["numero_carga"],
                        dados["nota_fiscal"],
                        dados["boleto"],
                        dados["acerto"],
                        dados["mapa"],
                        dados["troca"],
                        dados["problema"]
                    )
            )

            conexao.commit()

        except Exception as erro:
            print("Erro ao inserir carga concluída: ", erro)
            return []

        finally:
            if conexao:
                conexao.close()


    def excluir_carga_concluida(self, dados: dict):

        conexao = None
        try:
            conexao = conectar_banco_dados_cargas_concluidas()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                DELETE FROM {TABELA_CARGAS_CONCLUIDAS}
                WHERE numero_carga = ?
                """,
                    (
                        dados["numero_carga"],
                    )
            )

            conexao.commit()

        except Exception as erro:
            print("Erro ao excluir carga concluída: ", erro)
            return []

        finally:
            if conexao:
                conexao.close()

    def carregar_cargas_concluidas(self):

        conexao = None
        try:
            conexao = conectar_banco_dados_cargas_concluidas()
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
                FROM {TABELA_CARGAS_CONCLUIDAS}
                """
            )

            colunas = [desc[0] for desc in cursor.description]
            registros = [dict(zip(colunas, row)) for row in cursor.fetchall()]

            return registros
        
        except Exception as erro:
            print("Erro ao carregar cargas concluídas: ", erro)
            return []
        
        finally:
            if conexao:
                conexao.close()
