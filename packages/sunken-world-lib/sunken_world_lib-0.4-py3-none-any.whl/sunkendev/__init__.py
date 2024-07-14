import shutil
import os

def instalar_archivos_jar():

    user_window = os.getlogin()

    # Ruta relativa a la carpeta que contiene los archivos .jar dentro de tu librería
    ruta_carpeta_jars = "libs"

    # Ruta absoluta a la carpeta de destino (por ejemplo, "mi_carpeta_jars")
    ruta_destino = os.path.join(os.getcwd(), "mi_carpeta_jars")

    # Obtener la lista de archivos .jar en la carpeta
    archivos_jar = [archivo for archivo in os.listdir(ruta_carpeta_jars) if archivo.endswith(".jar")]

    # Copiar cada archivo .jar a la carpeta de destino
    for archivo_jar in archivos_jar:
        ruta_jar = os.path.join(ruta_carpeta_jars, archivo_jar)
        shutil.copy(ruta_jar, ruta_destino)
        print(f"Archivo {ruta_jar} copiado a {ruta_destino}")