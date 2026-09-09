from database.conexao import conexao
from models.usuario import usuario


class UsuarioRepository:
    def inserir(self, usuario: usuario):
        conn = conexao.conectar()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO usuario (
                cpf, cep, nome, id_perfil, email, senha, data_de_nascimento, sexo, tipo
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                usuario.cpf,
                usuario.cep,
                usuario.nome,
                usuario.id_perfil,
                usuario.email,
                usuario.senha,
                str(usuario.data_de_nascimento),
                usuario.sexo,
                usuario.tipo,
            ),
        )
        conn.commit()
        conn.close()

    def buscar_por_email(self, email):
        conn = conexao.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id_usuario, cpf, cep, nome, id_perfil, email, senha, data_de_nascimento, sexo, tipo FROM usuario WHERE email = ?", (email,))
        row = cursor.fetchone()
        conn.close()
        if not row:
            return None
        u = usuario(
            id_usuario=row[0],
            cpf=row[1],
            cep=row[2],
            nome=row[3],
            id_perfil=row[4],
            email=row[5],
            senha=row[6],
            data_de_nascimento=row[7],
            sexo=row[8],
            tipo=row[9],
        )
        return u

    def listar(self):
        conn = conexao.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id_usuario, cpf, cep, nome, id_perfil, email, senha, data_de_nascimento, sexo, tipo FROM usuario")
        rows = cursor.fetchall()
        conn.close()
        usuarios = []
        for row in rows:
            usuarios.append(usuario(
                id_usuario=row[0],
                cpf=row[1],
                cep=row[2],
                nome=row[3],
                id_perfil=row[4],
                email=row[5],
                senha=row[6],
                data_de_nascimento=row[7],
                sexo=row[8],
                tipo=row[9],
            ))
        return usuarios

    def buscar_por_id(self, id_usuario):
        conn = conexao.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id_usuario, cpf, cep, nome, id_perfil, email, senha, data_de_nascimento, sexo, tipo FROM usuario WHERE id_usuario = ?", (id_usuario,))
        row = cursor.fetchone()
        conn.close()
        if not row:
            return None
        return usuario(
            id_usuario=row[0],
            cpf=row[1],
            cep=row[2],
            nome=row[3],
            id_perfil=row[4],
            email=row[5],
            senha=row[6],
            data_de_nascimento=row[7],
            sexo=row[8],
            tipo=row[9],
        )

    def excluir(self, id_usuario):
        conn = conexao.conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuario WHERE id_usuario = ?", (id_usuario,))
        conn.commit()
        conn.close()
    
    def atualizar(self, usuario: usuario):
        conn = conexao.conectar()
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE usuario SET
                cpf = ?,
                cep = ?,
                nome = ?,
                id_perfil = ?,
                email = ?,
                senha = ?,
                data_de_nascimento = ?,
                sexo = ?,
                tipo = ?
            WHERE id_usuario = ?
            """,
            (
                usuario.cpf,
                usuario.cep,
                usuario.nome,
                usuario.id_perfil,
                usuario.email,
                usuario.senha,
                str(usuario.data_de_nascimento),
                usuario.sexo,
                usuario.tipo,
                usuario.id_usuario,
            ),
        )
        conn.commit()
        conn.close()