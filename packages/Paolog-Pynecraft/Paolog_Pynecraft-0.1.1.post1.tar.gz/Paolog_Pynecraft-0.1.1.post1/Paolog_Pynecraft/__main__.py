from .src.Graphics.window import PyneWindow
from .src.Menu.mainMenu import PyneMainMenu

class MenuManager:
    def __init__(self):
        self.current_menu = None
        self.old_menu = None

    def set_menu(self, menu):
        self.old_menu = self.current_menu
        if self.current_menu is not None:
            self.current_menu.hide()  # Hide the current menu
        self.current_menu = menu
        self.current_menu.show()  # Show the new menu

    def update(self):
        if self.current_menu is not None:
            self.current_menu.update()
    
    def input(self, key):
        if self.current_menu is not None:
            self.current_menu.input(key)
    
    def go_back(self):
        self.set_menu(self.old_menu)

window = PyneWindow("Pynecraft 0.1.1 Post1", True, False, 'assets/rs/window/icon.ico', False, False, True, True, 'assets/rs/title/startup2.png') # To enable splashscreen, put the last value to True
menu_manager = MenuManager()
pyneMainMenu = PyneMainMenu(menu_manager)
menu_manager.set_menu(pyneMainMenu)

def update():
    menu_manager.update()

def input(key):
    menu_manager.input(key=key)


window.run()

"""
python3 -bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]"; python3 -Bc "import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]"
"""
