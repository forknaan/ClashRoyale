# Furqan Saeed
# faseed@andrew.cmu.edu

from cmu_graphics import *
import math
import string
import random
import home
import time




def getCanvasDetails(app):
    app.h = app.height
    app.w = app.h/19.5 * 12
    app.x0 = app.width/2 - app.w/2
    app.y0 = 0


def onAppStart(app):
    app.HomePage = True
    getCanvasDetails(app)


def redrawAll(app):    
    if app.HomePage:
        home.home(app)


def onMouseClick(app, x1, y1):
    pass

def onStep(app):
    getCanvasDetails(app)


def onKeyPress(app, key):
    pass

def onMouseHover(app, x1, y1):
    pass

def onMouseRelease(app, x1, y1):
    pass







runApp()