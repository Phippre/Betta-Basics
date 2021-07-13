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

#Assorted variables~~~~~~~~~~~~~~~~~~~~~~~~
fish_list = []

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
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
#Function for playing sounds with pygame. Takes file path to sound and volume float as input.
def playSounds(sound, volume):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loops=0)

#openFishInfo() is easily one of the longest functions. It handles the whole informational page when you open the info on a fish in the main screen.
def openFishInfo(fish_name, image):
    file_text = NONE
    
    #This sets the screen view back to the top
    backend_canvas.yview_moveto(0)
    #Plays the sound for opening a new tab
    playSounds("res/sounds/bubble-pop.mp3", 0.1)
    #Creating the frame
    new_fish_tab = Frame(notebook, bg="#333333", name=fish_name.lower(), borderwidth=0)
    new_fish_tab.pack(fill=BOTH, expand=1)
    #Creating the fish name title
    fish_title = Label(new_fish_tab, text="~" + fish_name, bg="#333333", foreground="white", font=courier_new2)
    fish_title.place(x=10, y=5)
    #Creating the close button for when you want to close the tab
    close_tab_button = Button(new_fish_tab, text="Close Tab", background="gray", foreground="white", font=courier_new4, command=closeTab)
    close_tab_button.place(x=900, y=10)
    #Creating the submit button for when a user changes information in the tab. This starts up the writeInformation() function.
    submit_button = Button(new_fish_tab, text="Submit Information", background="gray", foreground="white", font=courier_new4, command=lambda: writeInformation(fish_name, primary_drop_down.current(), secondary_drop_down.current(), pattern_drop_down.current(), gender_drop_down.current(), tail_drop_down.current(), deformity_drop_down.current(), disease_drop_down.current(), personality_drop_down.current(), text_box))
    submit_button.place(x=980, y=10)
    #Displaying the image of the fish.
    fish_img = Label(new_fish_tab, image=image, background="#333333", relief="groove")
    fish_img.photo = image
    fish_img.place(x=5, y=50)

    #An ungodly amount of dropdowns options~~~~~~~~
    #The variable in these drop downs are declared above. 
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
    
    #Try and except statement set up for reading the data from the fish's data file
    try:
        with open('res/FishData/' + fish_name + '.csv', 'r') as f:
            csv_reader = csv.reader(f)
            #Looping through the lines in the file
            for line in csv_reader:
                #Making sure the first row in the line equals the fish's name
                if line[0] == fish_name:
                    #Setting all options and the text field to equal the data in the CSV file. 
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
        #If the try statement fails that means there is no fish data file for that fish.
        #So it creates one with the fish's name and gives it default data.
        fresh_fish_data = [fish_name, 0, 0, 0, 0, 0, 0, 0, 0, ""]
        with open('res/FishData/' + fish_name + '.csv', 'w') as f:
            csv_writer = csv.writer(f, lineterminator="\n")
            csv_writer.writerow(fresh_fish_data)
    #Making the text box
    text_box = Text(new_fish_tab, background="gray", foreground="white", relief="groove", borderwidth=3)
    text_box.insert(END, ''.join(file_text))
    text_box.place(x=mainWidth-830, y=50, width=800, height=600)
    #Putting a scroll bar in the text box
    text_scroll = Scrollbar(text_box)
    text_scroll.pack(side=RIGHT, fill=Y)

    text_box.configure(yscrollcommand=text_scroll.set)

    text_scroll.config(command=text_box.yview)
    #Adding the tab to the notebook in the render function
    notebook.add(new_fish_tab, text="~" + fish_name + "~")
    #Selecting the tab upon creation so it automatically switches over to the tab.
    indexes = notebook.index(END)
    notebook.select(notebook.index(int(indexes) - 1))

#closeTab() is a function made for closing a tab after the close button in select. Why is this here?
def closeTab():
    notebook.hide(notebook.select())

#writeInformation() is called when a user selects the submit button the fish info tab.
#Its here to write the inputted data into the fish's CSV data file. 
def writeInformation(fish_name, primary, secondary, pattern, gender, tail, deformity, disease, personality, text):
    #Getting all the text in the text field.
    sumbit_text = text.get("1.0", END)
    #Assigning all the data in the drop downs to an array.
    submit_data = [fish_name, primary, secondary, pattern, gender, tail, deformity, disease, personality, sumbit_text]
    with open('res/FishData/' + fish_name + '.csv', 'w') as f:
        csv_writer = csv.writer(f, lineterminator="\n")
        csv_writer.writerow(submit_data)

#The popUpConfirm() function is run when a user clicks the delete button on a fish in the main page. Its here to prevent accidental deletion.
def popUpConfirm(fish_name):
    global popup
    #Creating and editing a TopLevel window.
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
    
    #This is the message that appears and asks if you'd like to confirm deletion.
    confirm_message = Label(popup, text=f"Would you like to delete: \n {fish_name}", font=courier_new3, background="#333333", foreground="white")
    confirm_message.place(x=10, y=20)
    #Yes button will trigger the deleteFish() function.
    yes_button = Button(popup, width=10, text="Yes", background="gray", foreground="#38BC00", command=lambda: deleteFish(fish_name))
    yes_button.place(x=10, y=100)
    #No button will kill the pop-up window process.
    no_button = Button(popup, width=10, text="No", background="gray", foreground="red", command=popup.destroy)
    no_button.place(x=160, y=100)

#The deleteFish() function is called when the yes button is selected on the pop-up window. 
def deleteFish(fish_name):
    global x, y, fish_list
    #Destroy the pop-up window
    popup.destroy()
    #Opens the main fish csv list and prints all lines out into a list. Kinda like copy and paste here.
    with open("res/fish.csv", "r") as f:
        reader = csv.reader(f)
        data = list(reader)
    #Re-read the file, instead this time it checks each line for a name and removes the corresponding widgets on the front page.
    #In summary its removing all the fish from the main screen for re-adding. Re-adding all the fish to the main screen was my shorcut for filling the empty space after deleting a fish.
    with open("res/fish.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            #This is a handy little way of converting regular widgets into the url of its name. 
            #Each widget has a name assigned (ie. BoBImg, JerryTitle). These lines find each widget with the corresponding fish name and destroy them. 
            root.nametowidget(f".!frame.!canvas.!frame.!notebook.!frame.{line[0].lower()}Img").destroy()
            root.nametowidget(f".!frame.!canvas.!frame.!notebook.!frame.{line[0].lower()}").destroy()
            root.nametowidget(f".!frame.!canvas.!frame.!notebook.!frame.{line[0].lower()}Title").destroy()
            root.nametowidget(f".!frame.!canvas.!frame.!notebook.!frame.{line[0].lower()}Delete").destroy()
    #Here we open the same list CSV file, but for writing. 
    #It goes through each row in the "data" list variable created earlier and checks if the [0] position is equal to the fish name selected when this function was called.
    #If it doesnt equal, then it will write all the data to the file. This way, that specific fish is being left out and essentially removed from the program.
    with open("res/fish.csv", "w", newline='') as f:
        writer = csv.writer(f)
        for row in data:
            if row[0] != fish_name:
                writer.writerow(row)
    #Here we are deleting the fish's data file associated with it.
    #Essentially just checking if the file exists, if it does then remove it.
    if os.path.exists(f"res/FishData/{fish_name}.csv"):
        os.remove(f"res/FishData/{fish_name}.csv")
    else:
        print("File does not exist")
    #Resetting the X and Y coordinates for where the fish and labels are placed on the main screen. That way when we refresh, it doesnt start at the last position.
    x = 50
    y = 150
    #Resetting the fish_list array back to 0 for rewriting. (Also clearing that deleted fish out)
    fish_list = []
    #Re-running the readFish() function. This lights off the refresh process, in turn, re-rendering all the fish back onto the screen with the exception of the deleted one. 
    readFish()

#The addFish() function is used to display new fish on the main page and supply the buttons for deleting fish and opening new tabs.
#It has global x and y variables to other functions can manipulate the position and update it if a fish is deleted.
#Then it creates a name label for a title. Tries to get image selected. If no image is found it selects a default.
#Displays the image, info button and delete button. At the end it offsets the x and y coordinates to place the next fish in the correct place.
def addFish(fish_name, image):
    global x, y

    name = Label(frame1, text=fish_name, name=f"{fish_name.lower()}Title", font=courier_new, background="#333333", foreground="white")
    name.place(x = x + 2, y = y - 25)

    try:
        image_url = ImageTk.PhotoImage(Image.open(image).resize((300, 200)))
    except:
        image_url = ImageTk.PhotoImage(Image.open("res/img/betta.png").resize((300, 200)))
        print("No image provided. Selecting default image.")

    fish_img = Label(frame1, image=image_url, name=f"{fish_name.lower()}Img", background="#333333")
    fish_img.photo = image_url
    fish_img.place(x=x, y=y)
    
    info_button = Button(frame1, text=f"{fish_name}'s Info", name=f"{fish_name.lower()}", background="gray", foreground="white", font=courier_new3, command=lambda: openFishInfo(info_button._name[0].upper() + info_button._name[1:], image_url))
    info_button.place(x=x + 2, y=y + 205)

    delete_button = Button(frame1, text=f"Delete", name=f"{fish_name.lower()}Delete", background="#A52B2B", foreground="black", font=courier_new4, command=lambda: popUpConfirm(fish_name))#deleteFish(fish_name)
    delete_button.place(x=x + 250, y=y + 205)

    x += 360

    if (x >= mainWidth - 25):
        x = 50
        y += 265

#This function is called when you click the select_image button when adding a new fish.
#When this function is called. A dialog box is opened to allow the user to select an image to use.
#It renames the variable "selected_fish_image" to the file path of the image to later be used.
def openFishImage():
    global selected_fish_image
    root.filename = fd.askopenfilename(initialdir="res/img", title="~Select an image~", filetypes=(("~All Files~", "*.*"), (".png files", "*.png"), (".jpg files", "*.jpg")))
    selected_fish_image = root.filename

#appendFish() handles writing new fish to the CSV file so it can be read later.
#If the fish name is not already in the array "fish_list", it will continue.
#The data to be appened will be put into an array for insertion.
#Then append the row to the file and run the addFish() function to add it to screen.
def appendFish(fish_name, image):
    if fish_name not in fish_list:
        fish_list.append(fish_name)
        fish_data = [fish_name, image]
        with open('res/fish.csv', 'a', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(fish_data)
            addFish(fish_name, image)
    else:
        print("NEGATIVE GHOST RIDER")

#readFish() opens the main CSV list file to read all the fish names and image paths, then run the addFish() on each fish.
#During the loop process, it also adds just the fish name in each line to an array that will later be used to make sure the fish doesnt already exist.
def readFish():
    with open('res/fish.csv', 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for line in csv_reader:
            fish_list.append(line[0])
            addFish(line[0], line[1])

#Function to scroll the backend_canvas, only if you're on the main page. 
def _on_mouse_wheel(event):
    if notebook.index(notebook.select()) == 0:
        backend_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

#Render function is the main function. It creates the main frames and canvas needed to host the Notebook widget
#Also contains main page things in the GUI, as well as the scroll bar. 
#This function ultimately lights off the rest of the program. The add_element button is used to call appendFish() which will create new fish.
#At the end of this function we call the readFish() function. readFish() will start the process for displaying the fish on the screen.
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
