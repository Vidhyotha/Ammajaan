import random
import tkinter as tk
import tkinter.ttk as ttk
import math
import pickle
import csv

cartstuff={}
username=[]
things={}
f=open("Items.csv",newline="",encoding='utf-8')
reader=csv.reader(f)
for r in reader:
    things[r[0]]=[r[1],r[2],r[3]]
f.close()

classics={}
for a in things:
        
    h=random.randint(10,90)
    classics[a]=h



def login():

    global username

    def aloginthing(event=None):

        u=e1.get()
        p=g1.get()
        t1=tk.Tk()
        f1=tk.Frame(t1,width=1000,height=1000,bg='#f8b313')

        users={}
        f=open("users.txt",'r')
        l=f.readlines()
        for i in l:
            j=i.split()
            users[j[0]]=j[1]

        if u=='':

            t1.title("FAILURE")
            l=tk.Label(t1,text="No username entered",bg='#f8b313')
            l.configure(font=("Bebas Neue", 20))
            l.pack()

        elif p=='':

            t1.title("FAILURE")
            l=tk.Label(t1,text="No password entered",bg='#f8b313')
            l.configure(font=("Bebas Neue", 20))
            l.pack()
            
        elif u in users:

            if users[u]==p:

                t1.title("SUCCESS!")
                l1=tk.Label(t1,text="You have Successfully Logged In",bg='#f8b313')
                l1.pack()
                l1.configure(font=('Bebas Neue',20))

                try:
                    f=open(u+'.txt')
                    l=f.readlines()
                    for a in l:
                        j=a.split(',')
                        cartstuff[j[0]]=j[1].split("\\")[0]
                    f.close()
                    

                except:
                    f=open(u+'.txt','w')
                    f.close()

                username.append(u)

                rt.destroy()
                therealdeal(things)
                
            else:

                t1.title("FAILURE!")
                l1=tk.Label(t1,text="wrong password",bg='#f8b313')
                l1.configure(font=('Bebas Neue',20))
                l1.pack()
                
        else:

            t1.title("!")
            l1=tk.Label(t1,text="wrong username",bg='#f8b313')
            l1.configure(font=('Bebas Neue',20))
            l1.pack()

   
    def logtomain(event=None):

        rt.destroy()
        entrypage()
    
    rt=tk.Tk()
    rt.geometry('500x600')
    rt.resizable(0,0)
    rt.config(bg='#f7b407')

    fram=tk.Frame(master=rt,bg='#f7b407')
    fram.pack_propagate(0)
    fram.pack(fill=tk.BOTH,expand=1)

    rt.title("AMMAJAAN LOGIN")

    bleh=tk.Label(fram,background='#f7b407')
    bleh.grid(row=1,column=1,padx=130)

    labeli=tk.Label(fram,text='Enter Username',bg='#f7b407')
    labeli.grid(row=4,column=1,pady=50)
    labeli.configure(font=("Bebas Neue", 20))

    labelii=tk.Label(fram,text=' Enter Password',bg='#f7b407')
    labelii.configure(font=("Bebas Neue", 20))

    labelii.grid(row=7,column=1)
    e1=tk.Entry(fram,width=12)
    e1.grid(row=4,column=5)
    e1.configure(font=("Times New Roman", 20))

    g1=tk.Entry(fram,width=12,show='*')
    g1.configure(font=("Times New Roman", 20))
    g1.grid(row=7,column=5,)

    e1.bind('<Return>',aloginthing)

    g1.bind('<Return>',aloginthing)

    bleh2=tk.Label(fram,bg='#f7b407')
    bleh2.grid(row=8,column=2)
    bleh3=tk.Label(fram,bg='#f7b407')
    bleh3.grid(row=9,column=2)
    bleh4=tk.Label(fram,bg='#f7b407')
    bleh4.grid(row=9,column=3)

    b3=tk.Button(fram,text='Login',command=aloginthing,bg='#f7b407',width=5,height=1)
    b3.configure(font=("Bebas Neue", 20))
    b3.grid(row=9,column=1)

    b4=tk.Button(fram,text='Cancel',command=logtomain,bg='#f7b407',width=5,height=1)
    b4.grid(row=9,column=5,pady=50)
    b4.configure(font=("Bebas Neue", 20))

    image1=tk.PhotoImage(file='Logo.png',master=rt)
    Pi1c=tk.Label(rt,image=image1)
    Pi1c.pack(pady=30)
    Pi1c.image=image1
    rt.mainloop()
    
#registeration page:
def regi():

    def loginthing(event=None):
        
        u=e.get()
        p=g.get()
        t=tk.Tk()

        f=tk.Frame(t,width=1000,height=1000,bg='#f8b313')

        users={}
        f=open("users.txt",'r')
        l=f.readlines()

        for i in l:
            j=i.split()
            users[j[0]]=j[1]

        if u=='':

            t.title("FAILURE")
            l=tk.Label(t,text="No username entered",bg='#f8b313')
            l.configure(font=("Bebas Neue", 20))
            l.pack()

        elif p=='':

            t.title("FAILURE")
            l=tk.Label(t,text="No password entered",bg='#f8b313')
            l.configure(font=("Bebas Neue", 20))
            l.pack()

        elif u not in users:

            f=open("users.txt",'a+')
            s=u+' '+p 
            f.write(s)
            f.write('\n')
            f.close()

            t.title("SUCCESS!")
            l=tk.Label(t,text="You have Successfully Registered",bg='#f8b313')
            l.configure(font=("Bebas Neue", 20))
            l.pack()

            rt.destroy()

            entrypage()

        else:

            t.title("FAILURE!")
            l=tk.Label(t,text="Username Already Exists",bg='#f8b313')
            l.configure(font=("Bebas Neue", 20))
            l.pack()
    
          
    def logtomain(event=None):

        rt.destroy()
        entrypage()

    rt=tk.Tk()
    rt.geometry('500x600')
    rt.resizable(0,0)
    rt.config(bg='#f7b407')

    fram=tk.Frame(master=rt,bg='#f7b407')
    fram.pack_propagate(0)
    fram.pack(fill=tk.BOTH,expand=1)

    rt.title("AMMAJAAN REGISTRATION")

    bleh=tk.Label(fram,bg='#f7b407')
    bleh.grid(row=1,column=1,padx=130)

    labeli=tk.Label(fram,text='Enter Username',bg='#f7b407',fg="Black")
    labeli.grid(row=4,column=1,pady=50)
    labeli.configure(font=("Bebas Neue", 20))

    labelii=tk.Label(fram,text=' Enter Password',bg='#f7b407',fg="Black")
    labelii.grid(row=7,column=1)
    labelii.configure(font=("Bebas Neue", 20))

    e=tk.Entry(fram,width=12)
    e.grid(row=4,column=5)
    e.configure(font=("Times New Roman", 20))

    g=tk.Entry(fram,width=12,show='*')
    g.grid(row=7,column=5,)
    
    g.configure(font=("Times New Roman", 20))

    e.bind('<Return>',loginthing)

    g.bind('<Return>',loginthing)

    bleh2=tk.Label(fram,bg='#f7b407')
    bleh2.grid(row=8,column=2)
    bleh3=tk.Label(fram,bg='#f7b407')
    bleh3.grid(row=9,column=2)
    bleh4=tk.Label(fram,bg='#f7b407')
    bleh4.grid(row=9,column=3)

    b3=tk.Button(fram,text='Register',command=loginthing,bg='#f7b407',fg="Black",width=7,height=1)
    b3.configure(font=("Bebas Neue", 20))
    b3.grid(row=9,column=1)

    b4=tk.Button(fram,text='Cancel',command=logtomain,bg='#f7b407',fg="Black",width=7,height=1)
    b4.grid(row=9,column=5,pady=50)
    b4.configure(font=("Bebas Neue", 20))

    image=tk.PhotoImage(file='Logo.png',master=rt)
    Pic=tk.Label(rt,image=image)
    Pic.pack(pady=30)
    Pic.image=image
    rt.mainloop()        

#Page to be displayed on execution of prograam
def entrypage():

    def gotolog():

        root.destroy()
        login()

    def gotoreg():

        root.destroy()
        regi()

    root=tk.Tk()
    root.title("WELCOME TO AMMAJAAN")
    root.geometry('500x700')
    root.configure(bg='#f7b407')

    img=tk.PhotoImage(file='Logo.png',master=root)
    Pic=tk.Label(root,image=img)
    Pic.image=img
    Pic.grid()
    
    labeli=tk.Label(root,text='You have money? Give it to us',bg='#f7b407',fg="Black")
    labeli.grid(pady=20)
    labeli.configure(font=("Bebas Neue", 30))
    
    logbutt=tk.Button(root,text="Login",command=gotolog,height=3,width=33,bg='#f7b407',fg="Black")
    logbutt.grid(padx=60,pady=10)
    logbutt.configure(font=("Bebas Neue", 20))

    regbutt=tk.Button(root,text="Register",command=gotoreg,height=3,width=33,bg='#f7b407',fg="Black")
    regbutt.grid(padx=60,pady=10)
    regbutt.configure(font=("Bebas Neue", 20))

    exbutt=tk.Button(root,text="Exit",command=root.destroy,height=3,width=33,bg='#f7b407',fg="Black")
    exbutt.grid(padx=60,pady=10)
    exbutt.configure(font=("Bebas Neue", 20))

#entrypage()
def therealdeal(things):

    global classics

    def gotomain(event=None):

        root.destroy()

        t=tk.Tk()
        t.title("SUCCESS!")

        l=tk.Label(t,text="You have Successfully Logged Out",bg='#f8b313')
        l.configure(font=("Bebas Neue", 20))
        l.pack()
        entrypage()

    def gotocart(event=None):

        root.destroy()
        carty()

    def printer(event=None):

        q=Lb1.curselection()
        productpage(a[q[0]].split('   ')[0])
        root.destroy()

    def searcher(event=None):
        
        s=search.get()
        q=s.rstrip()
        t=q.lstrip()

        if t!='':

            root.destroy()
            searchresults(s)

        else:

            t=tk.Tk()
            t.title("ERROR!")
            l=tk.Label(t,text="No Keyword Entered",bg='#f8b313')
            l.configure(font=("Bebas Neue", 100))
            l.pack()

    root=tk.Tk()
    root.configure(height=1920,width=1080,bg='#f7b407')
    root.title('Ammajaan')
    root.geometry('1330x768')

    frame=tk.Frame(root,bg='#f8b313',height='200',width='200')
    frame.grid(row=0,column=0)

    label_4=tk.Label(frame,bg='#f8b313',fg='Black',text='Search')
    label_4.configure(font=("Bebas Neue", 20))

    search=tk.Entry(frame,text='Type Here',width=42,fg='Black')
    search.configure(font=("Bebas Neue", 20))
    search.bind('<Return>',searcher)
    search.grid(row=0,column=3)

    label_4.grid(row=0,column=2,padx=40,sticky='E')

    cartbutt=tk.Button(frame,bg='#f8b313',text='Cart',command=gotocart)
    cartbutt.grid(row=0,column=5,padx=25,ipadx=25)
    cartbutt.configure(font=("Bebas Neue", 20))

    logout=tk.Button(frame,bg='#f8b313',text='Logout',command=gotomain)
    logout.grid(row=0,column=6,ipadx=15)
    logout.configure(font=("Bebas Neue", 20))

    image=tk.PhotoImage(file='Logo.png',master=root)
    Pic=tk.Label(frame,image=image)
    Pic.grid(row=0,column=0)
    Pic.image=image
    image1=tk.PhotoImage(file='search.png',master=root)
    searchbutt=tk.Button(frame,bg='White',image=image1,command=searcher)
    searchbutt.grid(row=0,column=4)
    searchbutt.image=image1
    search.bind('<Return>',searcher)

    frame1=tk.Frame(root,bg='#f8b313',height='200',width='200')
    frame1.grid(row=3,column=0)

    klassics=tk.Label(frame1,text='Today\'s Klassics',bg='#f8b313')
    klassics.configure(font=("Bebas Neue", 20))
    klassics.pack(side='top')

    scrollx=tk.Scrollbar(frame1,orient='horizontal',jump=1)
    scrollx.configure(bg='#f8b313')
    scrollx.pack(side='bottom',fill='x')

    scroll=tk.Scrollbar(frame1,orient='vertical',jump=1)
    scroll.configure()
    scroll.pack(side='right',fill='y')
    Lb1 = tk.Listbox(frame1,selectmode='SINGLE',yscrollcommand=scroll.set(0,0),xscrollcommand=scrollx.set(0,0),width=40,height=9,selectbackground='Red')

    for a in classics:
        Lb1.insert(1,a+'   ( '+ str(classics[a])+'% OFF)')
    
    Lb1.pack(fill='both')
    Lb1.bind('<Double-Button-1>',printer)
    a=Lb1.get(0,len(things))
    Lb1.config(bg='#f8b313',font=('Bebas Neue',25))
    scroll.config( command = Lb1.yview )

    a=Lb1.get(0,len(things))

    credit=tk.Label(root,text=' © Samarth Vijay & Vidhyotha Shetty')
    credit.grid(row=4,column=0,pady=50)
    credit.config(font=('Bebas Neue',20),bg='#f8b313')
        
def carty():

    global things

    def clearer():
        global cartstuff,username

        if a=="Your cart is empty.":
            pass

        def yaw(Lb1):
            
            Lb1.delete(0,'end')
            Lb1.insert(1,"Your cart is empty.")
            cartstuff.clear()
            f=open(username[0]+'.txt','w')
            f.close()
            rt.destroy()
            
        def naw():

            rt.destroy()

        l=list(str.split('    '))
        rt=tk.Tk()
        rt.configure(bg='#f8b313')
        rt.title("WARNING")

        lbl=tk.Label(rt,text="Are you sure you want to clear your cart?",bg='#f8b313')
        lbl.configure(font=("Bebas Neue", 20))
        lbl.pack(side='top')

        ybutt=tk.Button(rt,bg='#f8b313',text='Yes',command=lambda : yaw(Lb1),width=20)
        ybutt.configure(font=("Bebas Neue", 30))
        ybutt.pack(side='left')

        nbutt=tk.Button(rt,bg='#f8b313',text='No',command=lambda : naw(),width=20)
        nbutt.configure(font=("Bebas Neue", 30))
        nbutt.pack(side='right')
               

    def gotomain(event=None):

        root.destroy()
        t=tk.Tk()
        t.title("SUCCESS!")
        l=tk.Label(t,text="You have Successfully Logged Out",bg='#f8b313')
        l.configure(font=("Bebas Neue", 20))
        l.pack()
        entrypage()

    def gotohome(event=None):

        root.destroy()
        therealdeal(things)

    def printer(event=None):

        q=Lb1.curselection()
        productpage(a)
        root.destroy()

    def searcher(event=None):

        s=search.get()
        q=s.rstrip()
        t=q.lstrip()

        if t!='':

            root.destroy()
            searchresults(s)

        else:

            t=tk.Tk()
            t.title("SUCCESS!")
            l=tk.Label(t,text="No Keyword Entered",bg='#f8b313')
            l.configure(font=("Bebas Neue", 100))
            l.pack()

    def gotobill(event=None):

        bill(cartstuff,things)
        root.destroy()

    def deleter(Lb1):

        if a=="Your cart is empty.":
            pass

        def yaw(Lb1,l,q):

            del cartstuff[l[0]]
            Lb1.delete(q[0])
            if len(cartstuff)==0:
                Lb1.insert(1,"Your cart is empty.")
            f=open(username[0]+'.txt','w')
            rt.destroy()
            for a in cartstuff:
                f.write(a+','+str(cartstuff[a]))
                f.write('\n')
            f.close()

        def naw():

            rt.destroy()

        x=Lb1.get(0,20)
        q=Lb1.curselection()
        str=x[q[0]]
        l=list(str.split('    '))
        rt=tk.Tk()
        rt.configure(bg='#f8b313')
        rt.title("WARNING")

        lbl=tk.Label(rt,text="Are you sure you want to delete "+l[0]+' From your cart?',bg='#f8b313')
        lbl.configure(font=("Bebas Neue", 20))
        lbl.pack(side='top')

        ybutt=tk.Button(rt,bg='#f8b313',text='Yes',command=lambda : yaw(Lb1,l,q),width=20)
        ybutt.configure(font=("Bebas Neue", 30))
        ybutt.pack(side='left')

        nbutt=tk.Button(rt,bg='#f8b313',text='No',command=lambda : naw(),width=20)
        nbutt.configure(font=("Bebas Neue", 30))
        nbutt.pack(side='right')        
 
    root=tk.Tk()
    root.configure(height=1920,width=1080,bg='#f7b407')
    root.title('Ammajaan Cart')
    root.geometry('1330x768')

    frame=tk.Frame(root,bg='#f8b313',height='200',width='200')
    frame.grid(row=0,column=0)

    img=tk.PhotoImage(file='Logo.png',master=root)
    Pic=tk.Label(frame,image=img)
    Pic.grid(row=0,column=0)
    Pic.image=img

    label_4=tk.Label(frame,bg='#f8b313',fg='Black',text='Search')
    label_4.configure(font=("Bebas Neue", 20))

    search=tk.Entry(frame,text='Type Here',width=42,fg='Black')
    search.configure(font=("Bebas Neue", 20))
    search.grid(row=0,column=3)

    label_4.grid(row=0,column=2,padx=40,sticky='E')

    home=tk.Button(frame,bg='#f8b313',text='Home',command=gotohome)
    home.grid(row=0,column=5,padx=25,ipadx=25)
    home.configure(font=("Bebas Neue", 20))

    logout=tk.Button(frame,bg='#f8b313',text='Logout',command=gotomain)
    logout.grid(row=0,column=7,ipadx=15)
    logout.configure(font=("Bebas Neue", 20))

    frame1=tk.Frame(root,bg='#f8b313',height='200',width='200')
    frame1.grid(row=3,column=0)

    carts=tk.Label(frame1,text='your Cart',bg='#f8b313')
    carts.configure(font=("Bebas Neue", 20))
    carts.pack(side='top')

    scrollx=tk.Scrollbar(frame1,orient='horizontal',jump=1)
    scrollx.configure(highlightbackground='#f8b313')
    scrollx.pack(side='bottom',fill='x')

    scroll=tk.Scrollbar(frame1,orient='vertical',jump=1)
    scroll.configure()
    scroll.pack(side='right',fill='y')

    Lb1 = tk.Listbox(frame1,selectmode='SINGLE',xscrollcommand=scrollx.set(0,0),yscrollcommand=scroll.set(0,0),width=20,height=5,selectbackground='Red')
    Lb1.pack(fill='both')
    Lb1.bind('<Double-Button-1>',printer)
    Lb1.config(bg='#f8b313',font=('Bebas Neue',50))

    scroll.config( command = Lb1.yview )

    scrollx.config( command = Lb1.xview )

    image1=tk.PhotoImage(file='search.png',master=root)
    searchbutt=tk.Button(frame,bg='White',image=image1,command=searcher)
    searchbutt.grid(row=0,column=4)
    searchbutt.image=image1

    search.bind('<Return>',searcher)

    if len(cartstuff)==0:
        Lb1.insert(1,"Your cart is empty.")
    else:
        for a in cartstuff:
            Lb1.insert(1,a+'    Qty: '+str(cartstuff[a]))

    frame2=tk.Frame(root,bg='#f8b313',height='200',width='200')
    frame2.grid(row=4,column=0)

    delbutt=tk.Button(frame2,bg='#f8b313',text='Delete Item',command=lambda : deleter(Lb1))           
    delbutt.grid(row=0,column=1,pady=10,padx=15)
    delbutt.configure(font=("Bebas Neue", 20))
    
    billbutt=tk.Button(frame2,bg='#f8b313',text='View Bill',command=gotobill)           
    billbutt.grid(row=0,column=0,pady=10,padx=15)
    billbutt.configure(font=("Bebas Neue", 20))

    clbutt=tk.Button(frame2,bg='#f8b313',text='Clear Cart',command=clearer)           
    clbutt.grid(row=0,column=2,pady=10,padx=5)
    clbutt.configure(font=("Bebas Neue", 20))

def searchresults(p):

    def gotomain(event=None):
        root.destroy()
        t=tk.Tk()
        t.title("SUCCESS!")

        l=tk.Label(t,text="You have Successfully Logged Out",bg='#f8b313')
        l.configure(font=("Bebas Neue", 20))
        l.pack()

        entrypage()

    def gotohome(event=None):
        root.destroy()
        therealdeal(things)


    def searcher(event=None):
        s=search.get()
        q=s.rstrip()
        t=q.lstrip()

        if t!='':
            root.destroy()
            searchresults(s)

        else:
            t=tk.Tk()
            t.title("ERROR!")

            l=tk.Label(t,text="No Keyword Entered",bg='#f8b313')
            l.configure(font=("Bebas Neue", 100))
            l.pack()

    def frinter(event=None):
        q=Lb1.curselection()
        productpage(a[q[0]])
        root.destroy()

    classics={}       
        
    root=tk.Tk()
    root.configure(height=1920,width=1080,bg='#f7b407')
    root.title('Showing Search Results for '+p)
    root.geometry('1330x768')

    frame=tk.Frame(root,bg='#f8b313',height='200',width='200')
    frame.grid(row=0,column=0)

    img=tk.PhotoImage(file='Logo.png',master=root)
    Pic=tk.Label(frame,image=img)
    Pic.grid(row=0,column=0)
    Pic.image=img

    label_4=tk.Label(frame,bg='#f8b313',fg='Black',text='Search')
    label_4.configure(font=("Bebas Neue", 20))

    search=tk.Entry(frame,text='Type Here',width=42,fg='Black')
    search.configure(font=("Bebas Neue", 20))
    search.grid(row=0,column=3)

    label_4.grid(row=0,column=2,padx=40,sticky='E')

    home=tk.Button(frame,bg='#f8b313',text='Home',command=gotohome)
    home.grid(row=0,column=5,padx=25,ipadx=25)
    home.configure(font=("Bebas Neue", 20))

    logout=tk.Button(frame,bg='#f8b313',text='Logout',command=gotomain)
    logout.grid(row=0,column=7,ipadx=15)
    logout.configure(font=("Bebas Neue", 20))

    frame1=tk.Frame(root,bg='#f8b313',height='200',width='200')
    frame1.grid(row=4,column=0)

    image1=tk.PhotoImage(file='search.png',master=root)

    searchbutt=tk.Button(frame,bg='White',image=image1,command=searcher)
    searchbutt.grid(row=0,column=4)
    searchbutt.image=image1
    search.bind('<Return>',searcher)

    scrollx=tk.Scrollbar(frame1,orient='horizontal',jump=1)
    scrollx.configure()
    scrollx.pack(side='bottom',fill='x')

    scroll=tk.Scrollbar(frame1,orient='vertical',jump=1)
    scroll.configure()
    scroll.pack(side='right',fill='y')

    Lb1 = tk.Listbox(frame1,selectmode='SINGLE',xscrollcommand=scrollx.set(0,0),yscrollcommand=scroll.set(0,0),width=20,height=5,selectbackground='Red')    

    q=p.lower()

    kwords=q.split()

    moal=[]
    resultlist=[]

    for b in kwords:
        for a in things.keys():
            if b in a.lower():
                resultlist.append(a)

    for a in things:
        moal.append([a,things[a][2].lower()])

    for b in kwords:
        for a in moal:
            if b in a[1]:
                resultlist.append(a[0])

    final=[]

    for a in resultlist:
        if a not in final:
            final.append(a)

    for a in final:
        Lb1.insert(1,a)
    
    Lb1.pack(side='bottom',fill='both')
    Lb1.bind('<Double-Button-1>',frinter)

    c=Lb1.get(0,len(things))

    if len(c)==0:
        Lb1.insert(1,p+' Not Found')

    Lb1.config(bg='#f8b313',font=('Bebas Neue',50))

    scroll.config( command = Lb1.yview )

    scrollx.config( command = Lb1.xview )

    a=Lb1.get(0,len(things))

    klassics=tk.Label(root,text='Search Results for '+p,bg='#f8b313')
    klassics.configure(font=("Bebas Neue", 20))
    klassics.grid(row=3,column=0)

    credit=tk.Label(root,text=' © Samarth Vijay & Vidhyotha Shetty')
    credit.grid(row=5,column=0,pady=50)
    credit.config(font=('Bebas Neue',20),bg='#f8b313')

    
    
def productpage(p):

    global cartstuff,username

    def back():
        therealdeal(things)
        root.destroy()

    def addtocart():
        quantity=qty.get()

        if quantity.isdigit()==True:

            if p not in cartstuff:

                cartstuff[p]=int(quantity)

            else:

                cartstuff[p]+=int(quantity)

            f=open(username[0]+'.txt','w')
            for a in cartstuff:
                f.write(a+','+str(cartstuff[a]))
                f.write('\n')
            f.close()

            t=tk.Tk()
            t.title("CONGRATS!")

            l=tk.Label(t,text=str(cartstuff[p])+' '+p+'(s) are in your cart',bg='#f8b313')
            l.configure(font=("Bebas Neue", 20))
            l.pack()

        else:
            t=tk.Tk()
            t.title("Failure")

            l=tk.Label(t,text='please enter a valid quantity',bg='#f8b313')
            l.configure(font=("Bebas Neue", 100))
            l.pack()
        
    i=str(things[p][2])
    text=tk.StringVar(value=i)

    root=tk.Tk()
    root.configure(height=768,bg='#f7b407')
    root.title(p+'-Ammajaan')
    root.columnconfigure(0,weight=300)

    head=tk.Label(root,text=p,bg='#f8b313')
    head.grid(row=0,column=0,sticky='w')
    head.configure(font=("Bebas Neue", 69))

    lbl1=tk.Label(root,bg='#f8b313')
    lbl2=tk.Label(root,bg='#f8b313')
    lbl3=tk.Label(root,bg='#f8b313')
    lbl4=tk.Label(root,bg='#f8b313')

    lbl1.grid(row=0,column=1,padx=0)
    lbl2.grid(row=0,column=2,padx=0)
    lbl3.grid(row=0,column=3,padx=0)
    lbl4.grid(row=0,column=4,padx=0,pady=10)

    frame=tk.Frame(root)
    frame.grid(row=1,column=0)

    scroll=tk.Scrollbar(frame,orient='vertical',jump=1)
    scroll.pack(side='right',fill='y')

    desc=tk.Text(frame,bg='#f8b313',fg='Black',relief='flat',state='normal',wrap='word',height=7)
    desc.pack(side='left')

    scroll.configure(command = desc.yview )

    desc.configure(font=('Bebas Neue',20),yscrollcommand=scroll.set(0,0))
    desc.insert('insert',str(things[p][2]))
    desc.configure(state='disabled')

    backbutt=tk.Button(root,text='Back',bg='#f8b313',command=back,height=2,width=10)
    backbutt.configure(font=('Bebas Neue',20))
    backbutt.grid(row=0,column=6,padx=20)

    cartbutt=tk.Button(root,text='Add to\nCart',bg='#f8b313',command=addtocart,height=2,width=10)
    cartbutt.configure(font=('Bebas Neue',20))
    cartbutt.grid(row=1,column=6,padx=20,sticky='s',pady=5)

    qtyl=tk.Label(root,text="Enter Qty:",bg='#f8b313')
    qtyl.configure(font=("Bebas Neue", 20))
    qtyl.grid(row=1,column=6,sticky='w')

    qty=tk.Entry(root,width=5)
    qty.configure(font=("Bebas Neue", 20))
    qty.grid(row=1,column=6,padx=5,sticky='e')

    qtyl=tk.Label(root,text="Price: INR "+str(round(int(things[p][0])-((classics[p]/100)*int(things[p][0]))))+'\n'+str(classics[p])+'% OFF',bg='#f8b313')
    qtyl.configure(font=("Bebas Neue", 20))
    qtyl.grid(row=1,column=6,sticky='n')   

def bill(carts,things):

    global classics,cartstuff

    def gotomain(event=None):
        root.destroy()

        t=tk.Tk()
        t.title("SUCCESS!")

        l=tk.Label(t,text="You have Successfully Logged Out",bg='#f8b313')
        l.configure(font=("Bebas Neue", 20))
        l.pack()

        entrypage()

    def gotohome(event=None):
        root.destroy()
        therealdeal(things)

    def buyer():

        def gotohome(event=None):
            t1.destroy()
            root.destroy()
            therealdeal(things)

        t1=tk.Tk()
        t1.title("SUCCESS!")
        t1.configure(bg='#f8b313')

        l1=tk.Label(t1,text="Congratulations on your purchase",bg='#f8b313')
        l1.grid(row=0,column=0)
        l1.configure(font=('Bebas Neue',20))
        cartstuff.clear()

        home=tk.Button(t1,bg='#f8b313',text='Home',command=lambda : gotohome())
        home.grid(row=1,column=0)
        home.configure(font=("Bebas Neue", 20))

    root=tk.Tk()
    root.configure(height=768,bg='#f7b407')
    root.title('your Bill')

    head=tk.Label(root,text='Invoice',bg='#f8b313')
    head.grid(row=0,column=4)
    head.configure(font=("Bebas Neue", 69))

    stringcart=''
    totalprice=0

    for a in cartstuff:
            stringcart+=a+'        '+'Qty: '+str(cartstuff[a])+'         '+'Price'+':'+str(cartstuff[a]*round(int(things.get(a)[0])-(classics[a]/100)*int(things.get(a)[0])))+'\n'
            totalprice+=int(cartstuff[a]*round(int(things.get(a)[0])+(classics[a]/100*int(things.get(a)[0]))))

    head=tk.Label(root,text=stringcart,bg='#f8b313',anchor='w',justify='left')
    head.grid(row=1,column=0,sticky='w')
    head.configure(font=("Bebas Neue", 25))        

    head=tk.Label(root,text='Total Price'+': '+str(totalprice),bg='#f8b313',anchor='w',justify='left')
    head.grid(row=2,column=0,sticky='w')
    head.configure(font=("Bebas Neue", 25))

    logout=tk.Button(root,bg='#f8b313',text='Logout',command=gotomain)
    logout.grid(row=2,column=4,ipadx=15)
    logout.configure(font=("Bebas Neue", 20))
    
    home=tk.Button(root,bg='#f8b313',text='Home',command=gotohome)
    home.grid(row=2,column=3,ipadx=25)
    home.configure(font=("Bebas Neue", 20))

    img=tk.PhotoImage(file='Logo.png',master=root)
    Pic=tk.Label(root,image=img)
    Pic.grid(row=0,column=0,sticky='w')
    Pic.image=img

    home=tk.Button(root,bg='#f8b313',text='Buy',command=buyer)
    home.grid(row=2,column=2,ipadx=25,padx=60)
    home.configure(font=("Bebas Neue", 20))


keys=list(things.keys())
l1=[]
count=0

while count<10:

        a=keys[random.randint(0,len(keys)-1)]  
        if a not in l1:

            l1.append(a)

        count+=1

entrypage()
