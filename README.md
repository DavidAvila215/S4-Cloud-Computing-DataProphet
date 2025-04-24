# S4-Cloud-Computing-DataProphet


**Nombre del equipo:** DataProphet.

Miembros del equipo:

1.- Ángel David Ávila Pérez. Departamento: Bases de datos. Puesto: Limpieza de datos

2.- Samantha Ruelas Valtierra. Departamento: Cloud Computing. Puesto: Software Development.

3.- Erika Martínez Meneses. Departamento: Modelos e implementación. Puesto: Científico de datos

4.- David Emmanuel Ramirez Stanford. Departamento: Ciberseguridad. Puesto: Control de Accesos.

5.- Andrea Axel Hernández Galgani. Departamento: Modelos e implementación. Puesto: Científico de datos.


*Este repositorio contiene el código y la documentación necesarios para montar una base de datos en SQL, entrenar un modelo de regresión para predecir fechas de modificación, y desplegar el modelo como un servicio en la nube.*


**Estructura**

- Model.ipynb: Notebook principal donde se limpian los datos, se entrena el modelo de regresión, se guarda como .pkl, se crea el score.py y se hace el deployment
- cleaned_data.csv: Datos ya procesados usados para entrenar el modelo.
- model.pkl: Modelo entrenado guardado listo para desplegarse
- score.py: Script que se usa en Azure para la API de recibir peticiones y devolver predicciones
- API.ipynb: Archivo de la creción del API y prueba del modelo desplegado enviando peticiones desde un archivo local
- prueba_1.csv: Archivo con datos de prueba simulando una entrada real al modelo


**Pasos para correr la API del proyecto**
1. Cargar el modelo (model.pkl) y el archivo de inferencia (score.py) en Azure 
2. Configurar un workspace y servicio de inferencia con las librerias necesarias
3. Obtener la URI generada por Azure y usarla en el archivo de la API
4. Probar la API ejecutando el notebook usando prueba_1.csv como entrada


**Pasos realizados para ejecutar el proyecto**
1. Conectar a la base de datos en Azure SQL y extraer los datos de "SalesLT.Customer"
2. Preprocesar los datos limpiando los datos y convirtiendo la fecha en una varible numèrica
3. Se entrena un modelo de regresión lineal para predecir la fecha de modificación y se guarda como model.pkl
4. Se crea el script score.py cargando el modelo y define cómo debe recibir los datos cuando se despliega la API
5. Despliegue en Azure, se configura el workspace y entorno
6. En API.ipynb, se envía una fila de prueba (prueba_1.csv) y se recibe la predicción
