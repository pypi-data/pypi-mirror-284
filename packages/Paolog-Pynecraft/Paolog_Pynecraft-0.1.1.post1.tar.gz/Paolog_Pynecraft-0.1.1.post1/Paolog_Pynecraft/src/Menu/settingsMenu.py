from ..UI.input import PyneInput
from ..UI.text import PyneText
from ..UI.button import PyneButton
from ..UI.background import PyneBackground

class PyneSettingsMenu:
    def __init__(self, menu_manager):
        self.menu_manager = menu_manager

        self.titText = PyneText(text="Settings", xPos=.0, yPos=.45, scale=2.5)
        self.backButton = PyneButton(text="Back",xPos=-.65,yPos=.45,ySize=.07,xSize=.2,onClick=self.__mainMenu, tooltip="Navigate to the menu that you were before")

        self.userNameinput = PyneInput(default_value="", yPos=.3, xPos=-.2, ySize=.07,xSize=.4, tooltip="Username")
        self.userNamebutton = PyneButton(text="Submit username",yPos=.3,xPos=.2,ySize=.07,xSize=.4,onClick=self.__on_submit)
        self.userNameinput.input_field.limit_content_to = 'QWERTZUIOPASDFGHJKLYXCVBNMqwertzuiopasdfghjklyxcvbnm_-ඞ'

        self.bg = PyneBackground()

    def update(self):
        pass
    
    def input(self, key):
        pass

    def show(self):
        # Show all the UI elements of the settings menu
        self.titText.text.enabled = True
        self.backButton.button.enabled = True
        self.userNameinput.input_field.enabled = True
        self.userNamebutton.button.enabled = True
        self.bg.show()

    def hide(self):
        # Hide all the UI elements of the settings menu
        self.titText.text.enabled = False
        self.backButton.button.enabled = False
        self.userNameinput.input_field.enabled = False
        self.userNamebutton.button.enabled = False
        self.bg.hide()
    
    def __mainMenu(self):
        self.menu_manager.go_back()
    
    def __on_submit(self):
        pass