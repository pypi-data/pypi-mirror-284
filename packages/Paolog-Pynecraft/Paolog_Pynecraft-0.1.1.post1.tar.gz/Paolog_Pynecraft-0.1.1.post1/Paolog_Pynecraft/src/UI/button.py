from ursina import *

class PyneButton:
    def __init__(self, text:str, xPos:int, yPos:int,xSize:int, ySize:int, onClick, tooltip = None):
        self.button = Button(text=text, x=xPos,y=yPos, color=color.lime, text_color=color.gray, scale=(xSize,ySize), model='quad', highlight_scale=1.1, pressed_scale=0.95)
        self.button.highlight_color = color.green
        self.button.pressed_color = color.green
        self.button.on_click = onClick
        if not tooltip == None or type(tooltip) is str: self.button.tooltip = Tooltip(text=tooltip)
        #self.button.text_entity.font = "assets/rs/fonts/Emizen.ttf"

    def killMe(self):
        destroy(self.button)