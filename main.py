# Furqan Saeed
# faseed@andrew.cmu.edu

from cmu_graphics import *
import math
import string
import random
import home
import time
import play


def onAppStart(app):
    # Initialisation Methods
    getCanvasDetails(app)
    
    # Modes
    app.HomePage = False
    app.battle = True
    
    # Arena Specific variables
    app.arenaRows = 30
    app.arenaCols = 18

    
    
    

def getCanvasDetails(app):
    # App details
    app.h = app.height
    app.w = app.h/19.5 * 12
    app.x0 = app.width/2 - app.w/2
    app.y0 = 0
    
    # Arena Details
    app.playgroundH = app.h*0.95
    app.playgroundW = app.playgroundH/30 * 18
    app.playgroundX0 = app.x0 + (app.w-app.playgroundW)/2
    app.playgroundY0 = app.y0 + (app.h-app.playgroundH)/2


def redrawAll(app):    
    
    # If the game is in the homepage
    if app.HomePage:
        home.home(app)
        
    
    # If the player is in a match
    if app.battle:
        play.drawArena(app)


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