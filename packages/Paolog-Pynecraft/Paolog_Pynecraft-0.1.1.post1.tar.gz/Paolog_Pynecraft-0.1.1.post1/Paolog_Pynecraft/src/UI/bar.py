from ursina.prefabs.health_bar import HealthBar
from ursina import color, Tooltip

class PyneBar:
    def __init__(self, color:color, max_value:int, xPos:int, yPos:int, xSize:int, ySize:int, tooltip = None):
        self.bar = HealthBar(max_value=max_value, roundness=0, color=color, scale=(xSize, ySize), x=xPos, y=yPos)
        if not tooltip == None or type(tooltip) is str: self.bar.tooltip = Tooltip(text=tooltip)

    def get_value(self) -> int:
        return self.bar.value
    
    def set_value(self, value:int) -> None:
        self.bar.value = value
    
    def get_max_value(self) -> int:
        return self.bar.max_value