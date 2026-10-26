import redis

conexionRedis = redis.ConnectionPool(host='localhost', port=6379, db=0,decode_responses=True)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

# Obtener el valor de la clave "libro_1" pero en binario:
# print(baseDatosRedis.get("libro_1"))

# Obtener el valor de la clave "libro_1" pero en String( Al tener la decodificación ya activada no nos haría falta)
# baseDatosRedis.get("libro_1").decode("utf-8")

# Obtener el valor de la clave "libro_2" que al tener tiempo de vida estará ya vacía
# print(baseDatosRedis.get("libro_2"))


claves = baseDatosRedis.keys()

print('----------------------------')
if len(claves) == 0:
    print('Sin datos')
else:
    for clave in claves:
        
        valor = baseDatosRedis.get(clave)
        print('Clave:', clave , ' y Valor: ',valor )
print('----------------------------')


baseDatosRedis.close()