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


def placeCard(app, x, y, side, cardSelected):
    # Placing Selected Card onto Arena
    if cardSelected != None:
        x, y = getCardPlacementLocation(side, x, y)
        if side == "player":
            if app.playerElixir - cardSelected.cost > 0:
                app.playerElixir -= cardSelected.cost
                app.playerCards.extend(initCard(str(cardSelected),x,y,"player"))
                #app.playerCardSelected = None
                app.playerDeck.remove(cardSelected)
                app.playerDeck.append(cardSelected)
        else:
            if app.enemyElixir - cardSelected.cost > 0:
                app.enemyElixir -= cardSelected.cost
                app.enemyCards.extend(initCard(str(cardSelected),x,y,"enemy"))
                #app.enemyCardSelected = None
                app.enemyDeck.remove(cardSelected)
                app.enemyDeck.append(cardSelected)

def getCardPlacementLocation(side, x, y):
    if side == "player":
        x0, y0 = 149, 425
        x1, y1 = 605, 780
    else:
        x0, y0 = 149, 20
        x1, y1 = 605, 375
    if x0 <= x <= x1:
        if y0 <= y <= y1:
            x = ((x-x0)//25)*25+x0+12.5
            y = ((y-y0)//25)*25+y0+12.5
        else:
            if side == "player":
                y = 437.5
            else:
                y = 362.5
            x = ((x-x0)//25)*25+x0+12.5
    return x, y


# Gets a random Deck and returns it
def randomizer(app):
    shuffled = getAllCards()
    random.shuffle(shuffled)
    for i in range(len(shuffled)):
        shuffled[i] = initCard(shuffled[i])[0]
    return shuffled

def getAllCards():
    return ['miniPekka', 'bomber', 'knight', 'skeletons', 'wizard',
            'fireSpirit'] # Add Tesla or Elixir Collecter maybe

class playingCard:
    def __init__(self):
        self.alive = True
        self.state = "Active"
        
    def onStep(self, app):

        if self.mode == "Battling":
            self.fight(app)
            if self.target.health <= 0:
                self.target.alive = False
                self.target = None
                self.mode = "Moving"
        elif self.mode == "Moving":
            closest = self.closestTarget(app, self.side)
            self.move(app, closest, self.side)
            
            if self.cooldown % (app.stepsPerSecond * self.hitSpeed) != 0:
                self.cooldown += 1

    
    def move(self, app, closestTarget, side):

        if self.movementType == "Ground":    
            point = self.getPointGround(closestTarget, side)
            check = self.inEnemyRangeCheck(app, side)
        else:
            point = self.getPointAir(closestTarget, side, app)
            check = self.inEnemyRangeCheck(app, side)

        if check:
            self.target = closestTarget
            self.mode = "Battling"
        else:
            self.moveCard(point)

    
    def fight(self, app):
        if self.cooldown % (app.stepsPerSecond * self.hitSpeed) == 0:
            self.target.health -= self.dmg
            self.attack()
        self.cooldown += 1
        if self.target.state == "Idle":
            self.target.activate()
    
    
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
            if i.alive:
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
        if closestTarget.x == 1000: # Checks if no target is seen by card
            if side == "player":
                point = self.closestTower(app.enemyTowers)
            else:
                point = self.closestTower(app.playerTowers)
        else:
            point = (closestTarget.x, closestTarget.y)
        return point

    # If no enemies in range then find the point for the card to move towards
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
                point = (517.5, 425)
        elif self.y > 375:
            if self.x < 377:
                point = (237.5, 375)
            else:
                point = (517.5, 375)
        elif self.y > 131:
            if self.x < 377:
                point = (237.5, 131)
            else:
                point = (517.5, 131)
        else:
            point = (377, 71)
        return point
    
    def closestPointEnemy(self):
        if self.y < 375:
            if self.x < 375:
                point = (237.5, 378)
            else:
                point = (517.5, 378)
        elif self.y < 425:
            if self.x < 377:
                point = (237.5, 428)
            else:
                point = (517.5, 428)
        elif self.y < 679:
            if self.x < 377:
                point = (237.5, 682)
            else:
                point = (517.5, 681)
        else:
            point = (377, 729)
        return point



# points = [  (377, 71), (516.5, 96), (237.5, 96),
#              (516.5, 159.5), (237.5, 159.5)       ]



# Card 1
class miniPekka(playingCard):
    moving = []
    card = "Images/miniPekka/miniPekkaCard.png"
    
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
        
        if side == "enemy":
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
        pass

    def __repr__(self):
        return "miniPekka"
    
    def drawCard(self, x, y):
        drawImage(miniPekka.card, x, y)

# Card 2
class knight(playingCard):
    card = "Images/knight/knightCard.png"


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

        if side == "enemy":
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
        pass

    def __repr__(self):
        return "knight"
    
    def drawCard(self, x, y):
        drawImage(knight.card, x, y)
        

# Card 3
class skeleton(playingCard):
    card = "Images/skeleton/skeletonCard.png"

    def __init__(self, x=0, y=0, side=None):
        super().__init__()
        self.health = 81
        self.maxHealth = self.health
        self.dmg = 81
        self.hitSpeed = 1
        self.movementSpeed = 2   # "Fast"
        self.range = 2
        self.targets = "Ground"
        self.atttackType = "Melee"
        self.cost = 1
        self.movementType = "Ground"
        self.side = side
        self.target = None
        self.sight = 4
        self.cooldown = 0
        self.mode = "Moving"

        if side == "enemy":
            self.angle = 180
        else:
            self.angle = 0

        self.x = x
        self.y = y

    def draw(self):
        drawCircle(self.x, self.y, 5, fill='red')
        drawLabel("Skeleton", self.x, self.y, fill='white')
        drawLabel(self.health, self.x, self.y-10, fill='white')

    def attack(self):
        pass

    def __repr__(self):
        return "skeletons"
    
    def drawCard(self, x, y):
        drawImage(skeleton.card, x, y)

# Card 4
class bomber(playingCard):
    card = "Images/bomber/bomberCard.png"

    def __init__(self, x=0, y=0, side=None):
        super().__init__()
        self.health = 332
        self.maxHealth = self.health
        self.dmg = 225
        self.hitSpeed = 1.8
        self.movementSpeed = 1    # "Medium"
        self.range = 4.5
        self.targets = "Ground"
        self.atttackType = "Ranged"
        self.cost = 2
        self.movementType = "Ground"
        self.mode = "Moving"
        self.sight = 6
        self.cooldown = 0
        self.side = side
        self.target = None

        if side == "enemy":
            self.angle = 180
        else:
            self.angle = 0

        self.x = x
        self.y = y
    
    def draw(self):
        drawCircle(self.x, self.y, 5, fill='red')
        drawLabel("Bomber", self.x, self.y, fill='white')
        drawLabel(self.health, self.x, self.y-10, fill='white')

    def attack(self):
        pass

    def __repr__(self):
        return "bomber"
    
    def drawCard(self, x, y):
        drawImage(bomber.card, x, y)


# Card 5
class wizard(playingCard):
    card = "Images/wizard/wizardCard.png"

    def __init__(self, x=0, y=0, side=None):
        super().__init__()
        self.health = 754
        self.maxHealth = self.health
        self.dmg = 281
        self.hitSpeed = 1.4
        self.movementSpeed = 1    # "Medium"
        self.range = 5.5
        self.targets = "All"
        self.atttackType = "Ranged"
        self.cost = 5
        self.movementType = "Ground"
        self.mode = "Moving"
        self.sight = 6
        self.cooldown = 0
        self.side = side
        self.target = None

        if side == "enemy":
            self.angle = 180
        else:
            self.angle = 0
        
        self.x = x
        self.y = y

    def draw(self):
        drawCircle(self.x, self.y, 5, fill='red')
        drawLabel("Wizard", self.x, self.y, fill='white')
        drawLabel(self.health, self.x, self.y-10, fill='white')
    
    def attack(self):
        pass

    def __repr__(self):
        return "wizard"
    
    def drawCard(self, x, y):
        drawImage(wizard.card, x, y)

# Card 6
class fireSpirit(playingCard):
    card = "Images/fireSpirit/fireSpiritCard.png"

    def __init__(self, x=0, y=0, side=None):
        super().__init__()
        self.health = 230
        self.maxHealth = self.health
        self.dmg = 207
        self.hitSpeed = 1000
        self.movementSpeed = 2.7   # "Very Fast"
        self.range = 3
        self.targets = "All"
        self.atttackType = "Ranged"
        self.cost = 1
        self.movementType = "Ground"
        self.mode = "Moving"
        self.sight = 6
        self.cooldown = 0
        self.side = side
        self.target = None
        
        if side == "enemy":
            self.angle = 180
        else:
            self.angle = 0
        
        self.x = x
        self.y = y
    
    def draw(self):
        drawCircle(self.x, self.y, 5, fill='red')
        drawLabel("Fire Spirit", self.x, self.y, fill='white')
        drawLabel(self.health, self.x, self.y-10, fill='white')
    
    def attack(self):
        self.alive = False
        self.health = 0

    def __repr__(self):
        return "fireSpirit"
    
    def drawCard(self, x, y):
        drawImage(fireSpirit.card, x, y)

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




def initCard(s, x=0, y=0, side=None):
    if s == "miniPekka":
        return [miniPekka(x, y, side)]
    elif s == "bomber":
        return [bomber(x, y, side)]
    elif s == "knight":
        return [knight(x, y, side)]
    elif s == "skeletons":
        return [skeleton(x+20, y, side),
                skeleton(x-20, y, side),
                skeleton(x, y+20, side)]
    elif s == "wizard":
        return [wizard(x, y, side)]
    elif s == "fireSpirit":
        return [fireSpirit(x, y, side)]
    elif s == "skeleton":
        return [skeleton(x, y, side)]


##########
# Towers #
##########

class towers:
    
    def __init__(self):
        self.alive = True
    
    def onStep(self, app):
        if self.alive:
            if self.mode == "Battling":
                self.fight(app)
                if self.target.health <= 0:
                    self.target.alive = False
                    self.target = None
                    self.mode = "Idle"
            elif self.mode == "Idle":
                target = self.getTarget(app)
                if self.targetInRange(target) and self.state == "Active":
                    self.mode = "Battling"
                    self.target = target
    
    def fight(self, app):
        if self.cooldown % (app.stepsPerSecond * self.hitSpeed) == 0:
            self.target.health -= self.dmg
            self.attack()
        self.cooldown += 1

    def getTarget(self, app):
        possibleTargets = [] # If cards are attacking tower, they take priority
        if self.side == "player":
            for card in app.enemyCards:
                if card.target == self:
                    possibleTargets.append(card)
        else:
            for card in app.playerCards:
                if card.target == self:
                    possibleTargets.append(card)
        if possibleTargets == []:
            if self.side == "player":
                closestCard = self.closestCard(app.enemyCards)
            else:
                closestCard = self.closestCard(app.playerCards)
        else:
            closestCard = self.closestCard(possibleTargets)
        return closestCard
        
    def closestCard(self, cards):
        lowDist = 1000
        closest = None
        radius = self.range * 25
        for i in cards:
            dist = distance(self.x, self.y, i.x, i.y)
            if dist <= radius and dist <= lowDist:
                lowDist = dist
                closest = i
        if closest == None:
            return templateCard()
        return closest
    
    def targetInRange(self, target):
        dist = distance(self.x, self.y, target.x, target.y)
        if dist <= self.range*25:
            return True
        else:
            return False


class princessTower(towers):
    
    def __init__(self, x, y, side):
        super().__init__()
        self.health = 3052
        self.dmg = 109
        self.hitSpeed = 0.8
        self.range = 7.5
        self.targets = "All"
        self.atttackType = "Ranged"
        self.x = x
        self.y = y
        self.mode = "Idle"
        self.target = None
        self.side = side
        self.state = "Active"
        self.cooldown = 0

    def draw(self):
        if self.alive:
            drawRect(self.x-37.5, self.y-37.5, 25*3, 25*3, fill='green')
            drawLabel("Princess Tower", self.x, self.y, fill='white')
            drawLabel(self.health, self.x, self.y-10, fill='white')
    
    def attack(self):
        pass

    def __repr__(self):
        return "princessTower"

class kingTower(towers):
    
    def __init__(self, x, y, side):
        super().__init__()
        self.health = 4824
        self.dmg = 109
        self.hitSpeed = 1
        self.range = 7
        self.targets = "All"
        self.atttackType = "Ranged"
        self.x = x
        self.y = y
        self.state = "Idle" # Can also be "Active" (The tower is hidden) 
        self.mode = "Idle" # The tower has no target
        self.side = side
        self.cooldown = 0

    def draw(self):
        if self.alive:
            drawRect(self.x-50, self.y-50, 25*4, 25*4, fill='red')
            drawLabel("King Tower", self.x, self.y, fill='white')
            drawLabel(self.health, self.x, self.y-10, fill='white')

    def attack(self):
        pass

    def activate(self):
        self.state = "Active"


    def __repr__(self):
        return "kingTower"


##############################
# Elixir and Other Mechanics #
##############################

def elixirOnStep(app):
    if app.playerElixir < 10:
        app.playerElixir += 1/45
    if app.playerElixir > 10:
        app.playerElixir = 10
    
    if app.enemyElixir < 10:
        app.enemyElixir += 1/45
    if app.enemyElixir > 10:
        app.enemyElixir = 10


# All stats gained from https://statsroyale.com (with slight modifications)