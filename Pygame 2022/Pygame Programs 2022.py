#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> THINGS TO KNOW <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#scr >>> used to identify screen
#pygame.init >>> used to initialize all the modules within pygame
#pygame.quit() >>> used to close the window
#scr.fill >>> chooses the color for the screen
#pygame.display.set_mode((500,400)pygame.RESIZABLE) >>> used to allow the user to change the size of the window accordingly
#blit() >>> will render an object in order to show it (BLITTING IS SLOW, USE IT MINIMALLY)
#canvas.blit(image, dest = position) >>> iamge = source of the image. dest / position = coordinates where the image is going to be displayed
#canvas.fill(255,255,255) >>> (255,255,255) represent RGB color. This will color the background
#pygame.update() >>> updates the screen
#
#
#
#
#

#Imports
import pygame
import os
import time

#=====================#

def pgame(): #Example of a pygame command
  
    pygame.init()

    size = width, height = 320, 240
    speed = [2, 2]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    ball = pygame.image.load("intro_ball.gif")
    ballrect = ball.get_rect()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()

def pgame_test2(): #My own test for pygame
    #pgame test2 accepts no arguments
    #it will be a simple test to see what pygame can do
    
    pygame.init() #Used to initialize all the required modules of the pygame
    
    scr = pygame.display.set_mode((600,500)) #used to display a window of desired
    #size. Here, width is 600 and height is 500.
    
    pygame.display.set_caption('Pygame Window') #used to defin our display "caption"
    #. So, we have given the name "Pygame Window".
    
    done = False #A variable that is set initially
    
    while not done: #A while loop that will run until it is done
        for event in pygame.event.get(): #used to empty the event queue. It's important to call, and if
        #it isn't called, then the window message will start to pile up, and it will become
        #unresponsive.
        
            if event.type == pygame.QUIT: #used to terminate the event when we click the close button of the window
                done = True
            
    pygame.display.flip() #shift the buffers. It is important to call this function in order to
    #make any updates that we will make ont he game screen
    
    pygame.quit() #once out of the file, close the screen
    
#=============================================================#

def not_my_test():
    #FOR SOME REASON, THE WINDOW DOES NOT CLOSE
    
    pygame.init()  
    scr = pygame.display.set_mode((600,500))  
    pygame.display.set_caption('Pygame Window')
    done = False  
    while not done:  
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                done = True  
    pygame.display.flip()
    pygame.quit()

#===============================================================#

def not_my_test2():
    
    x = 100 #Variable used for a specific spot
    y = 100 #Varialbe used for a specific spot
    
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (x,y) #Used so that environment variables
    #can be set in python
    
    pygame.init() #Initialize the modules in pygame
    
    win_screen = pygame.display.set_mode((500,500)) #used to set the size
    
    time.sleep(2) #used to wait for a while to show the window
    
#==============================================================#
    
def HowToGetTheSizeOfPythonPygameWindow():
    
    pygame.init() #Initialize the modules in Pygame
    
    scr = pygame.display.set_mode() #used to form a screen using this method
    
    x, y = scr.get_size() #Used to get the size of the screen
    
    pygame.display.quit() #used to quit py game, and print(x,y) uses for printing the value.
    
    print(x, y)
    
#==============================================================#

def resize_window():
    #resize window accepts no arguments
    #it will show how to resize the window for pygame in thonny
    #you can resize the screen by putting the mouse on the perimeter of the screen,
    #clicking and holding, and then dragging the mouse.
    
    scr = pygame.display.set_mode((500,400),pygame.RESIZABLE) #used to form a screen
    #that is adjustable. This is due to 'pygame.RESIZABLE'.
    
    pygame.display.set_caption('Resizeable Window') #Used to set the title
    
    #Boolean varaible
    running = True
    
    while running: #while loop to close the screen when chosen to
        
        for event in pygame.event.get(): #Constantly check for events
            
            if event.type == pygame.QUIT: #Check to see if the player clicks the close button
                
                running = False #If the user clicks close, then break the loop
                
    pygame.quit() #quit once outside of the loop
    
#====================================#
    
def image_shower():
    #image shower accepts no arguments
    #it will show an image on the screen
    
    pygame.init() #Initailize the modules in pygame
    
    #Choose a color for the canvas (Screen/Window)
    color = (255,255,255)
    
    #Get the position of the screen
    position = (0,0)
    
    #Create the canvas
    canvas = pygame.display.set_mode((500,500))
    
    #Title of convas
    pygame.display.set_caption("Show Image")
    
    #Find the image and show it
    image = pygame.image.load("tree.png") #MAKE SURE THE IMAGE IS IN THE SAME FILE AS 'Pygame Programs 2022.py'
    
    #Create a boolean variable
    done = False
    
    #Loop to check when the user is done
    while not done:
        #Choose the color for the window
        canvas.fill(color)
        
        #Paste the image in and it's position
        canvas.blit(image, dest = position)
        
        #Create a for loop to check when the user clicks the close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
        pygame.display.update()
    
    pygame.quit()
        
#===============================#
    
def drawing_rectangle(): #DRAW A RECTANGLE IN THE WINDOW
    #drawing rectangle accepts no arguments
    #it will draw a rectangle in the screen
    
    pygame.init() #Initialize the modules in pygame
    
    #Variables
    color = (255,255,255) #the color the background of the scree/window
    rect_color = (255,0,0) #the color of the rectangle
    
    x = 500 #width of the screen
    y = 500 #height of the screen
    
    
    #Create the canvas
    canvas = pygame.display.set_mode((x,y))
    
    #The title for the canvas
    pygame.display.set_caption('