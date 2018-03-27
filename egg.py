

import pygame
import time
import random

pygame.init()

black=(0,0,0)
block_color=(53,115,255)
white=(255,255,255)
red=(200,0,0)
green=(0,200,0)

bright_red=(255,0,0)
bright_green=(0,255,0)

basket_width=50
basket_h=54
egg_w=20
egg_h=27
green=(0,200,0)
display_width=800
display_height=600





pause=False






gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Eggs')
clock = pygame.time.Clock()
basketimg=pygame.image.load('N:\Project151219\b.jpg')
                        
eggimg = pygame.image.load('N:\Project151219\egg.png')

"""def col(x,y,w,h,x2,y2,w2,h2):
      
      if (x < (x2 + w2) and (x + w) > x2 and y < (y2 + h2) and (h + y) > y2):
            print 'j' """


def score(count):
      count=count+1
             
      count=count/3
      font = pygame.font.SysFont(None,25)
      text=font.render("Score:"+str(count),True,black)
      gameDisplay.blit(text,(0,0))



def egg(thingx,thingy,thing_width,thing_height):
      #pygame.draw.ellipse(gameDisplay,color,[thingx,thingy,thing_width,thing_height])
      #pygame.draw.ellipse(gameDisplay, red, [225, 10, 50, 20], 2) 
      lx=[]
      lx.append(thingx)
      jy=[]
      jy.append(thingy)
      gameDisplay.blit(eggimg,[thingx,thingy,thing_width,thing_height])
      return lx,jy
      
      
      # pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])
      
def basket(x,y):
      gameDisplay.blit(basketimg,(x,y))

def Text_objects(text,font):
      textSurface = font.render(text,True,black)
      return textSurface, textSurface.get_rect()


def message_display(text):
     
      largetext = pygame.font.Font('freesansbold.ttf',115)
      TextSurf,TextRect = Text_objects(text,largetext)
      TextRect.center = ((display_width/2),(display_height/2))
      gameDisplay.blit(TextSurf,TextRect)

      pygame.display.update()

      time.sleep(2)

      game_loop()

      
def crash():
      message_display('Game Over')
            
           
            
           

def button(msg,x,y,w,h,ic,ac,action =None):
                  mouse = pygame.mouse.get_pos() 
                  click = pygame.mouse.get_pressed()
                  #print (click)

                  if x+w> mouse[0]>x and y+h> mouse[1]>y:
                        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
                        if click[0] == 1 and action != None:
                              if action == "play":
                                    game_loop()
                              elif action == "quit":
                                    pygame.quit()
                                    quit()


                  else:
                        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))


                  smallText = pygame.font.Font("freesansbold.ttf",20)
                  textSurf,textRect = Text_objects(msg,smallText)
                  textRect.center = ((x+(w/2)),(y+(h/2)))
                  gameDisplay.blit(textSurf,textRect)
                        
            
            
         

def unpause():
      global pause
      pause = False
      

def paused():
            pause = True
            

            while pause:
                  for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                              pygame.quit()
                              quit()
                  gameDisplay.fill(white)
                  largetext = pygame.font.SysFont('comicsansms',115)
                  TextSurf,TextRect = Text_objects("Paused",largetext)   
                  TextRect.center = ((display_width/2),(display_height/2))
                  gameDisplay.blit(TextSurf,TextRect)
                  button("Continue",150,450,100,50,green,bright_green,"play")
                  button("Quit",550,450,100,50,red,bright_red,"quit")

                  pygame.display.update()
                  clock.tick(15)
                              
            
           
            
            
def quitgame():
      pygame.quit()
      quit()


def game_intro():
      intro=True

      while intro:
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        quit()
            gameDisplay.fill(white)
            myfont = pygame.font.Font('freesansbold.ttf', 30)
            f=pygame.font.Font('freesansbold.ttf', 30)
            label = myfont.render("Ahetesham Mansuri", 50, (255,69,0))
            l = f.render("151219", 50, (255,69,0))

            gameDisplay.blit(label, (16, 34))
            gameDisplay.blit(l, (50, 60))
            
            largetext = pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect = Text_objects("Egg Drop",largetext)
       
            
            TextRect.center = ((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf,TextRect)
            button("START",150,450,100,50,green,bright_green,"play")
            button("QUIT",550,450,100,50,red,bright_red,"quit")
            
                        
            
           
            
            pygame.display.update()
            clock.tick(15)

            
def game_loop():
      global pause
      
      
      x=(display_width*0.45)
      y=(display_height*0.90)

      x_change=0

      thing_startx = random.randrange(0,display_width)
      #thing_startx=360
      thing_starty = -600
      #thing_starty=540
      #thing_starty=0
      thing_speed =10
      
      thing_width = 20
      thing_height = 27
      c=0
      
      

      gameExit = False


      while not gameExit:
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  quit()

              if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_LEFT  :
                        
                        x_change = -15
                        #m,n = pygame.mouse.get_pos()

                

                  if event.key == pygame.K_RIGHT  :
                        
                        x_change = 15
                  if event.key == pygame.K_p:
                        pause = True
                        paused()

              if event.type == pygame.KEYUP:
                  if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                      x_change=0

              

                 
                    
                        
          x += x_change 
          gameDisplay.fill(white)

          
                
                     

          bx=[]
          cy=[]
          #egg(thing_startx,thing_starty,thing_width,thing_height,black)
          
          bx,cy=egg(thing_startx,thing_starty,thing_width,thing_height)
          thing_starty += thing_speed
          
          #print 'bx :',bx,'and cy :',cy
          basket(x,y)
          score(c)
          #print x,y
          #print thing_startx,thing_starty

         
          
          if x>display_width-basket_width or x<0 :
                x_change=0

          if thing_starty > display_height:
                thing_starty = 0 - thing_height
                thing_startx = random.randrange(0,display_width)
                #thing_startx = 360
                #count+=1
                #thing_speed+=1
                #thing_width+=(count*1.2)


                """if thing_starty >=600 or thing_starty<=590 and thing_startx>=0 or thing_startx<=800 :
                      if x  in xlist and y  in ylist:
                            crash()
                      
                  
                      
                
          

          if y<thing_starty+thing_height :
                      print 'y crossover'

                      if x>thing_startx and x+basket_width<thing_startx+thing_width or x+basket_width == thing_startx and x+basket_width==thing_startx+thing_width:
                            

                            print 'x crossover'
                            #c+=1
                            crash()"""

                      #if thing_startx>=0 or thing_startx<=800 or thing_starty>=600 or thing_starty<=590 
         
                            
                     
                            

          #if thing_startx>=0 or thing_startx<=800 or thing_starty>=600 or thing_starty<=590 :
               #crash()
               
               
               

         
                            
                            
                      
                            
         
          #if x == display_width-basket_width or thing_starty== display_height:
               # print 'h'

          #if x == thing_startx and y== thing_starty:
                #print 'h'

          #if k == random.randrange(thing_startx,x) and y == random.randrange(thing_starty,y):
                #print 'h'


          #print "X: %d, Y: %d"% (x,y)
          i=0
          if cy[0] in range(560,590):
                
                if bx[0]-x in range(70) :
                      i=i+1
                      #print 'h'
                      c+=1
                        
                else:
                    
                    crash()
                      
                    #print 'l'
                  #print thing_starty
                 # if cy[0] in range(560,590):"""
                    
                      
                
             
                
                      #print 'egg crosses a line'
                      #gameDisplay.blit(eggimg,[360,540,thing_width,thing_height])
                      #gameDisplay.fill(white) 
                
                     # gameDisplay.blit(gameDisplay, (bx[0], cy[0]), pygame.Rect(bx[0], cy[0], 360, 537))
                      #pygame.display.update()
          #print i         
          #if
          #print bx,cy

          #if set(xlist).intersection(bx) and set(ylist).intersection(cy):
               #
               #print 'hi'

          #if cy[0]==x and x==bx[0] or x-1==bx[0]:
                 #print 'h'

          

          

         
    
          
          
          
          pygame.display.update()

          clock.tick(50)
game_intro()

game_loop()
pygame.quit()
quit()
