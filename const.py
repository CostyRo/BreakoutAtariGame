import pygame as pg
#import pygame to make a simple breakout atari game

pg.init()
#initialise pygame

screen=pg.display.set_mode((1920,1080))
#initialise window

pg.display.set_caption("Breakout")
#set the name of the window

clock=pg.time.Clock()
#initialise clock

font = pg.font.Font("freesansbold.ttf",75)
#initialise the font

spaces="            "
#a variable that store some spaces

colors=[(255,0,0),(0,255,0),(0,0,255),(173,216,230),(255,255,0),(255,165,0),(186,85,211),(255,105,180)]
#a list with colors:
#red, green, blue, light blue, yellow, purple and pink