'''
CSC 201: Project 3
Project Group Members: Binayak, Simran

Move the archer to shoot arrows up at the pirates. If the archer shoots enough pirates
and gains enough points before a pirate catches them, they win.

Click left to move the archer left and click right to move the archer right.

Press the space key to throw the arrow.

If you shoot down a pirate you gain a point.

If a pirate crosses you, you lose a point.

If a pirate touches the archer, you lose the game.

Gain points to win the game, good luck have fun!

Bonus:
balloons fly during the win screen
pirates drop during the loss screen
both windows are on timers
when an arrow reaches the top, it gets removed
when a pirate reaches the bottom, it gets removed
both are removed to save processing speed
'''
from graphics2 import *
import time
import random
import math

PIRATE_SPEED = 5
ARCHER_SPEED = 25
ARROW_SPEED = -10
NUM_WIN = 20
STALL_TIME = 0.05
THRESHOLD_1 = 23
THRESHOLD_2 = 50
ARROW_HEIGHT = 540

def distance_between_points(point1, point2):
    '''
    Calculates the distance between two points
   
    Params:
    point1 (Point): the first point
    point2 (Point): the second point
   
    Returns:
    the distance between the two points
    '''
    p1x = point1.getX()
    p1y = point1.getY()
    p2x = point2.getX()
    p2y = point2.getY()
    return math.sqrt((p1x - p2x)*(p1x - p2x) + (p1y - p2y) * (p1y - p2y))


def is_close_enough(img1, img2, threshold):
    '''
    Determines if the first target is close enough to be in contact with the second target.
   
    Params:
    img1 (Image): the first image
    img2 (Image): the second image
    threshold: the range for distance
    
    Returns:
    True if the two objects are close enough
    '''
    center_one = img1.getCenter()
    center_two = img2.getCenter()
   
    distance = distance_between_points(center_one,center_two)
    if distance < threshold:
        return True
    else:
        return False
    
def is_pirate_out(pirate_img):
    '''
    Determines if the pirate crossed the line of the archer.
   
    Params:
    pirate_img (Image): the image of the pirate
   
    Returns:
    True if pirate gets past archer
    '''
    end = 666
    center_pirate = pirate_img.getCenter()
   
    distance = center_pirate.getY()
    if distance > end:
        return True
    else:
        return False

def is_arrow_out(arrow_img):
    '''
    Determines if the arrow crossed the top line.
   
    Params:
    arrow_img (Image): the image of the arrow
   
    Returns:
    True if arrow gets past the top
    '''
    end = 0
    center_arrow = arrow_img.getCenter()
   
    distance = center_arrow.getY()
    if distance < end:
        return True
    else:
        return False

def move_pirates(pirate_img_list):
    '''
    Moves every pirate one PIRATE_SPEED unit down the window
   
    Params:
    pirate_img_list (list): the list of falling pirates
   
    '''
    for pirate in pirate_img_list:
        pirate.move(0,PIRATE_SPEED)
        
def move_arrows(arrow_img_list):
    '''
    Moves every arrow one ARROW_SPEED unit down the window
   
    Params:
    arrow_img_list (list): the list of shooting
   
    '''
    for arrow in arrow_img_list:
        arrow.move(0,ARROW_SPEED)


def move_archer(window, archer_img):
    '''
    Each time the click is left of the archer it moves archer_SPEED units left and
    each time the click is right of the archer it moves archer_SPEED units right.
   
    window (GraphWin): the window where game play takes place
    archer_img (Image): the archer image
    '''
    click = window.checkMouse()
    
    if click != None:
        
        left_edge = (archer_img.getCenter()).getX() - (archer_img.getWidth() / 2)
        right_edge = (archer_img.getCenter()).getX() + (archer_img.getWidth() / 2)
        top_edge = (archer_img.getCenter()).getY() - (archer_img.getHeight() / 2)
        bottom_edge = (archer_img.getCenter()).getY() + (archer_img.getHeight() / 2)
        
        if click.getX() > right_edge and top_edge < click.getY() < bottom_edge:
            archer_img.move(ARCHER_SPEED, 0)
        
        elif click.getX() < left_edge and top_edge < click.getY() < bottom_edge:
            archer_img.move(-ARCHER_SPEED, 0)

def add_pirate_to_window(window, low_range, high_range):
    '''
    Adds one pirate to the top of the window at a random location
   
    Params:
    window (GraphWin): the window where game play takes place
   
    Returns:
    the pirate added to the window
    '''
    x_location = random.randrange(low_range, high_range)
    pirate = Image(Point(x_location, 0), 'pirate.gif')
    pirate.draw(window)
    return pirate

def add_arrow_to_window(window, archer_img):
    '''
    Adds one arrow to the bottom of the window at the
    location of the archer 
    
    Params:
    window (GraphWin): the window where game play takes place
   
    Returns:
    the arrow added to the window
    '''
    x_Arrow_location = archer_img.getCenter().getX()
    arrow = Image(Point(x_Arrow_location, ARROW_HEIGHT), 'arrow.gif')
    arrow.draw(window)
    return arrow

def add_balloon_to_window(window):
    '''
    Adds one balloon to the bottom of the window randomly
    
    Params:
    window (GraphWin): the window where screen is displayed
   
    Returns:
    the balloon added to the window
    '''
    x_Balloon_location = random.randrange(10, 401)
    balloon = Image(Point(x_Balloon_location, ARROW_HEIGHT), 'balloon.gif')
    balloon.draw(window)
    return balloon

def arrow_touch_pirate(pirate_list, arrow_list, score, scoreBoard):
    '''
    Removes the arrow and pirate if they contact, adding a point to score
    
    Params:
    pirate_list (list): list of pirates
    arrow_list (list): list of arrows
    score (int): number of pirates hit
    scoreBoard (text): text displaying score
    
    Returns:
    The score
    '''
    for pirate in pirate_list.copy():
        for arrow in arrow_list.copy():
            if is_close_enough(arrow, pirate, THRESHOLD_1):
                pirate.undraw()
                pirate_list.remove(pirate)
                arrow.undraw()
                arrow_list.remove(arrow)
                score += 1
                scoreBoard.setText(f"SCORE: {score}/{NUM_WIN}")
                break
    return score

def game_loop(window, archer):
    '''
    Loop continues to allow the pirates to fall and the archer to move
    until archer shoots enough pirates to end the game or pirate catches
    the archer.
   
    Params:
    window (GraphWin): the window where game play takes place
    archer (Image): the archer image
    
    Returns:
    The score
    '''
    score = 0
    pirate_list = []
    arrow_list = []
    scoreBoard = Text(Point(615, 25), f"SCORE: {score}/{NUM_WIN}")
    scoreBoard.setTextColor("white")
    scoreBoard.draw(window)
    has_won = True
    
    while has_won and score < NUM_WIN:
        move_archer(window, archer)
        
        
        if random.randrange(100) < 6:
            pirate = add_pirate_to_window(window,40,601)
            pirate_list.append(pirate)
           
        move_pirates(pirate_list)
        
        key = window.checkKey()
        if key == "space":
            arrow = add_arrow_to_window(window, archer)
            arrow_list.append(arrow)
            
        move_arrows(arrow_list)
        
        score = arrow_touch_pirate(pirate_list, arrow_list, score, scoreBoard)
                    
        for pirate in pirate_list:
            if is_pirate_out(pirate):
                pirate.undraw()
                pirate_list.remove(pirate)
                score -= 1
                scoreBoard.setText(f"SCORE: {score}/{NUM_WIN}")
                
            if is_close_enough(archer, pirate, THRESHOLD_2):
                for i in range(6):
                    archer.move(100,0)
                has_won = False
        
        if len(arrow_list) > 0:
            for arrow in arrow_list:
                if is_arrow_out(arrow):
                    arrow.undraw()
                    arrow_list.remove(arrow)
                
                 
               
        time.sleep(STALL_TIME)
    return score

def print_instructions():
    '''
    the instructions printed on the first window
    '''
    window = GraphWin("Instructions", 400,400)
    window.setBackground("white")
    pirate_map = Image(Point(200,200), "pirate_map.gif")
    pirate_map.draw(window)
    instructions = Text(Point(200, 200), '''
    Instructions:

    Click the mouse first to start the game!

    Click left to move the archer left and click right to move the archer right.

    Press the space key to throw the arrow.

    If you shoot down a pirate you gain a point.

    If a pirate crosses you, you lose a point.

    If a pirate touches the archer, you lose the game.

    Gain points to win the game, good luck have fun!
    ''')
    instructions.setSize(12)
    instructions.setTextColor("white")
    instructions.draw(window)
    
    x = window.getMouse()
    window.close()

def win():
    '''
    The screen displayed if player wins
    '''
    window = GraphWin("Congratulations!", 400, 400)
    window.setBackground("white")
    win_screen = Image(Point(200,200),"win.gif")
    win_screen.draw(window)
    timer = 0
    balloon_list = []
    
    while timer < 200:
        
        if random.randrange(100) < 6:
            balloon = add_balloon_to_window(window)
            balloon_list.append(balloon)
            
        move_arrows(balloon_list)
            
        timer += 1
        time.sleep(0.1)
    window.close()
        
def loss():
    '''
    The screen displayed if player loses
    '''
    window = GraphWin("Loss!", 400, 400)
    window.setBackground("white")
    loss_screen = Image(Point(200,200),"loss.gif")
    loss_screen.draw(window)
    timer = 0
    pirate_list = []
    while timer < 200:
        
        if random.randrange(100) < 6:
            pirate = add_pirate_to_window(window, 10, 401)
            pirate_list.append(pirate)
            
        move_pirates(pirate_list)
        
        for pirate in pirate_list:
            if is_pirate_out(pirate):
                pirate.undraw()
                pirate_list.remove(pirate)
            
        timer += 1
        time.sleep(0.1)
    window.close()
    
def main():
    # setup the game
    print_instructions()
    
    window = GraphWin("Protect the base!!!", 666,666)
    window.setBackground("white")
    background = Image(Point(333,333), "ship_deck.gif")
    background.draw(window)
    directions = Text(Point(333, 650), 'Click the mouse left/right of archer to move the archer.')
    directions.setTextColor("white")
    directions.setSize(16)
    directions.draw(window)
    
   
    archer = Image(Point(333,580), "archer.gif")
    archer.draw(window)
    
    arrow = Image(Point(333, 333), "arrow.gif")
    #arrow.draw(window)
    
    start = Text(Point(333, 333), "Click on your mouse to start!")
    start.setTextColor("white")
    start.setSize(32)
    start.draw(window)
    
    x = window.getMouse()
    start.undraw()
    score = game_loop(window, archer)
    
    window.close()
    
    if score == NUM_WIN:
        win()
    else:
        loss()

main()
