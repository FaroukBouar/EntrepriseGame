import os
import sqlite3

class DatabaseHandler2():
	def __init__(self, database_name : str):
		self.con = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{database_name}")
		self.con.row_factory = sqlite3.Row

	def create_tscore(self, NomEntreprise: str, CA: str, TC: str, ScoreEntreprise: str):
		cursor = self.con.cursor()
		query = f"INSERT INTO tscore (NomEntreprise, CA, TC, ScoreEntreprise) VALUES ('{NomEntreprise}', '{CA}', '{TC}','{ScoreEntreprise}');"
		cursor.execute(query)
		cursor.close()
		self.con.commit()