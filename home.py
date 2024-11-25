# Furqan Saeed
# faseed@andrew.cmu.edu

from cmu_graphics import *
import math
import string
import random
import time
import play
import ai



def bg(app):
    diamondWH = app.h/11
    diamondSide = ((diamondWH**2)/2)**0.5 

    drawRect(app.x0, app.y0, app.w, app.h, fill=rgb(19, 96, 153))

    for i in range(11):
        for j in range(8):
            drawRect(app.x0 + diamondWH*j, app.y0 + diamondWH*i, diamondSide,
                     diamondSide, fill=rgb(19, 83, 139), align='top',
                     rotateAngle=45)
    
    drawRect(app.x0, app.y0, app.w, app.height, fill='white',
             align='top-right')
    drawRect(app.x0 + app.w, 0, app.width - app.x0 + app.w, app.height,
             fill='white')
    drawRect(app.x0, app.y0, app.w, app.h, border='black', fill=None)

def battleButton(app):
    drawRect(app.x0 + app.w/2, app.h*0.75, app.w*0.5, app.h*0.1,
             fill=gradient(rgb(255, 208, 83), rgb(255, 188, 44), start='top'),
             align='center', border='black', borderWidth=app.w*0.001)
    drawLabel('Battle', app.x0 + app.w/2, app.h*0.75, fill=rgb(255, 255, 204),
              border='black', borderWidth=app.w*0.001, font='Supercell-Magic',
              size=app.h*0.05)

def nameCard(app):
    drawRect(app.x0 + app.w/2, app.h*0.15, app.w*0.4, app.h*0.08,
             fill=gradient(rgb(164,234,255), rgb(122,209,255), start='top'),
             align='center', border='black', borderWidth=app.w*0.001)
    

def home(app):
    bg(app)
    battleButton(app)
    nameCard(app)



def checkClick(app, x, y):
    if (254 <= x <= 500) and (560 <= y <= 640):
        clickBattleButton(app)

    

def clickBattleButton(app):
    app.HomePage = False
    app.battleArena = True
    app.enemyDeck = play.randomizer(app)
    app.playerDeck = play.randomizer(app)
    app.playerCardSelected = None
    app.enemyCardSelected = None
    app.enemyCards = []
    app.playerCards = []
    app.playerTowers = [play.princessTower(237.5, 640.5, "player"),
                        play.princessTower(516.5, 640.5, "player"),
                        play.kingTower(377, 729, "player")]
    app.enemyTowers = [play.princessTower(237.5, 159.5, "enemy"),
                       play.princessTower(516.5, 159.5, "enemy"),
                       play.kingTower(377, 71, "enemy")]
    app.playerElixir = 0
    app.enemyElixir = 0
    app.enemyCardSelectedIndex = None
    app.playerCardSelectedIndex = None
    app.winner = None
    app.gameOver = False
    app.ai = ai.lvl1(app)