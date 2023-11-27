from cmu_graphics import *
from PIL import Image
import os, pathlib
import gc

from Renderables.MainPage.mainPage import MainPage

CANVAS_WIDTH = 650
CANVAS_HEIGHT = 800

def openImage(fileName):
    return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))

def onAppStart(app):
    app.mouseX = None
    app.mouseY = None
    app.currentRenderable = MainPage()
    app.drawItems = []

def onMousePress(app, mouseX, mouseY):
    app.mouseX = mouseX
    app.mouseY = mouseY

def onStep(app):
    app.drawItems, app.currentRenderable = app.currentRenderable.getstep(app.mouseX, app.mouseY)
    if app.currentRenderable == None:
        app.currentRenderable = MainPage()
    gc.collect()

def redrawAll(app):
    for item in app.drawItems:
        if item[0] == "image":
            myImage = CMUImage(openImage(item[1]))
            drawImage(myImage, item[2], item[3])


if __name__ == "__main__":
    runApp(CANVAS_WIDTH, CANVAS_HEIGHT)