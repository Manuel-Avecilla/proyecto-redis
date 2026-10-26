import redis

conexionRedis = redis.ConnectionPool(host='localhost', port=6379, db=0,decode_responses=True)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

# Podemos guardar archivos JSON en nuestra base de datos Redis:
res1 = baseDatosRedis.json().set("usuarios:1", "$", {"nombre": "Jorge", "apellido": "Baron", "edad": 37})
res2 = baseDatosRedis.json().set("usuarios:2", "$", {"nombre": "Lucía", "apellido": "Benitez", "edad": 24})

# O podemos guardar un array de datos en json:
baseDatosRedis.json().set("usuarios_array", "$", [])
res3 = baseDatosRedis.json().arrappend("usuarios_array", "$", {"nombre": "Pepe", "apellido": "Sanchez", "edad": 45})
res4 = baseDatosRedis.json().arrappend("usuarios_array", "$", {"nombre": "Calisto", "apellido": "Melibea", "edad": 67})

print(baseDatosRedis.json().get("usuarios_array"))

# En este caso para filtrar en JSON, usaremos la segunda forma para guardarlos, la de array:
res1 = baseDatosRedis.json().get("usuarios_array", '$[?(@.edad > 50)]')
res2 = baseDatosRedis.json().get("usuarios_array", '$[?(@.nombre == "Pepe")]')

print(res1)
print(res2)

baseDatosRedis.json().delete('usuarios:1')
baseDatosRedis.json().delete('usuarios:2')
baseDatosRedis.json().delete('usuarios_array')

baseDatosRedis.close()