import random as rd
import sys, pygame

#init & parameters
pygame.init()

size = width, height = 800, 600
dspeed = [0,6]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

#creat number of drops and type
fdrop = [1] * 40 #foreground
fdroprect = [1] * 40

bdrop = [1] * 150 #background
bdroprect = [1] * 150

mdrop = [1] * 80 #middle
mdroprect = [1] * 80

def assign_drop(drop,droprect,image): #assigns all drops of one type to their image and hitbox
    for i in range(len(drop)):  #give each element in the list the drop image and hitbox
        drop[i] = pygame.image.load(image)
        droprect[i] = drop[i].get_rect()

assign_drop(fdrop,fdroprect,"fdrop.png")
assign_drop(bdrop,bdroprect,"bdrop.png")
assign_drop(mdrop,mdroprect,"mdrop.png")


def animate_drop(dspeed,drop,droprect,ground): #animates all drops of one type
    for i in range(len(drop)): #give each drop movement orders
        droprect[i] = droprect[i].move(dspeed)
        if droprect[i].top > ground:   #move drop to top of screen
            droprect[i].center=(rd.randrange(0,800),rd.randrange(-350,1)) 

def display_drop(drop,droprect):    #displays all drops of one type
    for i in range(len(drop)): #display each drop
        screen.blit(drop[i], droprect[i])

def place_drop(dspeed,drop,droprect,ground): #animates all drops of one type
    for i in range(len(drop)): #give each drop movement orders
        droprect[i] = droprect[i].move(dspeed)
        
        droprect[i].center=(rd.randrange(0,800),rd.randrange(-350,1))
            
place_drop([0,6],fdrop,fdroprect,800)
place_drop([0,4],mdrop,mdroprect,700)
place_drop([0,2],bdrop,bdroprect,600)
    
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    animate_drop([0,6],fdrop,fdroprect,800)
    animate_drop([0,4],mdrop,mdroprect,700)
    animate_drop([0,2],bdrop,bdroprect,600)

    screen.fill((26, 16, 71)) #color background

    display_drop(fdrop,fdroprect)
    display_drop(bdrop,bdroprect)
    display_drop(mdrop,mdroprect)

    pygame.display.flip()


