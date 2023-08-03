import tkinter
from tkinter import messagebox , END
import base64

window = tkinter.Tk()
window.title("Secret Notes")
window.config(padx=30,pady=30)

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def save_and_encrypt_notes():
    title = entry1.get()
    message = low_input.get("1.0",END)
    master_secret = entry2.get()

    if len(title) == 0 or len(message) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title="ERROR!",message="Please enter all info")
    else:
        
        message_encrypted = encode(master_secret,message)

        try:
            with open("mySecret.txt","a") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        except FileNotFoundError:
            with open("mySecret.txt","w") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        finally:
            entry1.delete(first=0,last=END)
            low_input.delete("0.0",END)
            entry2.delete(first=0,last=END)


def decrypt_notes():
    message_encrypted = low_input.get("1.0",END)
    master_secret = entry2.get()

    if len(message_encrypted) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title="ERROR!", message="Please enter all info.")
    else:
        try:
            decrypted_message = decode(master_secret,message_encrypted)
            low_input.delete("1.0",END)
            low_input.insert("1.0",decrypted_message)
        except:
            messagebox.showinfo(title="ERROR",message="Please enter encrypted text")


photo = tkinter.PhotoImage(file="topSecret.png")
photo_label = tkinter.Label(image=photo)
photo_label.pack()


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

button1 = tkinter.Button(text="Save&Encrypt",command=save_and_encrypt_notes)
button1.pack()

button2 = tkinter.Button(text="Decrypt",command=decrypt_notes)
button2.pack()

window.mainloop()
