# Furqan Saeed
# faseed@andrew.cmu.edu

from cmu_graphics import *
import math
import string
import random
import home
import time
import play
import arena

def onAppStart(app):
    # Initialisation Methods
    getCanvasDetails(app)
    app.stepsPerSecond = 60
    
    # Modes
    app.HomePage = False
    app.battleArena = True
    
    # Arena Specific variables
    app.arenaRows = 30
    app.arenaCols = 18
    
    # Other Variables
    app.time = 0
    app.enemyCards = [play.knight(350, 160, "enemy")]
    app.playerCards = []
    app.deckCards = [] # [ ( class, True/False ) ]
    app.cardSelected = "miniPekka" # testing right now, should be None
    app.buffer = 4


    
    
    # Testing

    app.playerTowers = [play.princessTower(237.5, 640.5),
                        play.princessTower(516.5, 640.5),
                        play.kingTower(377, 729)]
    
    app.enemyTowers = [play.princessTower(237.5, 159.5),
                       play.princessTower(516.5, 159.5),
                       play.kingTower(377, 71)]    
    




def getCanvasDetails(app):
    # App details
    app.h = app.height
    app.w = app.h/19.5 * 12
    app.x0 = app.width/2 - app.w/2 - app.w/4
    app.y0 = 0
    app.x1 = app.x0 + app.w
    app.y1 = 0
    
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
    if app.battleArena:
        arena.drawArena(app)
        
        for card in app.playerCards:
            card.draw()
            
        for card in app.enemyCards:
            card.draw()
            
        for i in range(4):
            pass


def onMousePress(app, x, y):
    if app.battleArena:
        
        play.placeCard(app, x, y)
            

def onStep(app):
    getCanvasDetails(app)
    app.time += 1
    
    
    if app.battleArena:
        
        #Movement of card on the arena
        for card in app.playerCards[:]:
            card.onStep(app)
            if card.alive == False:
                app.playerCards.remove(card)
        
        for card in app.enemyCards[:]:
            card.onStep(app)
            if card.alive == False:
                app.enemyCards.remove(card)



def onKeyPress(app, key):
    if key in "Rr":
        onAppStart(app)

def onMouseHover(app, x1, y1):
    pass

def onMouseRelease(app, x1, y1):
    pass







runApp(width=1000, height=800)