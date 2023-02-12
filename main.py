import time
from tkinter import *
from tkinter import messagebox
from tkinter import font

root = Tk()

root.geometry('200x175')
root.title('')
root.configure(background='#2B2B2B')

hour = StringVar()
minute = StringVar()
second = StringVar()

# Set default time
hour.set('00')
minute.set('00')
second.set('00')

# Get user input
hourEntry = Entry(root, width=3, font=('Arial', 18, ''),
                  textvariable=hour)
hourEntry.place(x=30, y=135)
minuteEntry = Entry(root, width=3, font=('Arial', 18, ''),
                  textvariable=minute)
minuteEntry.place(x=80, y=135)
secondEntry = Entry(root, width=3, font=('Arial', 18, ''),
                  textvariable=second)
secondEntry.place(x=130, y=135)

def submit():
    try:
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        print('Wrong input value')
    while temp > -1:
        mins, secs = divmod(temp, 60)
        hours = 0
        
        if mins > 60:
            hours, mins = divmod(mins, 60)
            
        hour.set('{0:2d}'.format(hours))
        minute.set('{0:2d}'.format(mins))
        second.set('{0:2d}'.format(secs))
        
        root.update()
        time.sleep(1)

        if (temp == 0):
            messagebox.showinfo('Time Countdown', 'Session Finished')
        
        temp -= 1
    
btnFont = font.Font(family='Helvetica', size=15)
btn = Button(root, text='START', bd='5', fg='#575757', height=4, width=12, font=btnFont,
             command = submit)
btn.place(x = 27, y = 10)

root.mainloop()