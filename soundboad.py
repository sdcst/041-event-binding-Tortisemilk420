import tkinter as tk
import playsound as p

def playsound0(event):
    print(event)
    p.playsound("byebye.mp3")

def playsound1(event):
    print(event)
    p.playsound("elprimosoundeffectmp3.mp3")

def playsound2(event):
    print(event)
    p.playsound("fortnite-default-dance-bass-boosted.mp3")

def playsound3(event):
    print(event)
    p.playsound("gojo-i-stroke-my-pickle.mp3")

def playsound4(event):
    print(event)
    p.playsound("villager-gyat-rizzler.mp3")

def playsound5(event):
    print(event)
    p.playsound("i-am-malenia-blade-of-miquella.mp3")

def playsound6(event):
    print(event)
    p.playsound("vine-boom.mp3")

win = tk.Tk()
win.attributes('-topmost',True)
l1 = tk.Label(win,text="Mewing")
l2 = tk.Label(win,text="El-primo")
l3 = tk.Label(win,text="Fortnite")
l4 = tk.Label(win,text="Gojo")
l5 = tk.Label(win,text="Villager")
l6 = tk.Label(win,text="Eleden Ring")
l7 = tk.Label(win,text="Boom")
# buttons b1 and b2 do the same
# note that the callback for b1 is included in its definition
# but the callback for b2 is in a separate command
b1 =  tk.Button(win,text="Click to play")
b1.bind("<Button-1>", playsound0)
b2 =  tk.Button(win,text="Click to play")
b2.bind("<Button>",playsound1)
b3 =  tk.Button(win,text="Click to play")
b3.bind("<Button>",playsound2)
b4 =  tk.Button(win,text="Click to play")
b4.bind("<Button>",playsound3)
b5 =  tk.Button(win,text="Click to play")
b5.bind("<Button>",playsound4)
b6 =  tk.Button(win,text="Click to play")
b6.bind("<Button>",playsound5)
b7 =  tk.Button(win,text="Click to play")
b7.bind("<Button>",playsound6)

l1.pack()
b1.pack()
l2.pack()
b2.pack()
l3.pack()
b3.pack()
l4.pack()
b4.pack()
l5.pack()
b5.pack()
l6.pack()
b6.pack()
l7.pack()
b7.pack()

win.mainloop()
