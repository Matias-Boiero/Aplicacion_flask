
from .Entidades.Usuario import Usuario

class UsuarioModelo():
    
    # el @classmethod es un decorador que me permite instanciar el metodo sin instanciarlo
    @classmethod
    def login(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, Contraseña, Email FROM Usuario
                    WHERE Email = '{}'""".format(usuario.email)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                print(row)
                #usuario = Usuario(row[0],Usuario.check_password(row[1], usuario.contraseña),row[2])
                usuario = Usuario(row[0],None,None,None,None,None,None,None,Usuario.check_password(row[1], usuario.contraseña),row[2])
                return usuario
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_id(self, db, id):
        
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id,Username, Email FROM usuario WHERE id= {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return Usuario(row[0],None,None,row[1],None,None,None,None,None,row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
            
