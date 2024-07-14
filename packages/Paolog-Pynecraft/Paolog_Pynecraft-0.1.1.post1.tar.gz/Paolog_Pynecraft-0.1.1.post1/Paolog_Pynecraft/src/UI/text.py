import ursina

class PyneText:
    def __init__(self, text, xPos: float, yPos: float, scale: float):
        """ ursina.Text.size = .4 """
        self.text = ursina.Text(text=text, x=xPos, y=yPos, origin=(0, 0))
        #self.text = ursina.Text(text=text, x=xPos, y=yPos, origin=(0, 0), font="assets/rs/fonts/Emizen.ttf")
        self.text.scale = scale

    def changeScale(self, scale: float):
        if self.text:
            self.text.scale = ursina.Vec3(scale, scale, scale)

    def getScale(self):
        if self.text:
            return self.text.scale.x  # Access x component of the scale Vec3
        else :
            return 0
    
    def setRotation(self, rotation: tuple):
        if self.text:
            self.text.rotation = rotation

    def killMe(self):
        ursina.destroy(self.text)