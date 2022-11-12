import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox

import pickle
import numpy as np
import warnings
warnings.filterwarnings('ignore')


root = tk.Tk()
root.title('Image Steganography')
root.resizable(False, False)
root.geometry('400x450')
frame = tk.Frame(master=root, relief=tk.RAISED)

def get_crop(frame,N,P,K,Temp,Humidity,PH,Rainfall,mdl_typ):
    N=float(N)
    P=float(P)
    K=float(K)
    Temp=float(Temp)
    Humidity=float(Humidity)
    PH=float(PH)
    Rainfall=float(Rainfall)

    data = np.array([[N, P, K, Temp, Humidity, PH, Rainfall]])

    mdl="DecisionTree.pkl"
    if mdl_typ=="Decision Tree":
        mdl="DecisionTree.pkl"
    elif mdl_typ=="Guassian Naive Bayes":
        mdl="NBClassifier.pkl"
    elif mdl_typ=="Logistic Regression":
        mdl="LogisticRegression.pkl"
    elif mdl_typ=="Random Forest":
        mdl="RandomForest.pkl"

    rcmd_model=pickle.load(open(mdl, "rb"))
    prediction = rcmd_model.predict(data)
    print(prediction)
    txt="Recommended Crop for this Soil is "+prediction[0]
    label1 = tk.Label(master=frame, text=txt,font=('Helvetica bold',12))
    label1.grid(row=7,column=0,padx=5,pady=5,columnspan=3)

def show_frm(model_type):
    global frame
    if (frame.winfo_exists()):
        frame.destroy()
    frame = tk.Frame(master=root, relief=tk.RAISED)
    N = tk.Entry(master=frame, width=15)
    P = tk.Entry(master=frame, width=15)
    K = tk.Entry(master=frame, width=15)
    temp = tk.Entry(master=frame, width=15)
    humidity = tk.Entry(master=frame, width=15)
    ph = tk.Entry(master=frame, width=15)
    rainfall = tk.Entry(master=frame, width=15)
    frame.grid(row=2,column=0,padx=5,pady=5,columnspan=3)
    label1 = tk.Label(master=frame, text="Nitrogen")
    label2 = tk.Label(master=frame, text="Phosphorous")
    label3 = tk.Label(master=frame, text="Pottasium")
    label4 = tk.Label(master=frame, text="Temperature ")
    label5 = tk.Label(master=frame, text="Humidity")
    label6 = tk.Label(master=frame, text="pH")
    label7 = tk.Label(master=frame, text="Rainfall ")

    label1.grid(row=0,column=0,padx=5,pady=5)
    N.grid(row=1,column=0,padx=5,pady=5)
    label2.grid(row=0, column=1, padx=5, pady=5)
    P.grid(row=1, column=1, padx=5, pady=5)
    label3.grid(row=0, column=2, padx=5, pady=5)
    K.grid(row=1, column=2, padx=5, pady=5)
    label4.grid(row=2, column=0, padx=5, pady=5)
    temp.grid(row=3, column=0, padx=5, pady=5)
    label5.grid(row=2, column=2, padx=5, pady=5)
    humidity.grid(row=3, column=2, padx=5, pady=5)
    label6.grid(row=4, column=0, padx=5, pady=5)
    ph.grid(row=5, column=0, padx=5, pady=5)
    label7.grid(row=4, column=2, padx=5, pady=5)
    rainfall.grid(row=5, column=2, padx=5, pady=5)
    rcmd_btn = ttk.Button(
        frame,
        width=15,
        text='Crop',
        command=lambda: get_crop(frame,N.get(),P.get(),K.get(),temp.get(),humidity.get(),ph.get(),rainfall.get(),model_type)
    )
    rcmd_btn.grid(row=6,column=1,padx=5, pady=5)
    print(model_type)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    label = tk.Label(master=root, text="Choose a Model")
    options = [
        "Decision Tree",
        "Guassian Naive Bayes",
        "Logistic Regression",
        "Random Forest",
    ]
    clicked = tk.StringVar()
    clicked.set("Decision Tree")
    drop = tk.OptionMenu(root, clicked, *options)
    Reco = ttk.Button(
        root,
        width = 15,
        text = 'Recomend',
        command = lambda: show_frm(clicked.get())
    )
    label.grid(row=0,column=0,padx=5,pady=5)
    drop.grid(row=0,column=1,padx=5,pady=5)
    Reco.grid(row=1,column=1,padx=5,pady=5)
    root.mainloop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
