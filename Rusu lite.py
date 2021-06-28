from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import webbrowser

root2 = Tk()
w = 860
h = 630
root2.geometry(f'{w}x{h}+{250}+{40}')
root2.configure(background="black")
root2.resizable(False, False)
root2.overrideredirect(True)

lbl1 = Label(root2, text="Movie Registration Form", font=('Cooper Black', 30, 'bold'), bg='black', fg='orange')
lbl1.place(x=150, y=20)

lbl = Label(root2, bg="black")
lbl.place(x=30, y=65)

#IMAGE
frm_image = Frame(root2, width=190, height=210, highlightbackground="orange", highlightthickness=1, bg="black")
frm_image.place(x=655, y=300)
browse_btn = Button(root2, text="BROWSE IMAGE", compound=CENTER, font=('Comic Sans MS', 10),  bg="orange", borderwidth=2)
browse_btn.place(x=693, y=520)

#DIRECTOR
d_lbl = Label(root2, text="DIRECTOR'S NAME:", font=('Cooper Black', 11), bg='black', fg="orange")
d_lbl.place(x=5, y=90)
d_name = Entry(root2, width=20, font=('Comic Sans MS', 10))
d_name.place(x=10, y=115)

d_lbl1 = Label(root2, text="AGE:", font=('Cooper Black', 11), bg='black', fg="orange")
d_lbl1.place(x=5, y=140)
d_age = Entry(root2, width=20, font=('Comic Sans MS', 10))
d_age.place(x=10, y=165)

d_lbl2 = Label(root2, text="BIRTHDATE:", font=('Cooper Black', 11), bg='black', fg="orange")
d_lbl2.place(x=5, y=190)
d_birth = Entry(root2, width=20, font=('Comic Sans MS', 10))
d_birth.place(x=10, y=215)

d_lbl3 = Label(root2, text="GENDER:",font=('Cooper Black', 11), bg='black', fg="orange")
d_lbl3.place(x=5, y=240)
d_gender = ttk.Combobox(root2, width=18, font=('Comic Sans MS', 10))
d_gender.set("Gender")
d_gender['values'] = ("Male", "Female", "Transgender", "Gender queer", "Gender Neutral", "Others")
d_gender.place(x=10, y=265)

#ACTOR
a_lbl = Label(root2, text="ACTOR'S NAME:", font=('Cooper Black', 11), bg='black', fg="orange")
a_lbl.place(x=200, y=90)
a_name = Entry(root2, width=20, font=('Comic Sans MS', 10))
a_name.place(x=205, y=115)

a_lbl1 = Label(root2, text="AGE:", font=('Cooper Black', 11), bg='black', fg="orange")
a_lbl1.place(x=200, y=140)
a_age = Entry(root2, width=20, font=('Comic Sans MS', 10))
a_age.place(x=205, y=165)

a_lbl2 = Label(root2, text="BIRTHDATE:",font=('Cooper Black', 11),  bg='black', fg="orange")
a_lbl2.place(x=200, y=190)
a_birth = Entry(root2, width=20, font=('Comic Sans MS', 10))
a_birth.place(x=205, y=215)

a_lbl3 = Label(root2, text="GENDER:",font=('Cooper Black', 11),  bg='black', fg="orange")
a_lbl3.place(x=200, y=240)
a_gender = ttk.Combobox(root2, width=18, font=('Comic Sans MS', 10))
a_gender.set("Gender")
a_gender['values'] = ("Male", "Female", "Transgender", "Gender queer", "Gender Neutral", "Others")
a_gender.place(x=205, y=265)

#YEAR
y_lbl = Label(root2, text="YEAR:", font=('Cooper Black', 11), bg='black', fg="orange")
y_lbl.place(x=665, y=90)
year_entry = Entry(root2, width=20, font=('Comic Sans MS', 10))
year_entry.place(x=670, y=115)

#COUNTRY
c_lbl = Label(root2, text="COUNTRY:", font=('Cooper Black', 11), bg='black', fg="orange")
c_lbl.place(x=665, y=150)
country_entry = Entry(root2, width=20, font=('Comic Sans MS', 10))
country_entry.place(x=670, y=175)

#MOVIE TITLE
t_lbl = Label(root2, text="MOVIE TITLE:", font=('Cooper Black', 11), bg='black', fg="orange")
t_lbl.place(x=665, y=210)
title = Entry(root2, width=20, font=('Comic Sans MS', 10))
title.place(x=670, y=235)

#LINK
lnk_lbl = Label(root2, text="LINK/URL:", font=('Cooper Black', 14), bg='black', fg="orange")
lnk_lbl.place(x=23, y=320)
link = Entry(root2, width=75, font=('Comic Sans MS', 10))
link.place(x=30, y=350)

#DESCRIPTION
dc_lbl = Label(root2, text="DESCRIPTION:", font=('Cooper Black', 14), bg='black', fg="orange")
dc_lbl.place(x=23, y=380)
description_text = Text(root2, height=11, width=75, font=('Comic Sans MS', 10))
description_text.place(x=30, y=410)

#GENRE
gnr_lbl = Label(root2, text="GENRE:", font=('Cooper Black', 12), bg='black', fg="orange")
gnr_lbl.place(x=420, y=90)
frm = Frame(root2, width=200, height=195, highlightbackground="orange", highlightthickness=1, bg="black")
frm.place(x=420, y=113)

h = StringVar()
r = StringVar()
c = StringVar()
a = StringVar()
d = StringVar()
m = StringVar()
an = StringVar()
s = StringVar()
f = StringVar()

horror = Checkbutton(root2, text="Horror", bg="black", fg="orange", activebackground="black", variable=h,
                     onvalue="Horror", offvalue="")
horror.place(x=430, y=120)

romance = Checkbutton(root2, text="Romance", bg="black", fg="orange", activebackground="black", variable=r,
                      onvalue="Romance", offvalue="")
romance.place(x=430, y=155)
comedy = Checkbutton(root2, text="Comedy", bg="black", fg="orange", activebackground="black", variable=c,
                     onvalue="Comedy", offvalue="")
comedy.place(x=430, y=190)

action = Checkbutton(root2, text="Action", bg="black", fg="orange", activebackground="black", variable=a,
                     onvalue="Action", offvalue="")
action.place(x=430, y=225)

drama = Checkbutton(root2, text="Drama", bg="black", fg="orange", activebackground="black", variable=d, onvalue="Drama",
                    offvalue="")
drama.place(x=430, y=260)

animation = Checkbutton(root2, text="Animated", bg="black", fg="orange", activebackground="black", variable=an,
                        onvalue="Animated", offvalue="")
animation.place(x=520, y=120)

scifi = Checkbutton(root2, text="SciFi", bg="black", fg="orange", activebackground="black", variable=s, onvalue="SciFi",
                    offvalue="")
scifi.place(x=520, y=155)

fantasy = Checkbutton(root2, text="Fantasy", bg="black", fg="orange", activebackground="black", variable=f,
                      onvalue="Fantasy", offvalue="")
fantasy.place(x=520, y=190)

thriller = Checkbutton(root2, text="Thriller", bg="black", fg="orange", activebackground="black", variable=f,
                      onvalue="Fantasy", offvalue="")
thriller.place(x=520, y=225)

mystery = Checkbutton(root2, text="Mystery", bg="black", fg="orange", activebackground="black", variable=m,
                      onvalue="Mystery", offvalue="")
mystery.place(x=520, y=260)

add_m = Button(root2, text="REGISTER MOVIE", font=('Comic Sans MS', 10), bg="orange")
add_m.place(x=689, y=580)


def des3():
    root2.destroy()

back = Button(root2, text="RETURN", font=('Comic Sans MS', 10), bg="orange", fg="black")
back.place(x=5, y=5)

root2.mainloop()
