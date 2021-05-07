import pygame as pg
#import pygame to make a simple breakout atari game

from random import randrange,choice,randint
#import 3 functions from random module to make the game more fun

import const,var,myRect
#import constant, variables adn classes from other files

def hideMouse():

    """Function that hide the cursor of the mouse"""

    pg.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
    #make the cursor of the mouse invisibl 

def createBlocks():

    """Function that create the blocks"""

    #try to create a random number of blocks
    for _ in range(randint(var.minBlocks,2*var.minBlocks)):
        rectangle=myRect.MyRect(pg.Rect(randrange(15,1890,135),randrange(105,855,15),135,15),choice(const.colors))
        #make a block

        exist=False
        #initialise the exist variable to false

        #pass the entire list with blocks
        for block in var.blockList:
            if rectangle.rect.x==block.rect.x and rectangle.rect.y==block.rect.y:
                exist=True
                break
            #if a block with same coordinates as new block exist,
            #set the exist to true and break the loop

        if not exist: var.blockList.append(rectangle)
        #if the block is unique, append it to the list with blocks

def makeNewWave():

    """Function that make a new wave for the game"""

    return (45,var.minBlocks+5) if var.fps==45 else (var.fps+1,var.minBlocks+5)
    #return the fps of 45 and more five blocks
    #if the fps already touch the limit
    #else return one more fps and more five blocks

def resetPlayerAndBall():

    """Function that reset the player and the ball"""

    var.player=pg.Rect(890,1065,140,15)
    #set the player to the initial position

    var.ball=pg.Rect(955,1055,10,10)
    #set the ball to the initial position

def resetGame():

    """Function that reset the stats of the game"""

    var.blockList.clear()
    #clear all the blocks

    return (3,0,10,10,resetMove())
    #return 3 lives, 0 score, 10 fps, 10 minimum blocks and a null move

def resetMove():

    """Function that reset the move"""

    return ""
    #return an empty string to reset the move

def movePlayer(direction):

    """Function that move the player in the given direction"""

    if direction==0: var.player.x-=25
    elif direction==1: var.player.x+=25
    #if the given direction is 0, move the player 25 pixels to the left
    #else move the player 25 pixels to the right

def prepareScreen(text):

    """Function that prepare the screen for the game"""

    const.screen.fill((0,0,0))
    #set the screen to black color

    drawBorder()
    #draw the border

    const.screen.blit(text,(15,15))
    #print the text with remaining lives, score and best score

    pg.draw.rect(const.screen,(255,255,255),var.player)
    #draw the player

    pg.draw.rect(const.screen,(255,255,255),var.ball)
    #draw the ball

    drawBlocks()
    #draq the blocks

def drawBorder():

    """Function that draw the border to the screen"""

    pg.draw.rect(const.screen,(255,255,255),pg.Rect(0,0,15,1080))
    #draw the left border

    pg.draw.rect(const.screen,(255,255,255),pg.Rect(1905,0,15,1080))
    #draw the right border

    pg.draw.rect(const.screen,(255,255,255),pg.Rect(15,0,1890,15))
    #draw the first top border

    pg.draw.rect(const.screen,(255,255,255),pg.Rect(15,90,1890,15))
    #draw the second top border

def drawBlocks():

    """Function that draw all the blocks"""

    for block in var.blockList:
        pg.draw.rect(const.screen,block.color,block.rect)
    #pass the entire list with blocks and draw every block

def selectMove():

    """Function that select the move"""

    if var.move=="linear": linearMove()
    elif var.move=="leftUp": leftUpMove()
    elif var.move=="rightUp": rightUpMove()
    elif var.move=="leftDown": leftDownMove()
    elif var.move=="rightDown": rightDownMove()
    #select the correct function for the move

def linearMove():

    """Function for linear move"""

    var.ball.y-=5
    #decrease y 5 pixels to go up

def leftUpMove():

    """Function for leftUp move"""

    var.ball.x-=5
    #decrease x 5 pixels to go left

    var.ball.y-=5
    #decrease y 5 pixels to go up

def rightUpMove():

    """Function for rightUp move"""

    var.ball.x+=5
    #increase x 5 pixels to go right

    var.ball.y-=5
    #decrease y 5 pixels to go up

def leftDownMove():

    """Function for leftDown move"""

    var.ball.x-=5
    #decrease x 5 pixels to go left

    var.ball.y+=5
    #increase y 5 pixels to go down

def rightDownMove():

    """Function for rightDown move"""

    var.ball.x+=5
    #increase x 5 pixels to go right

    var.ball.y+=5
    #increase y 5 pixels to go down

def playSound():

    """Function that play a sound"""

    pg.mixer.music.load("sound.wav")
    #load the music sound

    pg.mixer.music.play(1)
    #and play it once

def setRandomMove(typeOfRandomMove):

    """Function that set a random move"""

    if typeOfRandomMove==0:
        typeOfMove=randint(0,3)
        if typeOfMove==0: return "leftUp"
        elif typeOfMove==1: return "rightUp"
        elif typeOfMove==2: return "leftDown"
        elif typeOfMove==3: return "rightDown"
    elif typeOfRandomMove==1:
        typeOfMove=randint(0,2)
        if typeOfMove==0: return "leftUp"
        elif typeOfMove==1: return "rightUp"
        elif typeOfMove==2: return "linear"
    elif typeOfRandomMove==2:
        typeOfMove=randint(0,1)
        if typeOfMove==0: return "leftDown"
        else: return "rightDown"
    #move will become a random move depending on type of the random move
    #you know what i'm saying, don't need to explain every if

def calculateBest():

    """Function that calculate the best score"""

    if var.score>var.best:
        setNewBest()
        return var.score
    else: return var.best
    #if the actual score is bigger than the best score
    #set the best score to the actual score

def setNewBest():

    """Function that save the best score"""

    with open("bestscore.txt","w") as f:
        f.write(str(var.best+1))
    #open the file and write best score plus one
    #why plus one? good question
    #when this function is called the score isn't updated yet
    #and you need to set the best score to best plus one

def collisionWithBorder():

    """Function that check for a collision with the border"""

    if var.ball.y==100: return switchWay(),var.lives
    #if the ball collide with the top border change the way
    elif var.ball.x==15 or var.ball.x==1895: return switchDirection(),var.lives
    #if the ball collide with the marginal border change the direction
    elif var.ball.y==1090:
        #if the ball is gone

        resetPlayerAndBall()
        #reset player and the ball

        return resetMove(),var.lives-1
        #and reset the move and decrease a live
    else: return var.move,var.lives
    #if nothing happened only return the actual move and the actual no. of lives

def switchWay():

    """Function that change the way of the ball"""

    if var.move=="leftUp": return "leftDown"
    elif var.move=="rightUp": return "rightDown"
    elif var.move=="linear": return setRandomMove(2)
    #change the way of the ball to the opposite way

def switchDirection():

    """Function that change the direction of the ball"""

    if var.move=="leftUp": return "rightUp"
    elif var.move=="leftDown": return "rightDown"
    elif var.move=="rightUp": return "leftUp"
    elif var.move=="rightDown": return "leftDown"
    #change the direction of the ball to the opposite direction

def showMessage(win):

    """Function that show a message tot he screen"""

    if win:
        finalMessage=const.font.render("You win!",True,(255,255,255))
        #if is a win set the winning message

        text_rect=finalMessage.get_rect(center=const.screen.get_rect().center)
        #center the message

        const.screen.blit(finalMessage,text_rect)
        #and display the message
    else:
        finalMessage=const.font.render("Game Over!",True,(255,255,255))
        #if is a win set the lossing message

        text_rect=finalMessage.get_rect(center=const.screen.get_rect().center)
        #center the message

        const.screen.blit(finalMessage,text_rect)
        #and display the message