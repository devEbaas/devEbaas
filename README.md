Requerimientos:
-> Tener instalado python en su versión 3.8 (recomendado)
-> Tener instalado postgress
-> opcional: instalar un gestor visual de postgres (pgAdmin por ejemplo)
Instalación del proyecto:
-> Clonar el repositorio de la rama master

-> crear y activar un entorno virtual con python venv u otro creador de entornos
  pasos a seguir para crear el entorno con venv -> https://docs.python.org/es/3/library/venv.html
  
-> ejecutar el comando python -m pip install -r requirements.txt para instalar las dependencias del proyecto

-> crear el archivo .env en la carpeta raiz del proyecto y agregar la configuración de la base de datos (existe un .env.example en el proyecto)

-> ejecutar el comando: python manage.py migrate para trasladar los campos de los modelos a la base de datos y plasmarlos en tablas

-> crear superusuario para acceder al admin de django : python manage.py createsuperuser

-> ejecutar el servidor con el comando python manage.py runserver

#### rutas ####
### Admin de django ###
[...]/admin/



### Activity ###
[...]/activity/activity/  [GET, POST]
[...]/activity/cancel_activity/  [POST] -> cancelar actividad
[...]/activity/reagend_activity/  [POST[ -> reagendar actividad


### Property###
[...]/property/property/  [GET, POST]


### Survey ###
[...]/survey/survey/  [GET, POST]

  

<!---
Desarrollado por Eduardo Baas Kauil
--->
