import pygame as pg
#import pygame to make a simple breakout atari game

import const,var,func
#import constant, variables and functions from other files

func.hideMouse()
#hide the mouse

func.createBlocks()
#create the blocks of breakout game

#run until player want to close the game
while var.running:
    const.clock.tick(var.fps)
    #make the loop to run on given fps

    #check all the events
    for event in pg.event.get():
        #if a key is pressed
        if event.type==pg.KEYDOWN:
            #if the ESC key is pressed close the game
            if event.key==pg.K_ESCAPE: var.running=False
            #if the spacebar is pressed launch the ball or restart the game
            elif event.key==pg.K_SPACE:
                #if game isn't finished lauch the ball if the ball isn't moving
                if len(var.blockList)!=0: 
                    if var.move=="": var.move="linear"
                else:
                    #if is a win

                    var.fps,var.minBlocks=func.makeNewWave()
                    #increase the stats for the new wave

                    func.resetPlayerAndBall()
                    #reset player and the ball

                    func.createBlocks()
                    #create the new blocks
                if var.lives==0:
                    #if is a lose

                    var.lives,var.score,var.fps,var.minBlocks,var.move=func.resetGame()
                    #reset all stats of the game

                    func.createBlocks()
                    #create the new blocks
            #if the game isn't finished and the player press left arrow key or
            #A key
            elif (event.key==pg.K_LEFT or event.key==pg.K_a) and var.player.x!=15 and var.lives!=0 and len(var.blockList)!=0:
                func.movePlayer(0)
                #move the player to the left

                if var.move=="": var.move="leftUp"
                #if is the first move make the ball to go left
            #if the game isn't finished and the player press right arrow key or
            #D key
            elif (event.key==pg.K_RIGHT or event.key==pg.K_d) and var.player.x!=1765 and var.lives!=0 and len(var.blockList)!=0:
                func.movePlayer(1)
                #move the player to the right

                if var.move=="": var.move="rightUp"
                #if is the first move make the ball to go left

    text=const.font.render(f"Lives: {var.lives}{const.spaces}Score: {var.score*100}{const.spaces}Best: {var.best*100}",True,(255,255,255))
    #make the text white and make the text to contain the remaining lives,
    #the score and the best score

    func.prepareScreen(text)
    #prepare screen for the game

    func.selectMove()
    #select the move of the ball

    #check all the blocks
    for block in var.blockList:
        if var.ball.colliderect(block):
            #if the ball collide with a block

            var.blockList.remove(block)
            #remove the block

            func.playSound()
            #play the sound

            var.move=func.setRandomMove(0)
            #get a new move of type 0

            var.score+=1
            #increase the score

            var.best=func.calculateBest()
            #and calculate the new best

    if var.ball.colliderect(var.player):
        #if the ball collide with the player

        var.move=func.setRandomMove(1)
        #get a new move of type 1

    var.move,var.lives=func.collisionWithBorder()
    #check if the ball collide with the border,
    #if the ball collide with the border update the move and the remaining lives

    if var.lives==0:
        func.showMessage(False)
        #show the game over message if the the game is over
    elif len(var.blockList)==0:
        func.showMessage(True)
        #show the winning message if the player win the game

    pg.display.flip()
    #update the screen
    #documentation says display.flip() is much faster than display.update()
    #if you wonder why i'm not using display.update()

pg.quit()
#quit the game and end the program