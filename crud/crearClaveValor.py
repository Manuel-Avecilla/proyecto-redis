import redis

conexionRedis = redis.ConnectionPool(host='localhost', port=6379, db=0,decode_responses=True)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

# Para crar registros en la base de datos sólo debemos lanzar el comando set:
baseDatosRedis.set('libro_1', 'value_1')
baseDatosRedis.set('libro_2', 'value_2')
baseDatosRedis.set('libro_3', 'value_3')
baseDatosRedis.set('libro_4', 'value_4')
baseDatosRedis.set('libro_5', 'value_5')

baseDatosRedis.close()