
from ..UI.text import PyneText
from ..UI.button import PyneButton
from ..UI.input import PyneInput
from ..UI.background import PyneBackground
from ..UI.bar import PyneBar
from ..other.world_generator import WorldGenerator

from ursina.prefabs.input_field import ContentTypes
from ursina import color

from ..other.get_config_path import get_pynecraft_config_path as conf_path
from ..other.world_status import WORLD_STATUS

from ..Games.Solo.Pynecraft import Pynecraft

import os
import random

class PyneWorldMenu:
    def __init__(self, menu_manager):
        self.menu_manager = menu_manager
        self.worlds = []

        self.bg = PyneBackground()

        self.worldGenerator:WorldGenerator = WorldGenerator()
        self.percentageBar = PyneBar(color=color.green, max_value=100, xPos=-.2, yPos=.3, xSize=.4, ySize=.07, tooltip=None)
        self.percentageBar.bar.text_color_setter(color.gray)
        self.duringCreWorldText = PyneText(text="Creating world", xPos=.0, yPos=.4, scale=2)


        self.selWorldText = PyneText(text="Select World", xPos=-.3, yPos=.45, scale=2.5)
        self.creWorldText = PyneText(text="Create World", xPos=.3, yPos=.45, scale=2.5)

        self.creWorldNameText = PyneText(text="World Name:", xPos=.3, yPos=.35, scale=1.5)
        self.creWorldNameInput = PyneInput(default_value="", xPos=.3, yPos=.3, ySize=.07, xSize=.4)

        self.creWorldSeedText = PyneText(text="World Seed:", xPos=.3, yPos=.2, scale=1.5)
        self.creWorldSeedInput = PyneInput(default_value=str(random.randrange(1, int('9' * 32)))
                                           , xPos=.3, yPos=.15, ySize=.07, xSize=.4, character_limit=32)
        self.creWorldSeedInput.input_field.limit_content_to = ContentTypes.int

        self.creWorldSizeText = PyneText(text="World Size:", xPos=.3, yPos=.05, scale=1.5)
        self.creWorldSizeInput = PyneInput(default_value=str(60)
                                           , xPos=.3, yPos=.0, ySize=.07, xSize=.4)
        self.creWorldSizeInput.input_field.limit_content_to = ContentTypes.int
        
        self.creWorldButton = PyneButton(text="Create World",xPos=.3,yPos=-.1,ySize=.07,xSize=.4,onClick=self.__createWorld)

        self.backButton = PyneButton(text="Back",xPos=-.65,yPos=.45,ySize=.07,xSize=.2,onClick=self.__mainMenu, tooltip="Navigate to the menu that you were before")

    def update(self):
        if self.worldGenerator.get_progression() != 100 and self.worldGenerator.get_progression() > 0:
            self.percentageBar.bar.bar_color_setter(color.lime)
            self.percentageBar.set_value(self.worldGenerator.get_progression())
            self.percentageBar.bar.text = str(self.worldGenerator.get_progression()) + "%"
        elif self.worldGenerator.get_progression() == 100:
            self.percentageBar.bar.bar_color_setter(color.green)
            self.percentageBar.set_value(100)
            self.percentageBar.bar.text = "Finished"
            self.backButton.button.enabled = True
        elif self.worldGenerator.get_progression() == -1:
            self.percentageBar.bar.bar_color_setter(color.yellow)
            self.percentageBar.bar.text = "Invalid world name"
            self.backButton.button.enabled = True
        elif self.worldGenerator.get_progression() == -2:
            self.percentageBar.bar.bar_color_setter(color.yellow)
            self.percentageBar.bar.text = "World name can't be empty"
            self.backButton.button.enabled = True
        elif self.worldGenerator.get_progression() == -100:
            self.percentageBar.bar.bar_color_setter(color.orange)
            self.percentageBar.bar.text = "Can't create world :,("
            self.backButton.button.enabled = True
        elif self.worldGenerator.get_progression() == -101:
            self.percentageBar.bar.bar_color_setter(color.yellow)
            self.percentageBar.bar.text = "World size can't be 0"
            self.backButton.button.enabled = True
    
    def input(self, key):
        pass

    def show(self):
        self.__initWorlds()
        # Show all the UI elements of the settings menu
        self.selWorldText.text.enabled = True
        self.creWorldText.text.enabled = True
        self.creWorldButton.button.enabled = True
        self.creWorldNameText.text.enabled = True
        self.creWorldNameInput.input_field.enabled = True
        self.creWorldSeedText.text.enabled = True
        self.creWorldSeedInput.input_field.enabled = True
        self.creWorldSizeText.text.enabled = True
        self.creWorldSizeInput.input_field.enabled = True
        self.backButton.button.enabled = True
        self.percentageBar.bar.enabled = False
        self.duringCreWorldText.text.enabled = False
        for button in self.worlds:
            button.button.enabled = True
        
        self.bg.show()

    def hide(self):
        # Hide all the UI elements of the settings menu
        self.selWorldText.text.enabled = False
        self.creWorldText.text.enabled = False
        self.creWorldButton.button.enabled = False
        self.creWorldNameText.text.enabled = False
        self.creWorldNameInput.input_field.enabled = False
        self.creWorldSeedText.text.enabled = False
        self.creWorldSeedInput.input_field.enabled = False
        self.creWorldSizeText.text.enabled = False
        self.creWorldSizeInput.input_field.enabled = False
        self.percentageBar.bar.enabled = False
        self.backButton.button.enabled = False
        self.duringCreWorldText.text.enabled = False
        
        for button in self.worlds:
            button.button.enabled = False
        
        self.bg.hide()

    def __initWorlds(self):
        self.worlds.clear()
        subfolders = [f.path for f in os.scandir(conf_path()) if f.is_dir()]

        for sf in subfolders:
            """ self.worlds.append( 
                PyneButton( 
                    text=os.path.basename(sf),
                    xPos=-.3,
                    yPos=.45-(((len(self.worlds) + 1)/10)),
                    ySize=.07,
                    xSize=.4,
                    onClick=lambda name=sf: self.menu_manager.set_menu(Pynecraft(self.menu_manager, name, "User"))
                )
            ) """
            worldStatus = self.__isValidWorld(sf)
            if worldStatus == WORLD_STATUS.VALID:
                self.worlds.append(
                    PyneButton(
                        text=os.path.basename(sf),
                        xPos=-.3,
                        yPos=.45-(((len(self.worlds) + 1)/10)),
                        ySize=.07,
                        xSize=.4,
                        onClick=lambda name=sf: self.menu_manager.set_menu(Pynecraft(self.menu_manager, name, "User"))
                    )
                )
            elif worldStatus == WORLD_STATUS.NEWER:
                worldButton = PyneButton(
                    text=os.path.basename(sf) + " - Newer World?",
                    xPos=-.3,
                    yPos=.45-(((len(self.worlds) + 1)/10)),
                    ySize=.07,
                    xSize=.4,
                    onClick=lambda name=sf: self.menu_manager.set_menu(Pynecraft(self.menu_manager, name, "User"))
                )
                worldButton.button.color = color.red
                worldButton.button.text_color_setter(color.white)
                self.worlds.append(worldButton)
            elif worldStatus == WORLD_STATUS.DEPRECATED:
                worldButton = PyneButton(
                    text=os.path.basename(sf) + " - Need to be converted",
                    xPos=-.3,
                    yPos=.45-(((len(self.worlds) + 1)/10)),
                    ySize=.07,
                    xSize=.4,
                    onClick=lambda name=sf: self.menu_manager.set_menu(Pynecraft(self.menu_manager, name, "User"))
                )
                worldButton.button.color = color.orange
                self.worlds.append(worldButton)
            elif worldStatus == WORLD_STATUS.INVALID:
                # Invalid world, won't create button
                pass
                

        
    def __mainMenu(self):
        if (self.duringCreWorldText.text.enabled):
            self.show()
        else:
            self.menu_manager.go_back()
    
    def __createWorld(self):

        worldname:str = self.creWorldNameInput.get_value()
        seed:str = self.creWorldSeedInput.get_value()
        world_size:str = self.creWorldSizeInput.get_value()

        self.hide()
        self.percentageBar.bar.enabled = True

        self.duringCreWorldText.text.enabled = True
        self.bg.show()
        
        self.worldGenerator.generate_world(worldname, seed, world_size)
    
    def __isValidWorld(self, folder:str) -> WORLD_STATUS:
        try:
            with open(folder + "/info.txt") as file:
                lines:list[str] = file.readlines()
                for line in lines:
                    line:str = line.strip()
                    if line:
                        variable, value = line.split("=")
                        if variable == "world_version" and int(value) == 1:
                            return WORLD_STATUS.VALID
                        elif int(value) >= 1:
                            return WORLD_STATUS.NEWER
                        elif int(value) <= 1:
                            return WORLD_STATUS.DEPRECATED
                        else:
                            return WORLD_STATUS.INVALID

        except FileNotFoundError:
            # No info.txt file, which means Pynecraft world isn't valid
            return WORLD_STATUS.INVALID