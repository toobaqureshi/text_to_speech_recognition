#!/usr/bin/env python
# coding: utf-8

# # Text Recognition Python Program

# In[1]:


from tkinter import *
from gtts import gTTS
import os

root = Tk()
frame1 = Frame(root,bg = "white",height = "150")
frame1.pack(fill = X)


frame2 = Frame(root,bg = "dark blue",height = "750")
frame2.pack(fill=X)

label = Label(frame1, text = "Text to Voice Recognition",font = "bold, 20", bg = "white")
label.place(x = 180, y = 70)

entry = Entry(frame2, width = 45,bd = 4, font = 14)
entry.place(x = 130, y = 52)
entry.insert(0, "")

def play():
        language = "en"
        myobj = gTTS(text = entry.get(),lang = language,slow = False)
        myobj.save("convert.wav")
        os.system("convert.wav")
        
btn = Button(frame2, text = "SUBMIT",width = "15", pady = 10,font = "bold, 15",command = play, bg='white')
btn.place(x = 250,y = 130)

root.title("text_to_speech_convertor")
root.geometry("650x550+350+200")
root.mainloop()


# In[ ]:




