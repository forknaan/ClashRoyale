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
    app.stepsPerSecond = 30
    
    # Modes
    app.HomePage = False
    app.battleArena = True
    
    # Arena Specific variables
    app.arenaRows = 30
    app.arenaCols = 18
    
    # Other Variables
    app.time = 0
    app.playerElixir = 0
    app.enemyElixir = 0
    app.enemyCards = [play.miniPekka(350, 160, "enemy")] # testing right now, should be Empty
    app.playerCards = [] # The cards on the arena that the player has played
    app.playerDeck = [] # [ classes ]
    app.enemyDeck = [] # The deck the AI uses
    app.cardSelected = "fireSpirit" # testing right now, should be None
    app.gameOver = False



    # Testing
    
    
    app.playerTowers = [play.princessTower(237.5, 640.5, "player"),
                        play.princessTower(516.5, 640.5, "player"),
                        play.kingTower(377, 729, "player")]
    
    app.enemyTowers = [play.princessTower(237.5, 159.5, "enemy"),
                       play.princessTower(516.5, 159.5, "enemy"),
                       play.kingTower(377, 71, "enemy")]    
    




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
        
        for tower in app.playerTowers:
            tower.draw()
        
        for tower in app.enemyTowers:
            tower.draw()
        
        for card in app.playerCards:
            card.draw()
            
        for card in app.enemyCards:
            card.draw()
        
        if app.gameOver:
            drawRect(app.x0, app.y0, app.w, app.h, fill='grey', opacity=40)
            drawLabel(f"{app.winner} HAS WON!!!",
                      app.x0+app.w/2, app.y0+app.h/2)

def onMousePress(app, x, y):
    if app.battleArena:
        if not app.gameOver:
            play.placeCard(app, x, y, "player")
            

def onStep(app):
    getCanvasDetails(app)
    app.time += 1
    if app.battleArena:

        if app.gameOver:
            return
        
        play.elixirOnStep(app)

        #Movement of cards on the arena
        for card in app.playerCards[:]:
            card.onStep(app)
            if card.alive == False:
                app.playerCards.remove(card)
        
        for card in app.enemyCards[:]:
            card.onStep(app)
            if card.alive == False:
                app.enemyCards.remove(card)

        for tower in app.playerTowers[:]:
            tower.onStep(app)
        
        for tower in app.enemyTowers[:]:
            tower.onStep(app)


        if app.enemyTowers[2].alive == False:
            app.gameOver = True
            app.winner = "player"
            print(app.winner)
        elif app.playerTowers[2].alive == False:
            app.gameOver = True
            app.winner = "enemy"
            print(app.winner)



def onKeyPress(app, key):
    if key in "Rr":
        onAppStart(app)

def onMouseHover(app, x1, y1):
    pass

def onMouseRelease(app, x1, y1):
    pass







runApp(width=1000, height=800)