# Analizador de Privacidad de Perfiles de Instagram

## Descripción:

    Este script de Python permite analizar los perfiles de Instagram que sigue un usuario determinado y determinar si son públicos o privados. La información se almacena en un archivo CSV para su posterior análisis.

## Funcionalidades:

    Inicio de sesión en Instagram: Utiliza las credenciales proporcionadas en un archivo de configuración para iniciar sesión en Instagram.
    Obtención de datos: Extrae una lista de los usuarios que sigue el perfil especificado y verifica si sus perfiles son públicos o privados.
    Generación de reporte: Crea un archivo CSV con los nombres de usuario y su estado de privacidad.

## Instalación:

    git clone https://github.com/h3nr77/instagram-contacts.git
    pip install -r requirements.txt


## Configuración:
    Crea un archivo config.conf en la raíz del proyecto con el siguiente formato:

        [DEFAULT]
        USER = tu_usuario_de_instagram
        PASSWORD = tu_contraseña

## Ejecución:
    
    python instagram_data_collector.py


## Consideraciones:

    Limitaciones de Instagram: La API de Instagram puede tener limitaciones y cambios, lo que podría afectar el funcionamiento del script.
    Privacidad: Utiliza este script de forma responsable y respetuosa con las políticas de privacidad de Instagram.
    Personalización: Puedes personalizar el script para agregar más funcionalidades, como guardar imágenes de perfil, analizar publicaciones, etc.

## Contribuciones:

    ¡Las contribuciones son bienvenidas! Si encuentras algún error o deseas agregar nuevas características, por favor, crea un pull request.  

## Autor:

    Enrique

## Licencia:

    MIT


