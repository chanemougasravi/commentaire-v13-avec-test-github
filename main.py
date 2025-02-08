#structure du programme:

#1.main.py lance l interface graphique de l application grace a ui.py 
# =>creation instance et 
# =>lancement methode qui fait apparaitre l interface graphique

#2.puis ui.py lance deux instances de classes Methods et Database

from ui import InterfaceGraphique

if __name__ == "__main__":
    app = InterfaceGraphique() #creation de l instance InterfaceGraphique au lancement du programme
    app.run() #lancement de l application

#run copilot
