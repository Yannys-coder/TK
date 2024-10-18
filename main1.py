from tkinter import *
window=Tk()
window.title("Disney 101")
window.geometry("400x400")
lbl=Label(text="Enter your E-mail")
lbl.place(x= 100, y=100)
entry= Entry()
entry.place(x=90, y=150)
btn= Button(window, text="Enter", bg="blue")
btn.place(x=250, y= 200)
          
window.mainloop()