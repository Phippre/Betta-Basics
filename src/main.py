from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.font as font
from PIL import ImageTk, Image
import pygame
import csv
import os

#Window width and height~~~~~~~~~~~~~~~~~~~
mainWidth = 1140
mainHeight = 700
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Root Window~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
root = Tk()
root.title("~Betta Basics~")
root.iconbitmap('res/img/betta.ico')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
screenx = (screen_width / 2 - mainWidth / 2)
screeny = (screen_height / 2 - mainHeight / 2)
root.geometry(f"{mainWidth}x{mainHeight}+{int(screenx)}+{int(screeny)}")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pygame.mixer.init()

#Fonts(Always Courier New)~~~~~~~~~~~~~~~~~
courier_new = font.Font(family='Courier New', size=14)
courier_new2 = font.Font(family='Courier New', size=20)
courier_new3 = font.Font(family='Courier New', size=11)
courier_new4 = font.Font(family='Courier New', size=9)
courier_new5 = font.Font(family='Courier New', size=35)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

fish_data_path = "res/FishData"
selected_fish_image = NONE

primary_colors = ["Red", "Blue", "Turquoise", "Black", "Yellow", "White", "Orange", "Purple"]
secondary_colors = primary_colors + ["None"]
patterns = ["None", "Alien", "Butterfly", "Dragon", "Galaxy", "Koi"]
genders = ["Male", "Female", "LGBTQ+"]
tails = ["Veil", "Crown", "Comb", "Delta", "Double", "Dumbo", "Halfmoon", "Plakat", "DumboPK", "HMPK", "King", "Spade", "Rose"]
deformities = ["None", "Beard", "Curled", "Face", "Fins", "Scales", "Other"]
diseases = ["None/Other", "Fin Rot", "Swim Bladder", "Pop Eye", "Dropsy", "Fungus", "Ich", "Velvet (Not again)", "Anchor Worms"]
personalities = ["Agressive", "Active", "Lazy", "Retarded", "Sick"]

x = 50
y = 150

#Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ (Dont ask wtf this shit does. Get smart and understand it yourself fam :) )
def playSounds(sound, volume):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loops=0)

def openFishInfo(fish_name, image):
    file_text = NONE
    print(fish_name)
    backend_canvas.yview_moveto(0)

    playSounds("res/sounds/bubble-pop.mp3", 0.1)

    new_fish_tab = Frame(notebook, bg="#333333", name=fish_name.lower(), borderwidth=0)
    new_fish_tab.pack(fill=BOTH, expand=1)
    
    fish_title = Label(new_fish_tab, text="~" + fish_name, bg="#333333", foreground="white", font=courier_new2)
    fish_title.place(x=10, y=5)

    close_tab_button = Button(new_fish_tab, text="Close Tab", background="gray", foreground="white", borderwidth=0, font=courier_new4, command=closeTab)
    close_tab_button.place(x=905, y=10)

    submit_button = Button(new_fish_tab, text="Submit Information", background="gray", foreground="white", borderwidth=0, font=courier_new4, command=lambda: writeInformation(fish_name, primary_drop_down.current(), secondary_drop_down.current(), pattern_drop_down.current(), gender_drop_down.current(), tail_drop_down.current(), deformity_drop_down.current(), disease_drop_down.current(), personality_drop_down.current(), text_box))
    submit_button.place(x=980, y=10)

    fish_img = Label(new_fish_tab, image=image, background="#333333", relief="groove")
    fish_img.photo = image
    fish_img.place(x=5, y=50)

    #An ungodly amount of dropdowns~~~~~~~~
    primary_label = Label(new_fish_tab, text="Primary Colors", background="#333333", foreground="white", font=courier_new4)
    primary_label.place(x=5, y=265)
    primary_drop_down = ttk.Combobox(new_fish_tab, value=primary_colors, font=courier_new4)
    primary_drop_down.current(0)
    primary_drop_down.place(x=5, y=290)

    secondary_label = Label(new_fish_tab, text="Secondary Colors", background="#333333", foreground="white", font=courier_new4)
    secondary_label.place(x=5, y=315)
    secondary_drop_down = ttk.Combobox(new_fish_tab, value=secondary_colors, font=courier_new4)
    secondary_drop_down.current(0)
    secondary_drop_down.place(x=5, y=340)

    pattern_label = Label(new_fish_tab, text="Pattern", background="#333333", foreground="white", font=courier_new4)
    pattern_label.place(x=5, y=365)
    pattern_drop_down = ttk.Combobox(new_fish_tab, value=patterns, font=courier_new4)
    pattern_drop_down.current(0)
    pattern_drop_down.place(x=5, y=390)

    gender_label = Label(new_fish_tab, text="Gender", background="#333333", foreground="white", font=courier_new4)
    gender_label.place(x=5, y=415)
    gender_drop_down = ttk.Combobox(new_fish_tab, value=genders, font=courier_new4)
    gender_drop_down.current(0)
    gender_drop_down.place(x=5, y=440)

    tail_label = Label(new_fish_tab, text="Tail", background="#333333", foreground="white", font=courier_new4)
    tail_label.place(x=5, y=465)
    tail_drop_down = ttk.Combobox(new_fish_tab, value=tails, font=courier_new4)
    tail_drop_down.current(0)
    tail_drop_down.place(x=5, y=490)

    deformity_label = Label(new_fish_tab, text="Deformity", background="#333333", foreground="white", font=courier_new4)
    deformity_label.place(x=5, y=515)
    deformity_drop_down = ttk.Combobox(new_fish_tab, value=deformities, font=courier_new4)
    deformity_drop_down.current(0)
    deformity_drop_down.place(x=5, y=540)

    disease_label = Label(new_fish_tab, text="Disease", background="#333333", foreground="white", font=courier_new4)
    disease_label.place(x=5, y=565)
    disease_drop_down = ttk.Combobox(new_fish_tab, value=diseases, font=courier_new4)
    disease_drop_down.current(0)
    disease_drop_down.place(x=5, y=590)

    personality_label = Label(new_fish_tab, text="Personality", background="#333333", foreground="white", font=courier_new4)
    personality_label.place(x=5, y=615)
    personality_drop_down = ttk.Combobox(new_fish_tab, value=personalities, font=courier_new4)
    personality_drop_down.current(0)
    personality_drop_down.place(x=5, y=640)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    try:
        with open('res/FishData/' + fish_name + '.csv', 'r') as f:
            csv_reader = csv.reader(f)
            for line in csv_reader:
                if line[0] == fish_name:
                    primary_drop_down.current(line[1])
                    secondary_drop_down.current(line[2])
                    pattern_drop_down.current(line[3])
                    gender_drop_down.current(line[4])
                    tail_drop_down.current(line[5])
                    deformity_drop_down.current(line[6])
                    disease_drop_down.current(line[7])
                    personality_drop_down.current(line[8])
                    file_text = line[9]
    except:
        fresh_fish_data = [fish_name, 0, 0, 0, 0, 0, 0, 0, 0, ""]
        with open('res/FishData/' + fish_name + '.csv', 'w') as f:
            csv_writer = csv.writer(f, lineterminator="\n")
            csv_writer.writerow(fresh_fish_data)
    
    text_box = Text(new_fish_tab, background="gray", foreground="white", relief="groove", borderwidth=3)
    text_box.insert(END, ''.join(file_text))
    text_box.place(x=mainWidth-830, y=50, width=800, height=600)

    text_scroll = Scrollbar(text_box)
    text_scroll.pack(side=RIGHT, fill=Y)

    text_box.configure(yscrollcommand=text_scroll.set)

    text_scroll.config(command=text_box.yview)
    
    notebook.add(new_fish_tab, text="~" + fish_name + "~")

    indexes = notebook.index(END)
    notebook.select(notebook.index(int(indexes) - 1))

def closeTab():
    notebook.hide(notebook.select())

def writeInformation(fish_name, primary, secondary, pattern, gender, tail, deformity, disease, personality, text):
    sumbit_text = text.get("1.0", END)
    submit_data = [fish_name, primary, secondary, pattern, gender, tail, deformity, disease, personality, sumbit_text]
    with open('res/FishData/' + fish_name + '.csv', 'w') as f:
        csv_writer = csv.writer(f, lineterminator="\n")
        csv_writer.writerow(submit_data)

def popUpConfirm(fish_name):
    global popup
    popup = Toplevel(root)
    popup.title("Confirm")
    popup_width = 250
    popup_height = 150
    popup_screenx = popup.winfo_screenwidth()
    popup_screeny = popup.winfo_screenheight()
    popupx = (popup_screenx / 2 - popup_width / 2)
    popupy = (popup_screeny / 2 - popup_height / 2)
    popup.geometry(f"{popup_width}x{popup_height}+{int(popupx)}+{int(popupy)}")
    popup.config(bg="#333333")
    confirm_message = Label(popup, text=f"Would you like to delete: \n {fish_name}", font=courier_new3, background="#333333", foreground="white")
    confirm_message.place(x=10, y=20)

    yes_button = Button(popup, width=10, text="Yes", background="gray", foreground="#38BC00", command=lambda: deleteFish(fish_name))
    yes_button.place(x=10, y=100)

    no_button = Button(popup, width=10, text="No", background="gray", foreground="red", command=popup.destroy)
    no_button.place(x=160, y=100)

def deleteFish(fish_name):
    global x, y

    popup.destroy()
    
    with open("res/fish.csv", "r") as f:
        reader = csv.reader(f)
        data = list(reader)
    
    with open("res/fish.csv", "w", newline='') as f:
        writer = csv.writer(f)
        for row in data:
            if row[0] != fish_name:
                writer.writerow(row)

    if os.path.exists(f"res/FishData/{fish_name}.csv"):
        os.remove(f"res/FishData/{fish_name}.csv")
    else:
        print("File does not exist")

    x = root.nametowidget(f".!frame.!canvas.!frame.!notebook.!frame.{fish_name.lower()}Img").winfo_x()
    y = root.nametowidget(f".!frame.!canvas.!frame.!notebook.!frame.{fish_name.lower()}Img").winfo_y()

    root.nametowidget(f".!frame.!canvas.!frame.!notebook.!frame.{fish_name.lower()}Title").destroy()
    root.nametowidget(f".!frame.!canvas.!frame.!notebook.!frame.{fish_name.lower()}Img").destroy()
    root.nametowidget(f".!frame.!canvas.!frame.!notebook.!frame.{fish_name.lower()}").destroy()
    root.nametowidget(f".!frame.!canvas.!frame.!notebook.!frame.{fish_name.lower()}Delete").destroy()

def addFish(fish_name, image):
    global x, y

    name = Label(frame1, text=fish_name, name=f"{fish_name.lower()}Title", font=courier_new, background="#333333", foreground="white")
    name.place(x = x + 2, y = y - 25)

    try:
        image_url = ImageTk.PhotoImage(Image.open(image))
    except:
        image_url = ImageTk.PhotoImage(Image.open("res/img/betta.png"))
        print("No image provided. Selecting default image.")

    fish_img = Label(frame1, image=image_url, name=f"{fish_name.lower()}Img", background="#333333")
    fish_img.photo = image_url
    fish_img.place(x=x, y=y)
    
    info_button = Button(frame1, text=f"{fish_name}'s Info", name=f"{fish_name.lower()}", background="gray", foreground="white", font=courier_new3, command=lambda: openFishInfo(info_button._name[0].upper() + info_button._name[1:], image_url))
    info_button.place(x=x + 2, y=y + 205)

    delete_button = Button(frame1, text=f"Delete", name=f"{fish_name.lower()}Delete", background="gray", foreground="#FF0000", font=courier_new3, command=lambda: popUpConfirm(fish_name))#deleteFish(fish_name)
    delete_button.place(x=x + 235, y=y + 205)

    x += 360

    if (x >= mainWidth - 25):
        x = 50
        y += 265

def openFishImage():
    global selected_fish_image
    root.filename = fd.askopenfilename(initialdir="res/img", title="~Select an image~", filetypes=(("~All Files~", "*.*"), (".png files", "*.png"), (".jpg files", "*.jpg")))
    selected_fish_image = root.filename

def appendFish(fish_name, image):
    fish_data = [fish_name, image]
    with open('res/fish.csv', 'a', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(fish_data)
        addFish(fish_name, image)

def readFish():
    with open('res/fish.csv', 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for line in csv_reader:
            addFish(line[0], line[1])

def _on_mouse_wheel(event):
    if notebook.index(notebook.select()) == 0:
        backend_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

def render():
    global frame1, notebook, backend_canvas, full_scrollbar

    backend_frame = Frame(root)
    backend_frame.pack(fill=BOTH, expand=1)

    backend_canvas = Canvas(backend_frame)
    backend_canvas.pack(fill=BOTH, expand=1)

    frontend_frame = Frame(backend_canvas)

    backend_canvas.bind('<Configure>', lambda e: backend_canvas.configure(scrollregion=backend_canvas.bbox("all")))
    backend_canvas.create_window((-1, 0), window=frontend_frame, anchor="nw", width=1144, height=3000)

    notebook = ttk.Notebook(frontend_frame)
    notebook.pack(fill=BOTH, expand=1)

    frame1 = Frame(notebook, bg="#333333", borderwidth=3)
    frame1.pack(fill=BOTH, expand=1)

    notebook.add(frame1, text="~Main~")

    full_scrollbar = Scrollbar(backend_frame)
    #full_scrollbar.pack(side=RIGHT, fill=Y)
    backend_canvas.configure(yscrollcommand=full_scrollbar.set)
    full_scrollbar.configure(command=backend_canvas.yview)
    backend_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

    optionsFrame = Frame(frame1, width=200, height=100, highlightbackground="white", highlightthickness=2, bg="#333333")
    optionsFrame.pack(anchor=W)

    #Place Assets Here~~~~~~~~~~~~~~~~~~~~~
    element_name = Entry(frame1, width=26, background="gray", foreground="white", borderwidth=0, font=courier_new4)
    element_name.place(x=8, y=10)
    select_image = Button(frame1, width=25, text="Select Image", background="gray", foreground="white", font=courier_new4, command=openFishImage)
    select_image.place(x=10, y=35)
    add_element = Button(frame1, width=25, text="~Add Fish~", background="gray", foreground="white", font=courier_new4, command=lambda: appendFish(element_name.get(), selected_fish_image))
    add_element.place(x=10, y=65)
    titleLabel = Label(frame1, text="~Betta Basics~", font=("Courier New", 35, "underline"), background="#333333", foreground="white")
    titleLabel.place(x=250, y=25)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    readFish()
    #playSounds("res/sounds/bubbles.mp3", 0.1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Calling render function
render()
#Main Loop
root.mainloop()