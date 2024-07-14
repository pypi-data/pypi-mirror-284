import setuptools

from setuptools import find_packages, setup
setup(
    name = 'sunken_world_lib',
    version = '0.6',
    packages=find_packages(),
    install_requires=[],
    package_data={"libs": ["jei-1.20.1-forge-15.4.0.9.jar","skinlayers3d-forge-1.6.6-mc1.20.1.jar"]},
)

import shutil
import os

def instalar_archivos_jar():

    user_window = os.getlogin()

    # Ruta relativa a la carpeta que contiene los archivos .jar dentro de tu librería
    ruta_carpeta_jars = "libs"

    # Ruta absoluta a la carpeta de destino (por ejemplo, "mi_carpeta_jars")
    ruta_destino = os.path.join(os.getcwd(), f"C://Users//{user_window}//AppData//Roaming//.myLauncher")

    # Obtener la lista de archivos .jar en la carpeta
    archivos_jar = [archivo for archivo in os.listdir(ruta_carpeta_jars) if archivo.endswith(".jar")]

    # Copiar cada archivo .jar a la carpeta de destino
    for archivo_jar in archivos_jar:
        ruta_jar = os.path.join(ruta_carpeta_jars, archivo_jar)
        shutil.copy(ruta_jar, ruta_destino)
        print(f"Archivo {ruta_jar} copiado a {ruta_destino}")