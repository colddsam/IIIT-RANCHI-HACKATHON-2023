import tkinter as tk
import speech_recognition as sr
from PIL import Image,ImageTk
import speak as sp
import os
import time
import sign_to_speech as ss
class useful__tools:

    def extract__text__and__show(window,inputtext):
        inp=inputtext.get(1.0,"end-1c")
        useful__tools.signconvertor(window=window,inp=inp)

    def collect__audio(window,text__record,image__frame):
        setup__audiochannle=sr.Recognizer()
        with sr.Microphone() as source:
            print("say something......")
            setup__audiochannle.pause_threshold=1
            audio=setup__audiochannle.listen(source)
        try:
            print("your speech is recognizing......")
            string=setup__audiochannle.recognize_google(audio,language="en-in")
            text__record.config(text=string)
            submit__button=tk.Button(image__frame,text="submit",bg='lime green',width=20,command=lambda:useful__tools.signconvertor(window=window,inp=string))
            submit__button.pack()
            # useful__tools.signconvertor(window=window,inp=string)
        except Exception:
            text__record.config(text="there is an error while recording....")
    def signconvertor(window,inp):
        window.destroy()
        root__directory='./DATABASE2'
        string1=''
        for j in inp:
            if j!=' ':
                string1=string1+j
        for i in string1:
            root = tk.Tk()
            if i!=' ':
                sp.speakout(i)
                image = Image.open(os.path.join(root__directory,f'{i.upper()}.jpg'))
                resize_image = image.resize((500,500))
                img = ImageTk.PhotoImage(resize_image)
                label1 = tk.Label(image=img)
                label1.image = img
                label1.pack()
                label1.after(1000,label1.destroy)
                root.after(1000,root.destroy)
                root.mainloop()
        window=tk.Tk()
        window.geometry("500x500")
        window.title("Team Dark Phoenix")
        title__frame=tk.Frame(window,width=500,pady=20,padx=20)
        title__frame.pack(side="top")
        statment__frame=tk.Frame(window,width=500,pady=20,padx=20)
        statment__frame.pack(side="top")
        button1__frame=tk.Frame(window,width=500,pady=20,padx=20)
        button1__frame.pack(side="top")
        button2__frame=tk.Frame(window,width=500,pady=20,padx=20)
        button2__frame.pack(side="top")
        button3__frame=tk.Frame(window,width=500,pady=20,padx=20)
        button3__frame.pack(side="top")
        image__frame=tk.Frame(window,width=500,pady=20,padx=20)
        image__frame.pack(side="top")
        pagestructure.first__page(title__frame=title__frame,window=window,statment__frame=statment__frame,button1__frame=button1__frame,button2__frame=button2__frame,button3__frame=button3__frame,image__frame=image__frame)
        window.mainloop()



class pagestructure:

    def first__page(title__frame,statment__frame,button1__frame,button2__frame,button3__frame,image__frame,window):
        for i in title__frame.winfo_children():
            i.destroy()
        for i in statment__frame.winfo_children():
            i.destroy()
        for i in button1__frame.winfo_children():
            i.destroy()
        for i in button2__frame.winfo_children():
            i.destroy()
        for i in button3__frame.winfo_children():
            i.destroy()
        for i in image__frame.winfo_children():
            i.destroy()
        title__label=tk.Label(title__frame,bg="gray70",text="Welcome to Project Dark Phoenix",font=("Bell Gothic Std Black",20))
        title__label.pack()
        problem__statement=tk.Label(statment__frame,bg="grey70",text="which operation you want to do?",font=("Minion Pro Med",12))
        problem__statement.pack()
        button1=tk.Button(button1__frame,text="sign to speech",width=20,bg="lime green",font=("Minion Pro Med",10),command=lambda:ss.model__making())
        button1.pack(side="right")
        label1=tk.Label(button1__frame,width=10,font=("Minion Pro Med",10))
        label1.pack(side="right")
        button2=tk.Button(button1__frame,text="speech to sign",width=20,bg="lime green",font=("Minion Pro Med",10),command=lambda:pagestructure.second__page(title__frame=title__frame,statment__frame=statment__frame,button1__frame=button1__frame,button2__frame=button2__frame,button3__frame=button3__frame,image__frame=image__frame,window=window))
        button2.pack(side="right")
        direction__image=Image.open('direction.png')
        resized__direction__image=direction__image.resize((50,50))
        img=ImageTk.PhotoImage(resized__direction__image)
        label__image=tk.Label(button2__frame,image=img)
        label__image.image=img
        label__image.pack()
        previous__menu=tk.Button(button3__frame,text="Previous screen",width=20,bg="lime green",font=("Minion Pro Med",10))
        previous__menu.pack(side="right")
        space2=tk.Label(button3__frame,width=10)
        space2.pack(side="right")
        exit__button=tk.Button(button3__frame,text="exit",bg="lime green",width=20,font=("Minion Pro Med",10),command=lambda:window.destroy())
        exit__button.pack(side="right")

    def second__page(title__frame,statment__frame,button1__frame,button2__frame,button3__frame,image__frame,window):
        for i in title__frame.winfo_children():
            i.destroy()
        for i in statment__frame.winfo_children():
            i.destroy()
        for i in button1__frame.winfo_children():
            i.destroy()
        for i in button2__frame.winfo_children():
            i.destroy()
        for i in button3__frame.winfo_children():
            i.destroy()
        for i in image__frame.winfo_children():
            i.destroy()
        title__label=tk.Label(title__frame,bg="gray70",text="Welcome to Project Dark Phoenix",font=("Bell Gothic Std Black",20))
        title__label.pack()
        decision=tk.Label(statment__frame,bg="gray70",text="Which input you want to provide?",font=("Minion Pro Med",12))
        decision.pack()
        Button1=tk.Button(button1__frame,text="Text as input",bg="lime green",width=20,font=("Minion Pro Med",10),command=lambda:pagestructure.text__to__sign__page(title__frame=title__frame,statment__frame=statment__frame,button1__frame=button1__frame,button2__frame=button2__frame,button3__frame=button3__frame,image__frame=image__frame,window=window))
        Button1.pack(side="right")
        space1=tk.Label(button1__frame,width=10)
        space1.pack(side="right")
        Button2=tk.Button(button1__frame,text="speech as input",bg="lime green",width=20,font=("Minion Pro Med",10),command=lambda:pagestructure.speech__to__sign__page(title__frame=title__frame,statment__frame=statment__frame,button1__frame=button1__frame,button2__frame=button2__frame,button3__frame=button3__frame,image__frame=image__frame,window=window))
        Button2.pack(side="right")
        direction__image=Image.open('direction.png')
        resized__direction__image=direction__image.resize((50,50))
        img=ImageTk.PhotoImage(resized__direction__image)
        label__image=tk.Label(button2__frame,image=img)
        label__image.image=img
        label__image.pack()
        previous__menu=tk.Button(button3__frame,text="Previous screen",width=20,bg="lime green",font=("Minion Pro Med",10),command=lambda:pagestructure.first__page(title__frame=title__frame,statment__frame=statment__frame,button1__frame=button1__frame,button2__frame=button2__frame,button3__frame=button3__frame,image__frame=image__frame,window=window))
        previous__menu.pack(side="right")
        space2=tk.Label(button3__frame,width=10)
        space2.pack(side="right")
        exit__button=tk.Button(button3__frame,text="exit",bg="lime green",width=20,font=("Minion Pro Med",10),command=lambda:window.destroy())
        exit__button.pack(side="right")
    
    def text__to__sign__page(title__frame,statment__frame,button1__frame,button2__frame,button3__frame,image__frame,window):
        for i in title__frame.winfo_children():
            i.destroy()
        for i in statment__frame.winfo_children():
            i.destroy()
        for i in button1__frame.winfo_children():
            i.destroy()
        for i in button2__frame.winfo_children():
            i.destroy()
        for i in button3__frame.winfo_children():
            i.destroy()
        for i in image__frame.winfo_children():
            i.destroy()
        title__label=tk.Label(title__frame,bg="gray70",text="Welcome to Project Dark Phoenix",font=("Bell Gothic Std Black",20))
        title__label.pack()
        decision=tk.Label(statment__frame,bg="gray70",text="Please enter your text",font=("Minion Pro Med",12))
        decision.pack()
        inputtext=tk.Text(button1__frame,bg="gray70",height=5,font=("Minion Pro Med",10))
        inputtext.pack()
        submit__button=tk.Button(button2__frame,text="submit",width=20,bg="lime green",font=("Minion Pro Med",10),command=lambda:useful__tools.extract__text__and__show(window=window,inputtext=inputtext))
        submit__button.pack()
        previous__menu=tk.Button(button3__frame,text="Previous screen",width=20,bg="lime green",font=("Minion Pro Med",10),command=lambda:pagestructure.second__page(title__frame=title__frame,statment__frame=statment__frame,button1__frame=button1__frame,button2__frame=button2__frame,button3__frame=button3__frame,image__frame=image__frame,window=window))
        previous__menu.pack(side="right")
        space2=tk.Label(button3__frame,width=10)
        space2.pack(side="right")
        exit__button=tk.Button(button3__frame,text="exit",bg="lime green",width=20,font=("Minion Pro Med",10),command=lambda:window.destroy())
        exit__button.pack(side="right")
    
    def speech__to__sign__page(title__frame,statment__frame,button1__frame,button2__frame,button3__frame,image__frame,window):
        for i in title__frame.winfo_children():
            i.destroy()
        for i in statment__frame.winfo_children():
            i.destroy()
        for i in button1__frame.winfo_children():
            i.destroy()
        for i in button2__frame.winfo_children():
            i.destroy()
        for i in button3__frame.winfo_children():
            i.destroy()
        for i in image__frame.winfo_children():
            i.destroy()
        title__label=tk.Label(title__frame,bg="gray70",text="Welcome to Project Dark Phoenix",font=("Bell Gothic Std Black",20))
        title__label.pack()
        decision=tk.Label(statment__frame,bg="gray70",text="Please press the record buttom to start",font=("Minion Pro Med",12))
        decision.pack()
        record__button=tk.Button(button1__frame,text="record",bg="lime green",width=20,font=("Minion Pro Med",10),command=lambda:useful__tools.collect__audio(window=window,text__record=text__record,image__frame=image__frame))
        record__button.pack()
        text__record=tk.Label(button2__frame,width=20,height=5,bg="gray70",font=("Minion Pro Med",10))
        text__record.pack()
        previous__menu=tk.Button(button3__frame,text="Previous screen",width=20,bg="lime green",font=("Minion Pro Med",10),command=lambda:pagestructure.second__page(title__frame=title__frame,statment__frame=statment__frame,button1__frame=button1__frame,button2__frame=button2__frame,button3__frame=button3__frame,image__frame=image__frame,window=window))
        previous__menu.pack(side="right")
        space2=tk.Label(button3__frame,width=10)
        space2.pack(side="right")
        exit__button=tk.Button(button3__frame,text="exit",bg="lime green",width=20,font=("Minion Pro Med",10),command=lambda:window.destroy())
        exit__button.pack(side="right")
