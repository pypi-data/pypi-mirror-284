import random
import ursina
import pathlib
from screeninfo import get_monitors

from ..Menu.settingsMenu import PyneSettingsMenu
from ..Menu.worldMenu import PyneWorldMenu

from ..UI.input import PyneInput
from ..UI.button import PyneButton
from ..UI.text import PyneText
from ..UI.background import PyneBackground

from ..other.quit import PyneQuit


class PyneMainMenu:
    def __init__(self, menu_manager):
        self.menu_manager = menu_manager
        
        self.titText = PyneText(text="Pynecraft", xPos=.0, yPos=.3, scale=5)
		
        # Load splash texts from file
        with open(pathlib.Path(__file__).parent.parent.parent.resolve().__str__() + "/assets/rs/title/splash.txt", "r") as file:
            splash_lines = file.readlines()
        
        # Randomly choose a line from the splash texts
        splash_text = random.choice(splash_lines).strip()
        
        self.splashText = PyneText(text=splash_text, xPos=.05, yPos=.22, scale=1.25)
        self.splashText.setRotation((0, 0, -10))  # Rotating the hint text
        self.splashText.text.color = ursina.color.yellow  # Changing color to yellow
        self.splashText.text.origin = (-0.75, 0)  # Slightly offsetting the origin


        self.solbutton = PyneButton(text="Play Solo", xPos=.0,yPos=.1,ySize=.07, xSize=.4, onClick=self.__playSolo)
        self.mulbutton = PyneButton(text="Play Multiplayer", xPos=.0,yPos=.0,ySize=.07, xSize=.4, onClick=self.__playMulti)
        self.setbutton = PyneButton(text="Settings", xPos=-.0,yPos=-.1,ySize=.07, xSize=.4, onClick=self.__settingsMenu)
        self.quitbutton = PyneButton(text="Quit", xPos=.73,yPos=-.43,ySize=.07, xSize=.07, onClick=PyneQuit, tooltip="Quit the Game")
        

        self.bg = PyneBackground()

        self.direction = 1  # 1 for increasing size, -1 for decreasing size

    def update(self):
        current_scale = self.splashText.getScale()
        if current_scale >= 1.4:
            self.direction = -1
        elif current_scale <= 1.25:
            self.direction = 1
        self.splashText.changeScale(current_scale + self.direction * 0.002)
    
    def input(self, key):
        pass
    
    def show(self):
        # Show all the UI elements of the main menu
        self.titText.text.enabled = True
        self.splashText.text.enabled = True
        self.solbutton.button.enabled = True
        self.mulbutton.button.enabled = True
        self.setbutton.button.enabled = True
        self.quitbutton.button.enabled = True
        self.bg.show()

    def hide(self):
        # Hide all the UI elements of the main menu
        self.titText.text.enabled = False
        self.splashText.text.enabled = False
        self.solbutton.button.enabled = False
        self.mulbutton.button.enabled = False
        self.setbutton.button.enabled = False
        self.quitbutton.button.enabled = False
        self.bg.hide()



    def __playSolo(self):
        self.menu_manager.set_menu(PyneWorldMenu(self.menu_manager))

    def __playMulti(self):
        print("Playing Multiplayer")

    def __settingsMenu(self):
        self.menu_manager.set_menu(PyneSettingsMenu(self.menu_manager))
    
    

