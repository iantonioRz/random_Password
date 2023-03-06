import  random
import string

longitud = 10  # Longitud de la clave de seguridad

# Generamos una cadena de caracteres alfanuméricos aleatorios de la longitud deseada
clave = ''.join(random.choices(string.ascii_letters + string.digits, k=longitud))

print("Tu clave de seguridad aleatoria es:", clave)