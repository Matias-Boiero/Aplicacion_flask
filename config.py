# SETTINGS/Session
class Config:
    SECRET_KEY = 'mynewsecretKey'


class configuracionDesarrolo(Config):
    # CONFIGURACION DEL MYSQL
    DEBUG=True
    MYSQL_HOST='127.0.0.1'
    MYSQL_USER='Matias'
    MYSQL_PASSWORD='Silas_2021'
    MYSQL_DB='Datask-db'    
    

config={
    'development':configuracionDesarrolo
}