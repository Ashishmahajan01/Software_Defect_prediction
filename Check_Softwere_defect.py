from tkinter import *
def Train():
    """GUI"""
    import tkinter as tk
    import numpy as np
    import pandas as pd

    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder

    root = tk.Tk()

    root.geometry("800x850+250+5")
    root.title("Check Software prediction")
    root.configure(background="purple")
    
    loc   = tk.IntVar()
    vg = tk.IntVar()
    ev = tk.IntVar()
    iv = tk.IntVar()
    n = tk.IntVar()
    v1 = tk.IntVar()
    l = tk.IntVar()
    d = tk.IntVar()
    i = tk.IntVar()
    e = tk.IntVar()
    t = tk.IntVar()
    lOCode = tk.IntVar()
    lOComment = tk.IntVar()
    lOBlank = tk.IntVar()
    locCodeAndComment = tk.IntVar()
    uniq_Op = tk.IntVar()
    uniq_Opnd = tk.IntVar()
    total_Op = tk.IntVar()
    total_Opnd = tk.IntVar()
    branchCount = tk.IntVar()
     
    
    
    #===================================================================================================================



    def Detect():
        e1=loc.get()
        print(e1)
        e2=vg.get()
        print(e2)
        e3=ev.get()
        print(e3)
        e4=iv.get()
        print(e4)
        e5=n.get()
        print(e5)
        e6=v1.get()
        print(e6)
        e7=l.get()
        print(e7)
        e8=d.get()
        print(e8)
        e9=i.get()
        print(e9)
        e10=e.get()
        print(e10)
        e11=t.get()
        print(e11)
        e12=lOCode.get()
        print(e12)
        e13=lOComment.get()
        print(e13)
        e14=lOBlank.get()
        print(e14)
        e15=locCodeAndComment.get()
        print(e15)
        e16=uniq_Op.get()
        print(e16)
        e17=uniq_Opnd.get()
        print(e17)
        e18=total_Op.get()
        print(e18)
        e19=total_Opnd.get()
        print(e19)
        e20=branchCount.get()
        print(e20)
       
       
        
        
        
        
        #########################################################################################
        
        from joblib import dump , load
        a1=load('D://project//21cg148-software defect//SOFTWARE_MODEL.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9,e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20 ]])
        print(v)
        if v[0]==1:
            print("Yes")
            yes = tk.Label(root,text="software defect \nDetected!\nReport is Generated",background="red",foreground="white",font=('times', 20, ' bold '),width=15)
            yes.place(x=350,y=450)
            file = open(r"D://project//21cg148-software defect//Report.txt", 'w')
            file.write("-----Softwere Report-----\n As per input data and system model software defect prediction for Respective Paptien software."
                       "\n***Kindly Follow info***"
                    
                    )
            file.close()
            
        else:
            print("No")
            no = tk.Label(root, text="No software defect \nDetected", background="green", foreground="white",font=('times', 20, ' bold '),width=15)
            no.place(x=350, y=450)
            file = open(r"D://project//21cg148-software defect//Report.txt", 'w')
            file.write("-----Software Report-----\n As per input data and system model No Softwere defect Detected for Respective software."
                       "\n\n***Relax and Follow below mentioned software!!!***"
                    
                    )
            file.close()



    l1=tk.Label(root,text="loc",background="purple",font=('times', 20, ' bold '),width=10)
    l1.place(x=5,y=1)
    loc=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=loc)
    loc.place(x=200,y=1)

    l2=tk.Label(root,text="vg",background="purple",font=('times', 20, ' bold '),width=10)
    l2.place(x=5,y=50)
    vg=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=vg)
    vg.place(x=200,y=50)

    l3=tk.Label(root,text="EV",background="purple",font=('times', 20, ' bold '),width=10)
    l3.place(x=5,y=100)
    ev=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=ev)
    ev.place(x=200,y=100)
    
    
    #Lb1 = Listbox(root,width=20,height=3)
    #Lb1.place(x=200,y=100)
    #Lb1.insert(1, "1")
    #Lb1.insert(2, "2")
    #Lb1.insert(3, "3")
    #chest_pain=Lb1.curselection()
    #Lb1.pack()
    
    l4=tk.Label(root,text="IV",background="purple",font=('times', 20, ' bold '),width=10)
    l4.place(x=5,y=150)
    iv=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=iv)
    iv.place(x=200,y=160)

    l5=tk.Label(root,text="N",background="purple",font=('times', 20, ' bold '),width=10)
    l5.place(x=5,y=200)
    n=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=n)
    n.place(x=200,y=200)

    l6=tk.Label(root,text="V",background="purple",font=('times', 20, ' bold '),width=10)
    l6.place(x=5,y=250)
    v1=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=v1)
    v1.place(x=200,y=250)

    l7=tk.Label(root,text="l",background="purple",font=('times', 20, ' bold '),width=10)
    l7.place(x=5,y=300)
    l=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=l)
    l.place(x=200,y=300)

    l8=tk.Label(root,text="D",background="purple",font=('times', 20, ' bold '),width=10)
    l8.place(x=5,y=350)
    d=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=d)
    d.place(x=200,y=350)

    l9=tk.Label(root,text="i",background="purple",font=('times', 20, ' bold '),width=10)
    l9.place(x=5,y=400)
    i=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=i)
    i.place(x=200,y=400)

    
    l12=tk.Label(root,text="e",background="purple",font=('times', 20, ' bold '),width=10)
    l12.place(x=5,y=450)
    e=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=e)
    e.place(x=200,y=450)

    l10=tk.Label(root,text="t",background="purple",font=('times', 20, ' bold '),width=10)
    l10.place(x=5,y=500)
    t=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=t)
    t.place(x=200,y=500)
   

    l13=tk.Label(root,text="lOCode",background="purple",font=('times', 20, ' bold '),width=10)
    l13.place(x=5,y=550)
    lOCode=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=lOCode)
    lOCode.place(x=200,y=550)

    l12=tk.Label(root,text="lOComment",background="purple",font=('times', 20, ' bold '),width=10)
    l12.place(x=350,y=10)
    lOComment=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=lOComment)
    lOComment.place(x=550,y=10)
    
    l12=tk.Label(root,text="lOBlank",background="purple",font=('times', 20, ' bold '),width=10)
    l12.place(x=350,y=50)
    lOBlank=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=lOBlank)
    lOBlank.place(x=550,y=50)

    l12=tk.Label(root,text="locCodeAndComment",background="purple",font=('times', 20, ' bold '),width=16)
    l12.place(x=350,y=100)
    locCodeAndComment=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=locCodeAndComment)
    locCodeAndComment.place(x=550,y=100)


    l12=tk.Label(root,text="uniq_Op",background="purple",font=('times', 20, ' bold '),width=10)
    l12.place(x=350,y=150)
    uniq_Op=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=uniq_Op)
    uniq_Op.place(x=550,y=150)

    l12=tk.Label(root,text="uniq_Opnd",background="purple",font=('times', 20, ' bold '),width=10)
    l12.place(x=350,y=200)
    uniq_Opnd=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=uniq_Opnd)
    uniq_Opnd.place(x=550,y=200)

    l12=tk.Label(root,text="total_Op",background="purple",font=('times', 20, ' bold '),width=10)
    l12.place(x=350,y=250)
    total_Op=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=total_Op)
    total_Op.place(x=550,y=250)

    l12=tk.Label(root,text="total_Opnd",background="purple",font=('times', 20, ' bold '),width=10)
    l12.place(x=350,y=300)
    total_Opnd=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=total_Opnd)
    total_Opnd.place(x=550,y=300)

    l12=tk.Label(root,text="branchCount",background="purple",font=('times', 20, ' bold '),width=10)
    l12.place(x=350,y=350)
    branchCount=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=branchCount)
    branchCount.place(x=550,y=350)
    

    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=400,y=600)


    root.mainloop()

Train()