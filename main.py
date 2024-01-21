import pygame
import random
import asyncio
import time

async def main():
        timec=20.08
        #setup
        pygame.init()
        # display
        screenx=600
        screeny=600
        screen = pygame.display.set_mode((screenx,screeny))
        clock = pygame.time.Clock() 
        running = True
        pygame.display.set_caption("Hitman")
        icon=pygame.image.load("logo.png")
        pygame.display.set_icon(icon)
#man location
        x=300
        y=300
        sizex=30
        sizey=100
        speed=7
       #score
        score=0;
        shots=0;
        while running:
    
        
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        shots=shots+1
                        if(x>screenx/2-sizex and x<screenx/2 and y>screeny/2-sizey and y<screeny/2):
                            x=random.randrange(100,500)
                            y=random.randrange(100,500)
                            score=score+1;
                            if(y>280):
                                score=score+1;
                        pygame.mixer.music.load('shot.ogg')
                        pygame.mixer.music.play(1)
                    

            keys = pygame.key.get_pressed()
            x -= (keys[pygame.K_d] - keys[pygame.K_a]) * speed
            y -= (keys[pygame.K_s] - keys[pygame.K_w]) * speed
                

            # fill the screen with a color to wipe away anything from last frame
            screen.fill("white")
    

            # RENDER YOUR GAME HERE
    
            #manrender
            man=pygame.image.load("man.png")
            man = pygame.transform.scale(man,(sizex,sizey))
            screen.blit(man, (x,y))
    
            #scoperender
            scope=pygame.image.load("scope.png")
            scope = pygame.transform.scale(scope, (screenx,screeny))
            screen.blit(scope, (0,0))
    
    
    
            #Text displays score and shots
            myFont = pygame.font.SysFont("Arial", 18)
            scoreDisplay = myFont.render("score: "+str(score),1,"white")
            screen.blit(scoreDisplay, (500, 30))
            shotsDisplay = myFont.render("shots: "+str(shots),1,"white")
            screen.blit(shotsDisplay, (500, 50))
    
       # shows location of man 
       # screen.blit(myFont.render("x: "+str(x),1,"white"), (500, 70))
       # screen.blit(myFont.render("y: "+str(y),1,"white"), (500, 90))
    
    
       # flip() the display to put your work on screen
    
    
            if(timec<0):
                timec=0
                screen.blit(myFont.render("time: "+str(int(timec)),1,"white"), (500, 70))
                running=False
            else:
                time.sleep(0.01)
                timec=timec-0.08;
                screen.blit(myFont.render("time: "+str(int(timec)),1,"white"), (500, 70))
            pygame.display.flip()    
            clock.tick(100)  # limits FPS to 60
        myFont = pygame.font.SysFont("Arial", 30)
        screen.blit(myFont.render("Scored "+str(score)+" in "+str(int(20-timec))+" Seconds",1,"red"), (150, 200))
        pygame.display.flip()
        time.sleep(5)
        pygame.quit()
        await asyncio.sleep(0)
asyncio.run(main())
