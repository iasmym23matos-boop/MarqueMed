

import sqlite3


class Conexao:
    @staticmethod
    def conectar():
        # Cria (caso não exista) ou abre o banco de dados.
        conn = sqlite3.connect("MarqueMed.db")

        # Permite acessar as colunas pelo nome.
        conn.row_factory = sqlite3.Row

        # Retorna a conexão aberta.
        return conn


# Mantém compatibilidade com importações antigas que
# faziam `from database.conexao import conexao`.
conexao = Conexao
