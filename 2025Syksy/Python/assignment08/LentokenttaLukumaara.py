import mysql.connector
kenttatyypit = ("balloonport",
                "closed",
                "heliport",
                "large_airport",
                "medium_airport",
                "seaplane_base",
                "small_airport")
def sqlhaku(query):
    kursori = yhteys.cursor()
    kursori.execute(query)
    tulos = kursori.fetchall()
    return tulos
def get_airports_by_country(country_code):
    print(f"Airports in {country_code}:")
    for i in range(7):
        result = sqlhaku(f"SELECT count(name) FROM airport WHERE iso_country='{country_code}' AND type='{kenttatyypit[i]}'")
        print(f"{result} {kenttatyypit[i]} airports")
def run_country_program():
    code = input("Enter the country code (e.g., FI for Finland):")
    get_airports_by_country(code.upper())
yhteys = mysql.connector.connect(
    host='localhost',
    port='3306',
    database='flight_game',
    user='Lieto',
    password='test',
    autocommit=True
)
run_country_program()