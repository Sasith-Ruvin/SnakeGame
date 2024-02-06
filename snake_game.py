from tkinter import *
import random
import tkinter.messagebox


GAME_WIDTH = 1000
GAME_HEIGHT = 500
SPEED = 90
SPACE_SIZE = 20
BODY_PARTS = 3
SNAKE_COLOR = "#324aa8"
FOOD_COLOR = "#eb8807"
BACKGROUND_COLOR = "#24201b"


class Snake:
#Calling constants for snake
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.sqaures = []
#setting the snake head
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.sqaures.append(square)



class Food:
#Generating the food object in a random place
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
#Generating the food
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    #Moving the Snake

    snake.coordinates.insert(0, (x, y))

    sqaure = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.sqaures.insert(0, sqaure)

    #Updating the score
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score:{}".format(score))
    #Deleting the food when snake head overlap it
        canvas.delete("food")

        food = Food()

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.sqaures[-1])

        del snake.sqaures[-1]

#Ending the game there is a collision
    if check_collison(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)



def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction

    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction

    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction

    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collison(snake):
    x, y = snake.coordinates[0]

#Setting Game over if snake collide with borders
    if x < 0 or x >= GAME_WIDTH:
        tkinter.messagebox.showinfo("Game Over", "GAME OVER!!")
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        tkinter.messagebox.showinfo("Game Over", "GAME OVER!!")
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            tkinter.messagebox.showinfo("Game Over", "GAME OVER!!")
            return True
    return False





def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas',70), text="GAME OVER!!",
                       fill="red", tag="gameover")

window = Tk()
window.title("Feed it")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas',40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

#Setting the window to place at center of the screen
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

#Setting Controls for snake

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))




snake = Snake()
food = Food()

next_turn(snake, food)


window.mainloop()

