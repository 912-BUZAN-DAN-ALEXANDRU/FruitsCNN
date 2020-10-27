import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy
import os

from keras.models import load_model






classes = {  0:"Mar Braeburn",
             1:"Mar Crimson Snow",
             2:"Mar Golden",
             3:"Mar Golden",
             4:"Mar Golden",
             5:"Mar Granny Smith",
             6:"Mar Pink Lady",
             7:"Mar Rosu",
             8:"Mar Rosu",
             9:"Mar Rosu",
             10:"Mar Rosu Delicios",
             11:"Mar Golden Delicios",
             12:"Mar Golden Delicios",
             13:"Caise",
             14:"Avocado",
             15:"Avocado",
             16:"Banana",
             17:"Banana",
             18:"Banana Rosie",
             19:"Sfecla",
             20:"Coacaze",
             21:"Opuntia/Fruct de cactus",
             22:"Cantalup",
             23:"Cantalup",
             24:"Carambola",
             25:"Conopida",
             26:"Cirese",
             27:"Cirese",
             28:"Cirese Rainier",
             29:"Cirese Negre",
             30:"Visine",
             31:"Cirese Galbene",
             32:"Castane",
             33:"Clementine",
             34:"Cocos",
             35:"Curmale",
             36:"Vinete",
             37:"Ghimbir",
             38:"Granadila",
             39:"Struguri Negri",
             40:"Struguri Rose",
             41:"Struguri Albi",
             42:"Struguri Albi",
             43:"Struguri Albi",
             44:"Struguri Albi",
             45:"Grepfruit Roz",
             46:"Grepfruit Alb",
             47:"Guava",
             48:"Alune",
             49:"Afine",
             50:"Kaki",
             51:"Kiwi",
             52:"Kohlrabi",
             53:"Kumquat",
             54:"Lamaie",
             55:"Lamaie Meyer",
             56:"Lime",
             57:"Lici",
             58:"Mandarine",
             59:"Mango",
             60:"Mango Rosu",
             61:"Mangustan",
             62:"Fructul Pasiunii",
             63:"Pepenele lui Mos Craciun/Pel de Sapo",
             64:"Mure",
             65:"Nectarina",
             66:"Nectarina plata",
             67:"Alune de padure",
             68:"Nuci Pecan",
             69:"Ceapa Rosie",
             70:"Ceapa Rosie",
             71:"Ceapa Alba",
             72:"Portocala",
             73:"Papaya",
             74:"Fructul Pasiunii",
             75:"Piersica",
             76:"Piersica",
             77:"Piersica plata",
             78:"Para",
             79:"Para Abate",
             80:"Para Forelle",
             81:"Para Kaiser",
             82:"Para",
             83:"Para Rosie",
             84:"Para Williams",
             85:"Pepino",
             86:"Ardei Gras Verde",
             87: "Ardei Gras Rosu",
             88: "Ardei Gras Galben",
             89:"Physalis",
             90:"Physalis",
             91:"Ananas",
             92:"Ananas",
             93:"Pitahaya/Fructul Dragonului",
             94:"Pruna",
             95:"Pruna",
             96:"Pruna",
             97:"Rodie",
             98:"Pomelo",
             99:"Cartof Rosu",
             100:"Cartof Rosu",
             101:"Cartof Dulce",
             102:"Cartof Alb",
             103:"Gutuie",
             104:"Rambutan",
             105:"Zmeura",
             106:"Coacaz Rosu",
             107:"Salak",
             108:"Capsune",
             109:"Capsune",
             110:"Tamarillo",
             111:"Tangelo",
             112:"Rosie",
             113:"Rosie",
             114:"Rosie",
             115:"Rosie",
             116:"Rosie Cherry",
             117:"Rosie Neagra",
             118:"Rosie Galbena",
             119:"Nuci"
             }

model = load_model(os.getcwd() + '/' + 'fruit&veggies_classifier.h5')

top = tk.Tk()
top.geometry("800x600")
top.title('Legume si fructe')
top.configure(background="#AFEEEE")
label=Label(top,background='#AFEEEE', font=('arial',20,'bold'))
food_image = Label(top)

def classify(file_path):
    global label_packed
    image = Image.open(file_path).convert('RGB').resize((100,100))

    im = numpy.array(image) / 255.0 - 0.5
    im = numpy.expand_dims(im, axis=0)
    pred = model.predict_classes(im)[0]
    food = classes[pred]
    print(pred)
    label.configure(foreground='#011638', text=food)

def show_classify_button(file_path):
    classify_b=Button(top,text="Cauta",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(font=('arial',15,'bold'))
    classify_b.place(relx=0.45,rely=0.95)

def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25), (top.winfo_height()/2.25)))
        im = ImageTk.PhotoImage(uploaded)
        food_image.configure(image=im)
        food_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass



upload=Button(top,text="Incarca o imagine",command=upload_image,padx=10,pady=5)
upload.configure(background='#AFEEEE', foreground='black',font=('arial',15,'bold'))
upload.pack(side=BOTTOM,pady=50)
food_image.pack(side=BOTTOM, expand = True)
label.pack(side=TOP, expand=True)
top.mainloop()
