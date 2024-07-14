from ursina import *
from ursina.window import *
from ursina.prefabs.splash_screen import SplashScreen

class PyneWindow:
    def __init__(self, title:str, FPSCounter:bool, ExitButton:bool, icon:str, isBorderless:bool, alwaysOnTop:bool, hasSettingsButton:bool, show_startup_screen:bool, startup_screen_image:None|str):
        self.app = Ursina(title=title, icon=icon, borderless=isBorderless)

        if show_startup_screen and startup_screen_image:
            self.app.splash_screen = SplashScreen(texture=startup_screen_image)
        window.fps_counter.enabled = FPSCounter
        window.exit_button.visible = ExitButton
        window.cog_button.enabled = hasSettingsButton
        window.always_on_top = alwaysOnTop


    def run(self):
        self.app.run()
        