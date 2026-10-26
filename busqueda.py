import redis

conexionRedis = redis.ConnectionPool(host='localhost', port=6379, db=0,decode_responses=True)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

# Ahora utilizamos la función scan_iter, que recibe por parámetro un patrón en las claves para obtener sólo las que necesitamos:
baseDatosRedis.set("libro_1","Quijote")
baseDatosRedis.set("libro_2","Hamlet")
baseDatosRedis.set("libro_3","Otelo")
baseDatosRedis.set("comic_1","Mortadelo y Filemón")
baseDatosRedis.set("comic_2","Superman")

print("Los Libros:")
for clave in baseDatosRedis.scan_iter('libro*'):
    print(clave)

print("Los Comics:")   
for clave in baseDatosRedis.scan_iter('comic*'):
    print(clave)

"""
El patrón puede ir acompañado por:
    *  -> Cualquier número de caracteres o ninguno
    ?  -> Un Carácter
    [] -> Que contenga los caracteres dentro de los corchetes
"""

baseDatosRedis.delete('libro_1')
baseDatosRedis.delete('libro_2')
baseDatosRedis.delete('libro_3')
baseDatosRedis.delete('comic_1')
baseDatosRedis.delete('comic_2')

baseDatosRedis.close()