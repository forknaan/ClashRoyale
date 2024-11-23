# Furqan Saeed
# faseed@andrew.cmu.edu

from cmu_graphics import *
import math
import string
import random
import home
import time


##########################
# Draw arena to fight in #
##########################

# 30 * 18


def bg(app):


    drawImage("Images/arenaBase.png", app.x0-50, 0)

    

    y0 = app.h - app.h/10
    for i in range(9):
        drawLine(app.x0, y0 - (app.h/10)*i, app.x0-50, y0 - (app.h/10)*i,
                 fill='black')

#################
# Arena drawing #
#################

    # drawRect(app.x0, 0, 50, app.h, align='top-right', fill=None,
    #          border='black')

    # # The background of the whole arena
    # drawRect(app.x0, app.y0, app.w, app.h, fill=rgb(156,140,88))

    # drawRect(app.playgroundX0, app.playgroundY0, app.playgroundW,
    #          app.playgroundH, fill=rgb(183,196,82))
    
    # cellSize = app.playgroundW/18
    
    # # The tiles
    # # (Use two loops twice for optimization of decreasing total objects)
    # for row in range(0, 14, 2):
    #     for col in range(1, app.arenaCols, 2):
    #         drawRect(app.playgroundX0+cellSize*col,
    #                  app.playgroundY0+cellSize*row,
    #                  cellSize,cellSize, fill=rgb(170,189,73),border=None)
    
    # for row in range(16, app.arenaRows, 2):
    #     for col in range(1, app.arenaCols, 2):
    #         drawRect(app.playgroundX0+cellSize*col,
    #                  app.playgroundY0+cellSize*row,
    #                  cellSize,cellSize, fill=rgb(170,189,73),border=None)
    
    # for row in range(1, 15, 2):
    #     for col in range(0, app.arenaCols, 2):
    #         drawRect(app.playgroundX0+cellSize*col,
    #                  app.playgroundY0+cellSize*row,
    #                  cellSize,cellSize, fill=rgb(170,189,73),border=None)
            
    # for row in range(17, app.arenaRows, 2):
    #     for col in range(0, app.arenaCols, 2):
    #         drawRect(app.playgroundX0+cellSize*col,
    #                  app.playgroundY0+cellSize*row,
    #                  cellSize,cellSize, fill=rgb(170,189,73),border=None)
    

    # # The Main Path
    # drawRect(app.playgroundX0+cellSize*14, app.playgroundY0+cellSize*2,
    #          cellSize, cellSize*26, fill='black', opacity=20)
    
    # drawRect(app.playgroundX0+cellSize*3, app.playgroundY0+cellSize*2,
    #          cellSize, cellSize*26, fill='black', opacity=20)
    
    # drawRect(app.playgroundX0+cellSize*4, app.playgroundY0+cellSize*2,
    #          cellSize*10, cellSize, fill='black', opacity=20)
    
    # drawRect(app.playgroundX0+cellSize*4, app.playgroundY0+cellSize*27,
    #          cellSize*10, cellSize, fill='black', opacity=20)
    
    # drawRect(app.playgroundX0+cellSize*2, app.playgroundY0+cellSize*4,
    #          cellSize*3, cellSize*3, fill='black', opacity=50)
    
    # drawRect(app.playgroundX0+cellSize*13, app.playgroundY0+cellSize*4,
    #          cellSize*3, cellSize*3, fill='black', opacity=50)
    
    # drawRect(app.playgroundX0+cellSize*2, app.playgroundY0+cellSize*23,
    #          cellSize*3, cellSize*3, fill='black', opacity=50)
    
    # drawRect(app.playgroundX0+cellSize*13, app.playgroundY0+cellSize*23,
    #          cellSize*3, cellSize*3, fill='black', opacity=50)
    
    # drawRect(app.playgroundX0+cellSize*7, app.playgroundY0,
    #          cellSize*4, cellSize*4, fill='black', opacity=50)
    
    # drawRect(app.playgroundX0+cellSize*7, app.playgroundY0+cellSize*26,
    #          cellSize*4, cellSize*4, fill='black', opacity=50)
    

    # # The lake
    # drawRect(app.x0+app.w/2,app.h/2,app.w,2*cellSize,
    #          fill=rgb(0,233,200), border=None, align='center')

    
    
    # # The Bridges
    # drawRect(app.playgroundX0+cellSize*2.2, app.playgroundY0+cellSize*13.2,
    #          cellSize*2.7,cellSize*3.7, fill=rgb(224,186,108))
    
    # drawRect(app.playgroundX0+cellSize*13.2,
    #          app.playgroundY0+cellSize*13.2,cellSize*2.7,cellSize*3.7,
    #          fill=rgb(224,186,108))

    
    # # The Deck bg
    # drawRect(app.x1, 0, app.w*0.4, app.h, fill=rgb(141,107,79))
    # cardX = app.x1+app.w*0.05
    # cardY = app.h*0.03
    # for i in range(4):
    #     drawRect(cardX, cardY + app.h*0.2375*i, app.w*0.3, app.h*0.225,
    #             fill=rgb(84,59,40))


def drawArena(app):
    bg(app)