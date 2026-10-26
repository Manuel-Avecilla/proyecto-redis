import redis

conexionRedis = redis.ConnectionPool(host='localhost', port=6379, db=0,decode_responses=True)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

# Para eliminar claves-valor de la base de datos:
baseDatosRedis.delete("libro_1")
baseDatosRedis.delete("libro_2")
baseDatosRedis.delete("libro_3")
baseDatosRedis.delete("libro_4")
baseDatosRedis.delete("libro_5")

baseDatosRedis.close()