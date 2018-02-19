# Poke Version 3
# description

import pygame, time
from uagame import Window
from pygame.locals import *
import math

# Main algorithm
def main():
    # create window
    title = 'Poke the Dot'
    width = 500
    height = 400
    window = Window(title, width, height)
    window.set_auto_update(False)
    # create the Game Object
    # calls the init method
    game = Game(window)  # call a function that has the same name as the class
    #play the game
    game.play()
    # close the window
    window.close()
    
# user define classes
class Game:
    def __init__(self,window):
        self.window = Window
        self.close_clicked = False
        self.continue_game = True
        self.pause_time = 0.01 # smaller is faster game
        
        #create red dot
        color1 = pygame.Color('red')
        center1 = [50, 75]
        radius1 = 30
        velocity1 = [1, 2]
        surface = window.get_surface()
        self.small_dot = Dot(surface, color1, center1, radius1, velocity1) # calling the __init__ method of the dot class
        
        #create blue dot
        color2 = pygame.Color('blue')
        center2 = [250, 200]
        radius2 = 40
        velocity2 = [2, 1]
        self.big_dot = Dot(surface, color2, center2, radius2, velocity2)   
        
        self.score = 0
    def play(self):
            # Play the game until the player presses the close box.
            # - self is the Game that should be continued or not.
    
            while not self.close_clicked:
                # play frame
                self.handle_event() # method call from another class
                self.draw()
                if self.continue_game:
                    self.update()
                    self.decide_continue() # should game continue?
                time.sleep(self.pause_time) # set game velocity by pausing
                
        def handle_event(self):
            # Handle one user event by changing the game state
            # appropriately.
            # - self is the Game whose events will be handled.
    
            event = pygame.event.poll()
            if event.type == QUIT:
                self.close_clicked = True
                            
        def draw(self):
            # Draw all game objects.
            # - self is the Game to draw
            
            self.window.clear()
            self.small_dot.draw()
            self.big_dot.draw()
            self.draw_score()
            if self.continue_game == False:
                self.draw_game_over()   
            self.window.update()
            
        def draw_score(self):
            score_string = 'Score :' + str(self.score)
            font_size = 70
            fg_color = 'white'
            bg_color = 'black'
            # self.window is the reciever object
            # the type of self.window is uagame.window
            self.window.set_font_size(font_size)
            self.window.set_font_color(fg_color)
            x = 0
            y = 0
            
            window.draw_string(score_string,x,y)            
        def draw_game_over(self):
            game_over_string = 'Game Over'
            font_size = 100
            fg_color = 'red'
            bg_color = 'blue'
            self.window.set_font_size(font_size)
            self.window.set_font_color(fg_color)
            self.window.set_bg_color(bg_color)
            x = 0
            y = self.window.get_height() - self.window.get_font_height()
            self.window.draw_string(game_over_string,x,y)
            self.window_bg_color('black')
                
        def update(self):
            # Update all game objects with state changes
            # that are not due to user events
            # - self is the Game to update
            self.big_dot.move()
            self.small_dot.move()
            self.score = pygame.time.get_ticks()//1000
    
        def decide_continue(self):
            # Determine if the game should continue
            # - self is the Game to update
            self.small_dot.move()
            self.big_dot.move
            if self.small_dot.collide(self.big_dot):
                self.continue_game = False
                
            
class Dot:
    def __init__(self, surface, color, center, radius, velocity):
        self.surface = surface
        self.color = color
        self.center = center
        self.radius = radius
        self.velocity = velocity
    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.center, self.radius, self.velocity)
    def move(self):
        #self.center[0] = (self.center[0] + self.velocity[0]) % 500
        #self.center[1] = (self.center[1] + self.velocity[1]) % 400
        size_of_surface = self.surface.get_size() # returns a tuple with the width and height of the surface
        for coord in range(0,2):
            self.center[coord] = (self.center[coord] + self.velocity[coord]) % size_of_surface[coord]
            if self.center[coord] < self.radius:
                self.velocity[coord] = -self.velocity[coord]
            if self.center[coord] + self.radius > size_of_surface[coord]:
                self.velocity[coord] = -self.velocity[coord]
                
    def collision(self, other_dot):
        distance_x = self.center[0] - other_dot.center[1]
        distance_y = self.center[1] - other_dot.center[1]
        distance = math.sqrt(distance_x**2 + distance_y**2)
        
        return distance < self.radius + other_dot.radius
main()


# calling the __init__ method of the dot class, this function call Dot doesnt really exist but its actually a calling of the __init__ method int eh dot class 