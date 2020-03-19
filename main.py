from tkinter import *
from tkinter.messagebox import *
from gtts import gTTS
import os
import time
def Verification():
    if selected.get() == 1 :
        tts = gTTS(text=Champ.get(), lang='fr')
    if selected.get() == 2 :
        tts = gTTS(text=Champ.get(), lang='uk')
    if selected.get() == 3 :
        tts = gTTS(text=Champ.get(), lang='es')
    if selected.get() == 4 :
        tts = gTTS(text=Champ.get(), lang='ru')
    if selected.get() == 5 :
        tts = gTTS(text=Champ.get(), lang='ar')
    tts.save('son.mp3')
    time.sleep(0.5)
    os.system('son.mp3')
    print(selected.get())

Mafenetre = Tk()
Mafenetre.title('TTS by Ale-pe')
Mafenetre.geometry("300x100")


selected = IntVar()


Label1 = Label(Mafenetre, text = 'Texte :')
Label1.place(x=1, y=1)

txt= ""
Champ = Entry(Mafenetre, textvariable='fr', bg ='bisque', fg='maroon')
Champ.focus_set()
Champ.place(x=55, y=1)
Label1 = Label(Mafenetre, text = 'Langue :')
Label1.place(x=1, y=25)


Bouton = Button(Mafenetre, text ='Valider', command = Verification)
Bouton.place(x=230, y=1)





rad1 = Radiobutton(Mafenetre,text='fr', value=1, variable=selected)
rad2 = Radiobutton(Mafenetre,text='us', value=2, variable=selected)
rad3 = Radiobutton(Mafenetre,text='es', value=3, variable=selected)
rad4 = Radiobutton(Mafenetre,text='ru', value=4, variable=selected)
rad5 = Radiobutton(Mafenetre,text='ar', value=5, variable=selected)
rad1.place(x=65, y=25)
rad2.place(x=105, y=25)
rad3.place(x=145, y=25)
rad4.place(x=65, y=50)
rad5.place(x=105, y=50)

Mafenetre.mainloop()
