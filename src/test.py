import tkinter as tk

def toggle(num):
    if buttons[num].config('relief')[-1] == 'sunken':
      buttons[num].config(relief='raised')
    else:
      buttons[num].config(relief='sunken')

root = tk.Tk()

root.title("Chamber Calibration")

#------------------------------------------
# Sets up the different temperature buttons
#------------------------------------------

STEPS = ['-65C', '-40C', '-20C', '0C', '23C', '30C', '45C', '65C', '90C', '130C', '165C',
         '38C 15%RH', '38C 95%RH', '50C 95%RH', '85C 95%RH']

buttons = []
count = 0
for step in STEPS:
    buttons.append(tk.Button(root, text=step, width = 25, relief='raised',
                        command=lambda num=count: toggle(num)))
    buttons[count].grid(row = count, column = 3)
    count += 1

#-----------
# Starts GUI
#-----------
root.mainloop()