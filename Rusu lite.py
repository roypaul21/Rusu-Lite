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
                '''     
                my_cursor = mydb.cursor()
                # insert all value to Gallery table
                my_cursor.execute("SELECT gallery_id FROM gallery")
                gal_i = my_cursor.fetchall()
                for ga in gal_i:
                    gal = ga[0]
                mydb.commit()
                # insert all value to actor_Gallery table
                my_cursor.execute("SELECT actors_id FROM actor")
                actor_i = my_cursor.fetchall()
                for ac in actor_i:
                    ida = ac[0]
                mydb.commit()
                sql_ac = "INSERT INTO actor_gallery(gallery_id,actors_id)" "VALUES (%s, %s)"
                value_ac = (gal,ida)
                my_cursor.execute(sql_ac, value_ac)
                mydb.commit()
                # insert all value to director_Gallery table
                my_cursor.execute("SELECT directors_id FROM director")
                director_i = my_cursor.fetchall()
                for di in director_i:
                    idd = di[0]
                mydb.commit()
                sql_dd = "INSERT INTO director_gallery(gallery_id,directors_id)" "VALUES (%s, %s)"
                value_dd = (gal, idd)
                my_cursor.execute(sql_dd, value_dd)
                mydb.commit()
                # insert all value to movie_Gallery table
                my_cursor.execute("SELECT movie_id FROM movie")
                movie_i = my_cursor.fetchall()
                for mo in movie_i:
                    idm = mo[0]
                mydb.commit()
                sql_m = "INSERT INTO movie_gallery(gallery_id,movie_id)" "VALUES (%s, %s)"
                value_m = (gal, idm)
                my_cursor.execute(sql_m, value_m)
                mydb.commit()
                # insert all value to image_Gallery table
                my_cursor.execute("SELECT image_id FROM image")
                image_i = my_cursor.fetchall()
                for im in image_i:
                    idi = im[0]
                mydb.commit()
                sql_im = "INSERT INTO image_gallery(gallery_id,image_id)" "VALUES (%s, %s)"
                value_im = (gal, idi)
                my_cursor.execute(sql_im, value_im)
                mydb.commit()
                messagebox.showinfo("MOVIE REGISTRATION FORM","FILM SUCCESSFULLY REGISTER")
                '''
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
