from tkinter import *
from PIL import Image, ImageTk
from random import randint

#main window
root = Tk()
root.title("Rock Scissor Paper")
root.resizable(False,False)
root.configure(background="#9b59b6")

#picture
rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper2.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissor2.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock2.png"))


#insert picture
user_label = Label(root, image=paper_img)
comp_label = Label(root, image=paper_img_comp)
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

#score
playerscore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerscore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerscore.grid(row=1, column=1)
playerscore.grid(row=1, column=3)

#indicator
user_indicator = Label(root, font=50, text="USER", bg="#9b59b6", fg="white")
comp_indicator = Label(root, font=50, text="COMPUTER", bg="#9b59b6", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)



#message
msg = Label(root, font=50, bg="#9b59b6", fg="white")
msg.grid(row=3, column=2)

#update message
def updateMesssage(x):
    msg["text"] = x

#update user score
def updateUserscore():
    score = int(playerscore["text"])
    score += 1
    playerscore["text"] = str(score)

#update computer score
def updateCompScore():
    score = int(computerscore["text"])
    score += 1
    computerscore["text"] = str(score)
#check winner
def checkWin(player, computer):
    if player == computer:
        updateMesssage("It's a tie!!")
    elif player == "rock":
        if computer == "paper":
            updateMesssage("You Loose!!")
            updateCompScore()
        else:
            updateMesssage("You Win!!")
            updateUserscore()

    elif player == "paper":
        if computer == "scissor":
            updateMesssage("You Loose!!")
            updateCompScore()
        else:
            updateMesssage("You Win !!")
            updateUserscore()
    elif player == "scissor":
        if computer == "rock":
            updateMesssage("You Loose!!")
            updateCompScore()
        else:
            updateMesssage("You Win!!")
            updateUserscore()
    else:
        pass




#update choices
choices = ["rock", "paper", "scissor"]
def updateChoices(x):
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

#for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, compChoice)




#buttons
rock = Button(root, width=20, height=2, text="ROCK", bg="red", fg="white", command = lambda:updateChoices("rock"))
paper = Button(root, width=20, height=2, text="PAPER", bg="orange", fg="white", command = lambda:updateChoices("paper"))
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="blue", fg="white", command = lambda:updateChoices("scissor"))

rock.grid_configure(row=2, column=1)
paper.grid_configure(row=2, column=2)
scissor.grid_configure(row=2, column=3)







root.mainloop()
