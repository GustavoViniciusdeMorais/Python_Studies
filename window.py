from cgitb import text
from tkinter import Tk, ttk

w = Tk()
w.title('gustavo')
w.configure(bg="powder blue")
w.geometry('300x200')

button = ttk.Button(w, text="Exit", command= lambda: w.quit())

button.pack(ipadx=50, ipady=10, expand=True)

w.mainloop()