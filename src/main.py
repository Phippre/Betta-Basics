from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.font as font
from PIL import ImageTk, Image
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
root.geometry(f"{mainWidth}x{mainHeight}")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
def openFishInfo(name, image):
    file_text = NONE

    new_fish_tab = Frame(notebook, bg="#333333", name=name.lower(), borderwidth=0)
    new_fish_tab.pack(fill=BOTH, expand=1)
    
    fish_title = Label(new_fish_tab, text="~" + name, bg="#333333", foreground="white", font=courier_new2)
    fish_title.place(x=10, y=5)

    close_tab_button = Button(new_fish_tab, text="Close Tab", background="gray", foreground="white", borderwidth=0, font=courier_new4, command=closeTab)
    close_tab_button.place(x=905, y=10)

    submit_button = Button(new_fish_tab, text="Submit Information", background="gray", foreground="white", borderwidth=0, font=courier_new4, command=lambda: writeInformation(name, primary_drop_down.current(), secondary_drop_down.current(), pattern_drop_down.current(), gender_drop_down.current(), tail_drop_down.current(), deformity_drop_down.current(), disease_drop_down.current(), personality_drop_down.current(), text_box))
    submit_button.place(x=980, y=10)

    fish_img = Label(new_fish_tab, image=image, background="#333333", relief="groove")
    fish_img.photo = image
    fish_img.place(x=5, y=50)

    #An ungodly amount of dropdowns~~~~~~~~
    primary_label = Label(new_fish_tab, text="Primary Colors", background="#333333", foreground="white", font=courier_new4)
    primary_label.place(x=5, y=275)
    primary_drop_down = ttk.Combobox(new_fish_tab, value=primary_colors, font=courier_new4)
    primary_drop_down.current(0)
    #primary_drop_down.bind("<<ComboboxSelected>>", comboTest)
    primary_drop_down.place(x=5, y=300)

    secondary_label = Label(new_fish_tab, text="Secondary Colors", background="#333333", foreground="white", font=courier_new4)
    secondary_label.place(x=5, y=325)
    secondary_drop_down = ttk.Combobox(new_fish_tab, value=secondary_colors, font=courier_new4)
    secondary_drop_down.current(0)
    secondary_drop_down.place(x=5, y=350)

    pattern_label = Label(new_fish_tab, text="Pattern", background="#333333", foreground="white", font=courier_new4)
    pattern_label.place(x=5, y=375)
    pattern_drop_down = ttk.Combobox(new_fish_tab, value=patterns, font=courier_new4)
    pattern_drop_down.current(0)
    pattern_drop_down.place(x=5, y=400)

    gender_label = Label(new_fish_tab, text="Gender", background="#333333", foreground="white", font=courier_new4)
    gender_label.place(x=5, y=425)
    gender_drop_down = ttk.Combobox(new_fish_tab, value=genders, font=courier_new4)
    gender_drop_down.current(0)
    gender_drop_down.place(x=5, y=450)

    tail_label = Label(new_fish_tab, text="Tail", background="#333333", foreground="white", font=courier_new4)
    tail_label.place(x=5, y=475)
    tail_drop_down = ttk.Combobox(new_fish_tab, value=tails, font=courier_new4)
    tail_drop_down.current(0)
    tail_drop_down.place(x=5, y=500)

    deformity_label = Label(new_fish_tab, text="Deformity", background="#333333", foreground="white", font=courier_new4)
    deformity_label.place(x=5, y=525)
    deformity_drop_down = ttk.Combobox(new_fish_tab, value=deformities, font=courier_new4)
    deformity_drop_down.current(0)
    deformity_drop_down.place(x=5, y=550)

    disease_label = Label(new_fish_tab, text="Disease", background="#333333", foreground="white", font=courier_new4)
    disease_label.place(x=5, y=575)
    disease_drop_down = ttk.Combobox(new_fish_tab, value=diseases, font=courier_new4)
    disease_drop_down.current(0)
    disease_drop_down.place(x=5, y=600)

    personality_label = Label(new_fish_tab, text="Personality", background="#333333", foreground="white", font=courier_new4)
    personality_label.place(x=5, y=625)
    personality_drop_down = ttk.Combobox(new_fish_tab, value=personalities, font=courier_new4)
    personality_drop_down.current(0)
    personality_drop_down.place(x=5, y=650)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    try:
        with open('res/FishData/' + name + '.csv', 'r') as f:
            csv_reader = csv.reader(f)
            for line in csv_reader:
                if line[0] == name:
                    primary_drop_down.current(line[1])
                    secondary_drop_down.current(line[2])
                    pattern_drop_down.current(line[3])
                    gender_drop_down.current(line[4])
                    tail_drop_down.current(line[5])
                    deformity_drop_down.current(line[6])
                    disease_drop_down.current(line[7])
                    personality_drop_down.current(line[8])
                    file_text = line[8]
    except:
        fresh_fish_data = [name, 0, 0, 0, 0, 0, 0, 0, 0, ""]
        with open('res/FishData/' + name + '.csv', 'w') as f:
            csv_writer = csv.writer(f, lineterminator="\n")
            csv_writer.writerow(fresh_fish_data)
    
    text_box = Text(new_fish_tab, background="gray", foreground="white", relief="groove", borderwidth=3)
    text_box.insert(END, ''.join(file_text))
    text_box.place(x=mainWidth-830, y=50, width=800, height=1000)
    
    notebook.add(new_fish_tab, text="~" + name + "~")

def closeTab():
    notebook.hide(notebook.select())

def writeInformation(name, primary, secondary, pattern, gender, tail, deformity, disease, personality, text):
    sumbit_text = text.get("1.0", END)
    submit_data = [name, primary, secondary, pattern, gender, tail, deformity, disease, personality, sumbit_text]
    with open('res/FishData/' + name + '.csv', 'w') as f:
        csv_writer = csv.writer(f, lineterminator="\n")
        csv_writer.writerow(submit_data)
    

def addFish(fish_name, image):
    global x, y

    name = Label(frame1, text=fish_name, font=courier_new, background="#333333", foreground="white")
    name.place(x=x + 2, y=y - 25)

    try:
        image_url = ImageTk.PhotoImage(Image.open(image))
    except:
        image_url = ImageTk.PhotoImage(Image.open("res/img/betta.png"))
        print("No image provided.")

    fish_img = Label(frame1, image=image_url, background="#333333")
    fish_img.photo = image_url
    fish_img.place(x=x, y=y)

    info_button = Button(frame1, text=f"{fish_name}'s Info", name=fish_name.lower(), background="gray", foreground="white", borderwidth=0, font=courier_new3, command=lambda: openFishInfo(info_button._name[0].upper() + info_button._name[1:], image_url))
    info_button.place(x=x + 2, y=y + 205)

    x += 360
    if (x >= mainWidth - 25):
        x = 50
        y += 260

def appendFish(fish_name, image):
    fish_data = [fish_name, image]
    with open('res/fish.csv', 'a', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(fish_data)
        addFish(fish_name, image)

def openFishImage():
    global selected_fish_image
    root.filename = fd.askopenfilename(initialdir="res/img", title="~Select an image~", filetypes=((".png files", "*.png"), (".jpg files", "*.jpg"), ("~All Files~", "*.*")))
    selected_fish_image = root.filename
    print(selected_fish_image)

def readFish():
    with open('res/fish.csv', 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for line in csv_reader:
            addFish(line[0], line[1])

def render():
    global frame1, notebook

    backend_frame = Frame(root)
    backend_canvas = Canvas(backend_frame)
    full_scrollbar = ttk.Scrollbar(backend_frame, orient=VERTICAL, command=backend_canvas.yview)
    frontend_frame = Frame(backend_canvas)

    backend_canvas.configure(yscrollcommand=full_scrollbar.set)
    backend_canvas.bind('<Configure>', lambda e: backend_canvas.configure(scrollregion=backend_canvas.bbox("all")))
    backend_canvas.create_window((0, 0), window=frontend_frame, anchor="nw", width=mainWidth, height=3000)

    def _on_mouse_wheel(event):
        backend_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

    backend_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

    notebook = ttk.Notebook(frontend_frame)
    notebook.pack(fill=BOTH, expand=1)

    frame1 = Frame(notebook, bg="#333333", borderwidth=0)
    frame1.pack(fill=BOTH, expand=1)

    optionsFrame = Frame(frame1, width=200, height=100, highlightbackground="white", highlightthickness=2, bg="#333333")
    optionsFrame.pack(anchor=W)

    #Place Assets Here~~~~~~~~~~~~~~~~~~~~~
    element_name = Entry(frame1, width=26, background="gray", foreground="white", borderwidth=0, font=courier_new4)
    element_name.place(x=8, y=10)
    select_image = Button(frame1, width=25, text="Select Image", background="gray", foreground="white", borderwidth=0, font=courier_new4, command=openFishImage)
    select_image.place(x=10, y=35)
    add_element = Button(frame1, width=25, text="~Add Fish~", background="gray", foreground="white", borderwidth=0, font=courier_new4, command=lambda: appendFish(element_name.get(), selected_fish_image))
    add_element.place(x=10, y=60)
    titleLabel = Label(frame1, text="~Betta Basics~", font=("Courier New", 35, "underline"), background="#333333", foreground="white")
    titleLabel.place(x=250, y=25)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    readFish()

    notebook.add(frame1, text="~Main~")

    backend_frame.pack(fill=BOTH, expand=1)
    backend_canvas.pack(side=LEFT, fill=BOTH, expand=True)
    full_scrollbar.pack(side=RIGHT, fill=Y)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Calling render function
render()
#Main Loop
root.mainloop()