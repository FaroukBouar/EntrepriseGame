import os
import sqlite3

class DatabaseHandler():
	def __init__(self, database_name : str):
		self.con = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{database_name}")
		self.con.row_factory = sqlite3.Row

	def create_tentreprise(self, NomEntreprise: str, PVente: str, QVendu: str, CA: str):
		cursor = self.con.cursor()
		query = f"INSERT INTO tentreprise (NomEntreprise, PVente, QVendu, CA) VALUES ('{NomEntreprise}', '{PVente}', '{QVendu}', '{CA}');"
		cursor.execute(query)
		cursor.close()
		self.con.commit()



#Fonction d'appariement à la tentreprise