import mysql.connector
def sqlhaku(query):
    kursori = yhteys.cursor()
    kursori.execute(query)
    result = kursori.fetchone()
    return result
def lentoasemahaku(icao):
    sql = f"SELECT count(name) FROM airport WHERE ident='{icao}'"
    tulos = sqlhaku(sql)
    if tulos != "":
        sql = f"SELECT name FROM airport WHERE ident='{icao}'"
        tulos = sqlhaku(sql)
        print(f"Airport name: {tulos}")
        sql = f"SELECT municipality FROM airport WHERE ident='{icao}'"
        tulos = sqlhaku(sql)
        print(f"Location: {tulos}")
    else:
        print(f"No airport found with ICAO code {icao}")
yhteys = mysql.connector.connect(
    host='localhost',
    port='3306',
    database='flight_game',
    user='Lieto',
    password='test',
    autocommit=True
)
code = input("Enter the ICAO code of an airport: ")
lentoasemahaku(code.upper())