import mysql.connector

def sqlquery(query):
    cursor = sqlconnection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

sqlconnection = mysql.connector.connect(
    host='localhost',
    port='3306',
    database='flight_game',
    user='lietom',
    password='test',
    autocommit=True
)

from flask import Flask, request
airport = Flask(__name__)
@airport.route('/airport')
def airport_get():
    args = request.args
    icao = str(args.get("icao"))
    test = sqlquery(f"SELECT ident, name, municipality FROM airport WHERE ident='{icao}'")
    returndict = {"ICAO": test[0][0], "Name":test[0][1], "Location":[0][2]}
    return returndict

if __name__ == '__main__':
    airport.run(use_reloader=True, host='127.0.0.1', port=5000)
