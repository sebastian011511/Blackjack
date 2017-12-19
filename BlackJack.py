"""
Sebastian Vasco
This program allows the user to play the game of blackjack to a very limited extent
Fall 2017
"""

# Todo: Change minimum from 100 to 1000

from tkinter import *
import tkinter.messagebox as box
import random

total_made_lost=0


def PlayGame():

    # () rather than [] makes array immutable
    faces = ('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 'Jack', 'Queen', 'King')
    suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
    total_points=0

    global total_made_lost

    # random face and suit
    rand_face = 0  # str(random.choice(faces))
    rand_suit = 0  # str(random.choice(suits))

    card_value=['Starting Game...','Cards Pulled:\n\n']
    card_value_counter = 0  # This is used to use in text body of message box
    round_counter = 0  # To use in message box to display number of times a card has been played
    round_title="Deck:"  # Title of message box

    game_limit = -1000

    # loops until you stop of go over game limit= 21
    while True:

        """ 
        If round counter is 0, display starting game message box OR if # of round counter is greater than 1, display 
        message box with the first two cards drawn.  When starting the game, you have to automatically pull two cards.
        This if statement allows to only show message box when starting game and when you have done the loop twice 
        displaying the first two cards.  After the first two loops, user needs to click yes to pull next one.  
        """
        if round_counter > 1 or round_counter == 0:
            another_around=box.askyesno(round_title , card_value[card_value_counter])
            round_title="Cards Pulled:"  # Message box title

        # If YES is clicked to start game
        if another_around == 1:
            rand_face=str(random.choice(faces))
            rand_suit=str(random.choice(suits))

            # Collecting points based on value of card
            if rand_face == 'Ace':
                if total_points <= 10:
                    total_points += 11
                else:
                    total_points += 1
            elif rand_face == 'Jack' or rand_face == 'Queen' or rand_face == 'King':
                total_points += 10
            else:
                total_points += int(rand_face)

            # if points are over 21, you lost the bet, else
            if total_points >= 22:
                # looses bet
                total_made_lost -= 50

                # If user looses more than $1,000, quit game
                if total_made_lost <= game_limit:

                    """
                    If the player looses the round, check for funds.  If funds are below -$1,000, then
                    display message box with game over notice & close game
                    """
                    game_ending_message="GAME OVER--YOU ARE OUT OF FUNDS!\n" \
                                        "Current Funds: $"+str(total_made_lost)+"\n" \
                                        "You scored: "+str(total_points)+" points"+"\n" \
                                        "Last Card Pulled: "+str(rand_face)+" of "+str(rand_suit)

                    close_notice=box.showwarning("Game Ending...",game_ending_message)
                    window.destroy() # Close program
                    print('GAME OVER--RAN OUT OF FUNDS!!!!!')
                    break

                # Else you loose game but can pay again
                else:

                    sorry_message="You Lost the game, you went over 21:\n" \
                                  "Last Card Pulled: "+str(rand_face)+" of "+str(rand_suit) + \
                                  "\nYou scored: "+str(total_points)+" points" + \
                                  "\nTotal Funds: $"+str(total_made_lost)
                    box.showinfo('Sorry',sorry_message)
                    break

            # You reach exactly 21 points, you win
            elif total_points == 21:
                total_made_lost += 100
                winning_message = "You Won the game! \nYou scored: " + str(total_points)+"\nWinning Amount: $" \
                    + str(100)+"\nLast Card Pulled: "+str(rand_face)+" of "+str(rand_suit)+\
                    "\n\nTotal Funds: $" + str(total_made_lost)
                box.showinfo('Congrats!', winning_message)
                break

            round_counter += 1
            card_value[1]+=str(round_counter)+". "+str(rand_face)+" of "+str(rand_suit)+"\n" \
                "Total Points: "+str(total_points)+"\n\n"

            if card_value_counter < 1:
                card_value_counter += 1

            print("Points: ",total_points)
            print("Funds: ",total_made_lost)

        # If NO is clicked to not start the game
        else:
            break

    # Debugging purposes
    print(rand_face)
    print(rand_suit)
    print("Points: ",total_points)
    print("Funds: ",total_made_lost)


def DisplayFunds():

    funds_message='\nTotal Funds: $ %s' % total_made_lost  # Display text and subs %s for actual value of total funds

    box.showinfo('Displaying Funds',funds_message)

def ResetFunds():

    funds_message='\nYou are about to reset your funds.\n' \
                  'Are you sure you want to reset your funds?'
    reset_notice=box.askyesno("Reset Your Funds",funds_message)

    if reset_notice==1:
        global total_made_lost
        total_made_lost=0
        box.showwarning("Reset Funds","Your funds were reset to $0.")


def Quit():
    closeNotice=box.askyesno("Quit Game","Are you sure you want to QUIT GAME?")

    if closeNotice==1:  # yes
        box.showinfo('Good Bye','You have quit the Game...')
        window.destroy()  # Close program


window = Tk()
window.title('Black Jack in Python!')
window.geometry("600x375")
window.resizable(0, 0)  # Window is not resizable
window.configure(bg='white')

menu=Menu(window)
window.config(menu=menu)
gameMenu=Menu(menu)

# Create the menu which calls methods above
menu.add_cascade(label='Select Game Options',menu=gameMenu)
gameMenu.add_command(label='1. Play the Game',command=PlayGame)
gameMenu.add_command(label='2. Display Available Funds',command=DisplayFunds)
gameMenu.add_command(label='3. Reset Funds to Zero',command=ResetFunds)
gameMenu.add_separator()
gameMenu.add_command(label='4. Quit',command=Quit)

main_menu="\nWelcome to the Game of Blackjack\n"

labelWindow=Message(window,text=main_menu, fg="dark green",bg='white')  # Display main menu


# Method calls other methods that correspond to radio buttons in selection
def dialog():
    if menu_selection.get() == 1:
        PlayGame()
    elif menu_selection.get() == 2:
        DisplayFunds()
    elif menu_selection.get() == 3:
        ResetFunds()
    elif menu_selection.get() == 4:
        Quit()


# Value of the radio button
menu_selection=IntVar()

radio_1=Radiobutton(window,text='1. Play the Game',font="times 14",fg='dark red',bg='white',
                    variable=menu_selection,value=1)
radio_2=Radiobutton(window,text='2. Display Available Funds',font="times 14",fg='dark red',bg='white',
                    variable=menu_selection,value=2)
radio_3=Radiobutton(window,text='3. Reset Funds to Zero',font="times 14",fg='dark red',bg='white',
                    variable=menu_selection,value=3)
radio_4=Radiobutton(window,text='4. Quit the Game',font="times 14",fg='dark red',bg='white',
                    variable=menu_selection,value=4)

radio_1.select()

labelWindow.config(font=('times', 20, 'bold'), bg='white', justify='center')  # sets menu display style
labelWindow.pack(side=TOP)

btn=Button(window,text="    Select    ", fg='dark green', font='bold', bg='dark grey', command=dialog)
radio_1.pack()
radio_2.pack()
radio_3.pack()
radio_4.pack()
btn.pack(pady=10)

window.mainloop()
