from tkinter import *
from tkinter import  messagebox

root = Tk()
root.title('TIC TAE TOE')
root.resizable(False, False)

#X starts so true
clicked = True
count = 0


#disable all the button
def disable_all_button():
    b1.configure(state=DISABLED)
    b2.configure(state=DISABLED)
    b3.configure(state=DISABLED)
    b4.configure(state=DISABLED)
    b5.configure(state=DISABLED)
    b6.configure(state=DISABLED)
    b7.configure(state=DISABLED)
    b8.configure(state=DISABLED)
    b9.configure(state=DISABLED)


#check to see if someone won
def checkifwon():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.configure(bg="yellow")
        b2.configure(bg="yellow")
        b3.configure(bg="yellow")
        winner = True
        messagebox.showinfo("Tic tae toe", "X Wins!! Congrats!!\nGive it a another try O")
        disable_all_button()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.configure(bg="yellow")
        b5.configure(bg="yellow")
        b6.configure(bg="yellow")
        winner = True
        messagebox.showinfo("Tic tae toe", "X Wins!! Congrats!!\nGive it a another try O")
        disable_all_button()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.configure(bg="yellow")
        b8.configure(bg="yellow")
        b9.configure(bg="yellow")
        winner = True
        messagebox.showinfo("Tic tae toe", "X Wins!! Congrats!!\nGive it a another try O")
        disable_all_button()
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.configure(bg="yellow")
        b4.configure(bg="yellow")
        b7.configure(bg="yellow")
        winner = True
        messagebox.showinfo("Tic tae toe", "X Wins!! Congrats!!\nGive it a another try O")
        disable_all_button()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.configure(bg="yellow")
        b5.configure(bg="yellow")
        b8.configure(bg="yellow")
        winner = True
        messagebox.showinfo("Tic tae toe", "X Wins!! Congrats!!\nGive it a another try O")
        disable_all_button()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.configure(bg="yellow")
        b6.configure(bg="yellow")
        b9.configure(bg="yellow")
        winner = True
        messagebox.showinfo("Tic tae toe", "X Wins!! Congrats!!\nGive it a another try O")
        disable_all_button()
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.configure(bg="yellow")
        b5.configure(bg="yellow")
        b9.configure(bg="yellow")
        winner = True
        messagebox.showinfo("Tic tae toe", "X Wins!! Congrats!!\nGive it a another try O")
        disable_all_button()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.configure(bg="yellow")
        b5.configure(bg="yellow")
        b7.configure(bg="yellow")
        winner = True
        messagebox.showinfo("Tic tae toe", "X Wins!! Congrats!!\nGive it a another try O")
        disable_all_button()

    ###check for O
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.configure(bg="yellow")
        b2.configure(bg="yellow")
        b3.configure(bg="yellow")
        winner = True
        messagebox.showinfo("Tic tae toe", "O Wins!! Congrats!!\nGive it a another try X")
        disable_all_button()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.configure(bg="yellow")
        b5.configure(bg="yellow")
        b6.configure(bg="yellow")
        winner = True
        messagebox.showinfo("Tic tae toe", "O Wins!! Congrats!!\nGive it a another try X")
        disable_all_button()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.configure(bg="yellow")
        b8.configure(bg="yellow")
        b9.configure(bg="yellow")
        winner = True
        messagebox.showinfo("Tic tae toe", "O Wins!! Congrats!!\nGive it a another try X")
        disable_all_button()
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.configure(bg="yellow")
        b4.configure(bg="yellow")
        b7.configure(bg="yellow")
        winner = True
        messagebox.showinfo("Tic tae toe", "O Wins!! Congrats!!\nGive it a another try X")
        disable_all_button()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.configure(bg="yellow")
        b5.configure(bg="yellow")
        b8.configure(bg="yellow")
        winner = True
        messagebox.showinfo("Tic tae toe", "O Wins!! Congrats!!\nGive it a another try X")
        disable_all_button()
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.configure(bg="yellow")
        b6.configure(bg="yellow")
        b9.configure(bg="yellow")
        winner = True
        messagebox.showinfo("Tic tae toe", "O Wins!! Congrats!!\nGive it a another try X")
        disable_all_button()
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.configure(bg="yellow")
        b5.configure(bg="yellow")
        b9.configure(bg="yellow")
        winner = True
        messagebox.showinfo("Tic tae toe", "O Wins!! Congrats!!\nGive it a another try X")
        disable_all_button()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.configure(bg="yellow")
        b5.configure(bg="yellow")
        b7.configure(bg="yellow")
        winner = True
        messagebox.showinfo("Tic tae toe", "O Wins!! Congrats!!\nGive it a another try X")
        disable_all_button()

    #check if tie
    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It's a Tie!! No one wins ;\nBoth of them give a another try")


#button clicked function
def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkifwon()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkifwon()
    else:
        messagebox.showerror("Tic tac toe", "Hey!! That box has already been selected\nPick another box")

#start the game over!
#start the game over!
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0
    #build our button
    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="blue", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="blue", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="blue", command=lambda: b_click(b3))

    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="blue", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="blue", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="blue", command=lambda: b_click(b6))

    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="blue", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="blue", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="blue", command=lambda: b_click(b9))

    #grid button
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

#creat menu
my_menu = Menu(root)
root.configure(menu=my_menu)

#create option menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

reset()
root.mainloop()