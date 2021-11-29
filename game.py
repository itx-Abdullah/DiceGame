# =====================================
# author :  D'techo Solutions
# version : 1.0
# =====================================

# import tkinter and Pillow
from tkinter import *
from tkinter import messagebox
from PIL import (ImageTk, Image)
import random
import time

# Create Instance
window = Tk()

# Set screen size
win_xaxix = int((window.winfo_screenwidth() / 2) - 500)
win_yaxix = int((window.winfo_screenheight() / 2) - 400)
window.geometry(f"1000x700+{win_xaxix}+{win_yaxix}")

# set window icon
window.iconbitmap("..\images\icon.ico") 

# Set screen title
window.title("Dice Game")

# Set resizeable false
window.resizable(False, False)

# variables
amount = IntVar()
number = IntVar()

# Drault dice pic path
filepath = "..\DiceGame\images\dice.png"

# roll the dice
def rollDice():
    
    # get global variables
    global filepath, dice_image, set_dice_image, dice, coins
    
    # get inputs
    bet_amount = amount.get() 
    dice_number = number.get()
    
    # validate inputs 
    if bet_amount == 0 or dice_number == 0:
        messagebox.showerror("Field Error", "All fields are required!")
    elif dice_number > 6:
        messagebox.showerror("Field Error", "Enter Dice Number Between (1-6)")
    # Coin should be graeter then 0    
    elif int(coins["text"]) == 0:
        messagebox.showerror("Coin Error", "You don't have enough coin to play")
        bet_amount = amount.set(0)
        dice_number = number.set(0)
        messagebox.showinfo("Bonus", "You get Bonus of 100 coins")
        coins.configure(text = "100")
    # bet amount should be greater then remaining coins
    elif bet_amount > int(coins["text"]):
        messagebox.showerror("Coin Error", "You don't have enough coin")
        bet_amount = amount.set(0)
        dice_number = number.set(0)
    else:
        # get random number between 1-6    
        random_dice = random.randrange(1,6)
        # get dice pic that match with random number
        filepath = "..\DiceGame\images\dice-"+str(random_dice)+".png"
        # set new dice pic 
        dice_image = Image.open(filepath)
        set_dice_image = ImageTk.PhotoImage(dice_image)
        dice.configure(image = set_dice_image)
        if random_dice == dice_number:
            # =================================================
            # if dice number match then add win coin into remainig coin and set default entry fields
            # =================================================
            messagebox.showinfo("Congrats", f"Congrats! You won {bet_amount} coins")
            win_coin = str(int(coins["text"]) + bet_amount) 
            filepath = "..\DiceGame\images\dice.png"
            dice_image = Image.open(filepath)
            set_dice_image = ImageTk.PhotoImage(dice_image)
            dice.configure(image = set_dice_image)
            amount.set(0)
            number.set(0)
            coins.configure(text = win_coin)
        else:
            # =================================================
            # if dice number doesn't match then subtract bet amount from remainig coin and set default entry fields and images
            # =================================================
            messagebox.showinfo("Try Again", f"You lose {bet_amount} coins. Try Again!")
            filepath = "..\DiceGame\images\dice.png"
            dice_image = Image.open(filepath)
            set_dice_image = ImageTk.PhotoImage(dice_image)
            dice.configure(image = set_dice_image)
            amount.set(0)
            number.set(0)
            win_coin = str(int(coins["text"]) - bet_amount) 
            coins.configure(text = win_coin)
            

    

# Dice Frame
dice_frame = Frame(window,bd = 0, bg= "red")
dice_frame.place(x = 0, y= 0, w = 500, h = 900)

# set dice image 
dice_image = Image.open(filepath)
set_dice_image = ImageTk.PhotoImage(dice_image)
dice = Label(dice_frame, image = set_dice_image, bg = "red")
dice.place(x = 100, y = 180)

# Input Frame
input_frame = Frame(window, width = 500, height = 900, bd = 0, bg= "red")
input_frame.place(x = 500)

# coins
coin_image = Image.open("..\DiceGame\images\coin.png")
set_coint_image = ImageTk.PhotoImage(coin_image)
coin_image_label = Label(input_frame, image = set_coint_image, bg = "red")
coin_image_label.place(x = 430, y = 23)
coins = Label(input_frame, text = "100", bg = "RED", fg = "yellow", font = ("Helvetica", 28, "bold"), justify = LEFT)
coins.place(x = 360, y = 17, w = 70)

# Input Bet Label
bet_label = Label(input_frame, text = "Bet Amount:", font = ("Helvetica", 20, "bold"), fg = "yellow", bg = "red")
bet_label.place(x = 70, y = 250)

# Input Bet
bet = Entry(input_frame, bd = 0, font = ("Helvetica", 14, "bold"), textvariable = amount, highlightbackground = "yellow",  highlightcolor = "yellow", highlightthickness = 2)
bet.place(x = 72, y = 290, w = 250, h = 30)

# Input Dice Number Label
dice_number_label = Label(input_frame, text = "Dice Number:", font = ("Helvetica", 20, "bold"), fg = "yellow", bg = "red")
dice_number_label.place(x = 70, y = 350)

# Input Dice Number
dice_number = Entry(input_frame, bd = 0, font = ("Helvetica", 14, "bold"), textvariable = number,  highlightbackground = "yellow", highlightcolor = "yellow", highlightthickness = 2)
dice_number.place(x = 72, y = 390, w = 250, h = 30)

# Roll Dice Button
roll_dice_button = Button(input_frame, text = "Roll Dice", command = rollDice, font = ("Helvetica", 16, "bold"), bg = "yellow", fg = "red", activebackground = "yellow",  cursor = "hand2", highlightbackground = "yellow" , highlightcolor = "yellow", highlightthickness = 4, bd = 0)
roll_dice_button.place(x = 140, y = 440)



# Run window
window.mainloop()