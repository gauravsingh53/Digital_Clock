from tkinter import *
from time import strftime

# Create window
root = Tk()
root.title("Digital Clock")

# Function to update time
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# Clock label
label = Label(root, font=('Arial', 50, 'bold'),
              background='black',
              foreground='cyan')

label.pack(anchor='center')

# Call function
time()

# Run window
root.mainloop()