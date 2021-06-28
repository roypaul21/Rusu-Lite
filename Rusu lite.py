from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import mysql.connector
import webbrowser


mydb = mysql.connector.connect(
       host = "127.0.0.1",
       user = "root",
       password = "",
       database =  "rusulite",
       )
my_cursor = mydb.cursor()

start_p = Tk()
w = 860
h = 630
start_p.geometry(f'{w}x{h}+{250}+{40}')
start_p.overrideredirect(True)
start_p.configure(background="black")
start_p.resizable(False, False)

def mp():
    main_p = Tk()
    w = 860
    h = 630
    main_p.geometry(f'{w}x{h}+{250}+{40}')
    main_p.configure(background="black")
    main_p.resizable(False, False)
    main_p.overrideredirect(True)


    #add movie function
    def add_movie():
        main_p.destroy()
        root2 = Tk()
        w = 860
        h = 630
        root2.geometry(f'{w}x{h}+{250}+{40}')
        root2.configure(background="black")
        root2.resizable(False, False)
        root2.overrideredirect(True)

        def reg_movie():
            my_cursor = mydb.cursor()

            #Insert value into actor table
            sql = "INSERT INTO actor(name, age, birthday, gender)" "VALUES (%s, %s, %s, %s)"
            value =(a_name.get(), a_age.get(), a_birth.get(), a_gender.get())
            my_cursor.execute(sql,value)

            # Insert value into director table
            sql2 = "INSERT INTO director (name, age, birthday, gender)" "VALUES (%s, %s, %s, %s)"
            value2 = (d_name.get(), d_age.get(), d_birth.get(), d_gender.get())
            my_cursor.execute(sql2, value2)

            # Insert value into image table
            sql3 = "INSERT INTO director (image_name)" "VALUES (%s)"
            value3 = (image_entry.get())
            my_cursor.execute(sql3, value3)

            mydb.commit()







        lbl1 = Label(root2, text="Movie Registration Form", font=('helvetica', 30, 'bold'), bg='black', fg='orange')
        lbl1.place(x=200,y=20)


        lbl = Label(root2,bg="black")
        lbl.place(x=30, y=65)



        image_entry = Entry(root2)
        image_entry.place(x=-100, y=-100)

        def add_image():
            fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("PNG File", "*.png"),("All Files",'*.*')))
            img = Image.open(fln)
            img = ImageTk.PhotoImage(img)
            lbl.configure(image=img)
            lbl.image = img

            name_image = os.path.basename(fln)

            print(name_image)

            image_entry.insert(0, name_image)




        browse_btn = Button(root2, text="BROWSE IMAGE", compound=CENTER, bg="orange", borderwidth=2,
                              activebackground="black", command=add_image)
        browse_btn.place(x=300, y=112)


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

        horror = Checkbutton(root2, text="Horror", bg="black", fg="orange",activebackground="black")
        horror.place(x=50,y=320)
        romance = Checkbutton(root2, text="Romance", bg="black", fg="orange", activebackground="black")
        romance.place(x=160, y=320)
        comedy = Checkbutton(root2, text="Comedy", bg="black", fg="orange", activebackground="black")
        comedy.place(x=270, y=320)
        action = Checkbutton(root2, text="Action", bg="black", fg="orange", activebackground="black")
        action.place(x=50, y=377)
        drama = Checkbutton(root2, text="Drama", bg="black", fg="orange", activebackground="black")
        drama.place(x=160, y=377)
        mystery = Checkbutton(root2, text="Mystery", bg="black", fg="orange", activebackground="black")
        mystery.place(x=270, y=377)
        animation = Checkbutton(root2, text="Animated", bg="black", fg="orange", activebackground="black")
        animation.place(x=50, y=434)
        scifi = Checkbutton(root2, text="SciFi", bg="black", fg="orange", activebackground="black")
        scifi.place(x=160, y=434)
        fantasy = Checkbutton(root2, text="Fantasy", bg="black", fg="orange", activebackground="black")
        fantasy.place(x=270, y=434)

        add_m = Button(root2, text="REGISTER MOVIE", bg="gold", command=reg_movie)
        add_m.place(x=750, y=590)

        def des3():
            root2.destroy()
            mp()

        back = Button(root2, text="RETURN", bg="gray",fg="red", command=des3)
        back.place(x=680,y=590)

        root2.mainloop()


    def search():
            search_p = Tk()
            w = 860
            h = 630
            search_p.geometry(f'{w}x{h}+{250}+{40}')
            search_p.overrideredirect(True)
            search_p.configure(background="black")
            search_p.resizable(False, False)

            x=2
            for i in range(x):


                c3 = PhotoImage(file="her.png")
                movie_btn = Button(search_p, image=c3, compound=CENTER, bg="#161618", borderwidth=0,
                                   activebackground="#161618")
                movie_btn.grid(row=i, column=0, pady=30, padx=50)





            search_p.mainloop()


    #specific search function
    def specific_search():
        root3 = Tk()
        w = 400
        h = 400
        root3.geometry(f'{w}x{h}+{480}+{120}')
        root3.configure(background="black")
        root3.resizable(False, False)
        root3.overrideredirect(True)


        yr = ttk.Combobox(root3, width=20)
        yr.set("Year")
        yr['values'] = ("2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013")
        yr.place(x=30, y=80)

        actor = ttk.Combobox(root3, width=20)
        actor.set("Actor")
        actor['values'] = ("JohnnyDepp")
        actor.place(x=230, y=80)

        director = ttk.Combobox(root3, width=20)
        director.set("Director")
        director['values'] = ("Tim Burton")
        director.place(x=30, y=110)

        country = ttk.Combobox(root3, width=20)
        country.set("Country")
        country['values'] = ("Philippines")
        country.place(x=230, y=110)

        #Check box
        horror = Checkbutton(root3, text="Horror", bg="black", fg="orange", activebackground="black")
        horror.place(x=50, y=180)
        romance = Checkbutton(root3, text="Romance", bg="black", fg="orange", activebackground="black")
        romance.place(x=160, y=180)
        comedy = Checkbutton(root3, text="Comedy", bg="black", fg="orange", activebackground="black")
        comedy.place(x=270, y=180)
        action = Checkbutton(root3, text="Action", bg="black", fg="orange", activebackground="black")
        action.place(x=50, y=220)
        drama = Checkbutton(root3, text="Drama", bg="black", fg="orange", activebackground="black")
        drama.place(x=160, y=220)
        mystery = Checkbutton(root3, text="Mystery", bg="black", fg="orange", activebackground="black")
        mystery.place(x=270, y=220)
        animation = Checkbutton(root3, text="Animated", bg="black", fg="orange", activebackground="black")
        animation.place(x=50, y=260)
        scifi = Checkbutton(root3, text="SciFi", bg="black", fg="orange", activebackground="black")
        scifi.place(x=160, y=260)
        fantasy = Checkbutton(root3, text="Fantasy", bg="black", fg="orange", activebackground="black")
        fantasy.place(x=270, y=260)

        def des4():
            main_p.destroy()
            root3.destroy()
            search()


        search_btn = Button(root3, bg="orange",text="Search", borderwidth=5, activebackground="black", command=des4)
        search_btn.place(x=180, y=320)

        back = Button(root3, text="Return", bg="gray", command=root3.destroy)
        back.place(x=10, y=360)

        root3.mainloop()


    # Entry search box
    search_entry = Entry(main_p, width=30, bg='light goldenrod')
    search_entry.place(x=330, y=50)

    ms = ImageTk.PhotoImage(Image.open('minisearch.png'))
    ms_lbl = Label(main_p, image=ms, bg="black")
    ms_lbl.place(x=290, y=44)

    # rusu lite logo image
    rusu = ImageTk.PhotoImage(Image.open('miming.png'))
    rusu_logo = Label(main_p, image=rusu, bg="black")
    rusu_logo.place(x=0, y=0)

    def des5():
        if search_entry.get() == "":
            return messagebox.showwarning("SEARCH WARNING","NO INPUT ON THE ENTRY")
        else:
             main_p.destroy()
             search()





    # search button
    s = ImageTk.PhotoImage(Image.open('searchbtn.png'))
    search_btn = Button(main_p, image=s, compound=CENTER, bg="black", borderwidth=0
                        , activebackground="black", command=des5)
    search_btn.place(x=360, y=80)



    #add movie page button
    add_movie_btn = Button(main_p, text="ADD MOVIE", bg="black", fg="white", command=add_movie, borderwidth=5)
    add_movie_btn.place(x=700,y=50)

    #Specific Search
    add_movie_btn = Button(main_p, text="Specific Search", bg="orange",borderwidth=5, command=specific_search)
    add_movie_btn.place(x=375, y=136)







    '''
    #movie main page button
    def des():
        main_p.destroy()

    c3 = PhotoImage(file=)
    movie_btn = Button(main_p, image=c3, compound=CENTER, bg="#161618", borderwidth=0,
                         activebackground="#161618", command=lambda: [des(), movie()])
    movie_btn.place(x=50, y=350)
    '''




    main_p.mainloop()




def des():
    start_p.destroy()

start_p.after(2000, lambda :(des(), mp()))

start_p.mainloop()
