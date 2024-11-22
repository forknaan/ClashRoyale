# Furqan Saeed
# faseed@andrew.cmu.edu

from cmu_graphics import *
import math
import string
import random
import home
import time
    
    
##################
# Card Mechanics #
##################


def placeCard(app, x, y):
    # Placing Selected Card onto Arena
    if app.cardSelected != None:
        x0, y0 = 149, 425
        x1, y1 = 605, 780
        if x0 <= x <= x1:
            if y0 <= y <= y1:
                x = ((x-x0)//25)*25+x0+12.5
                y = ((y-y0)//25)*25+y0+12.5
            else:
                y = 437.5
                x = ((x-x0)//25)*25+x0+12.5
            app.playerCards.append(initCard(app.cardSelected, x, y,
                                            "player"))
            app.cardSelected = None

class playingCard:
    def __init__(self):
        self.alive = True
    
    def getAllCards(self):
        return ['miniPekka', 'bomber', 'knight', 'skeletons', 'wizard',
                'fireSpirit'] # Add Tesla or Elixir Collecter maybe
        
    def onStep(self, app):

        if self.mode == "Battling":
            self.fight(app)
            if self.enemy.health <= 0:
                self.enemy.alive = False
                self.enemy = None
                self.mode = "Moving"
        elif self.mode == "Moving":
            closest = self.closestTarget(app, self.side)
            self.move(app, closest, self.side)
    
    def move(self, app, closestTarget, side):

        if self.movementType == "Ground":    
            point = self.getPointGround(closestTarget, side)
            check = self.inEnemyRangeCheck(app, side)
        else:
            point = self.getPointAir(closestTarget, side, app)
            check = self.inEnemyRangeCheck(app, side)

        if check:
            self.enemy = closestTarget
            self.mode = "Battling"
        else:
            self.moveCard(point)

    
    def fight(self, app):
        if self.cooldown % (app.stepsPerSecond * self.hitSpeed) == 0:
            self.attack()
        self.cooldown += 1


    
    
    def closestTarget(self, app, side):
        if side == "player":
            closestTower = self.closestTower(app.enemyTowers)
            closestCard = self.closestCard(app.enemyCards)
        else:
            closestTower = self.closestTower(app.playerTowers)
            closestCard = self.closestCard(app.playerCards)
        
        distT = distance(self.x, self.y, closestTower.x, closestTower.y)
        distC = distance(self.x, self.y, closestCard.x, closestCard.y)
        
        if distT < distC:
            closest = closestTower
        else:
            closest = closestCard
        
        return closest

#         276, 478
#         200
#         554
        
    def closestTower(self, towers):
        lowDist = 1000
        closest = None
        radius = self.sight * 25
        for i in towers:
            dist = distance(self.x, self.y, i.x, i.y)
            if dist <= radius and dist <= lowDist:
                lowDist = dist
                closest = i
        if closest == None:
            return templateCard()
        
        return closest
    
    def closestCard(self, cards):
        lowDist = 1000
        closest = None
        radius = self.sight * 25
        for i in cards:
            dist = distance(self.x, self.y, i.x, i.y)
            if dist <= radius and dist <= lowDist:
                lowDist = dist
                closest = i
        if closest == None:
            return templateCard()
        
        return closest


    def moveCard(self, point):
        # Move Card to the closest Point
        dxdy = (self.y-point[1]) / (self.x-point[0])
        angle = 360 - angleTo(self.x, self.y, point[0], point[1])
        angle = math.radians(angle)
        dx = -self.movementSpeed * math.sin(angle)
        dy = -self.movementSpeed * math.cos(angle)
        self.x += dx
        self.y += dy

    def inEnemyRangeCheck(self, app, side):
        cardRange = self.range * 25        
        closest = self.closestTarget(app, side)
        lowDist = distance(self.x, self.y, closest.x, closest.y)
        if lowDist <= cardRange:
            return True 
        else:
            return False
    
    def getPointAir(self, closestTarget, side, app):
        if closestTarget.x == 1000: # Ensures no target can be seen by card
            if side == "player":
                point = self.closestTower(app.enemyTowers)
            else:
                point = self.closestTower(app.playerTowers)
        else:
            point = (closestTarget.x, closestTarget.y)
        return point

    def getPointGround(self, closestTarget, side):
        if closestTarget.x == 1000:
            if side == "player":
                point = self.closestPointPlayer()
            else:
                point = self.closestPointEnemy()
        else:
            point = (closestTarget.x, closestTarget.y)
        return point

    # Point refers to location on map, no specific card
    def closestPointPlayer(self):
        if self.y > 425:
            if self.x < 377:
                point = (237.5, 425)
            else:
                point = (516.5, 425)
        elif self.y > 375:
            if self.x < 377:
                point = (237.5, 375)
            else:
                point = (516.5, 375)
        elif self.y > 131:
            if self.x < 377:
                point = (237.5, 131)
            else:
                point = (516.5, 131)
        else:
            point = (377, 71)
        return point
    
    def closestPointEnemy(self):
        if self.y < 375:
            if self.x < 375:
                point = (237.5, 375)
            else:
                point = (516.5, 375)
        elif self.y < 425:
            if self.x < 377:
                point = (237.5, 425)
            else:
                point = (516.5, 425)
        elif self.y < 679:
            if self.x < 377:
                point = (237.5, 679)
            else:
                point = (516.5, 679)
        else:
            point = (377, 729)
        return point



# points = [  (377, 71), (516.5, 96), (237.5, 96),
#              (516.5, 159.5), (237.5, 159.5)       ]



# Card 1
class miniPekka(playingCard):
    moving = []
    card = "Images\miniPekka.png"
    
    def __init__(self, x=0, y=0, side=None):
        super().__init__()
        self.health = 1361
        self.maxHealth = self.health
        self.dmg = 680
        self.hitSpeed = 1.6
        self.movementSpeed = 2    # "Fast"
        self.range = 2
        self.targets = "Ground"
        self.attackType = "Melee"
        self.cost = 4
        self.movementType = "Ground"
        self.mode = "Moving"
        self.side = side
        self.target = None
        self.sight = 4
        self.cooldown = 0
        
        if side == "Enemy":
            self.angle = 180
        else:
            self.angle = 0
        
        self.x = x
        self.y = y

    def draw(self):
        drawCircle(self.x, self.y, 5, fill='blue')
        drawLabel("MINI PEKKA", self.x, self.y, fill='white')
        drawLabel(self.health, self.x, self.y-10, fill='white')
    
    def attack(self):
        self.enemy.health -= self.dmg

# Card 2
class knight(playingCard):
    def __init__(self, x=0, y=0, side=None):
        super().__init__()
        self.health = 1766
        self.maxHealth = self.health
        self.dmg = 202
        self.hitSpeed = 1.2
        self.movementSpeed = 1    # "Medium"
        self.range = 2
        self.targets = "Ground"
        self.atttackType = "Melee"
        self.cost = 3
        self.movementType = "Ground"
        self.mode = "Moving"
        self.side = side
        self.target = None
        self.sight = 4
        self.cooldown = 0

        if side == "Enemy":
            self.angle = 180
        else:
            self.angle = 0

        self.x = x
        self.y = y
    
    def draw(self):
        drawCircle(self.x, self.y, 5, fill='red')
        drawLabel("KNIGHT", self.x, self.y, fill='white')
        drawLabel(self.health, self.x, self.y-10, fill='white')
    
    def attack(self):
        self.enemy.health -= self.dmg

# Card 3
class skeletons(playingCard):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.health = 81
        self.maxHealth = self.health
        self.dmg = 81
        self.hitSpeed = 1
        self.movementSpeed = 8   # "Fast"
        self.range = "Short"
        self.targets = "Ground"
        self.atttackType = "Melee"
        self.cost = 1
        self.movementType = "Ground"
    
    def draw(self):
        pass

# Card 4
class bomber(playingCard):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.health = 332
        self.maxHealth = self.health
        self.dmg = 225
        self.hitSpeed = 1.8
        self.movementSpeed = 6    # "Medium"
        self.range = 4.5
        self.targets = "Ground"
        self.atttackType = "Ranged"
        self.cost = 2
        self.movementType = "Ground"
    
    def draw(self):
        pass

# Card 5
class wizard(playingCard):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.health = 754
        self.maxHealth = self.health
        self.dmg = 281
        self.hitSpeed = 1.4
        self.movementSpeed = 6    # "Medium"
        self.range = 5.5
        self.targets = "All"
        self.atttackType = "Ranged"
        self.cost = 5
        self.movementType = "Ground"
    
    def draw(self):
        pass

# Card 6
class fireSpirit(playingCard):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.health = 230
        self.maxHealth = self.health
        self.dmg = 207
        self.hitSpeed = "Instant"
        self.movementSpeed = 10   # "Very Fast"
        self.range = 2
        self.targets = "All"
        self.atttackType = "Ranged"
        self.cost = 1
        self.movementType = "Ground"
    
    def draw(self):
        pass
    
# Blank Card with template for all Properties

class templateCard(playingCard):
    def __init__(self, x=0, y=0, side=None):
        super().__init__()
        self.health = 0
        self.maxHealth = self.health
        self.dmg = 0
        self.hitSpeed = "Instant, A number"
        self.movementSpeed = "A number"
        self.range = 0
        self.targets = "All, Ground"
        self.atttackType = "Ranged, Melee"
        self.cost = 0
        self.movementType = "Ground, Air"
        self.x = 1000
        self.y = 1000
        self.side = side




def initCard(s, x, y, side):
    if s == "miniPekka":
        return miniPekka(x, y, side)
    elif s == "bomber":
        return bomber(x, y, side)
    elif s == "knight":
        return knight(x, y, side)
    elif s == "skeletons":
        return skeletons(x, y, side)
    elif s == "wizard":
        return wizard(x, y, side)
    elif s == "fireSpirit":
        return fireSpirit(x, y, side)


##########
# Towers #
##########

class towers:
    
    def __init__(self):
        self.alive = True
    
    def onStep(self, app):
        pass
    

class princessTower(towers):
    
    def __init__(self, x, y):
        super().__init__()
        self.health = 3052
        self.dmg = 109
        self.hitSpeed = 0.8
        self.range = 7.5
        self.targets = "All"
        self.atttackType = "Ranged"
        self.x = x
        self.y = y

    def draw(self):
        pass

class kingTower(towers):
    
    def __init__(self, x, y):
        super().__init__()
        self.health = 4824
        self.dmg = 109
        self.hitSpeed = 1
        self.range = 7
        self.targets = "All"
        self.atttackType = "Ranged"
        self.x = x
        self.y = y
        self.state = "Idle" # Can also be "Active"

    def draw(self):
        pass