import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='lukashe',
         password='JhTaS87526',
         autocommit=True
         )

def hae_lentokentta_tyypit_kaikki(maakoodi):
    kursori = yhteys.cursor()
    sql = f"SELECT type FROM airport WHERE iso_country LIKE %s"
    kursori.execute(sql, (maakoodi,))
    return kursori.fetchall()

def hae_lentokentta_tyypit(maakoodi):
    kursori = yhteys.cursor()
    sql = f"SELECT DISTINCT type FROM airport WHERE iso_country LIKE %s"
    kursori.execute(sql, (maakoodi,))
    return kursori.fetchall()

maakoodi = input("Anna maakoodi: ")
tyypit = hae_lentokentta_tyypit(maakoodi)
tyypit_kaikki = hae_lentokentta_tyypit_kaikki(maakoodi)


for i in tyypit:
    counter = 0
    for j in (tyypit_kaikki):
        if j[0] == i[0]:
            counter +=1
    print(i[0],":",counter)