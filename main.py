import tkinter as tk
import random
GUI = tk.Tk()
text = tk.Label(GUI, text="Choose rock, paper, or scissors")
def RockClicked():
  rock.pack_forget()
  scissors.pack_forget()
  paper.pack_forget()
  text.pack_forget()
  text2 = tk.Label(GUI, text="You have choosen: rock")
  text2.pack()
  computerChoice = random.randint(1, 3)
  if computerChoice == 1:
    text3 = tk.Label(GUI, text="The computer chooses: rock")
    text3.pack()
    text4 = tk.Label(GUI, text="You tied! Try again")
    text4.pack()
  if computerChoice == 2:
    text3 = tk.Label(GUI, text="The computer chooses: scissors")
    text3.pack()
    text4 = tk.Label(GUI, text="You win!")
    text4.pack()
  if computerChoice == 3:
    text3 = tk.Label(GUI, text="The computer chooses: paper")
    text3.pack()
    text4 = tk.Label(GUI, text="You lost. Try again")
    text4.pack()
def ScissorsClicked():
  rock.pack_forget()
  scissors.pack_forget()
  paper.pack_forget()
  text.pack_forget()
  text2 = tk.Label(GUI, text="You have choosen: scissors")
  text2.pack()
  computerChoice = random.randint(1, 3)
  if computerChoice == 1:
    text3 = tk.Label(GUI, text="The computer chooses: rock")
    text3.pack()
    text4 = tk.Label(GUI, text="You lost. Try again")
    text4.pack()
  if computerChoice == 2:
    text3 = tk.Label(GUI, text="The computer chooses: scissors")
    text3.pack()
    text4 = tk.Label(GUI, text="You tied! Try again")
    text4.pack()
  if computerChoice == 3:
    text3 = tk.Label(GUI, text="The computer chooses: paper")
    text3.pack()
    text4 = tk.Label(GUI, text="You win!")
    text4.pack()
def PaperClicked():
  rock.pack_forget()
  scissors.pack_forget()
  paper.pack_forget()
  text.pack_forget()
  text2 = tk.Label(GUI, text="You have choosen: paper")
  text2.pack()
  computerChoice = random.randint(1, 3)
  if computerChoice == 1:
    text3 = tk.Label(GUI, text="The computer chooses: rock")
    text3.pack()
    text4 = tk.Label(GUI, text="You win!")
    text4.pack()
  if computerChoice == 2:
    text3 = tk.Label(GUI, text="The computer chooses: scissors")
    text3.pack()
    text4 = tk.Label(GUI, text="You lost. Try again")
    text4.pack()
  if computerChoice == 3:
    text3 = tk.Label(GUI, text="The computer chooses: paper")
    text3.pack()
    text4 = tk.Label(GUI, text="You tied! Try again")
    text4.pack()
rock = tk.Button(GUI, text="Rock", command=RockClicked, bg="blue", activebackground="red", fg="black", activeforeground="white")
paper = tk.Button(GUI, text="Paper", command=PaperClicked, bg="blue", activebackground="red", fg="black", activeforeground="white")
scissors = tk.Button(GUI, text="Scissors", command=ScissorsClicked, bg="blue", activebackground="red", fg="black", activeforeground="white")

rock.pack()
paper.pack()
scissors.pack()
text.pack()




GUI.mainloop()
