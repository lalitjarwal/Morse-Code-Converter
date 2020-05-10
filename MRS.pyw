from tkinter import *
import winsound
from tkinter import messagebox
root=Tk()
root.title("Morse Generator")
root.geometry("500x300")
root.maxsize(width=500,height=300)
root.config(bg="DeepSkyBlue")
#########################################################
import pyttsx3
import engineio

engineio = pyttsx3.init()
voices = engineio.getProperty('voices')
engineio.setProperty('rate', 130)    
engineio.setProperty('voice',voices[1].id)

def speak(text):
    engineio.say(text)
    engineio.runAndWait()
##########################################################

def play():
    try:
        if  msg1==None:
            pass

    except:
        messagebox.showerror("Empty","Input Error")
    for i in msg1:
        if i == '.':
            winsound.Beep(1000, 200)
        if i == '-':
            winsound.Beep(1000, 500)
def play1():
    try :
        if msgs==None:
            pass
    except:
        messagebox.showerror("Empty", "Input Error")
    speak(msgs)

def Exit():
    messagebox.showinfo("Exit","See You soon!")
    root.destroy()

def morsetotext():
    root2 = Tk()
    root2.title("Text Converter")
    root2.geometry("500x500")
    root2.maxsize(width=500, height=500)
    root2.config(bg="DeepSkyBlue2")
    try:
        def Exit():
            #messagebox.showinfo("Exit", "See You Soon!")
            root2.destroy()

        def Morse():
            if txtx.get("1.0", INSERT) == "":
                messagebox.showerror("Empty Box", "Please enter something!")
            else:
                MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                                   'C': '-.-.', 'D': '-..', 'E': '.',
                                   'F': '..-.', 'G': '--.', 'H': '....',
                                   'I': '..', 'J': '.---', 'K': '-.-',
                                   'L': '.-..', 'M': '--', 'N': '-.',
                                   'O': '---', 'P': '.--.', 'Q': '--.-',
                                   'R': '.-.', 'S': '...', 'T': '-',
                                   'U': '..-', 'V': '...-', 'W': '.--',
                                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                                   '1': '.----', '2': '..---', '3': '...--',
                                   '4': '....-', '5': '.....', '6': '-....',
                                   '7': '--...', '8': '---..', '9': '----.',
                                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                                   '?': '..--..', '/': '-..-.', '-': '-....-',
                                   '(': '-.--.', ')': '-.--.-', '\n': ''}
                message = txtx.get("1.0", INSERT)
                message += ' '

                decipher = ''
                citext = ''
                for letter in message:

                    if letter != ' ':
                        i = 0
                        citext += letter

                    else:

                        i += 1

                        if i == 2:

                            decipher += ' '
                        else:
                            decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                                                                          .values()).index(citext)]
                            citext = ''
                global msgs
                msgs = decipher.lower()
                txty.config(state=NORMAL)
                txty.delete("1.0", INSERT)
                print(msgs)
                txty.insert(INSERT, msgs)
                txty.config(state=DISABLED)
                raise(...)
            except(...)
                print(""OOPs)

    lblx = Label(root2, text="           Welcome to Text Converter",
                 bg="DeepSkyBlue2", fg="black", font=('classic', 12, 'bold'))
    lblx.place(x=100, y=20)

    lbly = Label(root2, text="Enter Morse\n Message:", bg="DeepSkyBlue2",
                 fg="black", font=('classic', 10, 'bold'))
    lbly.place(x=10, y=70)

    txtx = Text(root2, height=8, width=40)
    txtx.place(x=100, y=75)

    btn1 = Button(root2, text="Convert", bg="DeepSkyBlue2",
                  fg="black", command=Morse)
    btn1.place(x=150, y=250)

    btn2 = Button(root2, text="Exit", bg="DeepSkyBlue2",
                  fg="black", width=7, command=Exit)
    btn2.place(x=250, y=250)

    btns = Button(root2, text="Play", bg="DeepSkyBlue2",
                  fg="black", width=7, command=play1)
    btns.place(x=350, y=250)

    lblz = Label(root2, text="Converted\n Message:", bg="DeepSkyBlue2",
                 fg="black", font=('classic', 10, 'bold'))
    lblz.place(x=10, y=300)

    txty = Text(root2, height=8, width=40, state=DISABLED)
    txty.place(x=100, y=300)
    root2.mainloop()

def texttomorse():
    root1 = Tk()
    root1.title("Morse Code Converter")
    root1.geometry("500x500")
    root1.maxsize(width=500, height=500)
    root1.config(bg="DeepSkyBlue2")

    def Exit():
        #messagebox.showinfo("Exit", "See You Soon!")
        root1.destroy()

    def Morse():
        if txtx.get("1.0", INSERT) == "":
            messagebox.showerror("Empty Box", "Please enter something!")
        else:
            MORSE_CODE_DICT ={'A': '.-', 'B': '-...',
                               'C': '-.-.', 'D': '-..', 'E': '.',
                               'F': '..-.', 'G': '--.', 'H': '....',
                               'I': '..', 'J': '.---', 'K': '-.-',
                               'L': '.-..', 'M': '--', 'N': '-.',
                               'O': '---', 'P': '.--.', 'Q': '--.-',
                               'R': '.-.', 'S': '...', 'T': '-',
                               'U': '..-', 'V': '...-', 'W': '.--',
                               'X': '-..-', 'Y': '-.--', 'Z': '--..',
                               '1': '.----', '2': '..---', '3': '...--',
                               '4': '....-', '5': '.....', '6': '-....',
                               '7': '--...', '8': '---..', '9': '----.',
                               '0': '-----', ', ': '--..--', '.': '.-.-.-',
                               '?': '..--..', '/': '-..-.', '-': '-....-',
                               '(': '-.--.', ')': '-.--.-'
                                , '\n': ''}
            cipher = ''
            msg = txtx.get("1.0", END).upper()
            for letter in msg:
                if letter != ' ':
                    cipher += MORSE_CODE_DICT[letter] + ' '
                else:
                    cipher += ' '
            msg=cipher
            global msg1
            msg1=cipher
            txty.config(state=NORMAL)
            txty.delete("1.0", INSERT)
            print(msg)
            txty.insert(INSERT, msg)
            txty.config(state=DISABLED)

    lblx = Label(root1, text="~Welcome to Morse Code Converter~",
                 bg="DeepSkyBlue2", fg="black",
                 font=('classic', 12, 'bold'))
    lblx.place(x=100, y=20)

    lbly = Label(root1, text="Enter text \n Message:", bg="DeepSkyBlue2",
                 fg="black", font=('classic', 10, 'bold'))
    lbly.place(x=10, y=70)

    txtx = Text(root1, height=8, width=40)
    txtx.place(x=100, y=75)

    btn1 = Button(root1, text="Convert", bg="DeepSkyBlue2",
                  fg="black", command=Morse)
    btn1.place(x=150, y=250)

    btn2 = Button(root1, text="Exit", bg="DeepSkyBlue2",
                  fg="black", width=7, command=Exit)
    btn2.place(x=250, y=250)

    btnp = Button(root1, text="Play", bg="DeepSkyBlue2",
                  fg="black", width=7, command=play)
    btnp.place(x=350, y=250)

    lblz = Label(root1, text="Converted\n Message:",
                 bg="DeepSkyBlue2", fg="black", font=('classic', 10, 'bold'))
    lblz.place(x=10, y=300)

    txty = Text(root1, height=8, width=40, state=DISABLED)
    txty.place(x=100, y=300)
    root1.mainloop()


lblx = Label(root, text="Welcome to Morse Code Converter",
             bg="DeepSkyBlue2", fg="black",font=('classic',13,'bold'))
lblx.place(x=100, y=20)

btn1=Button(root,text="Click",bg="DeepSkyBlue2",fg="black",
            command=texttomorse)
btn1.place(x=300,y=80)

lbly = Label(root, text="Text to Morse Converter:",
             bg="DeepSkyBlue", fg="black",font=('classic',10,'bold'))
lbly.place(x=30, y=80)

btn2=Button(root,text="Click",bg="DeepSkyBlue2",
            fg="black",command=morsetotext)
btn2.place(x=300,y=140)

lblz = Label(root, text="Morse to Text Converter:",
             bg="DeepSkyBlue", fg="black",font=('classic',10,'bold'))
lblz.place(x=30, y=140)

btn3=Button(root,text="Click",bg="DeepSkyBlue2",
            fg="black",command=Exit)
btn3.place(x=300,y=200)

lble= Label(root, text="         Exit:", bg="DeepSkyBlue",
            fg="black",font=('classic',10,'bold'))
lble.place(x=30, y=200)

root.mainloop()
