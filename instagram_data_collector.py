import instaloader
import configparser
import csv

# Inicializa Instaloader
L = instaloader.Instaloader()

# Lee las credenciales del archivo .conf
config = configparser.ConfigParser()
config.read('config.conf')

# Extrae el usuario y la contraseña
USER = config['DEFAULT']['USER']
PASSWORD = config['DEFAULT']['PASSWORD']

# Intenta iniciar sesión
try:
    L.login(USER, PASSWORD)
    print("Inicio de sesión exitoso.")
except instaloader.exceptions.BadCredentialsException:
    print("Error: Usuario o contraseña incorrectos.")
    exit()
except instaloader.exceptions.ConnectionException:
    print("Error: Problema de conexión.")
    exit()

# Obtiene el perfil
profile = instaloader.Profile.from_username(L.context, USER)

data = [["username", "status"]]

# Límite de contactos para pruebas
limit = 15
count = 0

# Itera sobre los seguidos y verifica si el perfil es privado
print(f"\nLista de usuarios seguidos (limitado a {limit} para pruebas):")
for following in profile.get_followees():
    if count >= limit:
        break
    status = "privado" if following.is_private else "público"
    print(f"{following.username} es {status}")
    data.append([following.username, status])
    count += 1

# Exporta los datos a un archivo CSV
with open("seguidores.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("\nLos resultados se han exportado a 'seguidores.csv' con éxito.")