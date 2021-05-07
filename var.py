import pygame as pg
#import pygame to make a simple breakout atari game

lives=3
#initialise life to 3

score=0
#initialise score to 0

move=""
#initialise move to an empty string

running=True
#initialise running with true

fps=10
#initialise fps to 10

minBlocks=10
#initialise minimum of blocks to 10

win=False
#initialise win to false

blockList=[]
#initialise the list with the blocks with an empty list

player=pg.Rect(890,1065,140,15)
ball=pg.Rect(955,1055,10,10)
#initialise player and ball to the initial positions

with open("bestscore.txt","r") as f:
    best=int(f.read())
#set best to the current best