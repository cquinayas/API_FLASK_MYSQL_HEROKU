# API_Flask_Heroku
Desarrollo y puesta en produción de una API usando Flask y Heroku Cloud. 

##  1. Proceso de ETL
* Carga de los archivos .csv utilizando pandas
* Transformación de los datos segun requerimientos de la empresa 
* Crear una base de datos en Free Mysql Hosting, registrarse, logearse, ir a MYSQL hosting y crear una base de datos gratuita. Te enviaran al mail los datos de la base de datos ( dabase host, name, database y password) 
* Ingesta de los datos en una base de datos en Mysql a traves de Python. 

   [ETL.ipynb]()
##  2. Desarrollo de la API en Flask
* Crear la conexión a la base de datos utilizando las siguientes credenciales: (
Host: sql10.freemysqlhosting.net,
Database name: sql10591684,
Database user: sql10591684,
Database password: 2vv82khQDF,
Port number: 3306 )
<https://www.phpmyadmin.co/>
* Crear los endpoint que reciven informacion desde la url y realizan consultas a la base de datos (get_word_count,get_score_count,get_second_score,get_longest,get_rating_count ) 

##  2.1 Producción en servidor local 
    $   Crear un entorno virtual (py -m venv venv)
    $   Activar el entorno virtual (.\venv\Scripts\activate)
    $   Instalar paqueteria necesaria (pip install -r requirements.txt)
    $   Correr la API  (app.py)
[api.py]()  
##  2.2 Producción en servidor remoto
*  Crear un usuario en la página de Heroku
*  Inicializar git en la carpeta del proyecto (git init, git add.,git commit -m "primer commit", crea un repositorio en gitHub y copia la url, git branch -m main, git remote add origin urlrepositorio, git push -u origin main)
*  Crear un proyecto en Heroku
*  Hacer click en el menu en Deploy y elegir Git y conectarse al repositorio de Git, hacer click en Deploy Automatico y luego en Deploy Branch main)
      
 

    
