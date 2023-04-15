import os
import sqlite3

class DatabaseHandler3():
	def __init__(self, database_name : str):
		self.con = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{database_name}")
		self.con.row_factory = sqlite3.Row

	def create_tressource(self, NomEntreprise: str, QOeuf: str, QFarine: str, QLait: str, PrixDesMP: str, NombreEmployé: str, SalaireàPayerParEmployé: str, SalaireTotaux: str, PrixEquipement: str,  EquipementAcheté: str, PrixTotalEquipement: str, TotalCharge: str):
		cursor = self.con.cursor()
		query = f"INSERT INTO tressource (NomEntreprise, QOeuf, QFarine, QLait, PrixDesMP, NombreEmployé, SalaireàPayerParEmployé, SalaireTotaux, PrixEquipement, EquipementAcheté, PrixTotalEquipement, TotalCharge) VALUES ('{NomEntreprise}', '{QOeuf}','{QFarine}','{QLait}','{PrixDesMP}','{NombreEmployé}','{SalaireàPayerParEmployé}','{SalaireTotaux}','{PrixEquipement}', '{EquipementAcheté}', '{PrixTotalEquipement}', '{TotalCharge}');"
		cursor.execute(query)
		cursor.close()
		self.con.commit()