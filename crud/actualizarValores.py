import redis

conexionRedis = redis.ConnectionPool(host='localhost', port=6379, db=0,decode_responses=True)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

# Para actualizar el valor de una clave, sólo debemos lanzar de nuevo el comando set con un valor diferente:
baseDatosRedis.set("libro_1","El señor de los anillos")

baseDatosRedis.close()