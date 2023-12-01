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
    app.stepsPerSecond = 400

def onMousePress(app, mouseX, mouseY):
    app.mouseX = mouseX
    app.mouseY = mouseY

def onMouseDrag(app, mouseX, mouseY):
    app.mouseX = mouseX
    app.mouseY = mouseY

def onMouseRelease(app, mouseX, mouseY):
    app.mouseX = None
    app.mouseY = None


def onStep(app):
    app.drawItems, app.currentRenderable = app.currentRenderable.getstep(app.mouseX, app.mouseY, )
    if app.currentRenderable == None:
        app.currentRenderable = MainPage()

def redrawAll(app):
    for item in app.drawItems:
        if item[0] == 'image':
            myImage = CMUImage(openImage(item[1]))
            drawImage(myImage, item[2], item[3], width = item[4], height = item[5])

        elif item[0] == 'line':
            drawLine(item[1], item[2], item[3], item[4], fill = item[5], lineWidth = 6)

        elif item[0] == 'circle':
            drawCircle(item[1], item[2], item[3], fill = item[4])

if __name__ == "__main__":
    runApp(CANVAS_WIDTH, CANVAS_HEIGHT)