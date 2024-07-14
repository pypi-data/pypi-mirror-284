from ursina.prefabs.input_field import InputField
from ursina import Tooltip

class PyneInput:
    def __init__(self, default_value:str, xPos:int, yPos:int,xSize:int,ySize:int,tooltip = None, on_value_changed = None, hide_content=False, on_submit=None, character_limit=24):
        self.input_field = InputField(default_value=default_value,x=xPos,y=yPos,scale=(xSize,ySize), model="quad", on_value_changed=on_value_changed, hide_content=hide_content, on_submit=on_submit, character_limit=character_limit)
        if not tooltip == None or type(tooltip) is str: self.input_field.tooltip = Tooltip(text=tooltip)

    def get_value(self):
        return self.input_field.text