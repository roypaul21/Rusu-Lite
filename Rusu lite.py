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
       password = "*****",
       database =  "rusulite",
       )
my_cursor = mydb.cursor()



def mp():
    main_p = Tk()
    main_p.attributes("-fullscreen", True)
    main_p.configure(background="black")

    def movie(i):
        my_cursor = mydb.cursor()
        frame5 = Frame(main_p, width=1366, height=768, bg='black')
        frame5.place(x=0, y=0)

        for iii in i:
            value = iii
            my_cursor.execute("SELECT image_id, image_name FROM image WHERE image_name =%s", (value,))
            imid = my_cursor.fetchall()


        for ii in imid:
            y = str(ii[0])

        x = y
        # insert image
        value = x
        query = "SELECT image_name FROM image_gallery INNER JOIN image ON image.image_id = image_gallery.image_id WHERE gallery_id=%s"
        my_cursor.execute(query, (value,))
        iml = my_cursor.fetchall()

        movie_pic = PhotoImage(file=iml)
        image_label = Label(frame5, image=movie_pic, bg='black')
        image_label.place(x=350, y=50)

        # insert movie name
        value = x
        query1 = "SELECT movie_title FROM gallery WHERE gallery_id=%s"
        my_cursor.execute(query1, (value,))
        inl = my_cursor.fetchall()
        inls = str(inl)
        reps = inls.replace("[('", "")
        reps2 = reps.replace("',)]", "")
        reps3 = reps2.replace("\n", "")

        title_label = Label(frame5, text=reps3, font=('Cooper Black', 32), bg="black", fg="orange")
        title_label.place(x=585, y=50)

        # insert description
        value = x
        query2 = "SELECT description FROM movie_gallery INNER JOIN movie ON movie.movie_id = movie_gallery.movie_id WHERE gallery_id=%s"
        my_cursor.execute(query2, (value,))
        ind = my_cursor.fetchall()
        indes = str(ind)

        text = Text(frame5, width=50, wrap="word", height=5, bg='black', fg="orange", font=('Cooper Black', 13),
                    borderwidth=0)
        text.place(x=585, y=110)

        # self.label["text"] = "Total tries: 0"
        rep1 = indes.replace('[(', '')
        rep2 = rep1.replace(',)]', '')
        text.insert("1.0", rep2)

        # insert country, year
        value3 = x
        query3 = "SELECT year, country FROM movie_gallery INNER JOIN movie ON movie.movie_id = movie_gallery.movie_id WHERE gallery_id=%s"
        my_cursor.execute(query3, (value3,))
        inyc = my_cursor.fetchall()
        for i in inyc:
            yr_label = Label(frame5, text=("Released Year:"), font=('Cooper Black', 11), bg="black", fg="orange")
            yr_label.place(x=585, y=213)
            yr1_label = Label(frame5, text=(i[0]), font=('Cooper Black', 11), bg="black", fg="orange")
            yr1_label.place(x=690, y=213)
            cntry_label = Label(frame5, text="Country:", font=('Cooper Black', 11), bg="black", fg="orange")
            cntry_label.place(x=780, y=213)
            cntry1_label = Label(frame5, text=i[1], font=('Cooper Black', 11), bg="black", fg="orange")
            cntry1_label.place(x=838, y=213)

        #insert Genre
        value6 = x
        query6 = "SELECT genre_name FROM genre_movie INNER JOIN genre ON genre.genre_id = genre_movie.genre_id WHERE movie_id= %s"
        my_cursor.execute(query6, (value6,))
        ig = my_cursor.fetchall()
        print(ig)

        ggg1 = str(ig).replace("[(", "")
        gg1 = ggg1.replace("'", "")
        ggg2 = gg1.replace(")]", "")
        gg2 = ggg2.replace("(", "")
        ggg3 = gg2.replace("),","")
        ggg4 = ggg3.replace(",", " ")

        genre_label = Label(frame5, text=("Genre:"), font=('Cooper Black', 11), bg="black", fg="orange")
        genre_label.place(x=585, y=245)
        genre_label1 = Label(frame5, text=ggg4, font=('Cooper Black', 11), bg="black", fg="orange")
        genre_label1.place(x=640, y=245)

        def act(i):
            my_cursor = mydb.cursor()
            frame_act = Frame(frame5, width=1366, height=768, bg='black')
            frame_act.place(x=0, y=0)
            for ic in i:
                value = ic
                my_cursor.execute("SELECT actor.actors_id FROM actor WHERE actor.name =%s", (value,))
                imic = my_cursor.fetchall()

            for iic in imic:
                ax = str(iic[0])


            my_cursor.execute(
                "SELECT performed_in.character FROM rusulite.performed_in WHERE performed_in.actors_id =%s AND performed_in.movie_id =%s ",
                (ax, x))
            actor_char = my_cursor.fetchall()

            for iac in actor_char:
                charc = iac[0]


            valuec = "%" + str(charc) + "%"
            queryc = """SELECT actor.name, actor.age, actor.birthday, actor.gender, performed_in.character FROM rusulite.performed_in
                     INNER JOIN rusulite.actor ON actor.actors_id = performed_in.actors_id WHERE performed_in.character LIKE %s LIMIT 1
                     """
            my_cursor.execute(queryc, (valuec,))
            actors = my_cursor.fetchall()

            for actors_i in actors:
                nm1 = str(actors_i[0])
                age1= str(actors_i[1])
                bd1= str(actors_i[2])
                gen1 = str(actors_i[3])
                char= str(actors_i[4])

                actor1_name= Label(frame_act, text=nm1, bg='black',font=('Cooper Black', 20) , fg='orange')
                actor1_name.place(x=560,y=80)

                actor1_age = Label(frame_act, text='AGE: '+ age1, bg='black', font=('Cooper Black', 15), fg='orange')
                actor1_age.place(x=560, y=180)

                actor1_bday = Label(frame_act, text='BIRTH DATE: '+ bd1, bg='black', font=('Cooper Black', 15), fg='orange')
                actor1_bday.place(x=560, y=280)

                actor1_gend = Label(frame_act, text='GENDER: '+gen1, bg='black', font=('Cooper Black', 15), fg='orange')
                actor1_gend.place(x=560, y=380)

                actor1_char= Label(frame_act, text='PLAY AS: ' + char, bg='black', font=('Cooper Black', 15),
                                    fg='orange')
                actor1_char.place(x=560, y=480)






            def des7():
                frame_act.destroy()

            b = ImageTk.PhotoImage(
                Image.open('C:/Users/LENOVO/PycharmProjects/Rusu lite /images buttons/back.bmp.png'))
            return_btnn = Button(frame_act, image=b, compound=CENTER, bg="black", borderwidth=0
                                 , activebackground="black", command=des7)
            return_btnn.place(x=10, y=10)
            frame_act.mainloop()



        #Insert Actor
        value4 = x
        query4 = "SELECT name FROM actor_gallery INNER JOIN actor ON actor.actors_id = actor_gallery.actors_id WHERE gallery_id= %s"
        my_cursor.execute(query4, (value4,))

        ina = my_cursor.fetchall()

        ac_buttons = list(range(len(ina)))
        ac_images = list(range(len(ina)))

        fract = Frame(frame5, width=400, height=200, bg='black',borderwidth=0)
        fract.place(x=350, y=350)

        fract1 = Frame(frame5, width=50, height=0, bg='orange', borderwidth=0)
        fract1.place(x=355, y=345)

        act_label = Label(frame5, text=("Actor(s):"), font=('Cooper Black', 12), bg="black", fg="orange")
        act_label.place(x=350, y=320)

        for count, i in enumerate(ina):
            img_nms = i[0]
            # print(count, i[0])
            ac_images[count] = str(img_nms.replace("\n",""))
            ac_buttons[count] = Button(fract, text=ac_images[count], bg="black",font=('Cooper Black', 11), borderwidth=0, fg="sky blue",
                                          activebackground="black",command=lambda i=i: act(i))
            ac_buttons[count].grid(row=0, column=count, pady=(0), padx=(6))



        def dct(idd):
            my_cursor = mydb.cursor()
            frame_dct = Frame(frame5, width=1366, height=768, bg='black')
            frame_dct.place(x=0, y=0)
            for ic in idd:
                value = ic
                my_cursor.execute("SELECT director.directors_id FROM director WHERE director.name =%s", (value,))
                imid = my_cursor.fetchall()

            for iid in imid:
                dx = str(iid[0])

            my_cursor.execute(
                "SELECT director.name, director.age, director.birthday, director.gender FROM rusulite.directed_by INNER JOIN rusulite.director ON director.directors_id = directed_by.directors_id WHERE director.directors_id =%s AND directed_by.movie_id =%s ",
                (dx, x))
            actor_char = my_cursor.fetchall()

            for idc in actor_char:
                nm1 = str(idc[0])
                age1 = str(idc[1])
                bd1 = str(idc[2])
                gen1 = str(idc[3])


            dir1_name = Label(frame_dct, text=nm1, bg='black', font=('Cooper Black', 20), fg='orange')
            dir1_name.place(x=560, y=80)

            dir1_age = Label(frame_dct, text='AGE: ' + age1, bg='black', font=('Cooper Black', 15), fg='orange')
            dir1_age.place(x=560, y=180)

            dir1_bday = Label(frame_dct, text='BIRTH DATE: ' + bd1, bg='black', font=('Cooper Black', 15),
                                fg='orange')
            dir1_bday.place(x=560, y=280)

            dir1_gend = Label(frame_dct, text='GENDER: ' + gen1, bg='black', font=('Cooper Black', 15), fg='orange')
            dir1_gend.place(x=560, y=380)


            def des7():
                frame_dct.destroy()

            b = ImageTk.PhotoImage(
                Image.open('C:/Users/LENOVO/PycharmProjects/Rusu lite/images buttons/back.bmp.png'))
            return_btnn = Button(frame_dct, image=b, compound=CENTER, bg="black", borderwidth=0
                                 , activebackground="black", command=des7)
            return_btnn.place(x=10, y=10)
            frame_dct.mainloop()


        # Insert Actor
        value9 = x
        query9 = "SELECT name FROM director_gallery INNER JOIN director ON director.directors_id = director_gallery.directors_id WHERE gallery_id= %s"
        my_cursor.execute(query9, (value9,))

        ind = my_cursor.fetchall()

        dc_buttons = list(range(len(ind)))
        dc_images = list(range(len(ind)))

        act_label = Label(frame5, text=("Director(s):"), font=('Cooper Black', 12), bg="black", fg="orange")
        act_label.place(x=750, y=320)
        fract1 = Frame(frame5, width=70, height=0, bg='orange', borderwidth=0)
        fract1.place(x=755, y=345)

        fractd = Frame(frame5, width=400, height=200, bg='black', borderwidth=0)
        fractd.place(x=750, y=350)

        for count, idd in enumerate(ind):
            img_nmsd = idd[0]
            # print(count, i[0])
            dc_images[count] = str(img_nmsd.replace("\n",""))
            dc_buttons[count] = Button(fractd, text=dc_images[count], bg="black",font=('Cooper Black', 11), borderwidth=0, fg="sky blue",
                                          activebackground="black",command=lambda idd=idd: dct(idd))
            dc_buttons[count].grid(row=0, column=count, pady=(0), padx=(6))



            # insert movie link
            value7 = x
            query7 = "SELECT movie.link FROM movie_gallery INNER JOIN movie ON movie.movie_id = movie_gallery.movie_id WHERE gallery_id=%s"
            my_cursor.execute(query7, (value7,))
            lnk = my_cursor.fetchall()

            lnks = str(lnk)

            def callback(lnks):
                lnks1 = lnks.replace("[('", "")
                lnks2 = lnks1.replace("',)]", "")

                chromedir = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

                webbrowser.get(chromedir).open(lnks2, new=0, autoraise=True)

            framelnk = Frame(frame5, width=700, height=80, bg='black', highlightbackground="orange",
                             highlightthickness=1)
            framelnk.place(x=350, y=490)

            lnk_label = Label(frame5, text=("Press Link to Redirect Movie Site"), font=('Cooper Black', 15), bg="black",
                              fg="orange")
            lnk_label.place(x=370, y=470)

            link1 = Label(framelnk, text=lnk, fg="orange", cursor="hand2", bg="black", font=('Cooper Black', 18))
            link1.place(x=5, y=20)
            link1.bind("<Button-1>", lambda e: callback(lnks))


        def des7():
            frame5.destroy()
        b = ImageTk.PhotoImage(Image.open('C:/Users/LENOVO/PycharmProjects/Rusu lite/images buttons/back.bmp.png'))
        return_btnn = Button(frame5, image=b, compound=CENTER, bg="black", borderwidth=0
                             , activebackground="black", command=des7)
        return_btnn.place(x=10, y=10)
        main_p.mainloop()

    def regs_movie():
        main_p.destroy()
        mr = Tk()
        mr.configure(background="black")
        mr.attributes("-fullscreen", True)
        global name_image
        my_cursor = mydb.cursor()

        def add_actor():
            frame_act = Frame(mr, width=1360, height=600, bg="black")
            frame_act.place(x=0, y=200)

            def reg_act():
                if messagebox.askyesno("Register Confirmation", "ARE YOU SURE TO REGISTER THIS ACTOR?") == False:
                    return

                else:
                    # Insert value into actor table
                    sql = "INSERT INTO actor(name, age, birthday, gender)" "VALUES (%s, %s, %s, %s)"
                    value = (a_name.get(), a_age.get(), a_birth.get(), a_gender.get())
                    my_cursor.execute(sql, value)
                    mydb.commit()

                    messagebox.showinfo("MOVIE REGISTRATION FORM", "ACTOR SUCCESSFULLY REGISTER")
                    frame_act.destroy()




            def rac():
                if a_name.get() == "" or a_age.get() == "" or a_birth.get() == "" or a_gender.get() == "Gender":
                    return messagebox.showwarning("REGISTER WARNING", "PLEASE COMPLETE THE OUTPUT TO BE REGISTER")

                reg_act()


            lbl1 = Label(frame_act, text="Actor Registration", font=('Cooper Black', 30, 'bold'), bg='black', fg='orange')
            lbl1.place(x=520, y=0)

            a_lbl = Label(frame_act, text="ACTOR NAME:", font=('Cooper Black', 11), bg='black', fg="orange")
            a_lbl.place(x=520, y=90)
            a_name = Entry(frame_act, width=20, font=('Comic Sans MS', 10))
            a_name.place(x=640, y=90)

            a_lbl1 = Label(frame_act, text="AGE:", font=('Cooper Black', 11), bg='black', fg="orange")
            a_lbl1.place(x=520, y=140)
            a_age = Entry(frame_act, width=20, font=('Comic Sans MS', 10))
            a_age.place(x=640, y=140)

            a_lbl2 = Label(frame_act, text="BIRTHDATE:", font=('Cooper Black', 11), bg='black', fg="orange")
            a_lbl2.place(x=520, y=190)
            a_birth = Entry(frame_act, width=20, font=('Comic Sans MS', 10))
            a_birth.place(x=640, y=190)

            a_lbl3 = Label(frame_act, text="GENDER:", font=('Cooper Black', 11), bg='black', fg="orange")
            a_lbl3.place(x=520, y=240)
            a_gender = Entry(frame_act, width=20, font=('Comic Sans MS', 10))
            a_gender.place(x=640, y=240)

            add_a = Button(frame_act, text="ADD ACTOR", bg="orange", command=rac)
            add_a.place(x=680, y=300)

            b = ImageTk.PhotoImage(Image.open('C:/Users/LENOVO/PycharmProjects/Rusu lite/images buttons/back.png'))
            back = Button(frame_act, image=b, compound=CENTER, bg="black", borderwidth=0
                          , activebackground="black", command=frame_act.destroy)
            back.place(x=200, y=50)
            mr.mainloop()

        def add_director():
            frame_dct = Frame(mr, width=1360, height=600, bg="black")
            frame_dct.place(x=0, y=200)

            def reg_dct():
                if messagebox.askyesno("Register Confirmation", "ARE YOU SURE TO REGISTER THIS DIRECTOR?") == False:
                    return

                else:
                    # Insert value into director table
                    sql2 = "INSERT INTO director (name, age, birthday, gender)" "VALUES (%s, %s, %s, %s)"
                    value2 = (d_name.get(), d_age.get(), d_birth.get(), d_gender.get())
                    my_cursor.execute(sql2, value2)
                    mydb.commit()

                    messagebox.showinfo("MOVIE REGISTRATION FORM", "DIRECTOR SUCCESSFULLY REGISTER")
                    frame_dct.destroy()


            def rdc():
                if d_name.get() == "" or d_age.get() == "" or d_birth.get() == "" or d_gender.get() == "Gender":
                    return messagebox.showwarning("REGISTER WARNING", "PLEASE COMPLETE THE OUTPUT TO BE REGISTER")

                reg_dct()

            lbl1 = Label(frame_dct, text="Director Registration", font=('Cooper Black', 30, 'bold'), bg='black', fg='orange')
            lbl1.place(x=520, y=0)

            d_lbl = Label(frame_dct, text="DIRECTOR NAME:", font=('Cooper Black', 11), bg='black', fg="orange")
            d_lbl.place(x=520, y=90)
            d_name = Entry(frame_dct, width=20, font=('Comic Sans MS', 10))
            d_name.place(x=660, y=90)

            d_lbl1 = Label(frame_dct, text="AGE:", font=('Cooper Black', 11), bg='black', fg="orange")
            d_lbl1.place(x=520, y=140)
            d_age = Entry(frame_dct, width=20, font=('Comic Sans MS', 10))
            d_age.place(x=660, y=140)

            d_lbl2 = Label(frame_dct, text="BIRTHDATE:", font=('Cooper Black', 11), bg='black', fg="orange")
            d_lbl2.place(x=520, y=190)
            d_birth = Entry(frame_dct, width=20, font=('Comic Sans MS', 10))
            d_birth.place(x=660, y=190)

            a_lbl3 = Label(frame_dct, text="GENDER:", font=('Cooper Black', 11), bg='black', fg="orange")
            a_lbl3.place(x=520, y=240)
            d_gender = Entry(frame_dct, width=20, font=('Comic Sans MS', 10))
            d_gender.place(x=660, y=240)

            add_d = Button(frame_dct, text="ADD DIRECTOR", bg="orange", command=rdc)
            add_d.place(x=680, y=300)

            b = ImageTk.PhotoImage(Image.open('C:/Users/LENOVO/PycharmProjects/Rusu lite/images buttons/back.png'))
            back = Button(frame_dct, image=b, compound=CENTER, bg="black", borderwidth=0
                          , activebackground="black", command=frame_dct.destroy)
            back.place(x=200, y=50)
            mr.mainloop()


        def add_genre():
            frame_gen = Frame(mr, width=1360, height=600, bg="black")
            frame_gen.place(x=0, y=200)

            def reg_gen():
                if messagebox.askyesno("Register Confirmation", "ARE YOU SURE TO REGISTER THIS GENRE?") == False:
                    return

                else:
                    # Insert value into genre table
                    value7 = genre1.get()
                    query7 = "INSERT INTO genre (genre_name) VALUES (%s)"
                    my_cursor.execute(query7, (value7,))
                    mydb.commit()

                    messagebox.showinfo("MOVIE REGISTRATION FORM", "GENRE SUCCESSFULLY REGISTER")

                    genre1.delete(0, END)


            def rgc():
                if genre1.get() == "":
                    return messagebox.showwarning("REGISTER WARNING", "PLEASE PUT GENRE")

                reg_gen()

            lbl1 = Label(frame_gen, text="Genre Registration", font=('Cooper Black', 30, 'bold'), bg='black', fg='orange')
            lbl1.place(x=520, y=0)

            a_lbl3 = Label(frame_gen, text="GENRE:", font=('Cooper Black', 11), bg='black', fg="orange")
            a_lbl3.place(x=550, y=150)
            genre1 = Entry(frame_gen, width=20, font=('Comic Sans MS', 10))
            genre1.place(x=660, y=150)

            add_g = Button(frame_gen, text="ADD GENRE", bg="orange", command=rgc)
            add_g.place(x=705, y=220)

            b = ImageTk.PhotoImage(Image.open('C:/Users/LENOVO/PycharmProjects/Rusu lite/images buttons/back.png'))
            back = Button(frame_gen, image=b, compound=CENTER, bg="black", borderwidth=0
                          , activebackground="black", command=frame_gen.destroy)
            back.place(x=200, y=50)
            mr.mainloop()


        def add_movie():
            frame_movie = Frame(mr, width=1366, height=768, bg='black')
            frame_movie.place(x=0,y=0)
            global name_image
            lbl1 = Label(frame_movie, text="Movie Registration", font=('Cooper Black', 30, 'bold'), bg='black',
                        fg='orange')
            lbl1.place(x=150, y=20)

            def regm():

                def gal():

                    def gal2():
                        # insert all value to movie_Gallery table
                        my_cursor.execute("SELECT movie_id FROM movie")
                        movie_i = my_cursor.fetchall()
                        for mo in movie_i:
                            idm = mo[0]
                        mydb.commit()
                        sql_m = "INSERT INTO movie_gallery(movie_id, gallery_id)" "VALUES (%s, %s)"
                        value_m = (idm, gal)
                        my_cursor.execute(sql_m, value_m)
                        mydb.commit()

                        # insert all value to image_Gallery table
                        my_cursor.execute("SELECT image_id FROM image")
                        image_i = my_cursor.fetchall()
                        for im in image_i:
                            idi = im[0]
                        mydb.commit()
                        sql_im = "INSERT INTO image_gallery(image_id, gallery_id)" "VALUES (%s, %s)"
                        value_im = (idi, gal)
                        my_cursor.execute(sql_im, value_im)
                        mydb.commit()

                        messagebox.showinfo("MOVIE REGISTRATION FORM", "FILM SUCCESSFULLY REGISTER")
                        frame_movie.destroy()

                    # insert all value to Gallery table
                    my_cursor.execute("SELECT gallery_id FROM gallery")
                    gal_i = my_cursor.fetchall()
                    for ga in gal_i:
                        gal = ga[0]

                    # insert all value to actor_Gallery table
                    #actor1
                    mydb.commit()
                    sql_ac = "INSERT INTO actor_gallery(actors_id, gallery_id)" "VALUES (%s, %s)"
                    value_ac = (act_ids, gal)
                    my_cursor.execute(sql_ac, value_ac)
                    mydb.commit()

                    #actor2
                    mydb.commit()
                    sql_ac = "INSERT INTO actor_gallery(actors_id, gallery_id)" "VALUES (%s, %s)"
                    value_ac = (act_ids2, gal)
                    my_cursor.execute(sql_ac, value_ac)
                    mydb.commit()


                    # insert all value to director_Gallery table
                    #director1
                    mydb.commit()
                    sql_dd = "INSERT INTO director_gallery(directors_id, gallery_id)" "VALUES (%s, %s)"
                    value_dd = (dct_ids, gal)
                    my_cursor.execute(sql_dd, value_dd)
                    mydb.commit()

                    if director2.get() != '':
                        # director2
                        my_cursor.execute("SELECT directors_id FROM director WHERE name LIKE %s LIMIT 1",
                                          ("%" + director2.get() + "%",))
                        dcts = my_cursor.fetchall()
                        for d in dcts:
                            dct_ids2 = d[0]
                        print(dct_ids2)
                        mydb.commit()

                        my_cursor.execute("SELECT movie_id FROM movie")
                        mov = my_cursor.fetchall()
                        for movi in mov:
                            movie_ids = movi[0]
                        print(movie_ids)
                        mydb.commit()

                        sqld = "INSERT INTO rusulite.directed_by (directed_by.directors_id, directed_by.movie_id) VALUES (%s, %s)"
                        valued = dct_ids2, movie_ids
                        my_cursor.execute(sqld, valued)
                        mydb.commit()

                        mydb.commit()
                        sql_dd = "INSERT INTO director_gallery(directors_id, gallery_id)" "VALUES (%s, %s)"
                        value_dd = (dct_ids2, gal)
                        my_cursor.execute(sql_dd, value_dd)
                        mydb.commit()
                        gal2()

                    else:
                        gal2()


                #insert into gallery table
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

                # Insert value into image table
                sql3 = "INSERT INTO image (image_name) VALUES (%s)"
                my_cursor.execute(sql3, (name_image,))
                mydb.commit()

                # Insert value into genre_movie table
                # genre1
                my_cursor.execute("SELECT genre.genre_id FROM rusulite.genre WHERE genre.genre_name LIKE %s LIMIT 1",
                                  ("%" + genre1.get() + "%",))
                gen_i = my_cursor.fetchall()
                for ga in gen_i:
                    genre_ids = ga[0]


                my_cursor.execute("SELECT movie_id FROM movie")
                mov = my_cursor.fetchall()
                for movi in mov:
                    movie_ids = movi[0]

                mydb.commit()
                sqlg = "INSERT INTO rusulite.genre_movie (genre_movie.genre_id, genre_movie.movie_id) VALUES (%s, %s)"
                valueg = genre_ids, movie_ids
                my_cursor.execute(sqlg, valueg)
                mydb.commit()

                # genre 2
                my_cursor.execute("SELECT genre.genre_id FROM rusulite.genre WHERE genre.genre_name LIKE %s LIMIT 1",
                                  ("%" + genre2.get() + "%",))
                gen_i = my_cursor.fetchall()
                for ga in gen_i:
                    genre_ids = ga[0]


                my_cursor.execute("SELECT movie_id FROM movie")
                mov = my_cursor.fetchall()
                for movi in mov:
                    movie_ids = movi[0]

                mydb.commit()

                sqlg = "INSERT INTO rusulite.genre_movie (genre_movie.genre_id, genre_movie.movie_id) VALUES (%s, %s)"
                valueg = genre_ids, movie_ids
                my_cursor.execute(sqlg, valueg)
                mydb.commit()

                # genre3
                my_cursor.execute("SELECT genre.genre_id FROM rusulite.genre WHERE genre.genre_name LIKE %s LIMIT 1",
                                  ("%" + genre3.get() + "%",))
                gen_i = my_cursor.fetchall()
                for ga in gen_i:
                    genre_ids = ga[0]


                my_cursor.execute("SELECT movie_id FROM movie")
                mov = my_cursor.fetchall()
                for movi in mov:
                    movie_ids = movi[0]

                mydb.commit()
                sqlg = "INSERT INTO rusulite.genre_movie (genre_movie.genre_id, genre_movie.movie_id) VALUES (%s, %s)"
                valueg = genre_ids, movie_ids
                my_cursor.execute(sqlg, valueg)
                mydb.commit()


                # Insert value into performed_in table
                #actor1
                my_cursor.execute("SELECT actors_id FROM actor WHERE name LIKE %s LIMIT 1", ("%" + actor.get() + "%",))
                acts = my_cursor.fetchall()
                for a in acts:
                    act_ids = a[0]


                my_cursor.execute("SELECT movie_id FROM movie")
                mov = my_cursor.fetchall()
                for movi in mov:
                    movie_ids = movi[0]

                sqlp = "INSERT INTO rusulite.performed_in (performed_in.character, performed_in.actors_id, performed_in.movie_id) VALUES (%s, %s, %s)"
                valuep = character.get(), act_ids, movie_ids
                my_cursor.execute(sqlp, valuep)
                mydb.commit()

                # actor2
                my_cursor.execute("SELECT actors_id FROM actor WHERE name LIKE %s LIMIT 1", ("%" + actor2.get() + "%",))
                acts = my_cursor.fetchall()
                for a in acts:
                    act_ids2 = a[0]


                my_cursor.execute("SELECT movie_id FROM movie")
                mov = my_cursor.fetchall()
                for movi in mov:
                    movie_ids = movi[0]


                sqlp = "INSERT INTO rusulite.performed_in (performed_in.character, performed_in.actors_id, performed_in.movie_id) VALUES (%s, %s, %s)"
                valuep = character2.get(), act_ids2, movie_ids
                my_cursor.execute(sqlp, valuep)
                mydb.commit()

                # Insert value into directed_by table
                #director1
                my_cursor.execute("SELECT directors_id FROM director WHERE name LIKE %s LIMIT 1",
                                  ("%" + director.get() + "%",))
                dcts = my_cursor.fetchall()
                for d in dcts:
                    dct_ids = d[0]
                mydb.commit()

                my_cursor.execute("SELECT movie_id FROM movie")
                mov = my_cursor.fetchall()
                for movi in mov:
                    movie_ids = movi[0]

                mydb.commit()

                sqld = "INSERT INTO rusulite.directed_by (directed_by.directors_id, directed_by.movie_id) VALUES (%s, %s)"
                valued = dct_ids, movie_ids
                my_cursor.execute(sqld, valued)
                mydb.commit()

                gal()

            def rmc():
                if year_entry.get() == "" or country_entry.get() == "" or title.get() == "":
                    return messagebox.showwarning("REGISTER WARNING", "PLEASE COMPLETE THE OUTPUT")

                if name_image == "":
                    return messagebox.showwarning("REGISTER WARNING", "PLEASE PUT MOVIE IMAGE ")

                if character == "":
                    return messagebox.showwarning("REGISTER WARNING",
                                                  "PLEASE COMPLETE THE OUTPUT IN THE MOVIE CHARACTER")
                if link.get() == "":
                    return messagebox.showwarning("REGISTER WARNING", "PLEASE COMPLETE THE OUTPUT")

                if actor == "Actor":
                    return messagebox.showwarning("REGISTER WARNING", "PLEASE SELECT ACTOR FOR THE MOVIE")

                if director == "Director":
                    return messagebox.showwarning("REGISTER WARNING", "PLEASE SELECT ACTOR FOR THE MOVIE")

                if genre1 == "Genre":
                    return messagebox.showwarning("REGISTER WARNING", "PLEASE SELECT ACTOR FOR THE MOVIE")

                regm()


            frm_image1 = Frame(frame_movie, width=220, height=227, highlightbackground="orange", highlightthickness=1,
                               bg="black")
            frm_image1.place(x=300, y=100)

            lbl = Label(frm_image1, bg="black")
            lbl.place(x=0, y=0)

            def add_image():
                global name_image
                my_cursor = mydb.cursor()

                fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File",
                                                 filetypes=(("PNG File", "*.png"), ("All Files", '*.*')))
                name_image = os.path.basename(fln)
                img = Image.open(fln)
                img = ImageTk.PhotoImage(img)
                lbl.configure(image=img)
                lbl.image = img

            browse_lbl = Label(frm_image1, text="219 x 227", font=('Comic Sans MS', 8), bg="black", fg="orange")
            browse_lbl.place(x=110, y=6)
            browse_lbl2 = Label(frm_image1, text="IMAGE", font=('Comic Sans MS', 8), bg="black", fg="orange")
            browse_lbl2.place(x=40, y=6)

            plus = ImageTk.PhotoImage(
                Image.open('C:/Users/LENOVO/PycharmProjects/Rusu lite/images buttons/plusimage.png'))
            browse_btn = Button(frm_image1, image=plus, compound=CENTER, bg="black", borderwidth=0,
                                activebackground="black", command=add_image)
            browse_btn.place(x=95, y=100)

            #actor1
            lbl_act = Label(frame_movie, text="ACTOR1:",font=('Cooper Black', 11), bg="black", fg="orange")
            lbl_act.place(x=810, y=95)
            my_cursor.execute("""SELECT name FROM actor""")
            act = my_cursor.fetchall()
            act_n = list(itertools.chain.from_iterable(OrderedDict.fromkeys(act)))
            actor = ttk.Combobox(frame_movie, width=20)
            actor.set("Actor")
            actor['values'] = (act_n)
            actor.place(x=810, y=115)

            charc_lbl = Label(frame_movie, text="PLAY AS:", font=('Cooper Black', 11), bg='black', fg="orange")
            charc_lbl.place(x=980, y=95)
            character = Entry(frame_movie, width=20, font=('Comic Sans MS', 10))
            character.place(x=980, y=115)

            #actor2
            lbl_act = Label(frame_movie, text="ACTOR2:", font=('Cooper Black', 11), bg="black", fg="orange")
            lbl_act.place(x=810, y=147)
            my_cursor.execute("""SELECT name FROM actor""")
            act = my_cursor.fetchall()
            act_n = list(itertools.chain.from_iterable(OrderedDict.fromkeys(act)))
            actor2 = ttk.Combobox(frame_movie, width=20)
            actor2.set("Actor")
            actor2['values'] = (act_n)
            actor2.place(x=810, y=170)

            charc_lbl = Label(frame_movie, text="PLAY AS:", font=('Cooper Black', 11), bg='black', fg="orange")
            charc_lbl.place(x=980, y=147)
            character2 = Entry(frame_movie, width=20, font=('Comic Sans MS', 10))
            character2.place(x=980, y=170)

            #director1
            lbl_act = Label(frame_movie, text="DIRECTOR1:", font=('Cooper Black', 11), bg="black", fg="orange")
            lbl_act.place(x=810, y=210)
            my_cursor.execute("""SELECT name FROM director""")
            dct = my_cursor.fetchall()
            dct_n = list(itertools.chain.from_iterable(OrderedDict.fromkeys(dct)))
            director = ttk.Combobox(frame_movie, width=20)
            director.set("Director")
            director['values'] = (dct_n)
            director.place(x=810, y=233)

            #Director2
            lbl_act = Label(frame_movie, text="DIRECTOR2:", font=('Cooper Black', 11), bg="black", fg="orange")
            lbl_act.place(x=980, y=210)
            my_cursor.execute("""SELECT name FROM director""")
            dct = my_cursor.fetchall()
            dct_n = list(itertools.chain.from_iterable(OrderedDict.fromkeys(dct)))
            director2 = ttk.Combobox(frame_movie, width=20)
            director2.set("")
            director2['values'] = (dct_n)
            director2.place(x=980, y=233)

            #movie genre
            lbl_act = Label(frame_movie, text="GENRE1:", font=('Cooper Black', 11), bg="black", fg="orange")
            lbl_act.place(x=580, y=277)
            my_cursor.execute("""SELECT genre_name FROM genre""")
            gen = my_cursor.fetchall()
            gen_n = list(itertools.chain.from_iterable(OrderedDict.fromkeys(gen)))
            genre1 = ttk.Combobox(frame_movie, width=20)
            genre1.set("Genre")
            genre1['values'] = (gen_n)
            genre1.place(x=580, y=300)

            lbl_act = Label(frame_movie, text="GENRE2:", font=('Cooper Black', 11), bg="black", fg="orange")
            lbl_act.place(x=740, y=277)
            my_cursor.execute("""SELECT genre_name FROM genre""")
            gen = my_cursor.fetchall()
            gen_n = list(itertools.chain.from_iterable(OrderedDict.fromkeys(gen)))
            genre2 = ttk.Combobox(frame_movie, width=20)
            genre2.set("Genre")
            genre2['values'] = (gen_n)
            genre2.place(x=740, y=300)

            lbl_act = Label(frame_movie, text="GENRE3:", font=('Cooper Black', 11), bg="black", fg="orange")
            lbl_act.place(x=900, y=277)
            my_cursor.execute("""SELECT genre_name FROM genre""")
            gen = my_cursor.fetchall()
            gen_n = list(itertools.chain.from_iterable(OrderedDict.fromkeys(gen)))
            genre3 = ttk.Combobox(frame_movie, width=20)
            genre3.set("Genre")
            genre3['values'] = (gen_n)
            genre3.place(x=900, y=300)


            # YEAR
            ycmt_image = Frame(frame_movie, width=183, height=150, highlightbackground="orange", highlightthickness=1,
                               bg="black")
            ycmt_image.place(x=570, y=100)
            y_lbl = Label(frame_movie, text="YEAR:", font=('Cooper Black', 11), bg='black', fg="orange")
            y_lbl.place(x=575, y=90)
            year_entry = Entry(frame_movie, width=20, font=('Comic Sans MS', 10))
            year_entry.place(x=580, y=115)

            # COUNTRY
            c_lbl = Label(frame_movie, text="COUNTRY:", font=('Cooper Black', 11), bg='black', fg="orange")
            c_lbl.place(x=575, y=140)
            country_entry = Entry(frame_movie, width=20, font=('Comic Sans MS', 10))
            country_entry.place(x=580, y=165)

            # MOVIE TITLE
            t_lbl = Label(frame_movie, text="MOVIE TITLE:", font=('Cooper Black', 11), bg='black', fg="orange")
            t_lbl.place(x=575, y=190)
            title = Entry(frame_movie, width=20, font=('Comic Sans MS', 10))
            title.place(x=580, y=215)

            # DESCRIPTION
            dscrptn_image = Frame(frame_movie, width=430, height=200, highlightbackground="orange", highlightthickness=1,
                                  bg="black")
            dscrptn_image.place(x=570, y=360)
            dc_lbl = Label(frame_movie, text="DESCRIPTION:", font=('Cooper Black', 12), bg='black', fg="orange")
            dc_lbl.place(x=580, y=350)
            description_text = Text(frame_movie, height=9, width=50, font=('Comic Sans MS', 10))
            description_text.place(x=580, y=380)

            # LINK
            url_image = Frame(frame_movie, width=965, height=50, highlightbackground="orange", highlightthickness=1,
                              bg="black")
            url_image.place(x=190, y=575)
            lnk_lbl = Label(frame_movie, text="LINK/URL:", font=('Cooper Black', 14), bg='black', fg="orange")
            lnk_lbl.place(x=200, y=560)
            link = Entry(frame_movie, width=117, font=('Comic Sans MS', 10))
            link.place(x=201, y=590)




            add_m = Button(frame_movie, text="REGISTER MOVIE", font=('Comic Sans MS', 16), bg="orange", command=rmc)
            add_m.place(x=570, y=650)

            b = ImageTk.PhotoImage(Image.open('C:/Users/LENOVO/PycharmProjects/Rusu lite/images buttons/back.bmp.png'))
            back = Button(frame_movie, image=b, compound=CENTER, bg="black", borderwidth=0
                          , activebackground="black", command=frame_movie.destroy)
            back.place(x=5, y=5)

            mr.mainloop()


        #rusu lite logo image
        rusu = ImageTk.PhotoImage(Image.open('C:/Users/LENOVO/PycharmProjects/Rusu lite/images buttons/miming.png'))
        rusu_logo = Label(mr, image=rusu, bg="black")
        rusu_logo.place(x=635, y=5)

        lbl1 = Label(mr, text="Registration", font=('Cooper Black', 30, 'bold'), bg='black', fg='orange')
        lbl1.place(x=580, y=220)

        adda= ImageTk.PhotoImage(
            Image.open('C:/Users/LENOVO/PycharmProjects/Rusu Lite/images buttons/addactor.png'))
        add_actor_btn = Button(mr, image=adda, bg="black", compound=CENTER, borderwidth=0, command=add_actor)
        add_actor_btn.place(x=300, y=450)

        addd = ImageTk.PhotoImage(
            Image.open('C:/Users/LENOVO/PycharmProjects/Rusu Lite/images buttons/adddirector.png'))
        add_director_btn = Button(mr, image=addd, bg="black", compound=CENTER, borderwidth=0, command=add_director)
        add_director_btn.place(x=550, y=450)

        addg = ImageTk.PhotoImage(
            Image.open('C:/Users/LENOVO/PycharmProjects/Rusu Lite/images buttons/addgenre.png'))
        add_genre_btn = Button(mr, image=addg, bg="black", compound=CENTER, borderwidth=0, command=add_genre)
        add_genre_btn.place(x=800, y=450)

        addm = ImageTk.PhotoImage(Image.open('C:/Users/LENOVO/PycharmProjects/Rusu lite/images buttons/addmovie.png'))
        add_movie_btn = Button(mr, image=addm, bg="black", compound=CENTER, borderwidth=0, command=add_movie)
        add_movie_btn.place(x=1000, y=450)

        def des3():
            mr.destroy()
            mp()

        b = ImageTk.PhotoImage(Image.open('C:/Users/LENOVO/PycharmProjects/Rusu lite/images buttons/back.bmp.png'))
        back = Button(mr, image=b, compound=CENTER, bg="black", borderwidth=0
                      , activebackground="black", command=des3)
        back.place(x=5, y=5)
        mr.mainloop()

        # search in search bar
    def search():

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
        my_scrollbar.config(command=my_canvas.xview)

        my_canvas.configure(xscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"), bg="black",
                                                                        highlightbackground="black"))

        second_frame = Frame(my_canvas, bg="black")

        my_canvas.create_window(0, 300, window=second_frame, anchor="sw")

        my_cursor = mydb.cursor()

        my_cursor.execute("""SELECT gallery.movie_title, image.image_name FROM gallery INNER JOIN image ON image.image_id = gallery.gallery_id""")

        id = my_cursor.fetchall()

        ent = search_entry.get()

        y = str(ent)
        x = y.title()

        movie_buttons = list(range(len(id)))
        movie_images = list(range(len(id)))

        for count, i in enumerate(id):
            img_nms = i[1]
            if x in i[0]:
                movie_images[count] = ImageTk.PhotoImage(Image.open(str(img_nms)))

                movie_buttons[count] = Button(second_frame, image=movie_images[count], bg="black",
                                              borderwidth=0,
                                              activebackground="black", command=lambda i=i: movie(i))
                movie_buttons[count].grid(row=0, column=count, pady=(40, 30), padx=(30))

        def des():
            my_canvas.destroy()
            my_scrollbar.destroy()

        b = ImageTk.PhotoImage(Image.open('C:/Users/LENOVO/PycharmProjects/Rusu lite/images buttons/back.png'))
        back_btn = Button(my_canvas, image=b, compound=CENTER, bg="black", borderwidth=0
                          , activebackground="black", command=des)
        back_btn.place(x=32, y=0)

        main_p.mainloop()

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

                my_scrollbar = ttk.Scrollbar(my_canvas, orient=HORIZONTAL, command=my_canvas.xview)
                my_scrollbar.pack(pady=(400, 5), fill=X)

                my_canvas.configure(xscrollcommand=my_scrollbar.set)
                my_canvas.bind('<Configure>',
                               lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"), bg="black",
                                                             highlightbackground="black"))

                second_frame = Frame(my_canvas, bg="black")

                my_canvas.create_window(0, 300, window=second_frame, anchor="sw")

                my_cursor = mydb.cursor()
                my_cursor.execute("""SELECT genre.genre_name, image.image_name FROM rusulite.genre_movie
                                             INNER JOIN rusulite.genre ON genre.genre_id = genre_movie.genre_id 
                                             INNER JOIN rusulite.image ON image.image_id = genre_movie.movie_id
                                             WHERE genre_movie.genre_id = genre_movie.genre_id  AND image.image_id = genre_movie.movie_id""")

                idd = my_cursor.fetchall()

                movie_buttons = list(range(len(idd)))
                movie_images = list(range(len(idd)))

                g1 = genre1.get()

                for count, i in enumerate(idd):
                    img_nms = i[1]
                    if g1 in i[0]:
                        movie_images[count] = ImageTk.PhotoImage(Image.open(str(img_nms)))

                        movie_buttons[count] = Button(second_frame, image=movie_images[count], bg="black",
                                                      borderwidth=0,
                                                      activebackground="black", command=lambda i=i: movie(i))
                        movie_buttons[count].grid(row=0, column=count, pady=(40, 30), padx=(30))



                def des():
                    my_canvas.destroy()
                    my_scrollbar.destroy()

                b = ImageTk.PhotoImage(Image.open('C:/Users/LENOVO/PycharmProjects/Rusu lite/images buttons/back.png'))
                back_btn2 = Button(my_canvas, image=b, compound=CENTER, bg="black", borderwidth=0
                                   , activebackground="black", command=des)
                back_btn2.place(x=32, y=0)

                frame2.destroy()
                frame3.destroy()
                frame3.mainloop()


            def des9():
                if genre1.get() == "" :
                    return messagebox.showwarning("SEARCH FILTER ERROR","Select Genre To Search")

                else:
                    genre_filt()

            # Genre Entry


            lbl_act = Label(frame3, text="GENRE:", font=('Cooper Black', 15), bg="black", fg="orange")
            lbl_act.place(x=160, y=80)
            my_cursor.execute("""SELECT genre_name FROM genre""")
            gen = my_cursor.fetchall()
            gen_n = list(itertools.chain.from_iterable(OrderedDict.fromkeys(gen)))
            genre1 = ttk.Combobox(frame3, width=20)
            genre1.set("")
            genre1['values'] = (gen_n)
            genre1.place(x=135, y=110)

            sgf = Button(frame3, text="Search", bg="orange", command=des9)
            sgf.place(x=182, y=155)

            b = ImageTk.PhotoImage(Image.open('C:/Users/LENOVO/PycharmProjects/Rusu lite/images buttons/back.png'))
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

            my_scrollbar = ttk.Scrollbar(my_canvas, orient=HORIZONTAL, command=my_canvas.xview)
            my_scrollbar.pack(pady=(400, 5), fill=X)

            my_canvas.configure(xscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"), bg="black",
                                                                        highlightbackground="black"))

            second_frame = Frame(my_canvas, bg="black")

            my_canvas.create_window(0, 300, window=second_frame, anchor="sw")

            my_cursor = mydb.cursor()
            my_cursor.execute("""
                                  SELECT actor.name, director.name, movie.country, movie.year, image.image_name FROM rusulite.gallery
                                  INNER JOIN rusulite.actor_gallery ON actor_gallery.gallery_id = gallery.gallery_id
                                  INNER JOIN rusulite.actor ON actor.actors_id = actor_gallery.actors_id 
                                  INNER JOIN rusulite.image_gallery ON image_gallery.gallery_id = gallery.gallery_id
                                  INNER JOIN rusulite.image ON image_gallery.image_id = image.image_id 
                                  INNER JOIN rusulite.director_gallery ON director_gallery.gallery_id = gallery.gallery_id
                                  INNER JOIN rusulite.director ON director.directors_id = director_gallery.directors_id
                                  INNER JOIN rusulite.movie_gallery ON movie_gallery.gallery_id = gallery.gallery_id
                                  INNER JOIN rusulite.movie ON movie.movie_id = movie_gallery.movie_id 
                                  WHERE gallery.gallery_id = actor_gallery.gallery_id AND gallery.gallery_id = director_gallery.gallery_id AND gallery.gallery_id = movie_gallery.gallery_id  AND gallery.gallery_id = image_gallery.gallery_id""")
            id = my_cursor.fetchall()

            actor_n = actor.get()
            direct_n = director.get()
            country_n = country.get()
            year_n = yr.get()

            movie_buttons = list(range(len(id)))
            movie_images = list(range(len(id)))

            temp_list = []
            for count, i in enumerate(id):
                img_nms = i[4]
                x = str(i[3])
                if actor_n in i[0]:

                    if direct_n in i[1]:

                        if country_n in i[2]:

                            if year_n in x:

                                if img_nms not in temp_list:

                                    temp_list.append(img_nms)

                                    print(img_nms)

                                    movie_images[count] = ImageTk.PhotoImage(Image.open(str(img_nms)))

                                    movie_buttons[count] = Button(second_frame, image=movie_images[count],
                                                                  bg="black",
                                                                  borderwidth=0,
                                                                  activebackground="black",
                                                                  command=lambda i=i: movie(i))
                                    movie_buttons[count].grid(row=0, column=count, pady=(40, 30), padx=(30))

            def des():
                my_canvas.destroy()
                my_scrollbar.destroy()

            b = ImageTk.PhotoImage(Image.open('C:/Users/LENOVO/PycharmProjects/Rusu lite/images buttons/back.png'))
            back_btn = Button(my_canvas, image=b, compound=CENTER, bg="black", borderwidth=0
                              , activebackground="black", command=des)
            back_btn.place(x=32, y=0)

            frame2.destroy()
            main_p.mainloop()

        lbl_yrs = Label(frame2, text="Year", bg="black", fg="white")
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
        act_n = (list(itertools.chain.from_iterable(OrderedDict.fromkeys(act))))
        actor = ttk.Combobox(frame2, width=20)
        actor.set("")
        actor['values'] = (act_n)
        actor.place(x=230, y=65)


        lbl_direct = Label(frame2, text="Director", bg="black", fg="white")
        lbl_direct.place(x=30, y=45)
        my_cursor.execute("""SELECT name FROM director""")
        director1 = my_cursor.fetchall()
        director_n = (list(itertools.chain.from_iterable(OrderedDict.fromkeys(director1))))
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

        b = ImageTk.PhotoImage(Image.open('C:/Users/LENOVO/PycharmProjects/Rusu lite/images buttons/back.png'))
        back = Button(frame2, image=b, compound=CENTER, bg="black", borderwidth=0
                      , activebackground="black", command=frame2.destroy)
        back.place(x=182, y=245)

        main_p.mainloop()


    directory_path = os.path.dirname(__file__)
    file_path = os.path.join(directory_path, 'images buttons')

    # Entry search box
    search_entry = Entry(main_p, width=40, bg='light goldenrod', font=("helvitica", 18))
    search_entry.place(x=420, y=180)

    ms = ImageTk.PhotoImage(Image.open('C:/Users/LENOVO/PycharmProjects/Rusu lite/images buttons/minisearch.png'))
    ms_lbl = Label(main_p, image=ms, bg="black")
    ms_lbl.place(x=365, y=174)

    # rusu lite logo image
    rusu = ImageTk.PhotoImage(Image.open('C:/Users/LENOVO/PycharmProjects/Rusu lite/images buttons/miming.png'))
    rusu_logo = Label(main_p, image=rusu, bg="black")
    rusu_logo.place(x=635, y=5)

    def des5():
        if search_entry.get() == "":
            return messagebox.showwarning("SEARCH WARNING",
                                          "Search by typing a word or phrase in the search box at the top of this page ")
        search()

    # search button
    s = ImageTk.PhotoImage(Image.open('C:/Users/LENOVO/PycharmProjects/Rusu lite/images buttons/searchbtn.png'))
    search_btn = Button(main_p, image=s, compound=CENTER, bg="black", borderwidth=0
                        , activebackground="black", command=des5)
    search_btn.place(x=643, y=220)

    # add movie page button
    addm = ImageTk.PhotoImage(Image.open('C:/Users/LENOVO/PycharmProjects/Rusu Lite/images buttons/registerbtn.png'))
    add_movie_btn = Button(main_p, image=addm, bg="black", compound=CENTER, borderwidth=0,  command=regs_movie)
    add_movie_btn.place(x=1150, y=10)

    # Specific Search
    fil_movie_btn = Button(main_p, text="Search Filter", bg="orange", borderwidth=5, command=specific_search)
    fil_movie_btn.place(x=950, y=180)

    def des6():
        if messagebox.askyesno("EXIT INFORMATION", "DO YOU WANNA LEAVE ME TOO? (T.T)") == False:
            return
        else:
            main_p.destroy()

    exitm = ImageTk.PhotoImage(Image.open('C:/Users/LENOVO/PycharmProjects/Rusu lite/images buttons/exit.png'))
    exit = Button(main_p, image=exitm, bg="black", command=des6, borderwidth=0)
    exit.place(x=15, y=15)

    # movie main page movie
    frame1 = Frame(main_p, width=860, height=300, bg="black", highlightbackground="black")
    frame1.place(x=266, y=300)

    my_canvas = Canvas(frame1)
    my_canvas.place(x=-43, y=40, width=900)

    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"), bg="black",
                                                                highlightbackground="black"))

    second_frame = Frame(my_canvas, bg="black", borderwidth=0)

    my_canvas.create_window(0, 100, window=second_frame, anchor="se")

    my_cursor = mydb.cursor()

    my_cursor.execute("SELECT image_name FROM image")
    id = my_cursor.fetchall()



    movie_buttons = list(range(len(id)))
    movie_images = list(range(len(id)))

    for count, i in enumerate(id):
        img_nms = i[0]
        # print(count, i[0])
        movie_images[count] = ImageTk.PhotoImage(Image.open(str(img_nms)))

        movie_buttons[count] = Button(second_frame, image=movie_images[count], bg="black", borderwidth=0,
                                      activebackground="black", command=lambda i=i: movie(i))
        movie_buttons[count].grid(row=0, column=count, pady=(40, 30), padx=(30))


    main_p.mainloop()

if __name__ == '__main__':
   mp()
