class InterfaceGraphique:
    def __init__(self):
        self.root = None  # Initialize the main window

    def setup_ui(self):
        # Method to set up the user interface components
        pass

    def run(self):
        self.root = self.setup_ui()  # Set up the UI
        self.root.mainloop()  # Start the Tkinter event loop