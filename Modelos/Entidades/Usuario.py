from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin

class Usuario(UserMixin):   
    def __init__(self,id, nombre, apellido,username,descripcion,fechaAlta,ciudad,imagenPerfil, contraseña,email)-> None:
        self.id=id
        self.Nombre=nombre
        self.Apellido=apellido
        self.Username=username
        self.email=email
        self.contraseña=contraseña
        self.Descripcion=descripcion
        self.FechaAlta=fechaAlta
        self.Ciudad=ciudad
        self.ImagenPerfil=imagenPerfil
        
    
    @classmethod
    def check_password(self, hashed_password, contraseña):
        return check_password_hash(hashed_password, contraseña)

# print(generate_password_hash('admin123'))
        



#     @property
#     def Nombre(self):
#         return self.__Nombre

# #Set
#     @Nombre.setter
#     def Nombre(self,valor):
#         self.__Nombre=valor

#     #Get
#     @property
#     def Apellido(self):
#         return self.__Apellido

# #Set
#     @Apellido.setter
#     def Apellido(self,valor):
#         self.__Apellido=valor

#    #Get
#     @property
#     def Username(self):
#         return self.__Username

# #Set
#     @Username.setter
#     def Username(self,valor):
#          self.__Username=valor

#   #Get
#     @property
#     def Email(self):
#         return self.__Email
# #Set
#     @Email.setter
#     def Email(self,valor):
#          self.__Email=valor

#     #Get
#     @property
#     def Contraseña(self):
#         return self.__Contraseña
# #Set
#     @Contraseña.setter
#     def Contraseña(self,valor):
#          self.__Contraseña=valor

#     #Get
#     @property
#     def Descripcion(self):
#         return self.__Descripcion



# #Set
#     @Descripcion.setter
#     def Descripcion(self,valor):
#          self.__Descripcion=valor

#     #Get
#     @property
#     def FechaAlta(self):
#         return self.__FechaAlta

# #Set
#     @FechaAlta.setter
#     def FechaAlta(self,valor):
#          self.__FechaAlta=valor

    
#     #Get
#     @property
#     def Ciudad(self):
#         return self.__Ciudad

# #Set
#     @Ciudad.setter
#     def Ciudad(self,valor):
#          self.__Ciudad=valor


