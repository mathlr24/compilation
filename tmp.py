from tkinter import *

window = Tk()
window.title("Apprendre tkinter")
window .geometry( '500x50' )

label = Label(window, text="Bonjour les champions!", font = ( "Arial Bold" , 15 ), fg='yellow',bg='black')
label.grid(column=0, row=0)

saisie = Entry(window, width=10, bg='yellow')
saisie.grid(column=1, row=0)

def click():
    label.configure(text="Bravo les amis!")

bouton = Button( window , text = "Clickez ici", bg = "orange" , fg = "blue", command=click )
bouton.grid(column=2, row=0)

window.mainloop()