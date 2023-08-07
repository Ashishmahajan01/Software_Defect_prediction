import tkinter as tk
#from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk



##############################################+=============================================================
root = tk.Tk()
root.configure(background="black")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Software Defect Prediction")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
# image2 = Image.open('crop5.jpg')
# image2 = image2.resize((w,h), Image.ANTIALIAS)

# background_image = ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)


#
lbl = tk.Label(root, text="Software Defect Prediction", font=('Elephant', 35,' bold '),bg="black",fg="white")
lbl.place(x=300, y=10)




img=ImageTk.PhotoImage(Image.open("im.png"))

img2=ImageTk.PhotoImage(Image.open("im1.png"))

img3=ImageTk.PhotoImage(Image.open("im3.png"))


logo_label=tk.Label()
logo_label.place(x=0,y=95)



# using recursion to slide to next image
x = 1

# function to change to next image
def move():
	global x
	if x == 4:
		x = 1
	if x == 1:
		logo_label.config(image=img,width=1800,height=700)
	elif x == 2:
		logo_label.config(image=img2,width=1800,height=700)
	elif x == 3:
		logo_label.config(image=img3,width=1800,height=700)
	x = x+1
	root.after(2000, move)

# calling the function
move()








def log():
#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    from subprocess import call
    call(["python","login.py"])
    #root.destroy()
    
def reg():
    from subprocess import call
    call(["python","registration.py"])
    #root.destroy()
    
def window():
  root.destroy()
  


#####################################################################################################################

button1 = tk.Button( text="Login", command=log, width=15, height=1,font=('times', 15, ' bold '), bg="green", fg="white")
button1.place(x=70, y=200)

button2 = tk.Button( text="Registration",command=reg,width=15, height=1,font=('times', 15, ' bold '), bg="green", fg="white")
button2.place(x=70, y=250)

button3 = tk.Button( text="Exit",command=window,width=15, height=1,font=('times',15, ' bold '), bg="red", fg="white")
button3.place(x=70, y=300)





root.mainloop()