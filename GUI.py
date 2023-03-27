from tkinter import *
import tkinter.font
import sys

win = Tk()

myFont = tkinter.font.Font(family = 'Helvetica', size = 15, weight = 'bold')

win.title('Dispense')
win.geometry('400x200')

def exitProgram():
    print('Exit Button Pressed')
    win.quit()
    sys.exit()

ledButton = Button(win, text = 'YES', font = myFont, command =exitProgram, height = 1, width = 4)
ledButton1 = Button(win, text = 'NO', font = myFont, command =exitProgram, height = 1, width = 4)
ledButton.pack()
ledButton1.pack()
l = Label(win, text = "The PH reading is too high/low.\nWould you like to dispense the normalizer?")
l.pack()
mainloop()
