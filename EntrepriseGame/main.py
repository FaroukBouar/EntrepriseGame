from Data.database_handler import DatabaseHandler
from Data.database_handler2 import DatabaseHandler2
from Data.database_handler3 import DatabaseHandler3

database_handler = DatabaseHandler("database.db")

def register():
    print("---Entreprise---")
    NomEntreprise = input("Nom de la créperie : ")
    PVente = float(input("Prix de Vente : "))
    QVendu = float(input("Quantité Vendu : "))

    def multiply(PVente, QVendu):
        result = PVente * QVendu
        return result
    
    CA = multiply(PVente, QVendu)
    print("Chiffres d'affaires : ", CA)

    database_handler.create_tentreprise(NomEntreprise, PVente, QVendu, CA)

def register2():
    print("---Ressource---")
    NomEntreprise = input("Nom de la créperie : ")
    QOeuf = float(input("Quantité Oeuf Disponible : "))
    QFarine = float(input("Quantité Farine Disponible : "))
    QLait = float(input("Quantité Lait Disponible : "))

    def addition(QOeuf, QFarine, QLait):
        result = QOeuf + QFarine + QLait
        return result

    PrixDesMP = addition(QOeuf, QFarine, QLait) * 1.2
    print("Prix total des Matières Premières : ", PrixDesMP)
      
    NombreEmploye = float(input("Nombre d'employés à charge : "))
    SalaireAPayerParEmploye = float(input("Salaire net à payer par employé : "))

    def multiply1(NombreEmploye, SalaireAPayerParEmploye):
        result = NombreEmploye * SalaireAPayerParEmploye
        return result

    SalaireTotaux = multiply1(NombreEmploye, SalaireAPayerParEmploye) 
    print("Salaires totaux : ", SalaireTotaux)

    PrixEquipement = float(input("Prix par unité de l'équipement : "))
    EquipementAchete = float(input("Equipement acheté : "))

    def multiply2(PrixEquipement, EquipementAchete):
        result = PrixEquipement * EquipementAchete
        return result

    PrixTotalEquipement = multiply2(PrixEquipement, EquipementAchete) * 1.2
    print("Prix total à l'achat d'équipement : ", PrixTotalEquipement)

    def addition2(PrixDesMP, SalaireTotaux, PrixTotalEquipement ):
        result = PrixDesMP + SalaireTotaux + PrixTotalEquipement
        return result

    TotalCharge = addition2(PrixDesMP, SalaireTotaux, PrixTotalEquipement)
    print("Charge totale à payer : ", TotalCharge)

    database_handler3 = DatabaseHandler3("database.db")
    database_handler3.create_tressource(NomEntreprise, QOeuf, QFarine, QLait, PrixDesMP, NombreEmploye, SalaireAPayerParEmploye, SalaireTotaux, PrixEquipement, EquipementAchete, PrixTotalEquipement, TotalCharge)





    

def register3():
    print("---Score---")
    NomEntreprise = input("Nom de la créperie : ")
    CA = float(input("Chiffre d'affaires : "))
    TC = float(input("Total des charges : "))
    
    def soustraction(CA, TC):
        result = CA - TC
        return result

    ScoreEntreprise = soustraction(CA, TC)
    print("Votre Score : ", ScoreEntreprise)

    database_handler2 = DatabaseHandler2("database.db")
    database_handler2.create_tscore(NomEntreprise, CA, TC, ScoreEntreprise)


def menu_not_connected():
    while True:
        print("Bienvenue sur EntrepriseGame ! (non connecté)")
        print("Choisissez une option")
        print("1. Quitter")
        print("2. Ajouter une entreprise")
        print("3. Ajouter une Ressource")
        print("4. Ajouter un score")
        choix = int(input())

        if choix == 4:
            register3()
        if choix == 3:
            register2()
        if choix == 2:
            register()
        if choix == 1:
            exit()

menu_not_connected()
