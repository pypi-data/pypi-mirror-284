from ursina import Entity, camera
from screeninfo import get_monitors

class PyneBackground:
    def __init__(self):
        self.bg = Entity(
            model="quad",
            texture="assets/rs/title/bg.png",
            scale_x=get_monitors()[0].width/800,
            scale_y=get_monitors()[0].height/800,
            z=1,
            origin=(0, 0),
            parent=camera.ui,
        )
    def hide(self):
        self.bg.enabled = False
    
    def show(self):
        self.bg.enabled = True