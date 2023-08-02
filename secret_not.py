import tkinter
from PIL import ImageTk , Image


window = tkinter.Tk()
window.title("Secret Notes")
window.config(padx=30,pady=30)

def button():
    pass

def buttonn():
    pass

img1 = ImageTk.PhotoImage(Image.open("secret.png"))
label1 = tkinter.Label(window , image=img1)
label1.pack()

label2 = tkinter.Label(text="Enter your title")
label2.pack()

entry1 = tkinter.Entry(width=30)
entry1.pack()

label3 = tkinter.Label(text="Enter your secret")
label3.pack()

low_input = tkinter.Text(width=20,height=10)
low_input.pack()

label4 = tkinter.Label(text="Enter master key")
label4.pack()

entry2 = tkinter.Entry(width=30)
entry2.pack()

button1 = tkinter.Button(text="Save&Encrypt",command=button)
button1.pack()

button2 = tkinter.Button(text="Decrypt",command=buttonn)
button2.pack()

window.mainloop()
