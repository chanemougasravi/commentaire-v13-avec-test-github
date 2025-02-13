# filepath: /my-tkinter-app/my-tkinter-app/src/main.py
from ui import InterfaceGraphique

if __name__ == "__main__":
    app = InterfaceGraphique()  # creation of the InterfaceGraphique instance at program launch
    app.run()  # launching the application