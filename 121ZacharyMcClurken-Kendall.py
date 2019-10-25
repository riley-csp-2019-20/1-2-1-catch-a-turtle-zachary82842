# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random

#-----game configuration----
turtleshape = "turtle"
turtlesize = 2.5
turtlecolor = "green"
score = 0

timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#colors to pick from
color_list = ["blue", "orange", "purple", "yellow", "brown"]


#-----initialize turtle-----
ted = trtl.Turtle(shape = turtleshape)
ted.color(turtlecolor)
ted.shapesize(turtlesize)
ted.speed(0)

score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-400, 300)
score_writer.ht()

font_setup = ("Arial", 30, "bold")
score_writer.write(score, font=font_setup)

counter =  trtl.Turtle()
counter.speed(0)
counter.ht()
counter.penup()
counter.goto(250,275)



#-----game functions--------
def ted_clicked(x,y):
    print("Ted got clicked")
    change_position()
    update_score()
    ted.color(random.choice(color_list))
    
def change_position():
    ted.penup()
    ted.ht()
    if not timer_up:
      tedx = random.randint(-400, 400)
      tedy = random.randint(-300, 300)
      ted.goto(tedx, tedy)
      ted.st()
      

def update_score():
    global score
    score += 1
    print(score)
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Game Over", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 


#-----events----------------

ted.onclick(ted_clicked)

wn = trtl.Screen()
wn.bgcolor("Blue") # change the background color
wn.ontimer(countdown, counter_interval) 
wn.mainloop()