# Aplicación en Python

Esta es una aplicación desarrollada en Python y ejecutada en un entorno Dockerizado. Utiliza Docker y Docker Compose (versión 3) para facilitar la configuración y ejecución de la aplicación.

## Modo de Uso

1. Asegúrate de tener Docker y Docker Compose instalados en tu máquina.

2. Clona este repositorio en tu sistema y ejecutar app:

   ```shell
   git clone https://github.com/esbasilio/console-python-app.git

   cd console-python-app

   docker-compose up -d

   docker exec -it appy bash

   python main.py
