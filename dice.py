#!/usr/bin/env python3

from random import randint
import statistics
from tkinter import *

#define the dice rolling function using two inputs:
rolls = []

def roll_many(n, x):
    try:
      for i in range(x):
          roll = randint(1, n)
          rolls.append(roll)
          print(roll)
          mean = statistics.mean(rolls)
          print(mean)
    except Exception as err:
          print(err)

#roll_many(6, 2)

def roll_dice(n):
      roll = randint(1, n)
      print(roll) #printing the roll

roll_dice(20)

class MyWindow:
      def __init__(self, win)  :
            self.lbl1 = Label(win, text=' # of Die Sides')
            self.lbl2 = Label(win, text='Roll Result ')
            self.lbl3 = Label(win, text='Dice Rolling Simulator', font=("Halvetica",20))
            self.t1 = Entry()
            self.t2 = Entry()
            self.btn1 = Button(win, text='Roll Dice')
            self.lbl1.place(x=100,y=100)
            self.t1.place(x=200,y=100)
            self.b1 = Button(win, text='Roll Dice', font=("Halvetica",16), command=self.roll)
            self.b1.place(x=200, y=140)
            self.b1.config(height=1, width=8)
            self.lbl2.place(x=100,y=200)
            self.t2.place(x=200,y=200)
            self.lbl3.place(x=100,y=35)

      def roll(self):
            self.t2.delete(0, 'end')
            #print(self.t1.get())
            try:
               n = int(self.t1.get())
               print(n)
               result = randint(1,n)
               self.t2.insert(END,str(result))
            except Exception as e:
               print(e)
            


window = Tk()
mywin = MyWindow(window)
window.title('Dice Roller')
window.geometry("400x300+10+10")
window.mainloop()
