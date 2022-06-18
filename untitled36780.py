import turtle
import random

w=500
h=500
f_s=10
delay=100

offsets ={  
    "up": (0,20),
    "down": (0,-20),
    "left": (20,0),
    "right": (-20,0),
    }

def reset(): 
    global snake , snake_dir, food_position, pen
snake = [[0,0],[0,20],[0,40],[0,60],[0,80]]
    snake_dir = "up"
    food_position= get_random_food_position()
    food.goto(food_position)
    move_snake()
    
    def move_snake