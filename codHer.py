import pyglet
import math
# imports pyglets library
import random
from pyglet.window import Window, mouse, gl, key
#from pyglet.media import avbin
 
platform = pyglet.window.get_platform()
display = platform.get_default_display()
screen = display.get_default_screen()
 
mygame = pyglet.window.Window(790, 700,                     # setting window
              resizable=False,  
              caption="CodHer",  
              config=pyglet.gl.Config(double_buffer=True),  # Avoids flickers
              vsync=False                                   # For flicker-free animation
              )                                             # Calling base class constructor
mygame.set_location(screen.width // 2 - 200,screen.height//2 - 350)
 
girlImage = pyglet.image.load_animation('sofi.gif')                 # Image for brick
#girlImage.anchor_x= girlImage.width/2
#girlImage.anchor_y=girlImage.height/2
girlSprite= pyglet.sprite.Sprite(girlImage, 200, 0)
girlSprite.visible = False
bgimage= pyglet.resource.image('city.png')
obstacleimage = pyglet.image.load_animation('firewall.gif')
obstacleSprite = pyglet.sprite.Sprite(obstacleimage, 800, 60)
obstacleSprite.scale = 2
obstacleSprite.visible =False

backSprite = pyglet.sprite.Sprite(bgimage, 0, 0)                 # sprite for help an instructions
backSprite.visible = False

logoimage=pyglet.resource.image('logoscreen.png')
logosprite=pyglet.sprite.Sprite(logoimage, 0, 0)                 # sprite for help an instructions
logosprite.visible=True

inst=pyglet.resource.image('help.png')
instsprite=pyglet.sprite.Sprite(inst, 0, 0)                 # sprite for help an instructions
instsprite.visible=False

menuimage = pyglet.resource.image('menu.png')
menusprite = pyglet.sprite.Sprite(menuimage, 0, 0)          # sprite for menu
menusprite.visible= True


liveimage=pyglet.resource.image('star.png')           #scoreboard sprite
live1= pyglet.sprite.Sprite(liveimage, 600, 600)
live1.scale = 0.1
live1.visible=False
live2= pyglet.sprite.Sprite(liveimage, 650, 600)
live2.scale = 0.1
live2.visible=False
live3= pyglet.sprite.Sprite(liveimage, 700, 600)
live3.scale = 0.1
live3.visible=False

bowlsound = pyglet.resource.media("Ball_Return.wav", streaming = False) #sounds to play
sparesound=pyglet.resource.media("SPARE.wav", streaming = False)
guttersound=pyglet.resource.media("gutter.wav", streaming = False)
strikesound=pyglet.resource.media("strike.wav", streaming = False)
fallsound=pyglet.resource.media("close.wav", streaming = False)



move=False
logo_on = 0
c=0
score = 0
lives =3
t =0
strike =0
q_num =0
level =1
frame =0
answer = ""


scorelabel = pyglet.text.Label("",
                             font_name='Comic Sans MS',
                             font_size=28,
                             x=20, y=650,
                             anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
strikelabel = pyglet.text.Label("",
                             font_name='Comic Sans MS',
                             font_size=48,
                             x=400, y=400,
                             anchor_x='center', anchor_y='center', color=(255, 0, 0, 255))
looselabel = pyglet.text.Label("",
                             font_name='Comic Sans MS',
                             font_size=28,
                             x=400, y=400,
                             anchor_x='center', anchor_y='center', color=(255, 0, 0, 255))
winlabel = pyglet.text.Label("",
                             font_name='Comic Sans MS',
                             font_size=28,
                             x=400, y=400,
                             anchor_x='center', anchor_y='center', color=(255, 0, 0, 255))
question = pyglet.text.Label("",
                             font_name='Comic Sans MS',
                             font_size=12,
                             x=400, y=600,
                             anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))

easy_questions = [" x = 'Hello World' \n  What Data Type is x? \n A. String B. Integer C. Boolean D. Char ", "x = 1.0 \n What Data Type is x? \n A. Integer B. Double C. String S. Char ", " How many bits are in a byte? \n A. 4 B. 2. C. 8 D. 12 ", " How many bytes are in a megabyte? \n A. 1000000 B. 100000000 C. 100 D. 1000000000000", "Convert Binary to Decimal: What is 1010 in decimal? \n A. 9 B. 8 C. 10 D. 4", "Convert Binary to Decimal: What is 0001 in decimal? \n A. 0 B. 3 C. 4. D. 1 "   ]
easy_answers = ["A", "b", "c" , "a", "c", "d"]

medium_questions = ["x = 'Hello World'\n print(x) \n The code above would output?\n A. Hello World B. x C. x = 'Hello World' D. 'Hello World'", " x = 5 if x == 5 \n { \n     print(x)\n }\n else\n{\n     print('x is not 5')\nThe code above would output?\nA. x is not 5 B. nothing C. 5 D. 6", "for(int i = 1; i <= 5; i++) \n{\n     print(i + " ")\n}\nThe code above would output?\nA. i i i i i B. 1 2 3 4 C. 1 2 3 4 5 D. 0 1 2 3 4", "int x = 1 \n while ( x < 6 )\n {\n     print(x + ' ')\n}\nThe code above would output?\nA. i i i i i B. 1 2 3 4 C. 1 2 3 4 5  D. 0 1 2 3 4", "How do you recognise a phishing scam?\n A. Email the sender back and ask if they meant to send the email B. Click on the links in the email and fill out the forms C. Forward the email to everyone D. Look at the sender's email, verify any logos and do not respond to anything within the email"]
easy_answers = ["a", "c", "c", "c", "d", "d"]

hard_questions = ["Which of the folowing is considered a definite indicator of an incident?\n A. Changes to system logs  B. Activities at unexpected times C. Presence of new accounts D. Presence of unfamiliar files", "Which data structure is indexable? \n A. Array B. Graph C. Linked List D. Tree", "What layer is the data link layer in the OSI model?\n A. First B. Second C. Third D. Fourth", "What is a Linked List?\nA. a data structure consisting of a collection of elements (values or variables), each identified by at least one index or key. B. a hierarchical tree structure, with a root value and subtrees of children with a parent node C. an ordered set of data elements, each containing a link to its successor D. a String", "What runtime is the fastest?\nA. O(nlogn) B. O(n) C. O(1) D. O(logn)"]
hard_answers = ["A", "A", "B" "C", "C" ]



        
@mygame.event

def on_draw():                                                                   # draws all the sprites
     
    mygame.clear()
    #bgimage.blit(0,0)
    
    menusprite.draw()
    instsprite.draw()
    backSprite.draw()
    girlSprite.draw()
    live1.draw()
    live2.draw()
    live3.draw()
    obstacleSprite.draw()
    strikelabel.draw()
    looselabel.draw()
    question.draw()
    logosprite.draw()
    scorelabel.draw()

@mygame.event
def on_mouse_release(x, y, button, modifiers):                                    # takes users mouse input
    global frame, lis, lis2, c, b, s, t, angle, cond, b, t, m1, m2, lock, lock2, lock3, ballsprite, g1, g2
    
    
    if menusprite.visible== True :# menu selection
        girlSprite.visible = False
        if button==mouse.LEFT: 
            if (277 <= x <= 478) and (388 <= y <= 460):                         # if play selected
                menusprite.visible= False
                backSprite.visible=True
                girlSprite.visible = True
                live1.visible = True
                live2.visible = True
                live3.visible =True
                scorelabel.text = "0"
            elif (277 <= x <= 478) and (292 <= y <= 368):                       # if help selected
                instsprite.visible=True
                menusprite.visible= False
            elif (277 <= x <= 478) and (202 <= y <= 276):                        # if quit selected
                mygame.close()
            
    elif menusprite.visible== False and instsprite.visible== True:              # help instructions
        if button==mouse.LEFT:
            if( 661 <= x <= 778) and ( 20 <= y <= 61):                          # if back is pressed
                instsprite.visible=False
                menusprite.visible=True
    elif menusprite.visible== False  and instsprite.visible==False:             # if back is pressed during game
        if button==mouse.LEFT:
            if frame< 21:
                menusprite.visible= True
                                    
                            
    

@mygame.event

def on_key_release(symbol, modifiers):                                         #takes key input if gamescreen is on only
    
    global c, frame, lives, t, strike, q_num, level, logo_on, logosprite, score, answer
    
    if menusprite.visible== False  and instsprite.visible==False :
        print("hey")
        if symbol == key.A:
            answer = "A"
        elif symbol == key.B:
            answer = "b"
        elif symbol == key.C:
            answer = "c"
        elif symbol == key.D:
            answer = "d"
        if level == 1:
            if answer == easy_questions[q_num]:
                print("yes")
                score+=1
                scorelabel.text = str(score)                
            
        elif level == 2:
            if answer == medium_questions[q_num]:
                score+=1
                scorelabel.text = str(score)
                
        elif level == 3:
            if answer == hard_questions[q_num]:
                score+=1
                scorelabel.text = str[q_num]
                    
            
    
def update(dt):
    
    global c, frame, lives, t, strike, q_num, level, logo_on, logosprite
    logo_on +=1
    if logo_on > 30:
        logosprite.visible= False
        
    backSprite.x -= 400 * dt
    if(backSprite.x <= -600):
        backSprite.x =0
    
    #c+=1
    #fram+=1
##    if(frame%2 == 0):
##        obstacleSprite = pyglet.sprite.Sprite(obs_part1, 800, 20)
##    elif(frame%3 == 0):
##        obstacleSprite = pyglet.sprite.Sprite(obs_part2, 800, 20)
##    elif (frame%4 ==0):
##        obstacleSprite = pyglet.sprite.Sprite(obs_part3, 800, 20)
        
    if menusprite.visible== False and instsprite.visible==False:
        
        c+=0.4
        if q_num >= 5:
            q_num =0
            level+=1
            if level >=4:
                winlabel.text = "CONGRATULATIONS"
        if(c >= 50):
            
            obstacleSprite.visible = True
            obstacleSprite.x -=5
            if level == 1:
                question.text = easy_questions[q_num]                            #question appears
            elif level == 2:
                question.text = medium_questions[q_num]
            elif level == 3:
                question.text = hard_questions[q_num]  
            
        
        if( obstacleSprite.x <= (girlSprite.x + girlSprite.width//2)):     #girl hit by obstacle
            obstacleSprite.x = 800
            c=0
            q_num+=1
            question.text =""
            t+=1
            lives -=1
            if(lives == 2):
                live1.visible = False
            elif lives == 1:
                live2.visible = False
            
            strike =1
            
        if (lives == 0 and strike ==1):
            live3.visible = False
            if t < 15:
                looselabel.text = "Game over. Press back to restart"
                t+=1
            else:
                looselabel.text = ""
                t=0
                strike =0
        elif (lives > 0 and strike ==1):
            if t < 15:
                strikelabel.text = "STRIKE!"
                t+=1
            else:
                strikelabel.text = ""
                t=0
                strike =0
                
            
        
           
##
##            if angle == 20 and ballsprite.x>=560.4 and ballsprite.y>=500.7:           #gutter balls
##                guttersound.play()
##                lock=False
##                lock2=True
##            if angle == 25 and ballsprite.x>=584.292 and ballsprite.y>=484.36:
##                guttersound.play()
##                lock=False
##                lock2=True
##            if angle == 30 and ballsprite.x>=620.5 and ballsprite.y>=441.9:
##                guttersound.play()
##                lock=False
##                lock2=True
##            if angle==35 and ballsprite.x >=652.9 and ballsprite.y>=421.24:
##                guttersound.play()
##                lock=False
##                lock2=True
##            if angle== 40 and ballsprite.x>= 660.97 and ballsprite.y>= 371:
##                guttersound.play()
##                lock=False
##                lock2=True
##            if angle== -20 and ballsprite.x<= 220.4 and ballsprite.y>= 553.34:
##                guttersound.play()
##                lock=False
##                lock3=True
##            if angle== -25 and ballsprite.x<= 201.79 and ballsprite.y>= 485:
##                guttersound.play()
##                lock=False
##                lock3=True
##            if angle== -30 and ballsprite.x<= 165.5 and ballsprite.y>= 466.16:
##                guttersound.play()
##                lock=False
##                lock3=True
##            if angle== -35 and ballsprite.x<=151 and ballsprite.y>= 415.51:
##                guttersound.play()
##                lock=False
##                lock3=True
##            if angle== -40 and ballsprite.x <= 112 and ballsprite.y>= 403.19:
##                guttersound.play()
##                lock=False
##                lock3=True
##            if lock == True:
##                ballsprite.y+=10*math.cos(angler)
##                ballsprite.x+=10*math.sin(angler)
##                ballsprite.rotation+= 45
##                ballsprite.scale=s
##                if c%2==0:
##                    s-=0.01
##        if lock2==True:                                                      #right gutter balls
##            
##            ballsprite.x-=2
##            ballsprite.y+=3
##            ballsprite.rotation+= 45
##            ballsprite.scale=s
##            if c%3==0:
##                s-=0.02
##        if lock3==True:                                                     #left gutter balls
##            
##            ballsprite.x+=2
##            ballsprite.y+=3
##            ballsprite.rotation+= 45
##            ballsprite.scale=s
##            if c%3==0:
##                s-=0.02   
##            
##        if ballsprite.y >= 555:                                            #after hittig pins 
##            abcsprite.visible=True                                          #shutter appears
##            if p<1:
##                fallsound.play()
##                p+=1
##            
##            
##            q2=str(m2)
##            q1=str(m1)
##            q3=str(summed)
##            if frame%2==0:
##                summed=g1+g2
##                if summed> 10:
##                    summed=10
##                scores[frame].text=q2                                    #displays score in even moves
##                m1=0
##                m2=0
##                if frame>0:
##                    sums[(frame-2)//2].text=q3                            #displays sum in each frame
##            if frame%2!=0:
##                scores[frame].text=q1                                      #displays score in odd moves
##                totallabel.text=str(total)                                 #displays total score
##
##            ballsprite.visible = False
##            move=False
##            angle=0
##            if b==False:
##                frame+=1
##                b=True
##        
##            if cond==False and abcsprite.y>450:                          #moves shutter down until y=450
##                abcsprite.y-=8
##               
##        if abcsprite.y<= 450:                                            #when shutter falls, fallen ins become invisible
##            for j in lis2:
##                j.visible= False 
##            cond = True
##            
##        if cond== True and abcsprite.y!=620:                            #moves shutter up again
##            abcsprite.y+=8
##            
##        if abcsprite.y>=620 and ballsprite.visible==False:              #sets ball in place again
##            
##            
##            cond=False
##            
##            ballsprite.scale=1
##            ballsprite.x=400
##            ballsprite.y=60
##            s=1
##            c=0
##            p=0
##            lock2= False
##            lock3=False
##            lock=True
##            ballsprite.visible=True
##            arrowsprite.visible=True
##            arrowsprite.rotation=0
##            arrange()
##
##
##                                                      
##        
##        if len(lis2)==10 and g1!=10:                                  #strike condition
##            if t<5:
##                strikesound.play()
##            if t<20:
##                strikelabel.text="STRIKE"
##                t+=1
##            else:
##                strikelabel.text=""
##            
##        if g1+g2 ==10 and g2!=10:                                  #spare condition
##            if t<20:
##                sparelabel.text="SPARE"
##                t+=1
##            else:
##                sparelabel.text=""
        
    
pyglet.clock.schedule_interval(update, 1/20.)
    
pyglet.app.run()
