from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import mysql.connector
import webbrowser
import glob
import re
from collections import OrderedDict
import itertools

mydb = mysql.connector.connect(
       host = "127.0.0.1",
       user = "root",
       password = "",
       database =  "rusu",
       )
my_cursor = mydb.cursor()

start_p = Tk()
w = 860
h = 630
start_p.geometry(f'{w}x{h}+{250}+{40}')
start_p.overrideredirect(True)
start_p.configure(background="black")
start_p.resizable(False, False)
style = ttk.Style()
style.theme_use('clam')
start_p.attributes('-alpha', 0.7)

# sis Gif animation
frameCnt = 90
frames = [PhotoImage(file='catload.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame, bg='black')
    start_p.after(50, update, ind)

label = Label(start_p)
label.place(x=30, y=-20)
start_p.after(0, update, 0)


frameCnt2 = 10
frames1 = [PhotoImage(file='loading.gif', format='gif -index %i' % (i)) for i in range(frameCnt2)]

def update2(ind):
    frame = frames1[ind]
    ind += 1
    if ind == frameCnt2:
        ind = 0
    label1.configure(image=frame, bg='black')
    start_p.after(50, update2, ind)

label1 = Label(start_p)
label1.place(x=240, y=500)
start_p.after(0, update2, 0)

def mp():
    main_p = Tk()
    main_p.attributes("-fullscreen", True)
    main_p.configure(background="black")
    #main_p.resizable(False, False)
    #main_p.overrideredirect(True)

    def movie(i):
        my_cursor = mydb.cursor()
        frame5 = Frame(main_p, width=1366, height=768, bg='black')
        frame5.place(x=0,y=0)

        def actor1():
            frm8 = Frame(frame5, width=1366, height=768, bg="black")
            frm8.place(x=0,y=0)

            my_cursor = mydb.cursor()
            value4 = x
            query4 = "SELECT name, age, birthday, gender FROM actor WHERE actors_id= %s"
            my_cursor.execute(query4, (value4,))
            ina = my_cursor.fetchall()

            for i in ina:
                nm1 = str(i[0])
                age1= str(i[1])
                bd1= str(i[2])
                gen1 = str(i[3])
                actor1_name= Label(frm8, text=nm1, bg='black',font=('Cooper Black', 20) , fg='orange')
                actor1_name.place(x=560,y=80)

                actor1_age = Label(frm8, text='AGE: '+ age1, bg='black', font=('Cooper Black', 15), fg='orange')
                actor1_age.place(x=560, y=180)

                actor1_bday = Label(frm8, text='BIRTH DATE: '+ bd1, bg='black', font=('Cooper Black', 15), fg='orange')
                actor1_bday.place(x=560, y=280)

                actor1_gend = Label(frm8, text='GENDER: '+gen1, bg='black', font=('Cooper Black', 15), fg='orange')
                actor1_gend.place(x=560, y=380)

            def des8():
                frm8.destroy()

            frm8returnbtn = Button(frm8,text="RETURN", bg="gray", command=des8)
            frm8returnbtn.place(x=5, y=5)

        def actor2():
            frm8 = Frame(frame5, width=1366, height=768, bg="black")
            frm8.place(x=0, y=0)

            my_cursor = mydb.cursor()
            value4 = x
            query4 = "SELECT name2, age2, birthday2, gender2 FROM actor WHERE actors_id= %s"
            my_cursor.execute(query4, (value4,))
            ina = my_cursor.fetchall()

            for i in ina:
                nm2 = str(i[0])
                age2 = str(i[1])
                bd2 = str(i[2])
                gen2 = str(i[3])
                actor2_name = Label(frm8, text=nm2, bg='black', font=('Cooper Black', 20), fg='orange')
                actor2_name.place(x=560, y=80)

                actor2_age = Label(frm8, text='AGE: ' + age2, bg='black', font=('Cooper Black', 15), fg='orange')
                actor2_age.place(x=560, y=180)

                actor2_bday = Label(frm8, text='BIRTH DATE: ' + bd2, bg='black', font=('Cooper Black', 15), fg='orange')
                actor2_bday.place(x=560, y=280)

                actor2_gend = Label(frm8, text='GENDER: ' + gen2, bg='black', font=('Cooper Black', 15), fg='orange')
                actor2_gend.place(x=560, y=380)

            def des8():
                frm8.destroy()

            frm8returnbtn = Button(frm8, text="RETURN", bg="gray", command=des8)
            frm8returnbtn.place(x=5, y=5)

        def director1():
            frm8 = Frame(frame5, width=1366, height=768, bg="black")
            frm8.place(x=0,y=0)

            my_cursor = mydb.cursor()
            value4 = x
            query4 = "SELECT name, age, birthday, gender FROM director WHERE directors_id= %s"
            my_cursor.execute(query4, (value4,))
            ina = my_cursor.fetchall()

            for i in ina:
                nm1 = str(i[0])
                age1= str(i[1])
                bd1= str(i[2])
                gen1 = str(i[3])
                director1_name= Label(frm8, text=nm1, bg='black',font=('Cooper Black', 20) , fg='orange')
                director1_name.place(x=560,y=80)

                director1_age = Label(frm8, text='AGE: '+ age1, bg='black', font=('Cooper Black', 15), fg='orange')
                director1_age.place(x=560, y=180)

                director1_bday = Label(frm8, text='BIRTH DATE: '+ bd1, bg='black', font=('Cooper Black', 15), fg='orange')
                director1_bday.place(x=560, y=280)

                director1_gend = Label(frm8, text='GENDER: '+gen1, bg='black', font=('Cooper Black', 15), fg='orange')
                director1_gend.place(x=560, y=380)

            def des8():
                frm8.destroy()

            frm8returnbtn = Button(frm8,text="RETURN", bg="gray", command=des8)
            frm8returnbtn.place(x=5, y=5)


        def director2():

            frm8 = Frame(frame5, width=1366, height=768, bg="black")
            frm8.place(x=0, y=0)

            my_cursor = mydb.cursor()
            value4 = x
            query4 = "SELECT name2, age2, birthday2, gender2 FROM director WHERE directors_id= %s"
            my_cursor.execute(query4, (value4,))
            ina = my_cursor.fetchall()

            for i in ina:
                nm2 = str(i[0])
                age2 = str(i[1])
                bd2 = str(i[2])
                gen2 = str(i[3])

                if nm2 == '':

                    frm8.destroy()

                else:
                    director2_name = Label(frm8, text=nm2, bg='black', font=('Cooper Black', 20), fg='orange')
                    director2_name.place(x=560, y=80)

                    director2_age = Label(frm8, text='AGE: ' + age2, bg='black', font=('Cooper Black', 15), fg='orange')
                    director2_age.place(x=560, y=180)

                    director2_bday = Label(frm8, text='BIRTH DATE: ' + bd2, bg='black', font=('Cooper Black', 15),
                                           fg='orange')
                    director2_bday.place(x=560, y=280)

                    director2_gend = Label(frm8, text='GENDER: ' + gen2, bg='black', font=('Cooper Black', 15),
                                           fg='orange')
                    director2_gend.place(x=560, y=380)

                    def des8():
                        frm8.destroy()

                    frm8returnbtn = Button(frm8, text="RETURN", bg="gray", command=des8)
                    frm8returnbtn.place(x=5, y=5)


        for iii in i:
            value = iii
            my_cursor.execute("SELECT image_id, image_name FROM image WHERE image_name =%s", (value,))
            imid = my_cursor.fetchall()


        for ii in imid:
            y = str(ii[0])

        x=y
        # insert image
        value = x
        query = "SELECT image_name FROM image WHERE image_id=%s"
        my_cursor.execute(query, (value,))
        iml = my_cursor.fetchall()

        movie_pic = PhotoImage(file=iml)
        image_label = Label(frame5, image=movie_pic, bg='black')
        image_label.place(x=350,y=50)


        #insert name
        value = x
        query1 = "SELECT movie_title FROM gallery WHERE gallery_id=%s"
        my_cursor.execute(query1, (value,))
        inl = my_cursor.fetchall()
        inls = str(inl)
        reps = inls.replace("[('", "")
        reps2 = reps.replace("',)]", "")
        reps3 =reps2.replace("\n", "")

        title_label = Label(frame5, text=reps3, font=('Cooper Black', 32), bg="black", fg="orange")
        title_label.place(x=585, y=50)

        #insert description
        value = x
        query2 = "SELECT description FROM movie WHERE movie_id=%s"
        my_cursor.execute(query2, (value,))
        ind = my_cursor.fetchall()
        indes = str(ind)

        text = Text(frame5, width=50, wrap="word", height=5, bg='black', fg="orange",font=('Cooper Black', 13), borderwidth=0)
        text.place(x=585,y=110)
        #self.label["text"] = "Total tries: 0"
        rep1 = indes.replace('[(','')
        rep2 = rep1.replace(',)]', '')
        text.insert("1.0", rep2)

        # insert country, year
        value3 = x
        query3 = "SELECT year, country FROM movie WHERE movie_id= %s"
        my_cursor.execute(query3, (value3,))
        inyc = my_cursor.fetchall()
        for i in inyc:

           yr_label = Label(frame5, text=("Year:"), font=('Cooper Black', 11), bg="black", fg="orange")
           yr_label.place(x=585, y=213)
           yr1_label = Label(frame5, text=(i[0]), font=('Cooper Black', 11), bg="black", fg="orange")
           yr1_label.place(x=620, y=213)
           cntry_label = Label(frame5, text="Country:", font=('Cooper Black', 11), bg="black", fg="orange")
           cntry_label.place(x=680, y=213)
           cntry1_label = Label(frame5, text=i[1], font=('Cooper Black', 11), bg="black", fg="orange")
           cntry1_label.place(x=738, y=213)

        # insert actor
        value4 = x
        query4 = "SELECT name, name2 FROM actor WHERE actors_id= %s"
        my_cursor.execute(query4, (value4,))
        ina = my_cursor.fetchall()

        for ic in ina:

            act_label = Label(frame5, text=("Actor(s):"), font=('Cooper Black', 11), bg="black", fg="orange")
            act_label.place(x=585, y=245)
            act_btn1 = Button(frame5, text=(ic[0]) , font=('Cooper Black', 11), bg="black", fg="orange", borderwidth=0, activebackground="orange", command=actor1)
            act_btn1.place(x=646, y=245)
            act_btn = Button(frame5, text=(ic[1]), font=('Cooper Black', 11), bg="black", fg="orange", borderwidth=0, activebackground="orange",command=actor2)
            act_btn.place(x=646, y=267)

        # insert actor
        value5= x
        query5 = "SELECT name, name2 FROM director WHERE directors_id= %s"
        my_cursor.execute(query5, (value5,))
        indi = my_cursor.fetchall()

        for id in indi:
            dic_label = Label(frame5, text=("Director(s):"), font=('Cooper Black', 11), bg="black", fg="orange")
            dic_label.place(x=820, y=245)
            dic_btn1 = Button(frame5, text=(id[0]), font=('Cooper Black', 11), bg="black", fg="orange", borderwidth=0,activebackground="orange", command=director1)
            dic_btn1.place(x=897, y=245)
            dic_btn = Button(frame5, text=(id[1]), font=('Cooper Black', 11), bg="black", fg="orange", borderwidth=0,activebackground="orange", command=director2)
            dic_btn.place(x=897, y=267)

        value6 = x
        query6 = "SELECT genre_name1,genre_name2,genre_name3 FROM genre WHERE genre_id= %s"
        my_cursor.execute(query6, (value6,))
        ig = my_cursor.fetchall()
        ggg1 = str(ig).replace("[(","")
        gg1 = ggg1.replace("'", "")
        ggg2 = gg1.replace(")]", "")

        genre_label = Label(frame5, text=("Genre:"), font=('Cooper Black', 11), bg="black", fg="orange")
        genre_label.place(x=870, y=212)
        genre_label1 = Label(frame5, text=ggg2, font=('Cooper Black', 11), bg="black", fg="orange")
        genre_label1.place(x=927, y=212)


        #insert movie link
        value7 = x
        query7 = "SELECT link FROM movie WHERE movie_id= %s"
        my_cursor.execute(query7, (value7,))
        lnk = my_cursor.fetchall()

        lnks = str(lnk)

        def callback(lnks):

            lnks1 = lnks.replace("[('", "")
            lnks2 = lnks1.replace("',)]","")

            chromedir = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            webbrowser.get(chromedir).open(lnks2, new=0, autoraise=True)

        framelnk = Frame(frame5, width=700, height=80, bg='black', highlightbackground="orange",highlightthickness=1)
        framelnk.place(x=350, y=490)

        lnk_label = Label(frame5, text=("Press Link to Redirect Movie Site"), font=('Cooper Black', 15), bg="black", fg="orange")
        lnk_label.place(x=370, y=470)


        link1 = Label(framelnk, text=lnk, fg="orange", cursor="hand2", bg="black",font=('Cooper Black', 18))
        link1.place(x=5,y=20)
        link1.bind("<Button-1>", lambda e: callback(lnks))

        def des7():
            frame5.destroy()
        b = ImageTk.PhotoImage(Image.open('back.bmp.png'))
        return_btnn = Button(frame5, image=b, compound=CENTER, bg="black", borderwidth=0
                             , activebackground="black", command=des7)
        return_btnn.place(x=10, y=10)
        main_p.mainloop()


    #add movie function
    def add_movie():
        main_p.destroy()
        root2 = Tk()
        root2.iconbitmap(r'miming2.ico')
        root2.configure(background="black")
        root2.attributes("-fullscreen", True)
        global name_image

        def reg_movie():
            
            def gall():
                messagebox.showinfo("MOVIE REGISTRATION FORM","FILM SUCCESSFULLY REGISTER")                
                root2.destroy()
                mp()
            

            my_cursor = mydb.cursor()
            # Insert value into image table
            sql3 = "INSERT INTO image (image_name) VALUES (%s)"
            my_cursor.execute(sql3, (name_image,))
            mydb.commit()

            #Insert value into actor table
            sql = "INSERT INTO actor(name, age, birthday, gender, name2, age2, birthday2, gender2)" "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            value =(a_name.get(), a_age.get(), a_birth.get(), a_gender.get(),a_name2.get(), a_age2.get(), a_birth2.get(), a_gender2.get())
            my_cursor.execute(sql, value)
            mydb.commit()

            # Insert value into director table
            sql2 = "INSERT INTO director (name, age, birthday, gender, name2, age2, birthday2, gender2)" "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            value2 = (d_name.get(), d_age.get(), d_birth.get(), d_gender.get(),d_name2.get(), d_age2.get(), d_birth2.get(), d_gender2.get())
            my_cursor.execute(sql2, value2)
            mydb.commit()

            # insert into gallery table
            ttl = title.get()
            titl = str(ttl)
            sql6 = "INSERT INTO gallery (movie_title) VALUES (%s)"
            value6 = (titl)
            my_cursor.execute(sql6, (value6,))
            mydb.commit()

            # Insert value into movie table
            descrip = description_text.get("1.0", "end-1c")
            sql4 = "INSERT INTO movie (title,link,year,country,description)" "VALUES (%s, %s, %s, %s, %s)"
            value4 = (title.get(), link.get(), year_entry.get(), country_entry.get(), descrip)
            my_cursor.execute(sql4, value4)
            mydb.commit()

            # Insert value into genre table


            value7 =genre1.get(),genre2.get(),genre3.get()
            query7 = "INSERT INTO genre (genre_name1,genre_name2,genre_name3) VALUES (%s,%s,%s)"
            my_cursor.executemany(query7, (value7,))
            mydb.commit()

            gall()


        lbl1 = Label(root2, text="Movie Registration Form", font=('Cooper Black', 30, 'bold'), bg='black', fg='orange')
        lbl1.place(x=150, y=20)

        frm_image1 = Frame(root2, width=220, height=227, highlightbackground="orange", highlightthickness=1, bg="black")
        frm_image1.place(x=960, y=315)

        lbl = Label(frm_image1,bg="black")
        lbl.place(x=0, y=0)

        def add_image():
            global name_image
            my_cursor = mydb.cursor()

            fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("PNG File", "*.png"),("All Files",'*.*')))
            name_image = os.path.basename(fln)
            img = Image.open(fln)
            img = ImageTk.PhotoImage(img)
            lbl.configure(image=img)
            lbl.image = img


        browse_lbl = Label(frm_image1, text="219 x 227", font=('Comic Sans MS', 8), bg="black", fg="orange")
        browse_lbl.place(x=75, y=10)

        plus = ImageTk.PhotoImage(Image.open('plusimage.png'))
        browse_btn = Button(frm_image1, image=plus, compound=CENTER, bg="black", borderwidth=0, activebackground="black" ,command=add_image)
        browse_btn.place(x=95, y=100)


        def regm():
            if d_name.get() == "" or d_age.get() == "" or d_birth.get() == "" or d_gender.get() == "Gender":
                return messagebox.showwarning("REGISTER WARNING","PLEASE COMPLETE THE OUTPUT AT LEAST ONE DIRECTOR AND ACTOR TO BE REGISTER")

            if a_name.get() == "" or a_age.get() == "" or a_birth.get() == "" or a_gender.get() == "Gender":
                return messagebox.showwarning("REGISTER WARNING","PLEASE COMPLETE THE OUTPUT AT LEAST ONE DIRECTOR AND ACTOR TO BE REGISTER")

            if year_entry.get() == "" or country_entry.get() == "" or title.get() == "":
                return messagebox.showwarning("REGISTER WARNING", "PLEASE COMPLETE THE OUTPUT")

            if name_image == "":
                return messagebox.showwarning("REGISTER WARNING", "PLEASE PUT MOVIE IMAGE ")

            if link.get() == "":
                return messagebox.showwarning("REGISTER WARNING", "PLEASE COMPLETE THE OUTPUT")

            if genre1.get() == "" or genre2.get() == "" or genre3.get() == "":
                return messagebox.showwarning("REGISTER WARNING", "PLEASE COMPLETE THE OUTPUT AT LEAST ONE GENRE TO BE REGISTER")

            reg_movie()
       
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
        d_name2 = Entry(root2, width=20, font=('Comic Sans MS', 10))
        d_name2.place(x=405, y=115)

        d_lbl5 = Label(root2, text="AGE:", font=('Cooper Black', 11), bg='black', fg="orange")
        d_lbl5.place(x=400, y=140)
        d_age2 = Entry(root2, width=20, font=('Comic Sans MS', 10))
        d_age2.place(x=405, y=165)

        d_lbl6 = Label(root2, text="BIRTHDATE:", font=('Cooper Black', 11), bg='black', fg="orange")
        d_lbl6.place(x=400, y=190)
        d_birth2 = Entry(root2, width=20, font=('Comic Sans MS', 10))
        d_birth2.place(x=405, y=215)

        d_lbl7 = Label(root2, text="GENDER:", font=('Cooper Black', 11), bg='black', fg="orange")
        d_lbl7.place(x=400, y=240)
        d_gender2 = ttk.Combobox(root2, width=18, font=('Comic Sans MS', 10))
        d_gender2.set("")
        d_gender2['values'] = ("Male", "Female", "Transgender", "Gender queer", "Gender Neutral", "Others")
        d_gender2.place(x=405, y=265)

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
        a_name2 = Entry(root2, width=20, font=('Comic Sans MS', 10))
        a_name2.place(x=405, y=345)

        a_lbl1 = Label(root2, text="AGE:", font=('Cooper Black', 11), bg='black', fg="orange")
        a_lbl1.place(x=400, y=370)
        a_age2 = Entry(root2, width=20, font=('Comic Sans MS', 10))
        a_age2.place(x=405, y=395)

        a_lbl2 = Label(root2, text="BIRTHDATE:", font=('Cooper Black', 11), bg='black', fg="orange")
        a_lbl2.place(x=400, y=420)
        a_birth2 = Entry(root2, width=20, font=('Comic Sans MS', 10))
        a_birth2.place(x=405, y=445)

        a_lbl3 = Label(root2, text="GENDER:", font=('Cooper Black', 11), bg='black', fg="orange")
        a_lbl3.place(x=400, y=470)
        a_gender2 = ttk.Combobox(root2, width=18, font=('Comic Sans MS', 10))
        a_gender2.set("")
        a_gender2['values'] = ("Male", "Female", "Transgender", "Gender queer", "Gender Neutral", "Others")
        a_gender2.place(x=405, y=495)

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
        dscrptn_image = Frame(root2, width=350, height=210, highlightbackground="orange", highlightthickness=1,
                              bg="black")
        dscrptn_image.place(x=590, y=320)
        dc_lbl = Label(root2, text="DESCRIPTION:", font=('Cooper Black', 12), bg='black', fg="orange")
        dc_lbl.place(x=599, y=310)
        description_text = Text(root2, height=9, width=41, font=('Comic Sans MS', 10))
        description_text.place(x=599, y=350)

        # GENRE
        frm = Frame(root2, width=345, height=80, highlightbackground="orange", highlightthickness=1, bg="black")
        frm.place(x=600, y=100)
        gnr_lbl = Label(root2, text="GENRE:", font=('Cooper Black', 12), bg='black', fg="orange")
        gnr_lbl.place(x=610, y=90)

        lbl_g1 = Label(frm, text="Genre 1", bg="black", fg="white")
        lbl_g1.place(x=5, y=10)
        genre1 = ttk.Combobox(frm, width=10)
        genre1.set("")
        genre1['values'] = ("Horror", "Action", "Romance", "SciFi", "Fantasy", "Animated", "Mystery", "Comedy", "Adventure", "Thriller", "Drama")
        genre1.place(x= 5, y=35)

        lbl_g2 = Label(frm, text="Genre 2", bg="black", fg="white")
        lbl_g2.place(x=120, y=10)
        genre2 = ttk.Combobox(frm, width=10)
        genre2.set("")
        genre2['values'] = ("Horror", "Action", "Romance", "SciFi", "Fantasy", "Animated", "Mystery", "Comedy", "Adventure", "Thriller", "Drama")
        genre2.place(x=120, y=35)

        lbl_g3 = Label(frm, text="Genre 3", bg="black", fg="white")
        lbl_g3.place(x=230, y=10)
        genre3 = ttk.Combobox(frm, width=10)
        genre3.set("")
        genre3['values'] = ("Horror", "Action", "Romance", "SciFi", "Fantasy", "Animated", "Mystery", "Comedy", "Adventure", "Thriller", "Drama")
        genre3.place(x=235, y=35)

        add_m = Button(root2, text="REGISTER MOVIE", font=('Comic Sans MS', 16), bg="orange", command=regm)
        add_m.place(x=570, y=650)

        def des3():
            root2.destroy()
            mp()

        b = ImageTk.PhotoImage(Image.open('back.bmp.png'))
        back = Button(root2, image=b, compound=CENTER, bg="black", borderwidth=0
                           , activebackground="black", command=des3)
        back.place(x=5, y=5)

        root2.mainloop()
              
    def search():

        style = ttk.Style()
        style.theme_use('clam')

        my_canvas = Canvas(main_p, width=300, height=400)
        my_canvas.pack(pady=(170,5), fill=X)

        no_lbl = Label(my_canvas, text="No Movie Exist Yet", bg="black", font=('helvetica', 13), fg="white")
        no_lbl.place(x=40, y=50)


        style.configure("Horizontal.TScrollbar", gripcount=0,
                        background="orange", darkcolor="black", lightcolor="black",
                        troughcolor="black", bordercolor="black", arrowcolor="black")

        my_scrollbar = ttk.Scrollbar(my_canvas, orient='horizontal')
        my_scrollbar.pack(pady=(400, 5), fill=X)
        my_scrollbar.config(command=my_canvas.xview)

        my_canvas.configure(xscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"), bg="black",
                                                                    highlightbackground="black"))

        second_frame = Frame(my_canvas, bg="black")

        my_canvas.create_window(0, 300, window=second_frame, anchor="sw")




        my_cursor = mydb.cursor()

        my_cursor.execute(
            "SELECT gallery.movie_title, image.image_name FROM gallery INNER JOIN image ON image.image_id = gallery.gallery_id")
        id = my_cursor.fetchall()

        ent = search_entry.get()

        y = str(ent)
        x = y.title()

        movie_buttons = list(range(len(id)))
        movie_images = list(range(len(id)))

        for count, i in enumerate(id):
            img_nms= i[1]
            if x in i[0]:
                movie_images[count] = ImageTk.PhotoImage(Image.open(str(img_nms)))

                movie_buttons[count] = Button(second_frame, image=movie_images[count], bg="black",
                                              borderwidth=0,
                                              activebackground="black", command=lambda i=i: movie(i))
                movie_buttons[count].grid(row=0, column=count, pady=(40, 30), padx=(30))

        def des():
            my_canvas.destroy()
            my_scrollbar.destroy()

        b = ImageTk.PhotoImage(Image.open('back.png'))
        back_btn = Button(my_canvas, image=b, compound=CENTER, bg="black", borderwidth=0
                           , activebackground="black", command=des)
        back_btn.place(x=32, y=0)

        main_p.mainloop()

       #specific search function
    def specific_search():

        frame2 = Frame(main_p, width=400, height=300, bg="black")
        frame2.place(x=960,y=-20)

        def search_genre_frm():
            frame3 = Frame(main_p, width=400, height=300, bg="black")
            frame3.place(x=960, y=-20)

            def genre_filt():
                global genress
                style = ttk.Style()
                style.theme_use('clam')

                my_canvas = Canvas(main_p, width=300, height=400)
                my_canvas.pack(pady=(170, 5), fill=X)

                no_lbl = Label(my_canvas, text="No Movie Exist Yet", bg="black", font=('helvetica', 13), fg="white")
                no_lbl.place(x=40, y=50)

                style.configure("Horizontal.TScrollbar", gripcount=0,
                                background="orange", darkcolor="black", lightcolor="black",
                                troughcolor="black", bordercolor="black", arrowcolor="black")

                my_scrollbar = ttk.Scrollbar(my_canvas, orient='horizontal')
                my_scrollbar.pack(pady=(400, 5), fill=X)
                my_canvas.configure(xscrollcommand=my_scrollbar.set)
                my_canvas.bind('<Configure>',
                               lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"), bg="black",
                                                             highlightbackground="black"))

                second_frame = Frame(my_canvas, bg="black")

                my_canvas.create_window(0, 300, window=second_frame, anchor="sw")

                my_cursor = mydb.cursor()
                my_cursor.execute("""SELECT  genre.genre_name1,genre.genre_name2,genre.genre_name3, image.image_name FROM gallery 
                                                      INNER JOIN genre ON genre.genre_id = gallery.gallery_id
                                                      INNER JOIN image ON image.image_id = gallery.gallery_id""")
                idd = my_cursor.fetchall()


                movie_buttons = list(range(len(idd)))
                movie_images = list(range(len(idd)))

                g1 = genres1.get()
                g2 = genres2.get()
                g3 = genres3.get()

                for count, i in enumerate(idd):
                    img_nms = i[3]
                    if g1 in i[0] or g1 in i[1] or g1 in i[2]:

                        if g2 in i[0] or g2 in i[1] or g2 in i[2]:

                            if g3 in i[0] or g3 in i[1] or g3 in i[2]:

                                movie_images[count] = ImageTk.PhotoImage(Image.open(str(img_nms)))

                                movie_buttons[count] = Button(second_frame, image=movie_images[count], bg="black",
                                                              borderwidth=0,
                                                              activebackground="black", command=lambda i=i: movie(i))
                                movie_buttons[count].grid(row=0, column=count, pady=(40, 30), padx=(30))
                def des():
                    my_canvas.destroy()
                    my_scrollbar.destroy()

                b = ImageTk.PhotoImage(Image.open('back.png'))
                back_btn2 = Button(my_canvas, image=b, compound=CENTER, bg="black", borderwidth=0
                              , activebackground="black", command=des)
                back_btn2.place(x=32, y=0)

                frame2.destroy()
                frame3.destroy()
                frame3.mainloop()          
              
            #Genre Entry
            lbl_g1 = Label(frame3, text="Genre 1", bg="black", fg="white")
            lbl_g1.place(x=50, y=130)
            genres1 = ttk.Combobox(frame3, width=10)
            genres1.set("")
            genres1['values'] = ("Horror", "Action", "Romance", "SciFi", "Fantasy", "Animated", "Mystery", "Comedy", "Adventure", "Thriller", "Drama")
            genres1.place(x=50, y=155)

            lbl_g2 = Label(frame3, text="Genre 2", bg="black", fg="white")
            lbl_g2.place(x=170, y=130)
            genres2 = ttk.Combobox(frame3, width=10)
            genres2.set("")
            genres2['values'] = ("Horror", "Action", "Romance", "SciFi", "Fantasy", "Animated", "Mystery", "Comedy", "Adventure", "Thriller", "Drama")
            genres2.place(x=170, y=155)

            lbl_g3 = Label(frame3, text="Genre 3", bg="black", fg="white")
            lbl_g3.place(x=285, y=130)
            genres3 = ttk.Combobox(frame3, width=10)
            genres3.set("")
            genres3['values'] = ("Horror", "Action", "Romance", "SciFi", "Fantasy", "Animated", "Mystery", "Comedy", "Adventure", "Thriller", "Drama")
            genres3.place(x=285, y=155)
       
            def des9():
                if genres1.get() == "" and genres2.get() == "" and genres3.get() == "":
                    return messagebox.showwarning("SEARCH FILTER ERROR", "Select at least one Genre filter to search")
                else:
                    genre_filt()
            sgf = Button(frame3, text="Search", bg="orange", command=des9)
            sgf.place(x=182, y=90)

            b = ImageTk.PhotoImage(Image.open('back.png'))
            back = Button(frame3, image=b, compound=CENTER, bg="black", borderwidth=0
                              , activebackground="black", command=frame3.destroy)
            back.place(x=5, y=50)
            main_p.mainloop()
              
         def search_spec():
            global genress
            style = ttk.Style()
            style.theme_use('clam')

            my_canvas = Canvas(main_p, width=300, height=400)
            my_canvas.pack(pady=(170, 5), fill=X)

            no_lbl = Label(my_canvas, text="No Movie Exist Yet", bg="black", font=('helvetica', 13), fg="white")
            no_lbl.place(x=40, y=50)

            style.configure("Horizontal.TScrollbar", gripcount=0,
                            background="orange", darkcolor="black", lightcolor="black",
                            troughcolor="black", bordercolor="black", arrowcolor="black")

            my_scrollbar = ttk.Scrollbar(my_canvas, orient='horizontal')
            my_scrollbar.pack(pady=(400, 5), fill=X)

            my_canvas.configure(xscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"), bg="black",
                                                                        highlightbackground="black"))

            second_frame = Frame(my_canvas, bg="black")

            my_canvas.create_window(0, 300, window=second_frame, anchor="sw")


            my_cursor = mydb.cursor()
            my_cursor.execute("""SELECT actor.name, actor.name2, director.name, director.name2, movie.country, movie.year, image.image_name FROM gallery 
                                     INNER JOIN actor ON actor.actors_id = gallery.gallery_id
                                     INNER JOIN director ON director.directors_id = gallery.gallery_id
                                     INNER JOIN movie ON movie.movie_id = gallery.gallery_id
                                     INNER JOIN image ON image.image_id = gallery.gallery_id""")
            id = my_cursor.fetchall()


            actor_n = actor.get()
            direct_n = director.get()
            country_n = country.get()
            year_n = yr.get()

            movie_buttons = list(range(len(id)))
            movie_images = list(range(len(id)))

            for count, i in enumerate(id):
                img_nms = i[6]
                x = str(i[5])
                if actor_n in i[0] or actor_n in i[1]:

                    if direct_n in i[2] or direct_n in i[3]:

                        if country_n in i[4]:

                            if year_n in x:
                                movie_images[count] = ImageTk.PhotoImage(Image.open(str(img_nms)))

                                movie_buttons[count] = Button(second_frame, image=movie_images[count], bg="black",
                                                              borderwidth=0,
                                                              activebackground="black", command=lambda i=i: movie(i))
                                movie_buttons[count].grid(row=0, column=count, pady=(40, 30), padx=(30))

            def des():
                my_canvas.destroy()
                my_scrollbar.destroy()

            b = ImageTk.PhotoImage(Image.open('back.png'))
            back_btn = Button(my_canvas, image=b, compound=CENTER, bg="black", borderwidth=0
                          , activebackground="black", command=des)
            back_btn.place(x=32, y=0)

            frame2.destroy()
            main_p.mainloop()  
       
        lbl_yrs= Label(frame2,text="Year", bg="black",fg="white")
        lbl_yrs.place(x=30, y=110)
        my_cursor = mydb.cursor()
        my_cursor.execute("""SELECT year FROM movie""")
        yrd = my_cursor.fetchall()
        yr_n = (list(OrderedDict.fromkeys(yrd)))
        yr = ttk.Combobox(frame2, width=20)
        yr.set("")
        yr['values'] = (yr_n)
        yr.place(x=30, y=130)


        lbl_act = Label(frame2, text="Actor", bg="black", fg="white")
        lbl_act.place(x=230, y=45)
        my_cursor.execute("""SELECT name FROM actor""")
        act = my_cursor.fetchall()
        my_cursor.execute("""SELECT name2 FROM actor""")
        act2 = my_cursor.fetchall()
        act_n = (list(itertools.chain.from_iterable(OrderedDict.fromkeys(act + act2))))
        actor = ttk.Combobox(frame2, width=20)
        actor.set("")
        actor['values'] = (act_n)
        actor.place(x=230, y=65)

        lbl_direct = Label(frame2, text="Director", bg="black", fg="white")
        lbl_direct.place(x=30, y=45)
        my_cursor.execute("""SELECT name FROM director""")
        director1 = my_cursor.fetchall()
        my_cursor.execute("""SELECT name2 FROM director""")
        director2 = my_cursor.fetchall()
        director_n =(list(itertools.chain.from_iterable(OrderedDict.fromkeys(director2 + director1))))
        director = ttk.Combobox(frame2, width=20)
        director.set("")
        director['values'] = (director_n)
        director.place(x=30, y=65)

        lbl_cons = Label(frame2, text="Country", bg="black", fg="white")
        lbl_cons.place(x=230, y=110)
        my_cursor.execute("""SELECT country FROM movie""")
        co = my_cursor.fetchall()
        con = (list(itertools.chain.from_iterable(OrderedDict.fromkeys(co))))
        country = ttk.Combobox(frame2, width=20)
        country.set("")
        country['values'] = (con)
        country.place(x=230, y=130)


        def des4():
            if yr.get() == "" and country.get() == "" and actor.get() == "" and director.get() == "":
                return messagebox.showwarning("SEARCH FILTER ERROR","Select at least one filter to search")
            else:
                search_spec()



        search_btn = Button(frame2, bg="orange",text="Search", borderwidth=5, activebackground="black", command=des4)
        search_btn.place(x=180, y=200)

        search_genre= Button(frame2, bg="orange", text="GENRE FILTER", borderwidth=2, activebackground="black", command=search_genre_frm)
        search_genre.place(x=250, y=200)

        b = ImageTk.PhotoImage(Image.open('back.png'))
        back = Button(frame2, image=b, compound=CENTER, bg="black", borderwidth=0
                      , activebackground="black", command=frame2.destroy)
        back.place(x=182, y=245)

        main_p.mainloop()


    # Entry search box
    search_entry = Entry(main_p, width=40, bg='light goldenrod', font=("helvitica",18))
    search_entry.place(x=420, y=180)

    ms = ImageTk.PhotoImage(Image.open('minisearch.png'))
    ms_lbl = Label(main_p, image=ms, bg="black")
    ms_lbl.place(x=365, y=174)

    # rusu lite logo image
    rusu = ImageTk.PhotoImage(Image.open('miming.png'))
    rusu_logo = Label(main_p, image=rusu, bg="black")
    rusu_logo.place(x=635, y=5)

    def des5(event):
        if search_entry.get() == "":
            return messagebox.showwarning("SEARCH WARNING","Search by typing a word or phrase in the search box at the top of this page ")
        else:
            search()


    # search button
    s = ImageTk.PhotoImage(Image.open('searchbtn.png'))
    search_btn = Button(main_p, image=s, compound=CENTER, bg="black", borderwidth=0
                        , activebackground="black", command=des5)
    search_btn.bind('<return>', des5)
    search_btn.place(x=643, y=220)


    #add movie page button
    addm = ImageTk.PhotoImage(Image.open('addmovie.png'))
    add_movie_btn = Button(main_p, image=addm, bg="black",compound=CENTER, command=add_movie, borderwidth=0)
    add_movie_btn.place(x=1260,y=10)

    #Specific Search
    fil_movie_btn = Button(main_p, text="Search Filter", bg="orange",borderwidth=5, command=specific_search)
    fil_movie_btn.place(x=950, y=180)

    def des6():
        if messagebox.askyesno("EXIT INFORMATION","ARE YOU SURE LEAVING ME? (T.T)") == False:
            return
        else:
            main_p.destroy()

    exitm = ImageTk.PhotoImage(Image.open('exit.png'))
    exit = Button(main_p, image=exitm, bg="black", command=des6, borderwidth=0)
    exit.place(x=15, y=15)

    #movie main page movie
    frame1 = Frame(main_p, width=860, height=300,bg="black", highlightbackground="black")
    frame1.place(x=266, y=300)

    my_canvas = Canvas(frame1)
    my_canvas.place(x=-43, y=40, width=900)

    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"), bg="black",highlightbackground="black" ))

    second_frame = Frame(my_canvas, bg="black", borderwidth=0)


    my_canvas.create_window(0, 100, window=second_frame, anchor="se")

    my_cursor = mydb.cursor()

    my_cursor.execute("SELECT image_name FROM image")
    id = my_cursor.fetchall()

   # def m(i):
        #movie(i)

    movie_buttons = list(range(len(id)))
    movie_images = list(range(len(id)))

    for count, i in enumerate(id):
        img_nms = i[0]
        #print(count, i[0])
        movie_images[count] = ImageTk.PhotoImage(Image.open(str(img_nms)))

        movie_buttons[count] = Button(second_frame, image=movie_images[count], bg="black", borderwidth=0,
                                      activebackground="black", command=lambda i=i: movie(i))
        movie_buttons[count].grid(row=0, column=count, pady=(40, 30), padx=(30))

    main_p.mainloop()

def des():
    start_p.destroy()

start_p.after(5000, lambda :(des(), mp()))

start_p.mainloop()
