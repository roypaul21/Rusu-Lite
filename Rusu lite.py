from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import mysql.connector
import webbrowser

main_p.destroy()
root2 = Tk()
w = 860
h = 630
root2.geometry(f'{w}x{h}+{250}+{40}')
root2.configure(background="black")
root2.resizable(False, False)
root2.overrideredirect(True)

lbl1 = Label(root2, text="Movie Registration Form", font=('helvetica', 30, 'bold'), bg='black', fg='orange')
lbl1.place(x=200,y=20)

lbl = Label(root2,bg="black")
lbl.place(x=30, y=65)

browse_btn = Button(root2, text="BROWSE IMAGE", compound=CENTER, bg="orange", borderwidth=2,
                              activebackground="black", command=add_image)
browse_btn.place(x=300, y=112)

t_lbl = Label(root2, text="MOVIE TITLE:", bg='black', fg="orange")
        t_lbl.place(x=600, y=400)
        title = Entry(root2, width=20)
        title.place(x=576, y=430)


        d_lbl= Label(root2,text="DIRECTOR:", bg='black', fg="orange")
        d_lbl.place(x=500,y=90)
        d_name = Entry(root2,width=20)
        d_name.place(x=467,y=115)

        d_age = Entry(root2,width=20)
        d_age.place(x=467,y=165)

        d_birth = Entry(root2,width=20)
        d_birth.place(x=467,y=215)

        d_gender = ttk.Combobox(root2, width=17)
        d_gender.set("Gender")
        d_gender['values'] = ("Male", "Female", "Transgender", "Gender queer", "Gender Neutral", "Others")
        d_gender.place(x=467, y=265)



        a_lbl = Label(root2, text="ACTOR:", bg='black', fg="orange")
        a_lbl.place(x=720, y=90)
        a_name = Entry(root2, width=20)
        a_name.place(x=680, y=115)

        a_age = Entry(root2, width=20)
        a_age.place(x=680, y=165)

        a_birth = Entry(root2, width=20)
        a_birth.place(x=680, y=215)

        a_gender = ttk.Combobox(root2, width=17)
        a_gender.set("Gender")
        a_gender['values'] = ("Male", "Female", "Transgender", "Gender queer", "Gender Neutral", "Others")
        a_gender.place(x=680, y=265)

        #Label
        c_lbl = Label(root2, text="NAME", bg='black', fg="orange")
        c_lbl.place(x=619, y=115)
        c_lbl = Label(root2, text="AGE", bg='black', fg="orange")
        c_lbl.place(x=622, y=165)
        c_lbl = Label(root2, text="B-DATE", bg='black', fg="orange")
        c_lbl.place(x=611, y=215)
        c_lbl = Label(root2, text="GENDER", bg='black', fg="orange")
        c_lbl.place(x=610, y=265)


        c_lbl = Label(root2, text="COUNTRY:", bg='black', fg="orange")
        c_lbl.place(x=500, y=330)
        country_entry = Entry(root2, width=20)
        country_entry.place(x=467, y=350)

        y_lbl = Label(root2, text="YEAR:", bg='black', fg="orange")
        y_lbl.place(x=720, y=330)
        year_entry = Entry(root2, width=20)
        year_entry.place(x=680, y=350)


        dc_lbl = Label(root2, text="DESCRIPTION:", bg='black', fg="orange")
        dc_lbl.place(x=30, y=505)
        description_text = Text(root2, height=5, width=70)
        description_text.place(x=30,y=530)

        #genre checkbox
        frm = Frame(root2, width=350, height=195, highlightbackground="orange", highlightthickness=1, bg="black")
        frm.place(x=30,y=300)

        h = StringVar()
        r = StringVar()
        c = StringVar()
        a = StringVar()
        d = StringVar()
        m = StringVar()
        an = StringVar()
        s = StringVar()
        f = StringVar()

        horror = Checkbutton(root2, text="Horror", bg="black", fg="orange",activebackground="black", variable=h, onvalue="Horror", offvalue="")
        horror.place(x=50,y=320)
        romance = Checkbutton(root2, text="Romance", bg="black", fg="orange", activebackground="black", variable=r, onvalue="Romance", offvalue="")
        romance.place(x=160, y=320)
        comedy = Checkbutton(root2, text="Comedy", bg="black", fg="orange", activebackground="black", variable=c, onvalue="Comedy", offvalue="")
        comedy.place(x=270, y=320)
        action = Checkbutton(root2, text="Action", bg="black", fg="orange", activebackground="black", variable=a, onvalue="Action", offvalue="")
        action.place(x=50, y=377)
        drama = Checkbutton(root2, text="Drama", bg="black", fg="orange", activebackground="black", variable=d, onvalue="Drama", offvalue="")
        drama.place(x=160, y=377)
        mystery = Checkbutton(root2, text="Mystery", bg="black", fg="orange", activebackground="black", variable=m, onvalue="Mystery", offvalue="")
        mystery.place(x=270, y=377)
        animation = Checkbutton(root2, text="Animated", bg="black", fg="orange", activebackground="black", variable=an, onvalue="Animated", offvalue="")
        animation.place(x=50, y=434)
        scifi = Checkbutton(root2, text="SciFi", bg="black", fg="orange", activebackground="black", variable=s, onvalue="SciFi", offvalue="")
        scifi.place(x=160, y=434)
        fantasy = Checkbutton(root2, text="Fantasy", bg="black", fg="orange", activebackground="black", variable=f, onvalue="Fantasy", offvalue="")
        fantasy.place(x=270, y=434)

        add_m = Button(root2, text="REGISTER MOVIE", bg="gold")
        add_m.place(x=750, y=590)

        def des3():
            root2.destroy()
            mp()

        back = Button(root2, text="RETURN", bg="gray",fg="red")
        back.place(x=680,y=590)

        root2.mainloop()
        
              
              
