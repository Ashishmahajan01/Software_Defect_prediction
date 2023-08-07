from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

root = tk.Tk()
root.title("Software Defect prediction")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
# ++++++++++++++++++++++++++++++++++++++++++++

image2 = Image.open('h.png')

image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)


background_label = tk.Label(root, image=background_image)
background_label.image = background_image



background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
lbl = tk.Label(root, text="Software Defect prediction", font=('times', 35,' bold '), height=1, width=32,bg="violet Red",fg="Black")
lbl.place(x=300, y=10)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++
data = pd.read_csv("D://project//21cg148-software defect//Soft_attributes.csv")



data = data.dropna()

le = LabelEncoder()



def Data_Preprocessing():
    data = pd.read_csv("D://All project//21cg148-software defect//21cg148-software defect//Soft_attributes.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    
    data['loc'] = le.fit_transform(data['loc'])
    
    data['v(g)'] = le.fit_transform(data['v(g)'])
    
    data['ev(g)'] = le.fit_transform(data['ev(g)'])

    data['iv(g)'] = le.fit_transform(data['iv(g)'])
    
    data['n'] = le.fit_transform(data['n'])
    
    data['v'] = le.fit_transform(data['v'])
    
    data['l'] = le.fit_transform(data['l'])
    
    data['d'] = le.fit_transform(data['d'])

    data['i'] = le.fit_transform(data['i'])
    
    data['e'] = le.fit_transform(data['e'])
    
  #  data['b'] = le.fit_transform(data['b'])
    
    data['t'] = le.fit_transform(data['t'])
    
    data['lOCode'] = le.fit_transform(data['lOCode'])

    data['lOComment'] = le.fit_transform(data['lOComment'])
    
    data['lOBlank'] = le.fit_transform(data['lOBlank'])
    
    data['locCodeAndComment'] = le.fit_transform(data['locCodeAndComment'])
    
    data['uniq_Op'] = le.fit_transform(data['uniq_Op'])
    
    data['uniq_Opnd'] = le.fit_transform(data['uniq_Opnd'])

    data['total_Opnd'] = le.fit_transform(data['total_Opnd'])
    
    data['branchCount'] = le.fit_transform(data['branchCount'])
    
   # data['defects'] = le.fit_transform(data['defects'])
    
  

    """Feature Selection => Manual"""
    x = data.drop(['b', 'defects'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['defects']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

    

    load = tk.Label(root, font=("Tempus Sans ITC", 15, "bold"), width=50, height=2, background="green",
                    foreground="white", text="Data Loaded=>Splitted into 80% for Training & 20% for Testing")
    load.place(x=200, y=80)


def Model_Training():
    data = pd.read_csv("D://All project//21cg148-software defect//21cg148-software defect//Soft_attributes.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    
    data['loc'] = le.fit_transform(data['loc'])
    
    data['v(g)'] = le.fit_transform(data['v(g)'])
    
    data['ev(g)'] = le.fit_transform(data['ev(g)'])

    data['iv(g)'] = le.fit_transform(data['iv(g)'])
    
    data['n'] = le.fit_transform(data['n'])
    
    data['v'] = le.fit_transform(data['v'])
    
    data['l'] = le.fit_transform(data['l'])
    
    data['d'] = le.fit_transform(data['d'])

    data['i'] = le.fit_transform(data['i'])
    
    data['e'] = le.fit_transform(data['e'])
    
    # data['b'] = le.fit_transform(data['b'])
    
    data['t'] = le.fit_transform(data['t'])
    
    data['lOCode'] = le.fit_transform(data['lOCode'])

    data['lOComment'] = le.fit_transform(data['lOComment'])
    
    data['lOBlank'] = le.fit_transform(data['lOBlank'])
    
    data['locCodeAndComment'] = le.fit_transform(data['locCodeAndComment'])
    
    data['uniq_Op'] = le.fit_transform(data['uniq_Op'])
    
    data['uniq_Opnd'] = le.fit_transform(data['uniq_Opnd'])

    data['total_Opnd'] = le.fit_transform(data['total_Opnd'])
    
    data['branchCount'] = le.fit_transform(data['branchCount'])
    
    # data['defects'] = le.fit_transform(data['defects'])
    
  


    

    """Feature Selection => Manual"""
    x = data.drop(['b', 'defects'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['defects']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30,random_state=999)

    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    
    # from sklearn.linear_model import LogisticRegression 
    # svcclassifier = LogisticRegression() 
    # svcclassifier.fit(x_train, y_train)
    
    from sklearn.tree import DecisionTreeClassifier 
    svcclassifier = DecisionTreeClassifier()
    svcclassifier.fit(x_train, y_train)
    
    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=200)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as SOFTWARE_MODEL.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=420)
    from joblib import dump
    dump (svcclassifier,"SOFTWARE_MODEL.joblib")
    print("Model saved as SOFTWARE_MODEL.joblib")



def call_file():
    import Check_Software_defect
    Check_Software_defect.Train()


def window():
    root.destroy()

# button2 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
#                     text="Data_Preprocessing", command=Data_Preprocessing, width=15, height=2)
# button2.place(x=5, y=90)

# button3 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
#                     text="Model Training", command=Model_Training, width=15, height=2)
# button3.place(x=5, y=170)

button4 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
                    text="Software prediction", command=call_file, width=15, height=2)
button4.place(x=5, y=250)
exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=5, y=330)

root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''