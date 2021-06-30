from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os
import webbrowser


def add():
    root2 = Tk()
    w = 1000
    h = 700
    root2.geometry(f'{w}x{h}+{250}+{3}')
    root2.configure(background="black")
    root2.attributes("-fullscreen", True)
    # root2.resizable(False, False)
    # root2.overrideredirect(True)

    lbl1 = Label(root2, text="Movie Registration Form", font=('Cooper Black', 30, 'bold'), bg='black', fg='orange')
    lbl1.pack(side = TOP)

    frm_image = Frame(root2, width=200, height=227, highlightbackground="orange", highlightthickness=1, bg="black")
    frm_image.place(x=950, y=305)

    lbl = Label(frm_image, bg="black")
    lbl.place(x=0, y=0)

    browse_btn = Button(root2, text="BROWSE IMAGE", compound=CENTER, font=('Comic Sans MS', 10), bg="orange",
                        borderwidth=2)
    browse_btn.place(x=995, y=400)

    # DIRECTOR 1
    frm_drctr = Frame(root2, width=385, height=200, highlightbackground="orange", highlightthickness=1, bg="black")
    frm_drctr.place(x=195, y=100)

    d_lbl = Label(root2, text="DIRECTOR 1 NAME:", font=('Cooper Black', 11), bg='black', fg="orange")
    d_lbl.place(x=200, y=90)
    d_name = Entry(root2, width=20, font=('Comic Sans MS', 10))
    d_name.place(x=205, y=115)

    d_lbl1 = Label(root2, text="AGE:", font=('Cooper Black', 11), bg='black', fg="orange")
    d_lbl1.place(x=200, y=140)
    d_age = Entry(root2, width=20, font=('Comic Sans MS', 10))
    d_age.place(x=205, y=165)

    d_lbl2 = Label(root2, text="BIRTHDATE:", font=('Cooper Black', 11), bg='black', fg="orange")
    d_lbl2.place(x=200, y=190)
    d_birth = Entry(root2, width=20, font=('Comic Sans MS', 10))
    d_birth.place(x=205, y=215)

    d_lbl3 = Label(root2, text="GENDER:", font=('Cooper Black', 11), bg='black', fg="orange")
    d_lbl3.place(x=200, y=240)
    d_gender = ttk.Combobox(root2, width=18, font=('Comic Sans MS', 10))
    d_gender.set("Gender")
    d_gender['values'] = ("Male", "Female", "Transgender", "Gender queer", "Gender Neutral", "Others")
    d_gender.place(x=205, y=265)

    # DIRECTOR 2
    d_lbl4 = Label(root2, text="DIRECTOR 2 NAME:", font=('Cooper Black', 11), bg='black', fg="orange")
    d_lbl4.place(x=400, y=90)
    d_name = Entry(root2, width=20, font=('Comic Sans MS', 10))
    d_name.place(x=405, y=115)

    d_lbl5 = Label(root2, text="AGE:", font=('Cooper Black', 11), bg='black', fg="orange")
    d_lbl5.place(x=400, y=140)
    d_age = Entry(root2, width=20, font=('Comic Sans MS', 10))
    d_age.place(x=405, y=165)

    d_lbl6 = Label(root2, text="BIRTHDATE:", font=('Cooper Black', 11), bg='black', fg="orange")
    d_lbl6.place(x=400, y=190)
    d_birth = Entry(root2, width=20, font=('Comic Sans MS', 10))
    d_birth.place(x=405, y=215)

    d_lbl7 = Label(root2, text="GENDER:", font=('Cooper Black', 11), bg='black', fg="orange")
    d_lbl7.place(x=400, y=240)
    d_gender = ttk.Combobox(root2, width=18, font=('Comic Sans MS', 10))
    d_gender.set("Gender")
    d_gender['values'] = ("Male", "Female", "Transgender", "Gender queer", "Gender Neutral", "Others")
    d_gender.place(x=405, y=265)

    # ACTOR 1
    frm_actr = Frame(root2, width=385, height=200, highlightbackground="orange", highlightthickness=1, bg="black")
    frm_actr.place(x=195, y=330)

    a_lbl = Label(root2, text="ACTOR 1 NAME:", font=('Cooper Black', 11), bg='black', fg="orange")
    a_lbl.place(x=200, y=320)
    a_name = Entry(root2, width=20, font=('Comic Sans MS', 10))
    a_name.place(x=205, y=345)

    a_lbl1 = Label(root2, text="AGE:", font=('Cooper Black', 11), bg='black', fg="orange")
    a_lbl1.place(x=200, y=370)
    a_age = Entry(root2, width=20, font=('Comic Sans MS', 10))
    a_age.place(x=205, y=395)

    a_lbl2 = Label(root2, text="BIRTHDATE:", font=('Cooper Black', 11), bg='black', fg="orange")
    a_lbl2.place(x=200, y=420)
    a_birth = Entry(root2, width=20, font=('Comic Sans MS', 10))
    a_birth.place(x=205, y=445)

    a_lbl3 = Label(root2, text="GENDER:", font=('Cooper Black', 11), bg='black', fg="orange")
    a_lbl3.place(x=200, y=470)
    a_gender = ttk.Combobox(root2, width=18, font=('Comic Sans MS', 10))
    a_gender.set("Gender")
    a_gender['values'] = ("Male", "Female", "Transgender", "Gender queer", "Gender Neutral", "Others")
    a_gender.place(x=205, y=495)

    # ACTOR 2
    a_lbl = Label(root2, text="ACTOR 2 NAME:", font=('Cooper Black', 11), bg='black', fg="orange")
    a_lbl.place(x=400, y=320)
    a_name = Entry(root2, width=20, font=('Comic Sans MS', 10))
    a_name.place(x=405, y=345)

    a_lbl1 = Label(root2, text="AGE:", font=('Cooper Black', 11), bg='black', fg="orange")
    a_lbl1.place(x=400, y=370)
    a_age = Entry(root2, width=20, font=('Comic Sans MS', 10))
    a_age.place(x=405, y=395)

    a_lbl2 = Label(root2, text="BIRTHDATE:", font=('Cooper Black', 11), bg='black', fg="orange")
    a_lbl2.place(x=400, y=420)
    a_birth = Entry(root2, width=20, font=('Comic Sans MS', 10))
    a_birth.place(x=405, y=445)

    a_lbl3 = Label(root2, text="GENDER:", font=('Cooper Black', 11), bg='black', fg="orange")
    a_lbl3.place(x=400, y=470)
    a_gender = ttk.Combobox(root2, width=18, font=('Comic Sans MS', 10))
    a_gender.set("Gender")
    a_gender['values'] = ("Male", "Female", "Transgender", "Gender queer", "Gender Neutral", "Others")
    a_gender.place(x=405, y=495)

    # YEAR
    ycmt_image = Frame(root2, width=183, height=200, highlightbackground="orange", highlightthickness=1, bg="black")
    ycmt_image.place(x=960, y=100)
    y_lbl = Label(root2, text="YEAR:", font=('Cooper Black', 11), bg='black', fg="orange")
    y_lbl.place(x=965, y=90)
    year_entry = Entry(root2, width=20, font=('Comic Sans MS', 10))
    year_entry.place(x=970, y=115)

     # COUNTRY
    c_lbl = Label(root2, text="COUNTRY:", font=('Cooper Black', 11), bg='black', fg="orange")
    c_lbl.place(x=965, y=160)
    country_entry = Entry(root2, width=20, font=('Comic Sans MS', 10))
    country_entry.place(x=970, y=185)

    # MOVIE TITLE
    t_lbl = Label(root2, text="MOVIE TITLE:", font=('Cooper Black', 11), bg='black', fg="orange")
    t_lbl.place(x=965, y=230)
    title = Entry(root2, width=20, font=('Comic Sans MS', 10))
    title.place(x=970, y=255)

    # LINK
    url_image = Frame(root2, width=965, height=50, highlightbackground="orange", highlightthickness=1, bg="black")
    url_image.place(x=190, y=575)
    lnk_lbl = Label(root2, text="LINK/URL:", font=('Cooper Black', 14), bg='black', fg="orange")
    lnk_lbl.place(x=200, y=560)
    link = Entry(root2, width=117, font=('Comic Sans MS', 10))
    link.place(x=201, y=590)

    # DESCRIPTION
    dscrptn_image = Frame(root2, width=350, height=210, highlightbackground="orange", highlightthickness=1, bg="black")
    dscrptn_image.place(x=590, y=320)
    dc_lbl = Label(root2, text="DESCRIPTION:", font=('Cooper Black', 12), bg='black', fg="orange")
    dc_lbl.place(x=599, y=310)
    description_text = Text(root2, height=9, width=41, font=('Comic Sans MS', 10))
    description_text.place(x=599, y=350)

    # GENRE
    frm = Frame(root2, width=345, height=200, highlightbackground="orange", highlightthickness=1, bg="black")
    frm.place(x=600, y=100)
    gnr_lbl = Label(root2, text="GENRE:", font=('Cooper Black', 12), bg='black', fg="orange")
    gnr_lbl.place(x=610, y=90)

    h = StringVar()
    r = StringVar()
    c = StringVar()
    a = StringVar()
    d = StringVar()
    m = StringVar()
    an = StringVar()
    s = StringVar()
    f = StringVar()
    t = StringVar()

    horror = Checkbutton(root2, text="Horror", bg="black", fg="orange", activebackground="black", variable=h,
                         onvalue="Horror", offvalue="")
    horror.place(x=625, y=140)

    romance = Checkbutton(root2, text="Romance", bg="black", fg="orange", activebackground="black", variable=r,
                          onvalue="Romance", offvalue="")
    romance.place(x=625, y=195)
    comedy = Checkbutton(root2, text="Comedy", bg="black", fg="orange", activebackground="black", variable=c,
                         onvalue="Comedy", offvalue="")
    comedy.place(x=625, y=250)

    action = Checkbutton(root2, text="Action", bg="black", fg="orange", activebackground="black", variable=a,
                         onvalue="Action", offvalue="")
    action.place(x=740, y=140)

    drama = Checkbutton(root2, text="Drama", bg="black", fg="orange", activebackground="black", variable=d,
                        onvalue="Drama",
                        offvalue="")
    drama.place(x=740, y=195)

    animation = Checkbutton(root2, text="Animated", bg="black", fg="orange", activebackground="black", variable=an,
                            onvalue="Animated", offvalue="")
    animation.place(x=740, y=250)

    scifi = Checkbutton(root2, text="SciFi", bg="black", fg="orange", activebackground="black", variable=s,
                        onvalue="SciFi",
                        offvalue="")
    scifi.place(x=850, y=140)

    fantasy = Checkbutton(root2, text="Fantasy", bg="black", fg="orange", activebackground="black", variable=f,
                          onvalue="Fantasy", offvalue="")
    fantasy.place(x=850, y=195)

    mystery = Checkbutton(root2, text="Mystery", bg="black", fg="orange", activebackground="black", variable=m,
                          onvalue="Mystery", offvalue="")
    mystery.place(x=850, y=250)

    add_m = Button(root2, text="REGISTER MOVIE", font=('Comic Sans MS', 16), bg="orange")
    add_m.place(x=570, y=650)

    def des3():
        root2.destroy()

    back = Button(root2, text="RETURN", font=('Comic Sans MS', 10), bg="orange", fg="black", command=des3)
    back.place(x=5, y=5)

    root2.mainloop()

add()
