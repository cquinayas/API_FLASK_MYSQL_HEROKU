#importing libraries
import numpy as np
import pandas as pd
import flask
from flask import Flask, render_template, request
import mysql.connector

mydb = mysql.connector.connect(
    user = 'sql10602710',
    password = 'CsendKslmw',
    host = 'sql10.freemysqlhosting.net',
    port = 3306,
    database = 'sql10602710'
)
myCursor = mydb.cursor()
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_word_count/<p>/<w>/')
def get_word_count(p,w):
    query = f"select title, count(*) from {p} where title like '%{w}%'"
    myCursor.execute(query)
    result = myCursor.fetchall() 
    for row in result:
        cant = str(row[1])
    return f"En la plataforma {p} aparece {cant} veces la palabra {w} en el título de películas/series "

@app.route('/get_score_count/<p>/<s>/<y>/')
def get_score_count(p,s,y):
    query = f"select id, count(*) as cant  from {p} where release_year={y} and score>{s}"
    myCursor.execute(query)
    result = myCursor.fetchall() 
    for row in result:
            cantidad = str(row[1])
    return f"Hay {cantidad} películas con un puntaje mayor de {s} en la plataforma {p}"

@app.route('/get_second_score/<p>/')
def get_second_score(p):
    query = f"select title from {p} where score = 100 order by title asc limit 2"
    myCursor.execute(query)
    result = myCursor.fetchall() 
    result = result[1][0]
    return f"La segunda película con mayor score según el orden alfabético de los títulos es  {result}"

@app.route('/get_longest/<p>/<t>/<y>/')
def get_longest(p,t,y):
    query = f"select title, duration_int from {p} where release_year = {y} and duration_type = '{t}' order by duration_int desc limit 1"
    myCursor.execute(query)
    result = myCursor.fetchall() 
    for row in result:
            title =str(row[0])
            min = str(row[1])
    return f"La película que más duro en la plataforma {p}, en el año {y} y tipo de duración en {t} fue {title}"

@app.route('/get_rating_count/<tipo>/')
def get_rating_count(tipo):
    query = f"select rating, count(*) from amazon where rating = '{tipo}'"
    myCursor.execute(query)
    result = myCursor.fetchall() 
    for row in result:
            rating =str(row[0])
            count = str(row[1])
    return f"La cantidad de películas/series en la plataforma amazon con el rating {tipo} es {count}"


if __name__=="__main__":

    app.run(port=5001,debug=True)