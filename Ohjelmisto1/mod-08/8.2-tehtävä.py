import mysql.connector

def hae_maan_lkm(iso_country):
    sql = f"SELECT type, count(*) FROM airport where iso_country = '{iso_country}' group by type"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"{rivi[1]} {rivi}")




yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='AdminST',
         autocommit=True
         )