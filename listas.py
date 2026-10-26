import redis

conexionRedis = redis.ConnectionPool(host='localhost', port=6379, db=0,decode_responses=True)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

# Podemos tener listas en redis también:
# Añadimos a la lista:
baseDatosRedis.lpush("usuarios:hobbies", "futbol:1") 
baseDatosRedis.lpush("usuarios:hobbies", "tenis:2")
baseDatosRedis.lpush("usuarios:hobbies", "rugby:2") 

# Obtener todos los elementos:
print(baseDatosRedis.lrange("usuarios:hobbies",0,-1))

# Obtener el primer elemento y eliminarlo:
baseDatosRedis.rpop("usuarios:hobbies")

baseDatosRedis.close()