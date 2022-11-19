# Carter W
# Dec 10 2019
import pygame
import sys
import random
pygame.init()
screenSize = (1280,704) # Defines screen size
screen = pygame.display.set_mode((screenSize),0)
pygame.display.set_caption("Robo Quest") # Lists the title of the game on game window

### Variable Defining/Image Uploading ###

# FPS
clock = pygame.time.Clock()
FPS = 60

# Colours
RED = (255,0,0)
BLUE = (0,0,255)
LIGHTBLUE = (173,216,230)
GREEN = (0,255,0)
YELLOW = (255,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
DARKGREEN = pygame.Color("#031203")
SKYBLUE = pygame.Color("#ADFBFF")

# getting the screen width and height
screenWidth = pygame.Surface.get_width(screen)
screenHeight = pygame.Surface.get_height(screen)

# getting the center x and y points of the screen
cx = screenWidth/2 
cy = screenHeight/2

# Animations #
playerWalkingAnimation = [pygame.image.load("images/robotWalking1.png"),pygame.image.load("images/robotWalking2.png"),pygame.image.load("images/robotWalking3.png"),pygame.image.load("images/robotWalking2.png")]
playerShootingAnimation = [pygame.image.load("images/robotWalking1Shooting.png"),pygame.image.load("images/robotWalking2Shooting.png"),pygame.image.load("images/robotWalking3Shooting.png"),pygame.image.load("images/robotWalking2Shooting.png")]

# Image Loading #
# Player Images #
playerStanding = pygame.image.load("images/robotStanding.png")
playerWalk1 = pygame.image.load("images/robotWalking1.png")
playerWalk2 = pygame.image.load("images/robotWalking2.png")
playerWalk3 = pygame.image.load("images/robotWalking3.png")
playerJumping = pygame.image.load("images/robotJumping.png")
playerStandingShooting = pygame.image.load("images/robotStandingShooting.png")
playerWalk1Shooting = pygame.image.load("images/robotWalking1Shooting.png")
playerWalk2Shooting = pygame.image.load("images/robotWalking2Shooting.png")
playerWalk3Shooting = pygame.image.load("images/robotWalking3Shooting.png")
playerJumpingShooting = pygame.image.load("images/robotJumpingShooting.png")

# Enemy images #
bouncerEnemy = pygame.image.load("images/bouncerEnemy.png")
flyerEnemy = pygame.image.load("images/flyerEnemy.png")
rollerEnemy = pygame.image.load("images/rollerEnemy.png")
seekerEnemy = pygame.image.load("images/seekerEnemy.png")

# Misc Images #
playerLaser = pygame.image.load("images/robotLaser.png")
enemyLaser = pygame.image.load("images/enemyLaser.png")
healthIcon = pygame.image.load("images/healthIcon.png")
energyIcon = pygame.image.load("images/energyIcon.png")
bossHealthIcon = pygame.image.load("images/bossHealthIcon.png")
scrapIcon = pygame.image.load("images/scrapIcon.png")
noneIcon = pygame.image.load("images/noneIcon.png")
grenadeIcon = pygame.image.load("images/grenadeIcon.png")
shieldIcon = pygame.image.load("images/shieldIcon.png")
sawbladeIcon = pygame.image.load("images/sawbladeIcon.png")
sparkIcon = pygame.image.load("images/sparkIcon.png")
grenadeImage = pygame.image.load("images/grenade.png")
explosionImage = pygame.image.load("images/explosion.png")
shield = pygame.image.load("images/forceField.png")
sawbladeImage = pygame.image.load("images/sawblade.png")
sparkImage = pygame.image.load("images/spark.png")
immuneShield = pygame.image.load("images/invincibleShield.png")
checkpointImage = pygame.image.load("images/checkpoint.png")

# Terrain Images #
level1Wall = pygame.image.load("images/level1Wall.png")
level2Wall = pygame.image.load("images/level2Wall.png")
level3Wall = pygame.image.load("images/level3Wall.png")

# Function that changes opacity of blitted images (not made by me)
def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

### Title Code ###

buttonSelection = 1

buttonColour1 = GREEN
buttonColour2 = GREEN
buttonColour3 = GREEN
buttonColour4 = GREEN

titleFont = pygame.font.Font("Fonts/PressStart2P.ttf", 90)
textFont = pygame.font.Font("Fonts/PressStart2P.ttf", 50)
infoFont = pygame.font.Font("Fonts/PressStart2P.ttf", 30)
statFont = pygame.font.Font("Fonts/PressStart2P.ttf", 60)

gameTitle = titleFont.render("Robo Quest", True,(WHITE)) # Text used on the title screen
playButtonText = textFont.render("Play",True, (WHITE))
instructionsButtonText = textFont.render("Instructions",True, (WHITE))
uploadProgressButtonText = textFont.render("Upload Progress",True, (WHITE))
quitButtonText = textFont.render("Quit",True, (WHITE))

gameTitleWidth = gameTitle.get_width() # Finds the width of the text
playButtonWidth = playButtonText.get_width()
instructionsButtonWidth = instructionsButtonText.get_width()
uploadProgressButtonWidth = uploadProgressButtonText.get_width()
quitButtonWidth = quitButtonText.get_width()

gameTitleHeight = gameTitle.get_height() # Finds the height of the text
playButtonHeight = playButtonText.get_height()
instructionsButtonHeight = instructionsButtonText.get_height()
uploadProgressButtonHeight = uploadProgressButtonText.get_height()
quitButtonHeight = quitButtonText.get_height()

def redrawTitleScreen(): # Function that redraws the entire title screen
    screen.fill(BLACK)

    buttonColour1 = GREEN
    buttonColour2 = GREEN
    buttonColour3 = GREEN
    buttonColour4 = GREEN
    
    if buttonSelection == 1: # Changes the button colour based on selected button
        buttonColour1 = LIGHTBLUE
    elif buttonSelection == 2:
        buttonColour2 = LIGHTBLUE
    elif buttonSelection == 3:
        buttonColour3 = LIGHTBLUE
    elif buttonSelection == 4:
        buttonColour4 = LIGHTBLUE
    
    pygame.draw.rect(screen,GREEN,(cx - gameTitleWidth/2 - 30, gameTitleHeight/2 + 15, gameTitleWidth + 60, gameTitleHeight + 30),0)
    screen.blit(gameTitle,(cx - gameTitleWidth/2, 80))
    
    pygame.draw.rect(screen,buttonColour1,(cx - gameTitleWidth/2, gameTitleHeight/2 +210, gameTitleWidth, gameTitleHeight/2 + 30),0)
    screen.blit(playButtonText,(cx - playButtonWidth/2, 270))
    
    pygame.draw.rect(screen,buttonColour2,(cx - gameTitleWidth/2, gameTitleHeight/2 +310, gameTitleWidth, gameTitleHeight/2 + 30),0)
    screen.blit(instructionsButtonText,(cx - instructionsButtonWidth/2, 370))
    
    pygame.draw.rect(screen,buttonColour3,(cx - gameTitleWidth/2, gameTitleHeight/2 +410, gameTitleWidth, gameTitleHeight/2 + 30),0)
    screen.blit(uploadProgressButtonText,(cx - uploadProgressButtonWidth/2, 470))
    
    pygame.draw.rect(screen,buttonColour4,(cx - gameTitleWidth/2, gameTitleHeight/2 +510, gameTitleWidth, gameTitleHeight/2 + 30),0)
    screen.blit(quitButtonText,(cx - quitButtonWidth/2, 570))
    
    pygame.display.flip()

globalTextHeight = 0 # Variables used to move all the text at once on information screen
globalTextHeightDY = 0

infoTitleText = textFont.render("Controls/Instructions",True, (WHITE))

infoTitleWitdh = infoTitleText.get_width()
infoTitleHeight = infoTitleText.get_height()

infoTextLine1 = infoFont.render("- Controls -",True, (WHITE)) #Defines all the text for instruction screen
infoTextLine2 = infoFont.render("Menus",True, (WHITE))
infoTextLine3 = infoFont.render("W/UP: Up",True, (WHITE))
infoTextLine4 = infoFont.render("S/DOWN: Down",True, (WHITE))
infoTextLine5 = infoFont.render("A/LEFT: Left",True, (WHITE))
infoTextLine6 = infoFont.render("D/RIGHT: Right",True, (WHITE))
infoTextLine7 = infoFont.render("ENTER: Select/Confirm",True, (WHITE))
infoTextLine8 = infoFont.render("ESCAPE: Back/Exit",True, (WHITE))
infoTextLine9 = infoFont.render("In Game",True, (WHITE))
infoTextLine10 = infoFont.render("A: Walk Left",True, (WHITE))
infoTextLine11 = infoFont.render("D: Walk Right",True, (WHITE))
infoTextLine12 = infoFont.render("J: Jump",True, (WHITE))
infoTextLine13 = infoFont.render("K: Shoot",True, (WHITE))
infoTextLine14 = infoFont.render("L: Gadget",True, (WHITE))
infoTextLine15 = infoFont.render("Q: Cycle Gadget Left",True, (WHITE))
infoTextLine16 = infoFont.render("E: Cycle Gadget Right",True, (WHITE))
infoTextLine17 = infoFont.render("W: Interact",True, (WHITE))
infoTextLine19 = infoFont.render("- Instructions -",True, (WHITE))
infoTextLine20 = infoFont.render("In Robo Quest, You play as a robot that",True, (WHITE))
infoTextLine21 = infoFont.render("was given free thinking due to a ",True, (WHITE))
infoTextLine22 = infoFont.render("malfunction in the robot factory, so",True, (WHITE))
infoTextLine23 = infoFont.render("you have decided to become the greatest",True, (WHITE))
infoTextLine24 = infoFont.render("robot to ever have been created. To",True, (WHITE))
infoTextLine25 = infoFont.render("accomplish this goal, you must defeat",True, (WHITE))
infoTextLine26 = infoFont.render("the Robot King, located far away in",True, (WHITE))
infoTextLine27 = infoFont.render("his castle.", True, (WHITE))
infoTextLine28 = infoFont.render("To do this, you must run and jump through",True, (WHITE))
infoTextLine29 = infoFont.render("many different worlds and levels,",True, (WHITE))
infoTextLine30 = infoFont.render("blasting through various enemies and",True, (WHITE))
infoTextLine31 = infoFont.render("vanquishing massive bosses, all while",True, (WHITE))
infoTextLine32 = infoFont.render("collecting scrap metal to purchase and",True, (WHITE))
infoTextLine33 = infoFont.render("upgrade unique skills and abilities",True, (WHITE))
infoTextLine34 = infoFont.render("at shops you find on your adventures.",True, (WHITE))
infoTextLine35 = infoFont.render("Throughout the worlds, you will find",True, (WHITE))
infoTextLine36 = infoFont.render("checkpoints, where you may recharge your",True, (WHITE))
infoTextLine37 = infoFont.render("health and energy, as well as save your",True, (WHITE))
infoTextLine38 = infoFont.render("progress so you can continue the same",True, (WHITE))
infoTextLine39 = infoFont.render("adventure across multiple sessions",True, (WHITE))
infoTextLine40 = infoFont.render("(Or even across different devices!)",True, (WHITE))



def redrawInfoScreen(): # Function that redraws the Information Screen
    screen.fill(BLACK)
    screen.blit(infoTextLine1,(20,100 + globalTextHeight))
    screen.blit(infoTextLine2,(20,150 + globalTextHeight))
    screen.blit(infoTextLine3,(20,200 + globalTextHeight))
    screen.blit(infoTextLine4,(20,250 + globalTextHeight))
    screen.blit(infoTextLine5,(20,300 + globalTextHeight))
    screen.blit(infoTextLine6,(20,350 + globalTextHeight))
    screen.blit(infoTextLine7,(20,400 + globalTextHeight))
    screen.blit(infoTextLine8,(20,450 + globalTextHeight))
    screen.blit(infoTextLine9,(20,550 + globalTextHeight))
    screen.blit(infoTextLine10,(20,600 + globalTextHeight))
    screen.blit(infoTextLine11,(20,650 + globalTextHeight))
    screen.blit(infoTextLine12,(20,700 + globalTextHeight))
    screen.blit(infoTextLine13,(20,750 + globalTextHeight))
    screen.blit(infoTextLine14,(20,800 + globalTextHeight))
    screen.blit(infoTextLine15,(20,850 + globalTextHeight))
    screen.blit(infoTextLine16,(20,900 + globalTextHeight))
    screen.blit(infoTextLine17,(20,950 + globalTextHeight))
    screen.blit(infoTextLine19,(20,1100 + globalTextHeight))
    screen.blit(infoTextLine20,(20,1150 + globalTextHeight))
    screen.blit(infoTextLine21,(20,1200 + globalTextHeight))
    screen.blit(infoTextLine22,(20,1250 + globalTextHeight))
    screen.blit(infoTextLine23,(20,1300 + globalTextHeight))
    screen.blit(infoTextLine24,(20,1350 + globalTextHeight))
    screen.blit(infoTextLine25,(20,1400 + globalTextHeight))
    screen.blit(infoTextLine26,(20,1450 + globalTextHeight))
    screen.blit(infoTextLine27,(20,1500 + globalTextHeight))
    screen.blit(infoTextLine28,(20,1600 + globalTextHeight))
    screen.blit(infoTextLine29,(20,1650 + globalTextHeight))
    screen.blit(infoTextLine30,(20,1700 + globalTextHeight))
    screen.blit(infoTextLine31,(20,1750 + globalTextHeight))
    screen.blit(infoTextLine32,(20,1800 + globalTextHeight))
    screen.blit(infoTextLine33,(20,1850 + globalTextHeight))
    screen.blit(infoTextLine34,(20,1900 + globalTextHeight))
    screen.blit(infoTextLine35,(20,1950 + globalTextHeight))
    screen.blit(infoTextLine36,(20,2000 + globalTextHeight))
    screen.blit(infoTextLine37,(20,2050 + globalTextHeight))
    screen.blit(infoTextLine38,(20,2100 + globalTextHeight))
    screen.blit(infoTextLine39,(20,2150 + globalTextHeight))
    screen.blit(infoTextLine40,(20,2200 + globalTextHeight))
    pygame.draw.rect(screen,GREEN,(0,0,screenWidth,85),0)
    screen.blit(infoTitleText,(cx - infoTitleWitdh/2, 20))
    pygame.display.flip()

### Checkpoint screen code ###

checkpointButtonSelection = 1

checkpointButtonColour1 = GREEN
checkpointButtonColour2 = GREEN
checkpointButtonColour3 = GREEN
checkpointButtonColour4 = GREEN

checkpointTitle = titleFont.render("Checkpoint", True,(WHITE)) # Text used on the checkpoint screen
rechargeText = textFont.render("Recharge",True, (WHITE))
shopText = textFont.render("Shop",True, (WHITE))
saveProgressButtonText = textFont.render("Save Progress",True, (WHITE))
exitButtonText = textFont.render("Exit",True, (WHITE))

checkpointTitleWidth = checkpointTitle.get_width() # Finds the width of the text
rechargeTextWidth = rechargeText.get_width()
shopTextWidth = shopText.get_width()
saveProgressButtonWidth = saveProgressButtonText.get_width()
exitButtonWidth = exitButtonText.get_width()

checkpointTitleHeight = checkpointTitle.get_height() # Finds the height of the text
rechargeTextHeight = rechargeText.get_height()
shopTextHeight = shopText.get_height()
saveProgressButtonHeight = saveProgressButtonText.get_height()
exitButtonHeight = exitButtonText.get_height()


def redrawCheckpointScreen(): # Redraws checkpoint screen
    screen.fill(BLACK)

    checkpointButtonColour1 = GREEN
    checkpointButtonColour2 = GREEN
    checkpointButtonColour3 = GREEN
    checkpointButtonColour4 = GREEN
    
    if checkpointButtonSelection == 1: # Changes colour based on button selection
        checkpointButtonColour1 = LIGHTBLUE
    elif checkpointButtonSelection == 2:
        checkpointButtonColour2 = LIGHTBLUE
    elif checkpointButtonSelection == 3:
        checkpointButtonColour3 = LIGHTBLUE
    elif checkpointButtonSelection == 4:
        checkpointButtonColour4 = LIGHTBLUE
    
    screen.blit(checkpointTitle,(cx - checkpointTitleWidth/2, 80))
    
    pygame.draw.rect(screen,checkpointButtonColour1,(cx - gameTitleWidth/2, gameTitleHeight/2 +210, gameTitleWidth, gameTitleHeight/2 + 30),0)
    screen.blit(rechargeText,(cx - rechargeTextWidth/2, 270))
    
    pygame.draw.rect(screen,checkpointButtonColour2,(cx - gameTitleWidth/2, gameTitleHeight/2 +310, gameTitleWidth, gameTitleHeight/2 + 30),0)
    screen.blit(shopText,(cx - shopTextWidth/2, 370))
    
    pygame.draw.rect(screen,checkpointButtonColour3,(cx - gameTitleWidth/2, gameTitleHeight/2 +410, gameTitleWidth, gameTitleHeight/2 + 30),0)
    screen.blit(saveProgressButtonText,(cx - saveProgressButtonWidth/2, 470))
    
    pygame.draw.rect(screen,checkpointButtonColour4,(cx - gameTitleWidth/2, gameTitleHeight/2 +510, gameTitleWidth, gameTitleHeight/2 + 30),0)
    screen.blit(exitButtonText,(cx - exitButtonWidth/2, 570))
    
    pygame.display.flip()

### Shop screen code ###

shopButtonSelection = 1

shopTitle = statFont.render("Shop", True,(WHITE)) # Text for shop screen
shopInfoLine1 = textFont.render("",True,(WHITE))
shopInfoLine2 = infoFont.render("",True,(WHITE))
shopInfoLine3 = infoFont.render("",True,(WHITE))
shopInfoLine4 = infoFont.render("",True,(WHITE))
shopInfoLine5 = infoFont.render("",True,(WHITE))
upgradeCostText = statFont.render("",True,pygame.Color("#989898"))
energyCostText = statFont.render("",True,pygame.Color("#e7c711"))
playerScrapCountText = infoFont.render("",True,pygame.Color("#989898"))

shopTitleWidth = shopTitle.get_width()

def redrawShopScreen(): # Redraws shop
    screen.fill(BLACK)

    shopButtonColour1 = WHITE
    shopButtonColour2 = WHITE
    shopButtonColour3 = WHITE
    shopButtonColour4 = WHITE
    shopButtonColour5 = WHITE
    shopButtonColour6 = WHITE
    
    if shopButtonSelection == 1: # Changes colour based on button selection
        shopButtonColour1 = GREEN
    elif shopButtonSelection == 2:
        shopButtonColour2 = GREEN
    elif shopButtonSelection == 3:
        shopButtonColour3 = GREEN
    elif shopButtonSelection == 4:
        shopButtonColour4 = GREEN
    elif shopButtonSelection == 5:
        shopButtonColour5 = GREEN
    elif shopButtonSelection == 6:
        shopButtonColour6 = GREEN

    pygame.draw.rect(screen,shopButtonColour1,(64,220,128,128),4)
    screen.blit(grenadeIcon,(100,256))
    pygame.draw.rect(screen,shopButtonColour2,(270,220,128,128),4)
    screen.blit(shieldIcon,(306,256))
    pygame.draw.rect(screen,shopButtonColour3,(476,220,128,128),4)
    screen.blit(sawbladeIcon,(512,256))
    pygame.draw.rect(screen,shopButtonColour4,(682,220,128,128),4)
    screen.blit(sparkIcon,(718,256))
    pygame.draw.rect(screen,shopButtonColour5,(888,220,128,128),4)
    screen.blit(healthIcon,(924,256))
    pygame.draw.rect(screen,shopButtonColour6,(1088,220,128,128),4)
    screen.blit(energyIcon,(1128,256))
    pygame.draw.rect(screen,WHITE,(0,400,screenWidth,304),10)

    if shopButtonSelection == 1: # Displays shop text based on button and player upgrades
        if player.grenadeLV == 0:
            shopInfoLine1 = textFont.render("Grenade",True,(WHITE))
            shopInfoLine2 = infoFont.render("Throws an explosive grenade in an arc",True,(WHITE))
            shopInfoLine3 = infoFont.render("that explodes upon contact with a wall",True,(WHITE))
            shopInfoLine4 = infoFont.render("or ememy, damaging all enemies caught",True,(WHITE))
            shopInfoLine5 = infoFont.render("in its blast",True,(WHITE))
            upgradeCostText = statFont.render("25",True,pygame.Color("#989898"))
            energyCostText = statFont.render("12",True,pygame.Color("#e7c711"))
            screen.blit(scrapIcon,(1050,430))
            screen.blit(energyIcon,(800,430))
        elif player.grenadeLV == 1:
            shopInfoLine1 = textFont.render("Grenade +",True,(WHITE))
            shopInfoLine2 = infoFont.render("Improved grenade reduces the energy cost",True,(WHITE))
            shopInfoLine3 = infoFont.render("and has a longer lasting explosion",True,(WHITE))
            shopInfoLine4 = infoFont.render("",True,(WHITE))
            shopInfoLine5 = infoFont.render("",True,(WHITE))
            upgradeCostText = statFont.render("30",True,pygame.Color("#989898"))
            energyCostText = statFont.render("9",True,pygame.Color("#e7c711"))
            screen.blit(scrapIcon,(1050,430))
            screen.blit(energyIcon,(800,430))
        elif player.grenadeLV == 2:
            shopInfoLine1 = textFont.render("Max Level Reached",True,(WHITE))
            shopInfoLine2 = infoFont.render("",True,(WHITE))
            shopInfoLine3 = infoFont.render("",True,(WHITE))
            shopInfoLine4 = infoFont.render("",True,(WHITE))
            shopInfoLine5 = infoFont.render("",True,(WHITE))
            upgradeCostText = statFont.render("",True,pygame.Color("#989898"))
            energyCostText = statFont.render("",True,pygame.Color("#e7c711"))
    elif shopButtonSelection == 2:
        if player.shieldLV == 0:
            shopInfoLine1 = textFont.render("Energy Shield",True,(WHITE))
            shopInfoLine2 = infoFont.render("Activates a shield that lasts until it",True,(WHITE))
            shopInfoLine3 = infoFont.render("absorbs 2 projectiles",True,(WHITE))
            shopInfoLine4 = infoFont.render("",True,(WHITE))
            shopInfoLine5 = infoFont.render("",True,(WHITE))
            upgradeCostText = statFont.render("25",True,pygame.Color("#989898"))
            energyCostText = statFont.render("20",True,pygame.Color("#e7c711"))
            screen.blit(scrapIcon,(1050,430))
            screen.blit(energyIcon,(800,430))
        elif player.shieldLV == 1:
            shopInfoLine1 = textFont.render("Energy Shield +",True,(WHITE))
            shopInfoLine2 = infoFont.render("Shield blocks an additional projectile",True,(WHITE))
            shopInfoLine3 = infoFont.render("and restores health for each blocked",True,(WHITE))
            shopInfoLine4 = infoFont.render("projectile",True,(WHITE))
            shopInfoLine5 = infoFont.render("",True,(WHITE))
            upgradeCostText = statFont.render("30",True,pygame.Color("#989898"))
            energyCostText = statFont.render("20",True,pygame.Color("#e7c711"))
            screen.blit(scrapIcon,(1050,430))
            screen.blit(energyIcon,(800,430))
        elif player.shieldLV == 2:
            shopInfoLine1 = textFont.render("Max Level Reached",True,(WHITE))
            shopInfoLine2 = infoFont.render("",True,(WHITE))
            shopInfoLine3 = infoFont.render("",True,(WHITE))
            shopInfoLine4 = infoFont.render("",True,(WHITE))
            shopInfoLine5 = infoFont.render("",True,(WHITE))
            upgradeCostText = statFont.render("",True,pygame.Color("#989898"))
            energyCostText = statFont.render("",True,pygame.Color("#e7c711"))
    elif shopButtonSelection == 3:
        if player.sawLV == 0:
            shopInfoLine1 = textFont.render("Sawblade",True,(WHITE))
            shopInfoLine2 = infoFont.render("Fires a sawblade that pierces enemies and",True,(WHITE))
            shopInfoLine3 = infoFont.render("walls, dealing damage to all enemies it",True,(WHITE))
            shopInfoLine4 = infoFont.render("passes through",True,(WHITE))
            shopInfoLine5 = infoFont.render("",True,(WHITE))
            upgradeCostText = statFont.render("25",True,pygame.Color("#989898"))
            energyCostText = statFont.render("16",True,pygame.Color("#e7c711"))
            screen.blit(scrapIcon,(1050,430))
            screen.blit(energyIcon,(800,430))
        elif player.sawLV == 1:
            shopInfoLine1 = textFont.render("Sawblade +",True,(WHITE))
            shopInfoLine2 = infoFont.render("Sawblade travels much faster and deals an",True,(WHITE))
            shopInfoLine3 = infoFont.render("additional point of damage to enemies",True,(WHITE))
            shopInfoLine4 = infoFont.render("",True,(WHITE))
            shopInfoLine5 = infoFont.render("",True,(WHITE))
            upgradeCostText = statFont.render("30",True,pygame.Color("#989898"))
            energyCostText = statFont.render("16",True,pygame.Color("#e7c711"))
            screen.blit(scrapIcon,(1050,430))
            screen.blit(energyIcon,(800,430))
        elif player.sawLV == 2:
            shopInfoLine1 = textFont.render("Max Level Reached",True,(WHITE))
            shopInfoLine2 = infoFont.render("",True,(WHITE))
            shopInfoLine3 = infoFont.render("",True,(WHITE))
            shopInfoLine4 = infoFont.render("",True,(WHITE))
            shopInfoLine5 = infoFont.render("",True,(WHITE))
            upgradeCostText = statFont.render("",True,pygame.Color("#989898"))
            energyCostText = statFont.render("",True,pygame.Color("#e7c711"))
    elif shopButtonSelection == 4:
        if player.sparkLV == 0:
            shopInfoLine1 = textFont.render("Spark Storm",True,(WHITE))
            shopInfoLine2 = infoFont.render("Releases damaging sparks that travel in 4",True,(WHITE))
            shopInfoLine3 = infoFont.render("directions that stop on contact with",True,(WHITE))
            shopInfoLine4 = infoFont.render("walls or enemies",True,(WHITE))
            shopInfoLine5 = infoFont.render("",True,(WHITE))
            upgradeCostText = statFont.render("25",True,pygame.Color("#989898"))
            energyCostText = statFont.render("16",True,pygame.Color("#e7c711"))
            screen.blit(scrapIcon,(1050,430))
            screen.blit(energyIcon,(800,430))
        elif player.sparkLV == 1:
            shopInfoLine1 = textFont.render("Spark Storm +",True,(WHITE))
            shopInfoLine2 = infoFont.render("Releases an additional 4 sparks and",True,(WHITE))
            shopInfoLine3 = infoFont.render("refunds a portion of energy for each",True,(WHITE))
            shopInfoLine4 = infoFont.render("successful hit",True,(WHITE))
            shopInfoLine5 = infoFont.render("",True,(WHITE))
            upgradeCostText = statFont.render("30",True,pygame.Color("#989898"))
            energyCostText = statFont.render("16",True,pygame.Color("#e7c711"))
            screen.blit(scrapIcon,(1050,430))
            screen.blit(energyIcon,(800,430))
        elif player.sparkLV == 2:
            shopInfoLine1 = textFont.render("Max Level Reached",True,(WHITE))
            shopInfoLine2 = infoFont.render("",True,(WHITE))
            shopInfoLine3 = infoFont.render("",True,(WHITE))
            shopInfoLine4 = infoFont.render("",True,(WHITE))
            shopInfoLine5 = infoFont.render("",True,(WHITE))
            upgradeCostText = statFont.render("",True,pygame.Color("#989898"))
            energyCostText = statFont.render("",True,pygame.Color("#e7c711"))
    elif shopButtonSelection == 5:
        if player.maxHealth == 50:
            shopInfoLine1 = textFont.render("Health Upgrade I",True,(WHITE))
            shopInfoLine2 = infoFont.render("Increases max health by 10 (max 50)",True,(WHITE))
            shopInfoLine3 = infoFont.render("",True,(WHITE))
            shopInfoLine4 = infoFont.render("",True,(WHITE))
            shopInfoLine5 = infoFont.render("",True,(WHITE))
            upgradeCostText = statFont.render("10",True,pygame.Color("#989898"))
            energyCostText = statFont.render("",True,pygame.Color("#e7c711"))
            screen.blit(scrapIcon,(1050,430))
        elif player.maxHealth == 60:
            shopInfoLine1 = textFont.render("Health Upgrade II",True,(WHITE))
            shopInfoLine2 = infoFont.render("Increases max health by 10 (max 50)",True,(WHITE))
            shopInfoLine3 = infoFont.render("",True,(WHITE))
            shopInfoLine4 = infoFont.render("",True,(WHITE))
            shopInfoLine5 = infoFont.render("",True,(WHITE))
            upgradeCostText = statFont.render("15",True,pygame.Color("#989898"))
            energyCostText = statFont.render("",True,pygame.Color("#e7c711"))
            screen.blit(scrapIcon,(1050,430))
        elif player.maxHealth == 70:
            shopInfoLine1 = textFont.render("Health Upgrade III",True,(WHITE))
            shopInfoLine2 = infoFont.render("Increases max health by 10 (max 50)",True,(WHITE))
            shopInfoLine3 = infoFont.render("",True,(WHITE))
            shopInfoLine4 = infoFont.render("",True,(WHITE))
            shopInfoLine5 = infoFont.render("",True,(WHITE))
            upgradeCostText = statFont.render("20",True,pygame.Color("#989898"))
            energyCostText = statFont.render("",True,pygame.Color("#e7c711"))
            screen.blit(scrapIcon,(1050,430))
        elif player.maxHealth == 80:
            shopInfoLine1 = textFont.render("Health Upgrade IV",True,(WHITE))
            shopInfoLine2 = infoFont.render("Increases max health by 10 (max 50)",True,(WHITE))
            shopInfoLine3 = infoFont.render("",True,(WHITE))
            shopInfoLine4 = infoFont.render("",True,(WHITE))
            shopInfoLine5 = infoFont.render("",True,(WHITE))
            upgradeCostText = statFont.render("25",True,pygame.Color("#989898"))
            energyCostText = statFont.render("",True,pygame.Color("#e7c711"))
            screen.blit(scrapIcon,(1050,430))
        elif player.maxHealth == 90:
            shopInfoLine1 = textFont.render("Health Upgrade V",True,(WHITE))
            shopInfoLine2 = infoFont.render("Increases max health by 10 (max 50)",True,(WHITE))
            shopInfoLine3 = infoFont.render("",True,(WHITE))
            shopInfoLine4 = infoFont.render("",True,(WHITE))
            shopInfoLine5 = infoFont.render("",True,(WHITE))
            upgradeCostText = statFont.render("30",True,pygame.Color("#989898"))
            energyCostText = statFont.render("",True,pygame.Color("#e7c711"))
            screen.blit(scrapIcon,(1050,430))
        elif player.maxHealth == 100:
            shopInfoLine1 = textFont.render("Max Level Reached",True,(WHITE))
            shopInfoLine2 = infoFont.render("",True,(WHITE))
            shopInfoLine3 = infoFont.render("",True,(WHITE))
            shopInfoLine4 = infoFont.render("",True,(WHITE))
            shopInfoLine5 = infoFont.render("",True,(WHITE))
            upgradeCostText = statFont.render("",True,pygame.Color("#989898"))
            energyCostText = statFont.render("",True,pygame.Color("#e7c711"))
    elif shopButtonSelection == 6:
        if player.maxEnergy == 50:
            shopInfoLine1 = textFont.render("Energy Upgrade I",True,(WHITE))
            shopInfoLine2 = infoFont.render("Increases max energy by 10 (max 50)",True,(WHITE))
            shopInfoLine3 = infoFont.render("",True,(WHITE))
            shopInfoLine4 = infoFont.render("",True,(WHITE))
            shopInfoLine5 = infoFont.render("",True,(WHITE))
            upgradeCostText = statFont.render("10",True,pygame.Color("#989898"))
            energyCostText = statFont.render("",True,pygame.Color("#e7c711"))
            screen.blit(scrapIcon,(1050,430))
        elif player.maxEnergy == 60:
            shopInfoLine1 = textFont.render("Energy Upgrade II",True,(WHITE))
            shopInfoLine2 = infoFont.render("Increases max energy by 10 (max 50)",True,(WHITE))
            shopInfoLine3 = infoFont.render("",True,(WHITE))
            shopInfoLine4 = infoFont.render("",True,(WHITE))
            shopInfoLine5 = infoFont.render("",True,(WHITE))
            upgradeCostText = statFont.render("15",True,pygame.Color("#989898"))
            energyCostText = statFont.render("",True,pygame.Color("#e7c711"))
            screen.blit(scrapIcon,(1050,430))
        elif player.maxEnergy == 70:
            shopInfoLine1 = textFont.render("Energy Upgrade III",True,(WHITE))
            shopInfoLine2 = infoFont.render("Increases max energy by 10 (max 50)",True,(WHITE))
            shopInfoLine3 = infoFont.render("",True,(WHITE))
            shopInfoLine4 = infoFont.render("",True,(WHITE))
            shopInfoLine5 = infoFont.render("",True,(WHITE))
            upgradeCostText = statFont.render("20",True,pygame.Color("#989898"))
            energyCostText = statFont.render("",True,pygame.Color("#e7c711"))
            screen.blit(scrapIcon,(1050,430))
        elif player.maxEnergy == 80:
            shopInfoLine1 = textFont.render("Energy Upgrade IV",True,(WHITE))
            shopInfoLine2 = infoFont.render("Increases max energy by 10 (max 50)",True,(WHITE))
            shopInfoLine3 = infoFont.render("",True,(WHITE))
            shopInfoLine4 = infoFont.render("",True,(WHITE))
            shopInfoLine5 = infoFont.render("",True,(WHITE))
            upgradeCostText = statFont.render("25",True,pygame.Color("#989898"))
            energyCostText = statFont.render("",True,pygame.Color("#e7c711"))
            screen.blit(scrapIcon,(1050,430))
        elif player.maxEnergy == 90:
            shopInfoLine1 = textFont.render("Energy Upgrade V",True,(WHITE))
            shopInfoLine2 = infoFont.render("Increases max energy by 10 (max 50)",True,(WHITE))
            shopInfoLine3 = infoFont.render("",True,(WHITE))
            shopInfoLine4 = infoFont.render("",True,(WHITE))
            shopInfoLine5 = infoFont.render("",True,(WHITE))
            upgradeCostText = statFont.render("30",True,pygame.Color("#989898"))
            energyCostText = statFont.render("",True,pygame.Color("#e7c711"))
            screen.blit(scrapIcon,(1050,430))
        elif player.maxEnergy == 100:
            shopInfoLine1 = textFont.render("Max Level Reached",True,(WHITE))
            shopInfoLine2 = infoFont.render("",True,(WHITE))
            shopInfoLine3 = infoFont.render("",True,(WHITE))
            shopInfoLine4 = infoFont.render("",True,(WHITE))
            shopInfoLine5 = infoFont.render("",True,(WHITE))
            upgradeCostText = statFont.render("",True,pygame.Color("#989898"))
            energyCostText = statFont.render("",True,pygame.Color("#e7c711"))
    
    screen.blit(shopTitle,(cx - shopTitleWidth/2,20))

    playerScrapCountText = infoFont.render("Player Scrap: " +str(player.scrap),True,pygame.Color("#989898"))
    playerScrapCountWidth = playerScrapCountText.get_width()
    screen.blit(playerScrapCountText,(cx-playerScrapCountWidth/2,130))
    
    screen.blit(shopInfoLine1,(30,430))
    screen.blit(upgradeCostText,(1118,430))
    screen.blit(energyCostText,(868,430))
    screen.blit(shopInfoLine2,(30,500))
    screen.blit(shopInfoLine3,(30,540))
    screen.blit(shopInfoLine4,(30,580))
    screen.blit(shopInfoLine5,(30,620))
    
    pygame.display.flip()

### Save/Upload Progress screen code ###

fileButtonSelection = 1

fileTitle = statFont.render("",True,WHITE)
warningText1 = infoFont.render("",True,WHITE)
warningText2 = infoFont.render("",True,WHITE)
warningText3 = infoFont.render("",True,WHITE)
file1Text = infoFont.render("File 1",True,WHITE)
file2Text = infoFont.render("File 2",True,WHITE)
file3Text = infoFont.render("File 3",True,WHITE)

fileTitleWidth = fileTitle.get_width()
warningTextWidth1 = warningText1.get_width()
warningTextWidth2 = warningText2.get_width()
warningTextWidth3 = warningText3.get_width()

def redrawFileScreen(): # redraws file screen

# Save files info (in order)
#1 Checkpoint number
#2 Room number
#3 Max HP
#4 Max Energy
#5 Scrap
#6 Grenade LV
#7 Shield LV
#8 Saw LV
#9 Spark LV

    screen.fill(BLACK)
    fileButtonColour1 = WHITE
    fileButtonColour2 = WHITE
    fileButtonColour3 = WHITE
    if fileButtonSelection == 1: # Changes button colour based on button
        fileButtonColour1 = GREEN 
    elif fileButtonSelection == 2:
        fileButtonColour2 = GREEN
    elif fileButtonSelection == 3:
        fileButtonColour3 = GREEN
    if saveProgressScreen == True:
        fileTitle = statFont.render("Save Game",True,WHITE)
        warningText1 = infoFont.render("WARNING! Saving to a file will",True,WHITE)
        warningText2 = infoFont.render("erase any data previously saved",True,WHITE)
        warningText3 = infoFont.render("on it.",True,WHITE)
    elif uploadProgressScreen == True:
        fileTitle = statFont.render("Load Game",True,WHITE)
        warningText1 = infoFont.render("WARNING! Tampering with save",True,WHITE)
        warningText2 = infoFont.render("files can cause the game to crash",True,WHITE)
        warningText3 = infoFont.render("or not work properly.",True,WHITE)
    else:
        fileTitle = statFont.render("",True,WHITE)
        warningText1 = infoFont.render("",True,WHITE)
        warningText2 = infoFont.render("",True,WHITE)
        warningText3 = infoFont.render("",True,WHITE)
    warningTextWidth1 = warningText1.get_width()
    warningTextWidth2 = warningText2.get_width()
    warningTextWidth3 = warningText3.get_width()
    fileTitleWidth = fileTitle.get_width()
    file1Text = infoFont.render("File 1",True,fileButtonColour1)
    file2Text = infoFont.render("File 2",True,fileButtonColour2)
    file3Text = infoFont.render("File 3",True,fileButtonColour3)
    screen.blit(file1Text,(148,340))
    screen.blit(file2Text,(532,340))
    screen.blit(file3Text,(916,340))
    pygame.draw.rect(screen,fileButtonColour1,(128,320,256,320),10)
    pygame.draw.rect(screen,fileButtonColour2,(512,320,256,320),10)
    pygame.draw.rect(screen,fileButtonColour3,(896,320,256,320),10)
    screen.blit(fileTitle,(cx - fileTitleWidth/2,20))
    screen.blit(warningText1,(cx - warningTextWidth1/2,110))
    screen.blit(warningText2,(cx - warningTextWidth2/2,170))
    screen.blit(warningText3,(cx - warningTextWidth3/2,230))
    pygame.display.flip()

resultText1 = infoFont.render("",True,WHITE)
resultText2 = infoFont.render("",True,WHITE)

resultText1Width = resultText1.get_width()
resultText2Width = resultText2.get_width()

def redrawFileResult(): # Redraws file result screen (when you save or upload)
    screen.fill(BLACK)
    if uploadSuccess == True:
        resultText1 = infoFont.render("Upload Successful!",True,WHITE)
        resultText2 = infoFont.render("Press Enter to continue",True,WHITE)
    elif uploadFailed == True:
        resultText1 = infoFont.render("Uh Oh!",True,WHITE)
        resultText2 = infoFont.render("The file could not be found!",True,WHITE)
    elif saveSuccess == True:
        resultText1 = infoFont.render("Save Successful!",True,WHITE)
        resultText2 = infoFont.render("Press Enter to continue",True,WHITE)
    elif saveFailed == True:
        resultText1 = infoFont.render("Uh Oh!",True,WHITE)
        resultText2 = infoFont.render("The file could not be found!",True,WHITE)
    else:
        resultText1 = infoFont.render("",True,WHITE)
        resultText2 = infoFont.render("",True,WHITE)
    resultText1Width = resultText1.get_width()
    resultText2Width = resultText2.get_width()
    screen.blit(resultText1,(cx - resultText1Width/2,300))
    screen.blit(resultText2,(cx - resultText2Width/2,400))
    pygame.display.flip()

### Death Screen Code ###

deathTitle = statFont.render("You Died!",True,WHITE) # Defines text
scrapLostText = infoFont.render("",True,WHITE)
continueText1 = infoFont.render("Press Enter to restart from",True,WHITE)
continueText2 = infoFont.render("last checkpoint",True,WHITE)
deathTitleWidth = deathTitle.get_width()
scrapLostWidth = scrapLostText.get_width()
continueTextWidth1 = continueText1.get_width()
continueTextWidth2 = continueText2.get_width()

def redrawDeathScreen(): #redraws death screen
    screen.fill(BLACK)
    scrapLostText = infoFont.render("And lost " +str(int(player.scrap/2)) + " scrap...",True,WHITE)
    scrapLostWidth = scrapLostText.get_width()
    screen.blit(deathTitle,(cx - deathTitleWidth/2, 40))
    screen.blit(scrapLostText,(cx - scrapLostWidth/2, 250))
    screen.blit(continueText1,(cx - continueTextWidth1/2, 480))
    screen.blit(continueText2,(cx - continueTextWidth2/2, 530))
    pygame.display.flip()

### Victory Screen Code ###

victoryTitle = statFont.render("Congratulations!",True,WHITE)
victoryText1 = infoFont.render("You have reached the end",True,WHITE)
victoryText2 = infoFont.render("of Robo Quest!",True,WHITE)
victoryText3 = infoFont.render("Press Escape to exit, or press",True,WHITE)
victoryText4 = infoFont.render("Enter to return to the main menu.",True,WHITE)
victoryText5 = infoFont.render("If you press play from the main menu,",True,WHITE)
victoryText6 = infoFont.render("you will keep all your upgrades, but",True,WHITE)
victoryText7 = infoFont.render("restart from level 1.",True,WHITE)
victoryText8 = infoFont.render("Thanks for playing!",True,WHITE)

victoryTitleWidth = victoryTitle.get_width()
victoryText1Width = victoryText1.get_width()
victoryText2Width = victoryText2.get_width()
victoryText3Width = victoryText3.get_width()
victoryText4Width = victoryText4.get_width()
victoryText5Width = victoryText5.get_width()
victoryText6Width = victoryText6.get_width()
victoryText7Width = victoryText7.get_width()
victoryText8Width = victoryText8.get_width()

def redrawVictoryScreen(): # Redraws victory screen
    screen.fill(BLACK)
    screen.blit(victoryTitle,(cx - victoryTitleWidth/2,40))
    screen.blit(victoryText1,(cx - victoryText1Width/2,130))
    screen.blit(victoryText2,(cx - victoryText2Width/2,170))
    screen.blit(victoryText3,(cx - victoryText3Width/2,250))
    screen.blit(victoryText4,(cx - victoryText4Width/2,290))
    screen.blit(victoryText5,(cx - victoryText5Width/2,330))
    screen.blit(victoryText6,(cx - victoryText6Width/2,370))
    screen.blit(victoryText7,(cx - victoryText7Width/2,410))
    screen.blit(victoryText8,(cx - victoryText8Width/2,500))
    pygame.display.flip()


### Main Game Code ###

blockX = 0
blockY = 0
walls = []
rooms = []
checkpointRoom = False
roomNumber = 0
room0 = [ # All of the game rooms
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", #rooms are 1280 by 602
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                       ",
"W                                       ",
"W                                       ",
"W                                       ",
"W                                       ",
"W                                       ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",]
room1 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W             WWWWWWWWWWWW             W",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",]
room2 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"WWWWWWWWWWWW            WWW            W",
"                        WWW             ",
"                        WWW             ",
"                        WWW             ",
"                        WWW             ",
"                        WWW             ",
"                        WWW             ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",]
room3 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"WWWWWWWW    WWWWWW    WWWWWW    WWWWWWWW",]
room4 = [
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W              WWWWWWWWWW              W",
"W                  WW                  W",
"W                  WW                  W",
"W                  WW                  W",
"WWWWWWWW           WW           WWWWWWWW",
"W                  WW                  W",
"                   WW                   ",
"                   WW                   ",
"             WWWWWWWWWWWWWW             ",
"                   WW                   ",
"                   WW                   ",
"                   WW                   ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",]
room5 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                    WWW               W",
"                                        ",
"              WWW                       ",
"                                        ",
"      WWW                   WWW         ",
"                                        ",
"                                        ",
"WWWW                                WWWW",]
room6 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                       ",
"W                                       ",
"W                                       ",
"W                                       ",
"W                                       ",
"W                                       ",
"W                  WWWWWWWWWWWWWWWWWWWWW",
"W                                      W",
"W                                      W",
"WWWWW                                  W",
"W                                      W",
"                                       W",
"                                       W",
"           WWWWW                       W",
"                                       W",
"                                       W",
"                                       W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",]
room7 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"                                       W",
"                                       W",
"                                       W",
"                                       W",
"                                       W",
"                                       W",
"WWWW                                   W",
"WWWW                                   W",
"WWWW                                   W",
"WWWW                                   W",
"WWWW                                   W",
"WWWW                                    ",
"WWWW                                    ",
"WWWW                                    ",
"WWWW                                    ",
"WWWW                                    ",
"WWWW                                    ",
"WWWW     WWWWWWWWWWWWWWW      WWWWWWWWWW",]
room8 = [
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWW    WWW    WWW    WWW    WWW    WWWW",
"WWWW    WWW    WWW    WWW    WWW    WWWW",
"WWWW    WWW    WWW    WWW    WWW    WWWW",
"WWWW    WWW    WWW    WWW    WWW    WWWW",
"WWWW    WWW    WWW    WWW    WWW    WWWW",
"WWWW    WWW    WWW    WWW    WWW    WWWW",
"WWWW    WWW    WWW    WWW    WWW    WWWW",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",]
room9 = [
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W        WWW           WWW             W",
"W    W          WWW           WWW      W",
"W    W                                 W",
"W    W                                 W",
"WW   W                                 W",
"     W                                  ",
"     W                                  ",
"     W                                  ",
"     W                                  ",
"     W                                  ",
"     W                                  ",
"WWWWWW                            WWWWWW",]
room10 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",]
room11 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W               WWWWWWW                W",
"W                                      W",
"W                                      W",
"W                                      W",
"W     WWWWWWWW            WWWWWWWW     W",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"WWWWWWW                          WWWWWWW",]
room12 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W               W      W               W",
"W               W      W               W",
"W               W  WW  W               W",
"                W      W                ",
"             WWWW      WWWW             ",
"                W      W                ",
"                W      W                ",
"                W      W                ",
"                W      W                ",
"WWWWWWWWWWWWWWWWW      WWWWWWWWWWWWWWWWW",]
room13 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                       ",
"W                                       ",
"W                                       ",
"W                                       ",
"W                                       ",
"W                                       ",
"W                                    WWW",
"W                                 W    W",
"W                             W        W",
"W                        W             W",
"W                                      W",
"                    W                  W",
"                                       W",
"              W                        W",
"                                       W",
"        W                              W",
"                                       W",
"WWWWWWWWW                              W",]
room14 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"                                       W",
"                                       W",
"                                       W",
"                                       W",
"                                       W",
"                                       W",
"WWW WWW WWW WWW WWW WWW WWW WWW        W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                   WWWW",
"W                                       ",
"W                                       ",
"W                                       ",
"W                                       ",
"W                                       ",
"W                                       ",
"WWW  WWWWW    WWWW   WWWWWW   WWWW  WWWW",]
room15 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                 W                      ",
"WWWWW    WWWW          WWWWWWW    WWWWWW",]
room16 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                       ",
"W                                       ",
"W                                       ",
"W                                       ",
"W                                       ",
"W                                       ",
"                                       W",
"                                       W",
"                       WWWWWWWWWWW     W",
"                                       W",
"       WWWWWWWWWWW                     W",
"                                       W",
"WWWWW                                  W",]
room17 = [
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"                                       W",
"                                       W",
"                                        ",
"                                        ",
"                       WWW              ",
"                       WWW              ",
"WWW     WWW     WWW    WWW              ",
"WWW     WWW     WWW    WWW              ",
"WWW     WWW     WWW    WWW             W",
"WWW     WWW     WWW    WWW     WWW     W",
"WWW     WWW     WWW    WWW     WWW     W",
"WWW     WWW     WWW    WWW     WWW     W",
"WWW     WWW     WWW    WWW     WWW     W",]
room18 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"                                       W",
"                                       W",
"                                       W",
"                                       W",
"                                        ",
"                                        ",
"WWWWW  WWW  WWW  WWW                    ",
"W                  W                    ",
"W                  W                    ",
"W                  W                    ",
"WWWWWWWWWWWWWWWWWWWWWWW   WWWWWW    WWWW",]
room19 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"              WWWWWWWWWWWW              ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",]
room20 = [
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",]
room21 = [
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"WWWWW     WWWWWWWWWWWWWWWWWWWW     WWWWW",]
room22 = [
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"             WWWWWWWWWWWW               ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",]
room23 = [
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                       W",
"                                       W",
"                                       W",
"                                 WWW   W",
"                                       W",
"                                       W",
"                           WWW         W",
"                                       W",
"                  WWW                  W",
"                                       W",
"                                       W",
"            WWW                        W",
"                                       W",
"WWWWWWWWW                              W",]
room24 = [
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"            WWWW                        ",
"                                        ",
"WWWWWWW                                 ",
"                                        ",
"                    WWWW                ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                            WWWWWWWWWWWW",]
room25 = [
"             W                          ",
"             W                          ",
"             W                          ",
"             W                          ",
"             W                          ",
"             W                          ",
"        W    W                          ",
"        W    W                          ",
"        W    W                          ",
"WW      W    W                          ",
"        W    W                          ",
"        W                               ",
"        W                               ",
"        W                               ",
"        W                               ",
"      WWW                               ",
"        W                               ",
"        W                               ",
"WWWWWWWWWWWWWWWWWW      WWWWWWWW     WWW",]
room26 = [
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                  WWWW                  ",
"                                        ",
"               WWW    WWW               ",
"                                        ",
"            WWW          WWW            ",
"                                        ",
"         WWW                WWW         ",
"                                        ",
"      WWW                      WWW      ",
"                                        ",
"                                        ",
"WWWWWW                            WWWWWW",]
room27 = [
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"               WWWWWWWWWW               ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"WWWWWW    WWWWWWWW    WWWWWWWW    WWWWWW",]
room28 = [
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                       W",
"            W                           ",
"                   W                    ",
"                                  W     ",
"                                        ",
"                                        ",
"         W                W             ",
"                                        ",
"                                        ",
"WWWWWW                                  ",]
room29 = [
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"WWWWWW                                  ",
"     W                                  ",
"     W                                  ",
"                                        ",
"     W                                  ",
"     W                                  ",
"                                        ",
"     W             WWWWWWWW             ",
"     W                                  ",
"     WWWWWWWWW                  WWWWWWWW",]
room30 = [
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",]
room31 = [
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"       W        W       W       W       ",
"       W        W       W       W       ",
"       W        W       W       W       ",
"       W        W       W       W       ",
"       W        W       W       W       ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",]
room32 = [
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                    WWWW",
"                              WWWW      ",
"                        WWWW            ",
"                  WWWW                  ",
"WWWWWWW    WWWW                         ",]
room33 = [
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"                                        ",
"                                        ",
"                                        ",
"                                        ",]
room34 = [
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"WWWWW                                   ",
"     WWWWW                              ",
"          WWWWW                         ",
"               WWWWW                    ",
"                    WWWWWWWWWWWWWWWWWWWW",]
room35 = [
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                   WWWWW",
"                                        ",
"                             WWW        ",
"                     WWWW               ",
"WWWWWWWWWWWWWWWWW                       ",]
room36 = [
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"                                        ",
"                                        ",
"                                        ",
"                                        ",]
room37 = [
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"    WWW                          WWW    ",
"     W                            W     ",
"     W                            W     ",
"     W                            W     ",]
room38 = [
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"    WWW                          WWW    ",
"     W                            W     ",
"     W                            W     ",
"     W                            W     ",]
room39 = [
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"    WWW                          WWW    ",
"     W                            W     ",
"     W                            W     ",
"     W                            W     ",]
room40 = [
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"                                        ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"    WWW                          WWW    ",
"     W                            W     ",
"     W                            W     ",
"     W                            W     ",]

rooms.append(room0) # Adds all rooms to a list
rooms.append(room1)
rooms.append(room2)
rooms.append(room3)
rooms.append(room4)
rooms.append(room5)
rooms.append(room6)
rooms.append(room7)
rooms.append(room8)
rooms.append(room9)
rooms.append(room10)
rooms.append(room11)
rooms.append(room12)
rooms.append(room13)
rooms.append(room14)
rooms.append(room15)
rooms.append(room16)
rooms.append(room17)
rooms.append(room18)
rooms.append(room19)
rooms.append(room20)
rooms.append(room21)
rooms.append(room22)
rooms.append(room23)
rooms.append(room24)
rooms.append(room25)
rooms.append(room26)
rooms.append(room27)
rooms.append(room28)
rooms.append(room29)
rooms.append(room30)
rooms.append(room31)
rooms.append(room32)
rooms.append(room33)
rooms.append(room34)
rooms.append(room35)
rooms.append(room36)
rooms.append(room37)
rooms.append(room38)
rooms.append(room39)
rooms.append(room40)


class player(pygame.sprite.Sprite): # defines the player class, which is used by the main character
    def __init__(self, x, y, width, height): # initializes the player class, giving it variables
        pygame.sprite.Sprite.__init__(self)
        self.x = x # x/y
        self.y = y
        self.oldX = x # Old x and y
        self.oldY = y
        self.width = width # Defines width and height
        self.height = height
        self.dx = 0 # x and y speed
        self.dy = 0 
        self.inMidair = True
        self.jumping = True
        self.movingRight = False # Used to test if player is moving (and which direction
        self.movingLeft = False
        self.facingRight = True # Used to test which direction the player is facing, even if they are stationary
        self.facingLeft = False
        self.shooting = False
        self.shootCount = 0 # variable to delay the player from shooting constantly
        self.walkCount = 0 # Variable used in the player's walk animation
        self.maxHealth = 50 # Sets the player's max health and energy
        self.maxEnergy = 50
        self.health = self.maxHealth # sets the player's current health and energy
        self.energy = self.maxEnergy
        self.scrap = 0 # Player scrap, used to buy upgrades
        self.gadgetSelection = 1 # Player's gadget selection
        self.grenadeLV = 0 # The level of all the player's gadgets
        self.shieldLV = 0
        self.shielded = False
        self.shieldHealth = 0
        self.sawLV = 0
        self.sparkLV = 0
        self.immuneTimer = 0 # Player's "immune timer" used to delay the player from being hit multiple times too quickly
        self.checkpoint = 0 # Which checkpoint the player has visited most recently
        self.rect = pygame.Rect(x,y,width,height) # Defines the players hitbox (in the form of a Rect)

    def update(self, x, y, dx, dy, width, height, walls): # Updates variables/Collision
        player.rect = pygame.Rect(player.x,player.y,player.width,player.height) # redefines the Rect (does it many times in the function to avoid buggy collision)
        self.x = self.x + self.dx # updates x and y
        self.y = self.y + self.dy
        self.rect = pygame.Rect(player.x,player.y,player.width,player.height)
        self.y += 1 # Moves the player down slightly to test if they are on the ground or not
        self.rect = pygame.Rect(player.x,player.y,player.width,player.height)
        if pygame.sprite.spritecollideany(self,platformGroup) == None: # Makes the player fall when not on the ground
            self.inMidair = True
            self.jumping = True
        self.y -= 1
        self.rect = pygame.Rect(player.x,player.y,player.width,player.height)
        for i in walls: # x collision with walls
            if pygame.sprite.collide_rect(self,i) == True:
                if self.dx > 0:
                    self.x = self.oldX
                elif self.dx < 0:
                    self.x = self.oldX
        self.rect = pygame.Rect(player.x,player.y,player.width,player.height)
        for i in walls: # y collision with walls
            if pygame.sprite.collide_rect(self,i) == True:
                if dy > 0:
                    self.dy = 0
                    self.inMidair = False
                    self.jumping = False
                    self.y = i.rect.top - self.height
                elif dy < 0:
                    self.y = i.rect.bottom + 1
                    self.dy = 1
        if self.y < 0:
                self.y = 0
                self.dy = 1
        if self.y > screenHeight + 10: # Makes the player die when falling below the screen
            self.health = 0
        self.rect = pygame.Rect(player.x,player.y,player.width,player.height)
        if self.immuneTimer == 0: # Tests for enemy collision, but only when your immune timer has run out
            if pygame.sprite.spritecollide(self,bouncerGroup, False):
                self.health -= 5 # Reduces HP
                self.immuneTimer = 90 # Sets the immune timer so the player can not be hit more than once
            elif pygame.sprite.spritecollide(self,flyerGroup, False):
                self.health -= 5
                self.immuneTimer = 90
            elif pygame.sprite.spritecollide(self,rollerGroup, False):
                self.health -= 6
                self.immuneTimer = 90
            elif pygame.sprite.spritecollide(self,seekerGroup, False):
                self.health -= 6
                self.immuneTimer = 90
            elif pygame.sprite.spritecollide(self,enemyLaserGroup, False):
                if self.shielded == True: # If a bullet hits your shield, it will block it instead of hurting you
                    hits = pygame.sprite.spritecollide(self,enemyLaserGroup, False)
                    if self.shieldLV == 1:
                        self.shieldHealth -= 1
                        for i in hits:
                            i.delete()
                    elif self.shieldLV == 2:
                        self.health += 2
                        self.shieldHealth -= 1
                        for i in hits:
                            i.delete()
                    if self.shieldHealth < 1:
                        self.shielded = False
                elif self.shielded == False: # If you are not shielded, the bullet will hit you
                    self.health -= 5
                    self.immuneTimer = 90
        self.rect = pygame.Rect(player.x,player.y,player.width,player.height)
        if self.inMidair == True: # How gravity is applied to the character
            self.dy += 1
        elif self.inMidair == False: # makes sure the character does not move when on the ground
            self.dy = 0
        self.shootCount -= 1 # reduces the timer for the "shoot count"
        if self.shootCount < 0:
            self.shootCount = 0 # sets it back to 0 if it is below 0
        self.immuneTimer -= 1 # reduces the timer for the player's immune frames
        if self.immuneTimer < 0:
            self.immuneTimer = 0 # sets back to 0 if it is below 0
        if self.health > self.maxHealth: # Tests if variables are over their limit, and resets them if they are
            self.health = self.maxHealth
        if self.energy > self.maxEnergy:
            self.energy = self.maxEnergy
        if self.scrap > 999:
            self.scrap = 999
        player.rect = pygame.Rect(player.x,player.y,player.width,player.height)

    def draw(self): # Draws the player
        if self.jumping == True: # Jumping animation
            if self.shooting == False:
                if self.facingRight == True:
                    screen.blit(playerJumping,self.rect)
                elif self.facingLeft == True:
                    screen.blit(pygame.transform.flip(playerJumping,True,False),self.rect)
            elif self.shooting == True: # Jumping + Shooting animation
                if self.facingRight == True:
                    screen.blit(playerJumpingShooting,self.rect)
                elif self.facingLeft == True:
                    screen.blit(pygame.transform.flip(playerJumpingShooting,True,False),self.rect)
        elif self.jumping == False:
            if self.shooting == False: # Walking animation
                if self.movingLeft == True:
                    screen.blit(pygame.transform.flip(playerWalkingAnimation[self.walkCount//8],True,False),self.rect)
                    self.walkCount += 1
                elif self.movingRight == True:
                    screen.blit(playerWalkingAnimation[self.walkCount//8],self.rect)
                    self.walkCount += 1
                else:
                    if self.facingRight == True:
                        screen.blit(playerStanding,self.rect)
                    elif self.facingLeft == True:
                        screen.blit(pygame.transform.flip(playerStanding,True,False),self.rect)
            elif self.shooting == True: # Walking + Shooting animation
                if self.movingLeft == True:
                    screen.blit(pygame.transform.flip(playerShootingAnimation[self.walkCount//8],True,False),self.rect)
                    self.walkCount += 1
                elif self.movingRight == True:
                    screen.blit(playerShootingAnimation[self.walkCount//8],self.rect)
                    self.walkCount += 1
                else:
                    if self.facingRight == True:
                        screen.blit(playerStandingShooting,self.rect)
                    elif self.facingLeft == True:
                        screen.blit(pygame.transform.flip(playerStandingShooting,True,False),self.rect)

                    
class block(pygame.sprite.Sprite): # the class for the blocks (terrain)
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x,y,32,32)

class bullet(pygame.sprite.Sprite): # Class for the player's bullets
    def __init__(self,x,y,right,left):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        if right == True: # gives the bullet its x velocity for its respective direction
            self.dx = 10
        elif left == True:
            self.dx = -10
        self.rect = pygame.Rect(x,y,16,8)
        laserGroup.add(self) # adds itself to the laser group and list
        lasers.append(self)

    def update(self,walls,lasers): # Updates variables
        self.rect = pygame.Rect(self.x,self.y,16,8)
        self.x += self.dx
        self.rect = pygame.Rect(self.x,self.y,16,8)
        if self.x > screenWidth or self.x + 16 < 0: # removes itself if it passes the edges of the screen
            lasers.pop(lasers.index(self))
            laserGroup.remove(self)
        self.rect = pygame.Rect(self.x,self.y,16,8)
        hits = pygame.sprite.spritecollide(self,platformGroup, False) 
        if hits:# reomves itself if it collides with a wall
            lasers.pop(lasers.index(self))
            laserGroup.remove(self)
        self.rect = pygame.Rect(self.x,self.y,16,8)

    def delete(self): # Function to delete the laser
        lasers.pop(lasers.index(self))
        laserGroup.remove(self)

class grenade(pygame.sprite.Sprite): # Class for player grenades
    def __init__(self,x,y,right,left):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        if right == True:
            self.dx = 7
        elif left == True:
            self.dx = -7
        self.dy = -19
        self.rect =  pygame.Rect(self.x,self.y,36,36)
        grenades.append(self)
        grenadeGroup.add(self)

    def update(self): # Updates variables
        self.rect =  pygame.Rect(self.x,self.y,36,36)
        self.x += self.dx
        self.y += self.dy
        self.dy += 1
        self.rect =  pygame.Rect(self.x,self.y,36,36)
        hits = pygame.sprite.spritecollide(self,platformGroup, False)
        if hits:
            explode = explosion(self.x -122,self.y -122)
            grenades.pop(grenades.index(self))
            grenadeGroup.remove(self)

    def explode(self): # Makes the grande "explode", creating a sprite with the explosion class
        explode = explosion(self.x - 122,self.y - 122)
        grenades.pop(grenades.index(self))
        grenadeGroup.remove(self)

class explosion(pygame.sprite.Sprite): # Class used for grenade explosions
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.explosionTimer = 0
        self.rect = pygame.Rect(self.x,self.y,280,280)
        explosions.append(self)
        explosionGroup.add(self)

    def update(self): # Updates variables
        self.rect = pygame.Rect(self.x,self.y,280,280)
        self.explosionTimer += 1
        if player.grenadeLV == 1:
            if self.explosionTimer > 15: # Makes grenade dissappear after a certain time
                explosions.pop(explosions.index(self))
                explosionGroup.remove(self)
        elif player.grenadeLV == 2:
            if self.explosionTimer > 55:
                explosions.pop(explosions.index(self))
                explosionGroup.remove(self)

class sawblade(pygame.sprite.Sprite): # Class used for player sawblades
    def __init__(self,x,y,right,left):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        if right == True:
            if player.sawLV == 1:
                self.dx = 8
            elif player.sawLV == 2:
                self.dx = 13
        elif left == True:
            if player.sawLV == 1:
                self.dx = -8
            elif player.sawLV == 2:
                self.dx = -13
        self.rect =  pygame.Rect(self.x,self.y,60,60)
        sawbladeGroup.add(self)
        sawblades.append(self)

    def update(self): # Updates variables
        self.rect =  pygame.Rect(self.x,self.y,60,60)
        self.x += self.dx
        self.rect =  pygame.Rect(self.x,self.y,60,60)
        if self.x > screenWidth or self.x + 60 < 0:
            sawblades.pop(sawblades.index(self))
            sawbladeGroup.remove(self)


class spark(pygame.sprite.Sprite): # Class used for the player's sparks
    def __init__(self,x,y,dx,dy):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.rect = pygame.Rect(self.x,self.y,52,52)
        sparkGroup.add(self)
        sparks.append(self)

    def update(self): # Updates variables
        self.rect = pygame.Rect(self.x,self.y,52,52)
        self.x += self.dx
        self.y += self.dy
        self.rect = pygame.Rect(self.x,self.y,52,52)
        hits = pygame.sprite.spritecollide(self,platformGroup, False)
        if hits:
            self.delete()
        if self.x > screenWidth or self.x + 52 < 0:
            self.delete()
        elif self.y > screenHeight or self.y + 52 < 0:
            self.delete()

    def delete(self): # Deletes sparks
        sparks.pop(sparks.index(self))
        sparkGroup.remove(self)


class bouncer(pygame.sprite.Sprite): # Class for the "Bouncer" enemy
    def __init__(self,x,y,dx,dy):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.health = 3
        self.sawTimer = 0
        self.grenadeTimer = 0
        self.rect = pygame.Rect(self.x,self.y,64,32)
        bouncerGroup.add(self)
        bouncers.append(self)

    def update(self): # Updates variables
        self.rect = pygame.Rect(self.x,self.y,64,32)
        self.x += self.dx
        self.y += self.dy
        self.rect = pygame.Rect(self.x,self.y,64,32)
        bounce = pygame.sprite.spritecollide(self,platformGroup, False)
        if bounce:
            self.dx = - self.dx
            self.dy = - self.dy
        if self.x < 0 or self.x + 64 > screenWidth:
            self.dx = - self.dx
            self.dy = - self.dy
        if self.y < 0 or self.y + 32 > screenHeight:
            self.dx = - self.dx
            self.dy = - self.dy
        hit = pygame.sprite.spritecollide(self,laserGroup, False)
        if hit:
            self.health -= 1
            for i in hit:
                i.delete()
            if self.health < 1:
                bouncerGroup.remove(self)
                bouncers.pop(bouncers.index(self))
                player.scrap += 2
        hit = pygame.sprite.spritecollide(self,sawbladeGroup, False)
        if hit:
            if self.sawTimer == 0:
                if player.sawLV == 1:
                    self.health -= 1
                elif player.sawLV == 2:
                    self.health -= 2
                self.sawTimer = 60
                if self.health < 1:
                    bouncerGroup.remove(self)
                    bouncers.pop(bouncers.index(self))
                    player.scrap += 2
        self.sawTimer -= 1
        if self.sawTimer < 0:
            self.sawTimer = 0
        hit = pygame.sprite.spritecollide(self,sparkGroup, False)
        if hit:
            for i in hit:
                i.delete()
            self.health -= 1
            if player.sparkLV == 2:
                player.energy += 2
            if self.health < 1:
                    bouncerGroup.remove(self)
                    bouncers.pop(bouncers.index(self))
                    player.scrap += 2
        hit = pygame.sprite.spritecollide(self,grenadeGroup, False)
        if hit:
            for i in hit:
                i.explode()
        hit = pygame.sprite.spritecollide(self,explosionGroup, False)
        if hit:
            if self.grenadeTimer == 0:
                self.health -= 1
                self.grenadeTimer = 60
                if self.health < 1:
                    bouncerGroup.remove(self)
                    bouncers.pop(bouncers.index(self))
                    player.scrap += 2
        self.grenadeTimer -= 1
        if self.grenadeTimer < 0:
            self.grenadeTimer = 0
        self.rect = pygame.Rect(self.x,self.y,64,32)

        

class flyer(pygame.sprite.Sprite): # Class for the "flyer" enemy
    def __init__(self,x,y,d):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.health = 3
        self.shootTimer = 0
        self.shootDirection = d
        self.sawTimer = 0
        self.grenadeTimer = 0
        self.rect = pygame.Rect(self.x,self.y,32,64)
        flyerGroup.add(self)
        flyers.append(self)

    def update(self): # Updates variables
        self.rect = pygame.Rect(self.x,self.y,32,64)
        self.shootTimer -= 1
        if self.shootTimer < 0:
            self.shootTimer = 0
        if self.shootTimer == 0:
            enemyLaser = enemyBullet(self.x+10,self.y+32,self.shootDirection)
            self.shootTimer = 120
        hit = pygame.sprite.spritecollide(self,laserGroup, False)
        if hit:
            self.health -= 1
            for i in hit:
                i.delete()
            if self.health < 1:
                flyerGroup.remove(self)
                flyers.pop(flyers.index(self))
                player.scrap += 2
        hit = pygame.sprite.spritecollide(self,sawbladeGroup, False)
        if hit:
            if self.sawTimer == 0:
                if player.sawLV == 1:
                    self.health -= 1
                elif player.sawLV == 2:
                    self.health -= 2
                self.sawTimer = 60
                if self.health < 1:
                    flyerGroup.remove(self)
                    flyers.pop(flyers.index(self))
                    player.scrap += 2
        self.sawTimer -= 1
        if self.sawTimer < 0:
            self.sawTimer = 0
        hit = pygame.sprite.spritecollide(self,sparkGroup, False)
        if hit:
            for i in hit:
                i.delete()
            self.health -= 1
            if player.sparkLV == 2:
                player.energy += 2
            if self.health < 1:
                    flyerGroup.remove(self)
                    flyers.pop(flyers.index(self))
                    player.scrap += 2
        hit = pygame.sprite.spritecollide(self,grenadeGroup, False)
        if hit:
            for i in hit:
                i.explode()
        hit = pygame.sprite.spritecollide(self,explosionGroup, False)
        if hit:
            if self.grenadeTimer == 0:
                self.health -= 1
                self.grenadeTimer = 60
                if self.health < 1:
                    flyerGroup.remove(self)
                    flyers.pop(flyers.index(self))
                    player.scrap += 2
        self.grenadeTimer -= 1
        if self.grenadeTimer < 0:
            self.grenadeTimer = 0
        self.rect = pygame.Rect(self.x,self.y,32,64)

class roller(pygame.sprite.Sprite): # Class for the "Roller" enemy
    def __init__(self,x,y,dx):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.dx = dx
        self.health = 4
        self.sawTimer = 0
        self.grenadeTimer = 0
        self.rect = pygame.Rect(self.x,self.y,84,156)
        rollerGroup.add(self)
        rollers.append(self)

    def update(self): # Updates variables
        self.rect = pygame.Rect(self.x,self.y,84,156)
        self.x += self.dx
        self.rect = pygame.Rect(self.x,self.y,84,156)
        hit = pygame.sprite.spritecollide(self,platformGroup, False)
        if hit:
            self.dx = self.dx * -1
        self.y += 1
        self.rect = self.rect = pygame.Rect(self.x,self.y,84,156)
        if pygame.sprite.spritecollideany(self,platformGroup) == None:
            self.dx = self.dx * -1
        self.y -= 1
        self.rect = self.rect = pygame.Rect(self.x,self.y,84,156)
        if self.x < 0 or self.x + 84 > screenWidth:
            self.dx = self.dx * -1
        hit = pygame.sprite.spritecollide(self,laserGroup, False)
        if hit:
            self.health -= 1
            for i in hit:
                i.delete()
            if self.health < 1:
                rollerGroup.remove(self)
                rollers.pop(rollers.index(self))
                player.scrap += 3
        hit = pygame.sprite.spritecollide(self,sawbladeGroup, False)
        if hit:
            if self.sawTimer == 0:
                if player.sawLV == 1:
                    self.health -= 1
                elif player.sawLV == 2:
                    self.health -= 2
                self.sawTimer = 60
                if self.health < 1:
                    rollerGroup.remove(self)
                    rollers.pop(rollers.index(self))
                    player.scrap += 3
        self.sawTimer -= 1
        if self.sawTimer < 0:
            self.sawTimer = 0
        hit = pygame.sprite.spritecollide(self,sparkGroup, False)
        if hit:
            for i in hit:
                i.delete()
            self.health -= 1
            if player.sparkLV == 2:
                player.energy += 2
            if self.health < 1:
                    rollerGroup.remove(self)
                    rollers.pop(rollers.index(self))
                    player.scrap += 3
        hit = pygame.sprite.spritecollide(self,grenadeGroup, False)
        if hit:
            for i in hit:
                i.explode()
        hit = pygame.sprite.spritecollide(self,explosionGroup, False)
        if hit:
            if self.grenadeTimer == 0:
                self.health -= 1
                self.grenadeTimer = 60
                if self.health < 1:
                    rollerGroup.remove(self)
                    rollers.pop(rollers.index(self))
                    player.scrap += 3
        self.grenadeTimer -= 1
        if self.grenadeTimer < 0:
            self.grenadeTimer = 0
        self.rect = pygame.Rect(self.x,self.y,84,156)

    def draw(self): # Draws individual rollers, since they change the directions they face
        if self.dx < 0:
            screen.blit(pygame.transform.flip(rollerEnemy,True,False),self.rect)
        elif self.dx > 0:
            screen.blit(rollerEnemy,self.rect)

class seeker(pygame.sprite.Sprite): # Class for the "Seeker" enemy
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.health = 4
        self.moveTimer = 0
        self.sawTimer = 0
        self.grenadeTimer = 0
        self.rect = pygame.Rect(self.x,self.y,84,48)
        seekerGroup.add(self)
        seekers.append(self)

    def update(self): # Updates variables
        self.rect = pygame.Rect(self.x,self.y,84,48)
        if player.rect.centerx > self.rect.centerx:
            self.dx = 1
        elif player.rect.centerx < self.rect.centerx:
            self.dx = -1
        if player.rect.centery > self.rect.centery:
            self.dy = 1
        elif player.rect.centery < self.rect.centery:
            self.dy = -1
        self.x += self.dx
        if self.moveTimer == 0:
            self.y += self.dy
            self.moveTimer = 2
        self.moveTimer -= 1
        if self.moveTimer < 0:
            self.moveTimer = 0
        self.rect = pygame.Rect(self.x,self.y,84,48)
        hit = pygame.sprite.spritecollide(self,laserGroup, False)
        if hit:
            self.health -= 1
            for i in hit:
                i.delete()
            if self.health < 1:
                seekerGroup.remove(self)
                seekers.pop(seekers.index(self))
                player.scrap += 3
        hit = pygame.sprite.spritecollide(self,sawbladeGroup, False)
        if hit:
            if self.sawTimer == 0:
                if player.sawLV == 1:
                    self.health -= 1
                elif player.sawLV == 2:
                    self.health -= 2
                self.sawTimer = 60
                if self.health < 1:
                    seekerGroup.remove(self)
                    seekers.pop(seekers.index(self))
                    player.scrap += 3
        self.sawTimer -= 1
        if self.sawTimer < 0:
            self.sawTimer = 0
        hit = pygame.sprite.spritecollide(self,sparkGroup, False)
        if hit:
            for i in hit:
                i.delete()
            self.health -= 1
            if player.sparkLV == 2:
                player.energy += 2
            if self.health < 1:
                    seekerGroup.remove(self)
                    seekers.pop(seekers.index(self))
                    player.scrap += 3
        hit = pygame.sprite.spritecollide(self,grenadeGroup, False)
        if hit:
            for i in hit:
                i.explode()
        hit = pygame.sprite.spritecollide(self,explosionGroup, False)
        if hit:
            if self.grenadeTimer == 0:
                self.health -= 1
                self.grenadeTimer = 60
                if self.health < 1:
                    seekerGroup.remove(self)
                    seekers.pop(seekers.index(self))
                    player.scrap += 3
        self.grenadeTimer -= 1
        if self.grenadeTimer < 0:
            self.grenadeTimer = 0
        self.rect = pygame.Rect(self.x,self.y,84,48)

class enemyBullet(pygame.sprite.Sprite): # Class for the enemy bullet
    def __init__(self,x,y,d):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        if d == "U":
            self.dx = 0
            self.dy = -8
        elif d == "D":
            self.dx = 0
            self.dy = 8
        elif d == "R":
            self.dx = 8
            self.dy = 0
        elif d == "L":
            self.dx = -8
            self.dy = 0
        self.rect = pygame.Rect(self.x,self.y,12,12)
        enemyLaserGroup.add(self)
        enemyLasers.append(self)

    def update(self,walls,enemyLasers): # Updates variables
        self.rect = pygame.Rect(self.x,self.y,12,12)
        self.x += self.dx
        self.y += self.dy
        if self.x > screenWidth or self.x + 12 < 0:
            enemyLasers.pop(enemyLasers.index(self))
            enemyLaserGroup.remove(self)
        self.rect = pygame.Rect(self.x,self.y,12,12)
        if self.y > screenHeight or self.y + 12 < 0:
            enemyLasers.pop(enemyLasers.index(self))
            enemyLaserGroup.remove(self)
        hits = pygame.sprite.spritecollide(self,platformGroup, False)
        if hits:
            enemyLasers.pop(enemyLasers.index(self))
            enemyLaserGroup.remove(self)
        self.rect = pygame.Rect(self.x,self.y,12,12)

    def delete(self): # Function used to delete enemy bullets
        enemyLasers.pop(enemyLasers.index(self))
        enemyLaserGroup.remove(self)
        

platformGroup = pygame.sprite.Group() # Creates groups that contain all the sprites
playerGroup = pygame.sprite.Group()
laserGroup = pygame.sprite.Group()
grenadeGroup = pygame.sprite.Group()
explosionGroup = pygame.sprite.Group()
sawbladeGroup = pygame.sprite.Group()
sparkGroup = pygame.sprite.Group()
enemyLaserGroup = pygame.sprite.Group()
bouncerGroup = pygame.sprite.Group()
flyerGroup = pygame.sprite.Group()
rollerGroup = pygame.sprite.Group()
seekerGroup = pygame.sprite.Group()

lasers = [] # Creates lists that contain all instances of the classes
grenades = []
explosions = []
sawblades = []
sparks = []
enemyLasers = []
bouncers = []
flyers = []
rollers = []
seekers = []

flyerTimer = 0 # Timer to change the flyer's image

player = player(50,200,92,156) # Creates an instance of the player class

gadgetDisplay = pygame.Rect(894,20,56,56) # Display for the player gadget
immuneBarrier = pygame.Rect(player.x+10,player.y+20,72,116) # Rect for the player's immune shield

playerGroup.add(player) # Adds player to the player Group

clock = pygame.time.Clock()
FPS = 60

# Redraws the game screen
def redrawGameScreen():
    if roomNumber >= 0 and roomNumber <= 19:
        screen.fill(BLACK)
    elif roomNumber >= 20 and roomNumber <= 36:
        screen.fill(DARKGREEN)
    elif roomNumber >= 37:
        screen.fill(SKYBLUE)
    global walls
    pygame.sprite.Group.empty(platformGroup)
    walls = []
    blockX = 0
    blockY = 96
    for row in rooms[roomNumber]:
        for col in row:
            if col == "W":
                wall = block(blockX,blockY)
                platformGroup.add(wall)
                walls.append(wall)
            blockX += 32
        blockY += 32
        blockX = 0

    pygame.draw.rect(screen,BLACK,(0,0,screenWidth,96)) # Draws various things onto the screen
    screen.blit(healthIcon,(20,20))
    screen.blit(energyIcon,(320,20))
    screen.blit(scrapIcon,(620,20))
    healthText = statFont.render(str(player.health), True,pygame.Color("#ee0f0f"))
    energyText = statFont.render(str(player.energy), True,pygame.Color("#e7c711"))
    scrapText = statFont.render(str(player.scrap), True,pygame.Color("#989898"))
    screen.blit(healthText,(96,20))
    screen.blit(energyText,(388,20))
    screen.blit(scrapText,(688,20))
    pygame.draw.rect(screen,WHITE,(886,12,72,72),2)

    interactText = statFont.render("W",True,WHITE)
    interactWidth = interactText.get_width()
    interactHeight = interactText.get_height()

    for wall in walls: # Draws walls based on level
        if roomNumber >= 0 and roomNumber <= 19:
            screen.blit(level1Wall,wall)
        elif roomNumber >= 20 and roomNumber <= 36:
            screen.blit(level2Wall,wall)
        elif roomNumber >= 37:
            screen.blit(level3Wall,wall)

    if checkpointRoom == True: # Draws game elements and enemies
        screen.blit(checkpointImage,checkpoint)
    
    for bouncer in bouncers:
        screen.blit(bouncerEnemy,bouncer)

    for flyer in flyers: # Switches the flyer images so their propellers spin
        if flyerTimer <= 10:
            screen.blit(flyerEnemy,flyer)
        elif flyerTimer >= 11:
            screen.blit(pygame.transform.flip(flyerEnemy,True,False),flyer)

    for roller in rollers:
        roller.draw()

    for seeker in seekers:
        screen.blit(seekerEnemy,seeker)
    
    for laser in enemyLasers:
        screen.blit(enemyLaser,laser)

    for spark in sparks:
        screen.blit(sparkImage,spark)

    for saw in sawblades:
        screen.blit(sawbladeImage,saw)

    for grenade in grenades:
        screen.blit(grenadeImage,grenade)

    for explosion in explosions:
        screen.blit(explosionImage,explosion)

    if player.shielded == True:
        blit_alpha(screen,shield,(player.x - 20,player.y + 12,132,132),170)

    if player.walkCount +1 >= 32:
        player.walkCount = 0

    if player.gadgetSelection == 1:
        screen.blit(grenadeIcon,gadgetDisplay)
        if player.grenadeLV == 0:
            blit_alpha(screen,noneIcon,gadgetDisplay,255)
        elif player.grenadeLV == 1:
            if player.energy < 12:
                blit_alpha(screen,noneIcon,gadgetDisplay,255)
        elif player.grenadeLV == 2:
            if player.energy < 9:
                blit_alpha(screen,noneIcon,gadgetDisplay,255)    
    elif player.gadgetSelection == 2:
        screen.blit(shieldIcon,gadgetDisplay)
        if player.shieldLV == 0:
            blit_alpha(screen,noneIcon,gadgetDisplay,255)
        elif player.shieldLV > 0:
            if player.energy < 20:
                blit_alpha(screen,noneIcon,gadgetDisplay,255)
    elif player.gadgetSelection == 3:
        screen.blit(sawbladeIcon,gadgetDisplay)  
        if player.sawLV == 0:
            blit_alpha(screen,noneIcon,gadgetDisplay,255)
        elif player.sawLV > 0:
            if player.energy < 16:
                blit_alpha(screen,noneIcon,gadgetDisplay,255)
    elif player.gadgetSelection == 4:
        screen.blit(sparkIcon,gadgetDisplay)
        if player.sparkLV == 0:
            blit_alpha(screen,noneIcon,gadgetDisplay,255)
        elif player.sparkLV > 0:
            if player.energy < 16:
                blit_alpha(screen,noneIcon,gadgetDisplay,255)

    if checkpointRoom == True: # Shows prompt when colliding with checkpoint
        if player.rect.colliderect(checkpoint):
            pygame.draw.rect(screen,BLACK,(player.x,player.y - 100,92,92),0)
            pygame.draw.rect(screen,WHITE,(player.x,player.y - 100,92,92),4)
            screen.blit(interactText,(player.x+50-interactWidth/2,player.y - 50-interactHeight/2))
            
    
    player.draw() # Calls the draw player function
    
    for laser in lasers:
        screen.blit(playerLaser,laser)

    immuneBarrier = pygame.Rect(player.x+10,player.y+20,72,116)
    if player.immuneTimer > 0:
        blit_alpha(screen,immuneShield,immuneBarrier,100)

    pygame.display.flip()




### Loops ###

main = True # All of the loops for different parts of the game
startScreen = True
uploadProgressScreen = False
uploadSuccess = False
uploadFailed = False
informationScreen = False
game = False
pauseScreen = False
checkpointScreen = False
shopScreen = False
saveProgressScreen = False
saveSuccess = False
saveFailed = False
deathScreen = False
victoryScreen = False

while main == True: # Main loop


    
    while startScreen == True: # Start screen loop
        for event in pygame.event.get(): # Looks for events
            if event.type == pygame.QUIT: # Looks for if the game is exited
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN: # Looks for key input
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    buttonSelection += 1
                    if buttonSelection > 4:
                        buttonSelection = 1
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    buttonSelection -= 1
                    if buttonSelection < 1:
                        buttonSelection = 4
                elif event.key == pygame.K_RETURN: # Switches screens based on highlighted button
                    if buttonSelection == 1:
                        startScreen = False
                        game = True
                    elif buttonSelection == 2:
                        globalTextHeightDY = 0
                        globalTextHeight = 0
                        startScreen = False
                        informationScreen = True
                    elif buttonSelection == 3:
                        startScreen = False
                        uploadProgressScreen = True
                        fileButtonSelection = 1
                    elif buttonSelection == 4:
                        pygame.quit()
                        sys.exit()        
        redrawTitleScreen()
        clock.tick(FPS)



    while informationScreen == True: # Instructions Screen Loop
        for event in pygame.event.get(): # Looks for events
            if event.type == pygame.QUIT: # Looks for if the game is exited
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN: # Looks for key input
                if event.key == pygame.K_ESCAPE:
                    informationScreen = False
                    startScreen = True
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s: # moves all the info screen text up or down
                    globalTextHeightDY = -5
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    globalTextHeightDY = 5

            if event.type == pygame.KEYUP: # Looks for keys to be released
                if event.key == pygame.K_DOWN or event.key == pygame.K_s or event.key == pygame.K_UP or event.key == pygame.K_w:
                    globalTextHeightDY = 0
        globalTextHeight = globalTextHeight + globalTextHeightDY
        if globalTextHeight > 0:
            globalTextHeight = 0
        if globalTextHeight < -1800:
            globalTextHeight = -1800
        redrawInfoScreen()
        clock.tick(FPS)

    while uploadProgressScreen: # Loop for uploading progress
        for event in pygame.event.get(): # Looks for events
            if event.type == pygame.QUIT: # Looks for if the game is exited
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN: # Looks for key input
                if event.key == pygame.K_ESCAPE:
                    uploadProgressScreen = False
                    startScreen = True
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    fileButtonSelection -= 1
                    if fileButtonSelection < 1:
                        fileButtonSelection = 3
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    fileButtonSelection += 1
                    if fileButtonSelection > 3:
                        fileButtonSelection = 1
                elif event.key == pygame.K_RETURN:
                    if fileButtonSelection == 1: # Tries to open save files to read
                        try:
                            openFile = open("Saves/file1.TXT","r")
                            player.checkpoint = int(openFile.readline())
                            roomNumber = int(openFile.readline())
                            player.maxHealth = int(openFile.readline())
                            player.maxEnergy = int(openFile.readline())
                            player.scrap = int(openFile.readline())
                            player.grenadeLV = int(openFile.readline())
                            player.shieldLV = int(openFile.readline())
                            player.sawLV = int(openFile.readline())
                            player.sparkLV = int(openFile.readline())
                            openFile.close()
                            player.health = player.maxHealth
                            player.energy = player.maxEnergy
                            uploadProgressScreen = False
                            uploadSuccess = True
                        except Exception:
                            uploadProgressScreen = False
                            uploadFailed = True
                    elif fileButtonSelection == 2:
                        try:
                            openFile = open("Saves/file2.TXT","r")
                            player.checkpoint = int(openFile.readline())
                            roomNumber = int(openFile.readline())
                            player.maxHealth = int(openFile.readline())
                            player.maxEnergy = int(openFile.readline())
                            player.scrap = int(openFile.readline())
                            player.grenadeLV = int(openFile.readline())
                            player.shieldLV = int(openFile.readline())
                            player.sawLV = int(openFile.readline())
                            player.sparkLV = int(openFile.readline())
                            openFile.close()
                            player.health = player.maxHealth
                            player.energy = player.maxEnergy
                            uploadProgressScreen = False
                            uploadSuccess = True
                        except Exception:
                            uploadProgressScreen = False
                            uploadFailed = True
                    elif fileButtonSelection == 3:
                        try:
                            openFile = open("Saves/file3.TXT","r")
                            player.checkpoint = int(openFile.readline())
                            roomNumber = int(openFile.readline())
                            player.maxHealth = int(openFile.readline())
                            player.maxEnergy = int(openFile.readline())
                            player.scrap = int(openFile.readline())
                            player.grenadeLV = int(openFile.readline())
                            player.shieldLV = int(openFile.readline())
                            player.sawLV = int(openFile.readline())
                            player.sparkLV = int(openFile.readline())
                            openFile.close()
                            player.health = player.maxHealth
                            player.energy = player.maxEnergy
                            uploadProgressScreen = False
                            uploadSuccess = True
                        except Exception:
                            uploadProgressScreen = False
                            uploadFailed = True
        redrawFileScreen()
        clock.tick(FPS)

    while uploadSuccess == True: # loop if upload is successful
        for event in pygame.event.get(): # Looks for events
            if event.type == pygame.QUIT: # Looks for if the game is exited
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN: # Looks for key input
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    uploadSuccess = False
                    startScreen = True
        redrawFileResult()
        clock.tick(FPS)
        
    while uploadFailed == True: # loop if upload fails
        for event in pygame.event.get(): # Looks for events
            if event.type == pygame.QUIT: # Looks for if the game is exited
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN: # Looks for key input
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    uploadFailed = False
                    uploadProgressScreen = True
        redrawFileResult()
        clock.tick(FPS)
        
    
    while checkpointScreen == True: #Checkpoint screen loop
        for event in pygame.event.get(): # Looks for events
            if event.type == pygame.QUIT: # Looks for if the game is exited
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN: # Looks for key input
                if event.key == pygame.K_ESCAPE:
                    checkpointScreen = False
                    game = True
                    checkpointButtonSelection = 1
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    checkpointButtonSelection += 1
                    if checkpointButtonSelection > 4:
                        checkpointButtonSelection = 1
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    checkpointButtonSelection -= 1
                    if checkpointButtonSelection < 1:
                        checkpointButtonSelection = 4
                elif event.key == pygame.K_RETURN: # Switches screens based on highlighted button
                    if checkpointButtonSelection == 1:
                        player.health = player.maxHealth
                        player.energy = player.maxEnergy
                        checkpointScreen = False
                        game = True
                        checkpointButtonSelection = 1
                    elif checkpointButtonSelection == 2:
                        checkpointScreen = False
                        shopScreen = True
                    elif checkpointButtonSelection == 3:
                        checkpointScreen = False
                        saveProgressScreen = True
                        fileButtonSelection = 1
                    elif checkpointButtonSelection == 4:
                        checkpointScreen = False
                        game = True
                        checkpointButtonSelection = 1
        redrawCheckpointScreen()
        clock.tick(FPS)

    while shopScreen == True: # Shop screen loop
        for event in pygame.event.get(): # Looks for events
            if event.type == pygame.QUIT: # Looks for if the game is exited
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN: # Looks for key input
                if event.key == pygame.K_ESCAPE:
                    shopScreen = False
                    checkpointScreen = True
                    shopButtonSelection = 1
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    shopButtonSelection -= 1
                    if shopButtonSelection < 1:
                        shopButtonSelection = 6
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    shopButtonSelection += 1
                    if shopButtonSelection > 6:
                        shopButtonSelection = 1
                elif event.key == pygame.K_RETURN:
                    if shopButtonSelection == 1:
                        if player.grenadeLV == 0:
                            if player.scrap >= 25:
                                player.scrap -= 25
                                player.grenadeLV = 1
                        elif player.grenadeLV == 1:
                            if player.scrap >= 30:
                                player.scrap -= 30
                                player.grenadeLV = 2
                        else:
                            pass
                    elif shopButtonSelection == 2:
                        if player.shieldLV == 0:
                            if player.scrap >= 25:
                                player.scrap -= 25
                                player.shieldLV = 1
                        elif player.shieldLV == 1:
                            if player.scrap >= 30:
                                player.scrap -= 30
                                player.shieldLV = 2
                        else:
                            pass
                    elif shopButtonSelection == 3:
                        if player.sawLV == 0:
                            if player.scrap >= 25:
                                player.scrap -= 25
                                player.sawLV = 1
                        elif player.sawLV == 1:
                            if player.scrap >= 30:
                                player.scrap -= 30
                                player.sawLV = 2
                        else:
                            pass
                    elif shopButtonSelection == 4:
                        if player.sparkLV == 0:
                            if player.scrap >= 25:
                                player.scrap -= 25
                                player.sparkLV = 1
                        elif player.sparkLV == 1:
                            if player.scrap >= 30:
                                player.scrap -= 30
                                player.sparkLV = 2
                        else:
                            pass
                    elif shopButtonSelection == 5:
                        if player.maxHealth == 50:
                            if player.scrap >= 10:
                                player.scrap -= 10
                                player.maxHealth = 60
                                player.health = player.maxHealth
                        elif player.maxHealth == 60:
                            if player.scrap >= 15:
                                player.scrap -= 15
                                player.maxHealth = 70
                                player.health = player.maxHealth
                        elif player.maxHealth == 70:
                            if player.scrap >= 20:
                                player.scrap -= 20
                                player.maxHealth = 80
                                player.health = player.maxHealth
                        elif player.maxHealth == 80:
                            if player.scrap >= 25:
                                player.scrap -= 25
                                player.maxHealth = 90
                                player.health = player.maxHealth
                        elif player.maxHealth == 90:
                            if player.scrap >= 30:
                                player.scrap -= 30
                                player.maxHealth = 100
                                player.health = player.maxHealth
                        else:
                            pass
                    elif shopButtonSelection == 6:
                        if player.maxEnergy == 50:
                            if player.scrap >= 10:
                                player.scrap -= 10
                                player.maxEnergy = 60
                                player.energy = player.maxEnergy
                        elif player.maxEnergy == 60:
                            if player.scrap >= 15:
                                player.scrap -= 15
                                player.maxEnergy = 70
                                player.energy = player.maxEnergy
                        elif player.maxEnergy == 70:
                            if player.scrap >= 20:
                                player.scrap -= 20
                                player.maxEnergy = 80
                                player.energy = player.maxEnergy
                        elif player.maxEnergy == 80:
                            if player.scrap >= 25:
                                player.scrap -= 25
                                player.maxEnergy = 90
                                player.energy = player.maxEnergy
                        elif player.maxEnergy == 90:
                            if player.scrap >= 30:
                                player.scrap -= 30
                                player.maxEnergy = 100
                                player.energy = player.maxEnergy
                        else:
                            pass
                        
        redrawShopScreen()
        clock.tick(FPS)
        
    while saveProgressScreen == True: # Loop for saving progress
        for event in pygame.event.get(): # Looks for events
            if event.type == pygame.QUIT: # Looks for if the game is exited
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN: # Looks for key input
                if event.key == pygame.K_ESCAPE:
                    saveProgressScreen = False
                    checkpointScreen = True
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    fileButtonSelection -= 1
                    if fileButtonSelection < 1:
                        fileButtonSelection = 3
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    fileButtonSelection += 1
                    if fileButtonSelection > 3:
                        fileButtonSelection = 1
                elif event.key == pygame.K_RETURN:
                    if fileButtonSelection == 1:
                        try:
                            openFile = open("Saves/file1.TXT","w")
                            openFile.write(str(player.checkpoint) + "\n")
                            openFile.write(str(roomNumber) + "\n")
                            openFile.write(str(player.maxHealth) + "\n")
                            openFile.write(str(player.maxEnergy) + "\n")
                            openFile.write(str(player.scrap) + "\n")
                            openFile.write(str(player.grenadeLV) + "\n")
                            openFile.write(str(player.shieldLV) + "\n")
                            openFile.write(str(player.sawLV) + "\n")
                            openFile.write(str(player.sparkLV) + "\n")
                            openFile.close()
                            saveProgressScreen = False
                            saveSuccess = True
                        except Exception:
                            saveProgressScreen = False
                            saveFailed = True
                    elif fileButtonSelection == 2:
                        try:
                            openFile = open("Saves/file2.TXT","w")
                            openFile.write(str(player.checkpoint) + "\n")
                            openFile.write(str(roomNumber) + "\n")
                            openFile.write(str(player.maxHealth) + "\n")
                            openFile.write(str(player.maxEnergy) + "\n")
                            openFile.write(str(player.scrap) + "\n")
                            openFile.write(str(player.grenadeLV) + "\n")
                            openFile.write(str(player.shieldLV) + "\n")
                            openFile.write(str(player.sawLV) + "\n")
                            openFile.write(str(player.sparkLV) + "\n")
                            openFile.close()
                            saveProgressScreen = False
                            saveSuccess = True
                        except Exception:
                            saveProgressScreen = False
                            saveFailed = True
                    elif fileButtonSelection == 3:
                        try:
                            openFile = open("Saves/file3.TXT","w")
                            openFile.write(str(player.checkpoint) + "\n")
                            openFile.write(str(roomNumber) + "\n")
                            openFile.write(str(player.maxHealth) + "\n")
                            openFile.write(str(player.maxEnergy) + "\n")
                            openFile.write(str(player.scrap) + "\n")
                            openFile.write(str(player.grenadeLV) + "\n")
                            openFile.write(str(player.shieldLV) + "\n")
                            openFile.write(str(player.sawLV) + "\n")
                            openFile.write(str(player.sparkLV) + "\n")
                            openFile.close()
                            saveProgressScreen = False
                            saveSuccess = True
                        except Exception:
                            saveProgressScreen = False
                            saveFailed = True
        redrawFileScreen()
        clock.tick(FPS)

    while saveSuccess == True: # loop for when the save is successful
        for event in pygame.event.get(): # Looks for events
            if event.type == pygame.QUIT: # Looks for if the game is exited
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN: # Looks for key input
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    saveSuccess = False
                    checkpointScreen = True
        redrawFileResult()
        clock.tick(FPS)

    while saveFailed == True: # loop for if the save fails
        for event in pygame.event.get(): # Looks for events
            if event.type == pygame.QUIT: # Looks for if the game is exited
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN: # Looks for key input
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    saveFailed = False
                    saveProgressScreen = True
        redrawFileResult()
        clock.tick(FPS)
        
    while game == True: # Main Game Loop
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a: # Moves Left
                        player.dx = -4
                        player.movingLeft = True
                        player.movingRight = False
                        player.facingLeft = True
                        player.facingRight = False
                    elif event.key == pygame.K_d: # Moves Right
                        player.dx = 4
                        player.movingRight = True
                        player.movingLeft = False
                        player.facingRight = True
                        player.facingLeft = False
                    elif event.key == pygame.K_j: # How the player jumps
                        if player.jumping == False and player.inMidair == False: # tests if the player is already in midair or not
                            player.dy = -23
                            player.jumping = True
                            player.inMidair = True
                    elif event.key == pygame.K_k:
                        player.shooting = True
                    elif event.key == pygame.K_l:
                        if player.gadgetSelection == 1:
                            if player.grenadeLV == 1:
                                if player.energy >= 12:
                                    gren = grenade(player.x+28,player.y+60,player.facingRight,player.facingLeft)
                                    player.energy -= 12
                            elif player.grenadeLV == 2:
                                if player.energy >= 9:
                                    gren = grenade(player.x+28,player.y+60,player.facingRight,player.facingLeft)
                                    player.energy -= 9
                            else:
                                pass
                        elif player.gadgetSelection == 2:
                            if player.shieldLV >= 1:
                                if player.energy >= 20:
                                    player.shielded = True
                                    player.energy -= 20
                                    if player.shieldLV == 1:
                                        player.shieldHealth = 2
                                    elif player.shieldLV == 2:
                                        player.shieldHealth = 3
                        elif player.gadgetSelection == 3:
                            if player.sawLV > 0:
                                if player.energy >= 16:
                                    saw = sawblade(player.x + 16,player.y + 48,player.facingRight,player.facingLeft)
                                    player.energy -= 16
                        elif player.gadgetSelection == 4:
                            if player.sparkLV > 0:
                                if player.energy >= 16:
                                    spark1 = spark(player.x+20,player.y+52,6,0)
                                    spark2 = spark(player.x+20,player.y+52,-6,0)
                                    spark3 = spark(player.x+20,player.y+52,0,6)
                                    spark4 = spark(player.x+20,player.y+52,0,-6)
                                    if player.sparkLV == 2:
                                        spark5 = spark(player.x+20,player.y+52,4,4)
                                        spark6 = spark(player.x+20,player.y+52,4,-4)
                                        spark7 = spark(player.x+20,player.y+52,-4,4)
                                        spark8 = spark(player.x+20,player.y+52,-4,-4)
                                    player.energy -= 16
                                    
                    elif event.key == pygame.K_q:
                        player.gadgetSelection -= 1
                        if player.gadgetSelection < 1:
                            player.gadgetSelection = 4
                    elif event.key == pygame.K_e:
                        player.gadgetSelection += 1
                        if player.gadgetSelection > 4:
                            player.gadgetSelection = 1
                    elif event.key == pygame.K_w:
                        if checkpointRoom == True:
                            if player.rect.colliderect(checkpoint):
                                game = False
                                checkpointScreen = True
                                player.movingRight = False
                                player.movingLeft = False
                                player.walkCount = 0
                                player.dx = 0

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        player.movingRight = False
                        player.movingLeft = False
                        player.walkCount = 0
                        player.dx = 0
                    elif event.key == pygame.K_k:
                        player.shooting = False
        flyerGroup.update()
        bouncerGroup.update()
        rollerGroup.update()
        seekerGroup.update()
        enemyLaserGroup.update(walls,enemyLasers)
        sawbladeGroup.update()
        sparkGroup.update()
        grenadeGroup.update()
        explosionGroup.update()
        player.update(player.x,player.y,player.dx,player.dy,player.width,player.height,walls)
        laserGroup.update(walls,lasers)
        if roomNumber == 10 or roomNumber == 20 or roomNumber == 30:
            checkpoint = pygame.Rect(552,320,176,352)
            checkpointRoom = True
        if player.shootCount == 0 and player.shooting == True:
            player.shootCount = 35
            laser = bullet(player.rect.centerx - 8,player.rect.centery - 10,player.facingRight,player.facingLeft)
        if player.x > screenWidth: # Changes rooms 
            player.x = player.x - screenWidth
            roomNumber += 1 # Goes to the next room
            laserGroup.empty() # Removes all instances of enemies, lasers, etc
            lasers = []
            grenadeGroup.empty()
            grenades = []
            explosionGroup.empty()
            explosions = []
            sawbladeGroup.empty()
            sawblades = []
            sparkGroup.empty()
            sparks = []
            enemyLaserGroup.empty()
            enemyLasers = []
            bouncerGroup.empty()
            bouncers = []
            flyerGroup.empty()
            flyers = []
            rollerGroup.empty()
            rollers = []
            seekerGroup.empty()
            seekers = []
            checkpointRoom = False
            if roomNumber == 1: # Spawns enemies based on the room you enter
                bouncer1 = bouncer(128,192,0,3)
                bouncer2 = bouncer(1088,192,0,3)
            elif roomNumber == 2:
                flyer1 = flyer(128,256,"R")
            elif roomNumber == 3:
                flyer1 = flyer(304,160,"D")
                flyer2 = flyer(624,160,"D")
                flyer3 = flyer(944,160,"D")
            elif roomNumber == 4:
                bouncer1 = bouncer(32,352,3,0)
                bouncer2 = bouncer(672,352,3,0)
            elif roomNumber == 5:
                flyer1 = flyer(1216,320,"L")
            elif roomNumber == 6:
                flyer1 = flyer(1216,480,"L")
                bouncer1 = bouncer(672,128,0,3)
                bouncer2 = bouncer(832,128,0,3)
                bouncer3 = bouncer(992,128,0,3)
            elif roomNumber == 7:
                bouncer1 = bouncer(512,128,0,3)
                bouncer2 = bouncer(992,128,0,3)
            elif roomNumber == 8:
                flyer1 = flyer(1248,576,"L")
                flyer2 = flyer(1248,512,"L")
            elif roomNumber == 9:
                bouncer1 = bouncer(32,96,3,0)
            elif roomNumber == 10:
                player.checkpoint = 1
            elif roomNumber == 11:
                bouncer1 = bouncer(288,416,0,3)
                bouncer2 = bouncer(928,416,0,3)
                flyer1 = flyer(608,256,"U")
            elif roomNumber == 12:
                bouncer1 = bouncer(544,672,0,3)
                bouncer2 = bouncer(672,672,0,3)
                bouncer3 = bouncer(604,128,0,3)
            elif roomNumber == 13:
                pass
            elif roomNumber == 14:
                flyer1 = flyer(96,352,"U")
                flyer2 = flyer(224,352,"U")
                flyer3 = flyer(352,352,"U")
                flyer4 = flyer(480,352,"U")
                flyer5 = flyer(608,352,"U")
                flyer6 = flyer(736,352,"U")
                flyer7 = flyer(864,352,"U")
            elif roomNumber == 15:
                flyer1 = flyer(1248,576,"L")
            elif roomNumber == 16:
                flyer1 = flyer(1216,480,"L")
                flyer2 = flyer(704,544,"L")
                bouncer1 = bouncer(384,128,0,3)
                bouncer2 = bouncer(896,128,0,3)
            elif roomNumber == 17:
                flyer1 = flyer(32,224,"R")
                flyer2 = flyer(864,480,"R")
            elif roomNumber == 18:
                bouncer1 = bouncer(160,640,0,3)
                bouncer2 = bouncer(320,640,0,3)
                bouncer3 = bouncer(480,640,0,3)
            elif roomNumber == 19:
                flyer1 = flyer(128,256,"D")
                flyer2 = flyer(160,256,"D")
                flyer3 = flyer(1088,256,"D")
                flyer4 = flyer(1120,256,"D")
            elif roomNumber == 20:
                player.checkpoint = 2
            elif roomNumber == 21:
                roller1 = roller(352,516,3)
            elif roomNumber == 22:
                seeker1 = seeker(1000,516)
            elif roomNumber == 23:
                seeker1 = seeker(1000,96)
                seeker2 = seeker(1100,96)
            elif roomNumber == 24:
                flyer1 = flyer(288,576,"U")
                flyer2 = flyer(544,576,"U")
                flyer3 = flyer(800,576,"U")               
            elif roomNumber == 25:
                roller1 = roller(928,516,-3)
                seeker1 = seeker(1000,516)
            elif roomNumber == 26:
                seeker1 = seeker(32,32)
                seeker2 = seeker(1100,32)
                seeker3 = seeker(1100,608)
            elif roomNumber == 27:
                roller1 = roller(928,516,-3)
                roller2 = roller(416,516,3)
                roller3 = roller(672,292,-3)
            elif roomNumber == 28:
                pass
            elif roomNumber == 29:
                bouncer1 = bouncer(32,480,3,0)
                bouncer2 = bouncer(32,576,3,0)
                seeker1 = seeker(1100,384)
            elif roomNumber == 30:
                player.checkpoint = 3
            elif roomNumber == 31:
                flyer1 = flyer(1248,384,"L")
                flyer2 = flyer(1248,320,"L")
            elif roomNumber == 32:
                flyer1 = flyer(1248,384,"L")
                flyer2 = flyer(1248,320,"L")
                seeker1 = seeker(1000,96)
            elif roomNumber == 33:
                roller1 = roller(928,388,-3)
                roller2 = roller(416,388,3)
            elif roomNumber == 34:
                bouncer1 = bouncer(672,128,0,3)
                bouncer2 = bouncer(832,128,0,3)
                bouncer3 = bouncer(992,128,0,3)
                seeker1 = seeker(1000,96)
            elif roomNumber == 35:
                pass
            elif roomNumber == 36:
                roller1 = roller(928,388,-3)
                roller2 = roller(416,388,3)
                seeker1 = seeker(0,-50)
                seeker2 = seeker(100,-50)
                seeker3 = seeker(200,-50)
                seeker4 = seeker(300,-50)
                seeker5 = seeker(400,-50)
                seeker6 = seeker(500,-50)
                seeker7 = seeker(600,-50)
                seeker8 = seeker(700,-50)
                seeker9 = seeker(800,-50)
                seeker10 = seeker(900,-50)
                seeker11 = seeker(1000,-50)
                seeker12 = seeker(1100,-50)
                seeker13 = seeker(1200,-50)
            elif roomNumber == 37:
                pass
            elif roomNumber == 38:
                pass
            elif roomNumber == 39:
                pass
            elif roomNumber == 40:
                game = False
                victoryScreen = True
        if player.x < 0:
            player.x = 0
        player.oldY = player.y
        player.oldX = player.x
        flyerTimer -= 1
        if flyerTimer < 0:
            flyerTimer = 20
        if player.health <= 0: # Goes to death screen loop if player health is 0
            game = False
            deathScreen = True
        redrawGameScreen()
        clock.tick(FPS)
        
    while deathScreen == True: # Death screen loop
        redrawDeathScreen()
        for event in pygame.event.get(): # Looks for events
            if event.type == pygame.QUIT: # Looks for if the game is exited
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN: # Looks for key input
                if event.key == pygame.K_RETURN: # When enter is pressed, all enemies are removed and room is reset
                    player.health = player.maxHealth
                    player.energy = player.maxEnergy
                    player.scrap = player.scrap - int(player.scrap/2)
                    if player.checkpoint == 0:
                        roomNumber = 0
                    elif player.checkpoint == 1:
                        roomNumber = 10
                    elif player.checkpoint == 2:
                        roomNumber = 20
                    elif player.checkpoint == 3:
                        roomNumber = 30
                    player.x = 544
                    player.y = 384
                    player.movingRight = False
                    player.movingLeft = False
                    player.walkCount = 0
                    player.dx = 0
                    player.dy = 1
                    laserGroup.empty()
                    lasers = []
                    grenadeGroup.empty()
                    grenades = []
                    explosionGroup.empty()
                    explosions = []
                    sawbladeGroup.empty()
                    sawblades = []
                    sparkGroup.empty()
                    sparks = []
                    enemyLaserGroup.empty()
                    enemyLasers = []
                    bouncerGroup.empty()
                    bouncers = []
                    flyerGroup.empty()
                    flyers = []
                    rollerGroup.empty()
                    rollers = []
                    seekerGroup.empty()
                    seekers = []
                    deathScreen = False
                    game = True
        clock.tick(FPS)


    while victoryScreen == True: # Victory Screen Loop
        redrawVictoryScreen()
        for event in pygame.event.get(): # Looks for events
            if event.type == pygame.QUIT: # Looks for if the game is exited
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN: # Looks for key input
                if event.key == pygame.K_RETURN: # Returns you to the title screen
                    victoryScreen = False
                    startScreen = True
                    player.checkpoint = 0
                    roomNumber = 0
                    player.x = 600
                    player.y = 400
                    player.movingRight = False
                    player.movingLeft = False
                    player.walkCount = 0
                    player.dx = 0
                    player.health = player.maxHealth
                    player.energy = player.maxEnergy
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

pygame.quit()
sys.exit()
