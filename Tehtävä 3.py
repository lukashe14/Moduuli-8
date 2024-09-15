import mysql.connector
from geopy import distance
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='lukashe',
         password='JhTaS87526',
         autocommit=True
         )

def hae_lentokentta(icao):
    kursori = yhteys.cursor()

    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    kursori.execute(sql, (icao,))
    return kursori.fetchone()

icao1 = input("Anna ensimmäinen icao koodi: ")
icao2 = input("Anna toinen icao koodi: ")

koordinaatisto = hae_lentokentta(icao1)
koordinaatisto2 = hae_lentokentta(icao2)

print(distance.distance(koordinaatisto, koordinaatisto2).km.__round__(2),"km")



