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
query1 = "SELECT * FROM city WHERE population > 1000000;"
cur.execute(query1)
result1 = cur.fetchall()


query2 = "SELECT * FROM country_language WHERE percentage < 60;"
cur.execute(query1)
result2 = cur.fetchall()


query3 = "FROM city GROUP BY country_code HAVING COUNT(*) >= 30;;"
cur.execute(query3)
result3 = cur.fetchall()