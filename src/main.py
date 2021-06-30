from tkinter import *
from tkinter import ttk
import tkinter.font as font
from PIL import ImageTk, Image
import os

mainWidth = 1140
mainHeight = 700

random_name = "Cute Little Kitty"

root = Tk()
root.title("~Betta Basics~")
root.geometry(f"{mainWidth}x{mainHeight}")

courier_new = font.Font(family='Courier New', size=14)
courier_new2 = font.Font(family='Courier New', size=20)

fish_data_path = "res/FishData"
fish_list = []

x = 205
y = 50

with open('res/fish.txt', 'r') as f:
    for line in f:
        fish_list.append(line.strip())

#Fucntions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def openFishInfo(name):
    new_fish_tab = Frame(notebook, bg="#333333")
    new_fish_tab.pack(fill=BOTH, expand=1)
    
    file_text = NONE

    for file in os.listdir("res/FishData"):
        if file.endswith(".txt"):
            print("Yup")

    """for files in os.listdir(fish_data_path):
        print(files)
        if files.replace('.txt', '') == name:
            f = open('res/FishData/' + files, 'r')
            file_text = f.readlines()
            f.close()
            print(name)
            break
        else:
            #file = open("res/FishData/" + name + ".txt", "w")
            #file.close()
            print(name)"""
            
        
    text_box = Label(new_fish_tab, text=file_text, width=150, height=30, background="gray", foreground="white")
    text_box.pack(pady=100)
    
    notebook.add(new_fish_tab, text="~" + name + "~")

def addFish(fish_name):
    global x, y

    name = Label(frame1, text=fish_name, font=courier_new, background="#333333", foreground="white")
    name.place(x=x + 2, y=y - 25)

    asset =  ImageTk.PhotoImage(Image.open("res/betta.png"))
    my_label = Label(frame1, image=asset, background="#333333")
    my_label.photo = asset
    my_label.place(x=x, y=y)

    info_button = Button(frame1, text=f"{fish_name} Info", name=fish_name.lower(), command=lambda: openFishInfo(info_button._name[0].upper() + info_button._name[1:]))
    info_button.place(x=x + 100, y=y + 205)

    x += 305
    if (x >= mainWidth - 25):
        x = 205
        y += 260

def appendFish(fish_name):
    f = open('res/fish.txt', 'a')
    f.write(fish_name + "\n")
    addFish(fish_name)
    f.close()

def render():
    global frame1, notebook

    backend_frame = Frame(root)
    backend_canvas = Canvas(backend_frame)
    full_scrollbar = ttk.Scrollbar(backend_frame, orient=VERTICAL, command=backend_canvas.yview)
    frontend_frame = Frame(backend_canvas)

    backend_canvas.bind('<Configure>', lambda e: backend_canvas.configure(scrollregion=backend_canvas.bbox("all")))
    backend_canvas.create_window((0, 0), window=frontend_frame, anchor="nw", width=mainWidth, height=3000)
    backend_canvas.configure(yscrollcommand=full_scrollbar.set)

    notebook = ttk.Notebook(frontend_frame)
    notebook.pack(fill=BOTH, expand=1)

    frame1 = Frame(notebook, bg="#333333")
    frame1.pack(fill=BOTH, expand=1)

    optionsFrame = Frame(frame1, width=200, height=mainHeight, highlightbackground="white", highlightthickness=2, bg="#333333")
    optionsFrame.pack(anchor=W)

    #Place Assets Here~~~~~~~~~~~~~~~~~~~~~
    element_name = Entry(frame1, width=30)
    element_name.place(x=5, y=5)
    add_element = Button(frame1, width=25, text="~Add Fish~", command=lambda: appendFish(element_name.get()))
    add_element.place(x=5, y=30)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
    for fish in fish_list:
        addFish(fish)

    notebook.add(frame1, text="~Main~")

    backend_frame.pack(fill=BOTH, expand=1)
    backend_canvas.pack(side=LEFT, fill=BOTH, expand=True)
    full_scrollbar.pack(side=RIGHT, fill=Y)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

render()

root.mainloop()