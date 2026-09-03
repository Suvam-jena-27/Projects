# Making A Rock, paper, Scissor GUI based app
#Import Tkinter and random module
import tkinter as tk
import random

#Body
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x500")
root.config(bg="light blue")


#Labels
'''Heading = tk.Label(root, text="Rock, Paper and Scissors", font="Calibri 22 bold")
Heading.pack(pady=25)

choosing_line = tk.Label(root, text="Choose Wisely", font="Calibri 15 italic")
choosing_line.pack(pady=10)'''

Heading = tk.Label(root, text="Rock, Paper and Scissors", font="Calibri 22 bold")
Heading.grid(row=0, column=0, padx=50, pady=20)

choosing_line = tk.Label(root, text="Choose Wisely", font="Calibri 15 italic")
choosing_line.grid(row=1, column=0, pady=50)


#Logic Unit
#Button Logic (Response for main logic)
rps = {1: "Rock", 2:"Paper", 3:"Scissors"}

#Input from input buttons
user_response = ""

def set_user_response(n):   #for user response
    user_response = rps[n]

# Main Logic
user_score = 0
comp_score = 0

#Who is the winner ?
def same():
    pass
def user_win():
    user_score += 1
def comp_win():
    comp_score += 1

    
def RPS():
    comp_response = rps[random.choice([1, 2, 3])]   #computer response

    if comp_response == user_response:
        same()
    else:
        if user_response == rps[1]:
            if comp_response == rps[2]:
                comp_win()
            else:
                user_win()
        if user_response == rps[2]:
            if comp_response == rps[3]:
                comp_win()
            else:
                user_win()
        if user_response == rps[3]:
            if comp_response == rps[1]:
                comp_win()
            else:
                user_win()



def result():
    #add a output window here
    pass



#Buttons
'''r_btn = tk.Button(root, text="Rock", command=set_user_response(1), width=8).pack(side="bottom", padx=10, pady=10)
p_btn = tk.Button(root, text="Paper", command=set_user_response(2), width=8).pack(side="left", padx=5, pady=10)
s_btn = tk.Button(root, text="Scissors", command=set_user_response(3), width=8).pack(side="left", padx=5, pady=10)
'''
r_btn = tk.Button(root, text="Rock", command=set_user_response(1), width=8)
p_btn = tk.Button(root, text="Paper", command=set_user_response(2), width=8)
s_btn = tk.Button(root, text="Scissors", command=set_user_response(3), width=8)

r_btn.grid(row=2, column=0, padx=5, pady=5)
p_btn.grid(row=2, column=1, padx=5, pady=5)
s_btn.grid(row=2, column=2, padx=5, pady=5)

root.mainloop()