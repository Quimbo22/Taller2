# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 07:47:25 2023

@author: juane
"""

import psycopg2
engine = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="1463jwJE2212*",
    host="esteban.cpq1o3uew0fx.us-east-1.rds.amazonaws.com",
    port='5432'
)

# Crear un cursor
cur = engine.cursor()

# Ejecutar consultas
query1 = "SELECT local_name,region FROM country WHERE (surface_area BETWEEN 2000000 AND 10000) OR indep_year >=1920 ORDER BY region ASC;;"
cur.execute(query1)
result1 = cur.fetchall()


query2 = "SELECT country_code,language FROM country_language WHERE (percentage BETWEEN 70 AND 90)"
cur.execute(query1)
result2 = cur.fetchall()


query3 = "SELECT COUNT(*) FROM city WHERE district = 'Herat';"
cur.execute(query3)
result3 = cur.fetchall()