import tkinter as tk
import sqlite3
import csv
from tkinter import *
from tkinter import messagebox


def submit_gui(main_frame):
        main_frame.destroy()
        main_frame=tk.Tk()
        main_frame.title("")
        main_frame.geometry("1920x1080")
        sex=tk.StringVar()
        sex.set(1)
        root = tk.Frame(main_frame,bg = "grey")
        root.place(x=0,y=0,width = 1920, height = 1080)
        tk.Label(root,text = "Prediction Of Heart Diseases Using Machine Learning",relief="solid",fg="cyan",bg="grey",font=("times",22,"bold")).place(x = 300,y =20)
        tk.Label(root,text = "Patient Name",fg="black",bg="grey",font=("times","12","bold")).place(x =70,y = 80)
        nameid = tk.Entry(root,font=("time","12","bold"))
        nameid.place(x=260,y=80,width=250)
        tk.Label(root,text = "Age",fg="black",bg="grey",font=("times","12","bold")).place(x = 70,y = 140)
        age = tk.Entry(root,font=("time","12","bold"))
        age.place(x=260,y=140,width=250)
        tk.Label(root,text = "Sex",fg="black",bg="grey",font=("times","12","bold")).place(x = 70,y = 200)
        tk.Radiobutton(root,text="Male",variable=sex,value=1,bg="grey",font=("times","12","bold")).place(x=260,y=200)
        tk.Radiobutton(root,text="Female",variable=sex,value=0,bg="grey",font=("times","12","bold")).place(x=360,y=200)
        tk.Label(root,text = "Chest Pain",fg="black",bg="grey",font=("times","12","bold")).place(x = 70,y = 260)
        chest = tk.Entry(root,font=("time","12","bold"))
        chest.place(x=260,y=260,width=250)
        tk.Label(root,text = "Resting Blood Pressure",fg="black",bg="grey",font=("times","12","bold")).place(x = 70,y = 320)
        bps = tk.Entry(root,font=("time","12","bold"))
        bps.place(x=260,y=320,width=250)
        tk.Label(root,text = "Cholestrol",fg="black",bg="grey",font=("times","12","bold")).place(x = 70,y = 380)
        ch  = tk.Entry(root,font=("time","12","bold"))
        ch.place(x=260,y=380,width=250)
        tk.Label(root,text = "Fasting Blood sugar",fg="black",bg="grey",font=("times","12","bold")).place(x = 70,y = 440)
        fbs = tk.Entry(root,font=("time","12","bold"))
        fbs.place(x=260,y=440,width=250)
        tk.Label(root,text = "Restecg",fg="black",bg="grey",font=("times","12","bold")).place(x = 70,y = 500)
        rest = tk.Entry(root,font=("time","12","bold"))
        rest.place(x=260,y=500,width=250)
        tk.Label(root,text = "Thalach",fg="black",bg="grey",font=("times","12","bold")).place(x = 70,y = 560)
        tha = tk.Entry(root,font=("time","12","bold"))
        tha.place(x=260,y=560,width=250)
        tk.Label(root,text = "Exang",fg="black",bg="grey",font=("times","12","bold")).place(x = 650,y = 80)
        ex = tk.Entry(root,font=("time","12","bold"))
        ex.place(x=750,y=80,width=250)
        tk.Label(root,text = "Oldpeak",fg="black",bg="grey",font=("times","12","bold")).place(x = 650,y = 140)
        op = tk.Entry(root,font=("time","12","bold"))
        op.place(x=750,y=140,width=250)
        tk.Label(root,text = "Slope",fg="black",bg="grey",font=("times","12","bold")).place(x = 650,y = 200)
        slop = tk.Entry(root,font=("time","12","bold"))
        slop.place(x=750,y=200,width=250)
        tk.Label(root,text = "Ca",fg="black",bg="grey",font=("times","12","bold")).place(x = 650,y = 260)
        ca = tk.Entry(root,font=("time","12","bold"))
        ca.place(x=750,y=260,width=250)
        tk.Label(root,text = "Thal",fg="black",bg="grey",font=("times","12","bold")).place(x = 650,y = 320)
        thl = tk.Entry(root,font=("time","12","bold"))
        thl.place(x=750,y=320,width=250)
        submit_button = tk.Button(root,text ="Reset",font=("times","14","bold"),bg="green",fg="black",command = lambda: submit_gui(main_frame))
        submit_button.place(x =600,y=500,height=40,width=80)
        exit_button = tk.Button(root,text ="Exit",font=("times",14,"bold"),bg="red",fg="black",command = lambda :main_frame.destroy())
        exit_button.place(x =950,y=500,height=40,width=80)
        chd = tk.Button(root,text ="Check Heart Disease",font=("times","14","bold"),bg="black",fg="white",command=lambda :second(nameid,age,sex,chest,bps,ch,fbs,rest,tha,ex,op,slop,ca,thl))#def name will be given for command to work here def second
        chd.place(x =600,y=600,height=50,width=200)
        test = tk.Button(root,text="Testing Results",font=("times","14","bold"),bg="black",fg="white",command=lambda :tst())
        test.place(x=900,y=600,height=50,width=200)
        main_frame.mainloop()


def tst():
	window=tk.Tk()
	window.title("Output")
	window.geometry("600x400")
	frame =tk.Frame(window,width=1200,height=650, bd=2, relief=tk.SUNKEN)
	frame.grid_rowconfigure(0, weight=1)
	frame.grid_columnconfigure(0, weight=1)
	xscrollbar = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
	xscrollbar.grid(row=1, column=0, sticky=tk.E+tk.W)
	yscrollbar = tk.Scrollbar(frame)
	yscrollbar.grid(row=0, column=1, sticky=tk.N+tk.S)
	text = tk.Text(frame, wrap=tk.NONE, width=1200,height=650, bd=0,xscrollcommand=xscrollbar.set,yscrollcommand=yscrollbar.set)
	text.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
	xscrollbar.config(command=text.xview)
	yscrollbar.config(command=text.yview)
	frame.pack()
	import numpy as np
	import pandas as pd
	data=pd.read_csv("heart.csv")
	# data.head()
	features=list(data.columns)
	# features
	from sklearn.neighbors import KNeighborsClassifier as KNNC
	from sklearn.tree import DecisionTreeClassifier as DTC
	from sklearn.svm import SVC
	from sklearn.naive_bayes import GaussianNB as NBC
	from sklearn.metrics import accuracy_score
	from sklearn.model_selection import train_test_split
	from sklearn.ensemble import RandomForestClassifier as RFC
	from matplotlib import pyplot as plt
	import seaborn
	# data.info()
	# data.hist(figsize=(20,12))
	# plt.show()
	target=data['target']
	features=data.drop(columns=['target'])
	train_features,test_features,train_target,test_target=train_test_split(features,target,test_size=0.25)
	clfKNN=KNNC()
	clfDT=DTC()
	clfSV=SVC(gamma='scale')
	clfNB=NBC()
	clfRF=RFC(n_estimators=10)
	clfKNN.fit(train_features,train_target)
	clfDT.fit(train_features,train_target)
	clfSV.fit(train_features,train_target)
	clfNB.fit(train_features,train_target)
	clfRF.fit(train_features,train_target)
	pDT=clfDT.predict(test_features)
	pKNN=clfKNN.predict(test_features)
	pNB=clfNB.predict(test_features)
	pSV=clfSV.predict(test_features)
	pRF=clfRF.predict(test_features)
	asDT=accuracy_score(test_target,pDT)
	asKNN=accuracy_score(test_target,pKNN)
	asSV=accuracy_score(test_target,pSV)
	asNB=accuracy_score(test_target,pNB)
	asRF=accuracy_score(test_target,pRF)
	# text.insert(tk.INSERT,'DecisionTree: {}'.format(asDT))
	# text.insert(tk.INSERT,'\nKNN: {}'.format(asKNN))
	# text.insert(tk.INSERT,'\nSVM: {}'.format(asSV))
	# text.insert(tk.INSERT,'\nNaiveBayes: {}'.format(asNB))
	# text.insert(tk.INSERT,'\nRandom Forest: {}'.format(asRF))
	from sklearn.metrics import classification_report,confusion_matrix
	text.insert(tk.INSERT,'DecisionTree: {}\n'.format(asDT))
	text.insert(tk.INSERT,confusion_matrix(test_target,pDT))
	text.insert(tk.INSERT,classification_report(test_target,pDT))
	text.insert(tk.INSERT,"\n---------------------------------------------\n")
	text.insert(tk.INSERT,'\nKNN: {}\n'.format(asKNN))
	text.insert(tk.INSERT,confusion_matrix(test_target,pKNN))
	text.insert(tk.INSERT,classification_report(test_target,pKNN))
	text.insert(tk.INSERT,"\n---------------------------------------------\n")
	text.insert(tk.INSERT,'\nSVM: {}\n'.format(asSV))
	text.insert(tk.INSERT,confusion_matrix(test_target,pNB))
	text.insert(tk.INSERT,classification_report(test_target,pNB))
	text.insert(tk.INSERT,"\n---------------------------------------------\n")
	text.insert(tk.INSERT,'\nNaiveBayes: {}\n'.format(asNB))
	text.insert(tk.INSERT,confusion_matrix(test_target,pSV))
	text.insert(tk.INSERT,classification_report(test_target,pSV))
	text.insert(tk.INSERT,"\n---------------------------------------------\n")
	text.insert(tk.INSERT,'\nRandom Forest: {}\n'.format(asRF))
	text.insert(tk.INSERT,confusion_matrix(test_target,pRF))
	text.insert(tk.INSERT,classification_report(test_target,pRF))

#for appearing second window
def second(nameid,age,sex,chest,bps,ch,fbs,rest,tha,ex,op,slop,ca,thl):
	window=tk.Tk()
	window.title("Report")
	window.geometry("1920x1080")
	print(sex.get())
	print(sex)


	a=0
	if sex=='1':
		a=1
	print(a)
	f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14=int(age.get()),a,int(chest.get()),int(bps.get()),int(ch.get()),int(fbs.get()),int(rest.get()),int(tha.get()),int(ex.get()),float(op.get()),int(slop.get()),int(ca.get()),int(thl.get())
	if(f2<1 or f2 >100):
		tk.Label(window,text="Error: Age should be between 1 and 100",font=("times",22,"bold"),relief="solid",bg="grey",fg="red").place(x=400,y=400)
	elif(f4<0 or f4 >3):
		tk.Label(window,text="Error: chest pain",font=("times",22,"bold"),relief="solid",bg="grey",fg="red").place(x=400,y=400)
	elif(f5<70 or f5>180):
	 	tk.Label(window,text="Error:  blood pressure",font=("times",22,"bold"),relief="solid",bg="grey",fg="red").place(x=400,y=400)
	elif(f6<100 or f6>400):
		tk.Label(window,text="Error: cholostroel",font=("times",22,"bold"),relief="solid",bg="grey",fg="red").place(x=400,y=400)
	elif(f7<0 or f7>1):
		tk.Label(window,text="Error: fasting blood pressure",font=("times",22,"bold"),relief="solid",bg="grey",fg="red").place(x=400,y=400)
	elif(f8<0 or f8>2):
		tk.Label(window,text="Error: resting ElectroCardiocResults",font=("times",22,"bold"),relief="solid",bg="grey",fg="red").place(x=400,y=400)
	elif(f9<60 or f9>200):
		tk.Label(window,text="Error: Thalcg",font=("times",22,"bold"),relief="solid",bg="grey",fg="red").place(x=400,y=400)
	elif(f10<0 or f10>1):
		tk.Label(window,text="Error: Exercised induced angina",font=("times",22,"bold"),relief="solid",bg="grey",fg="red").place(x=400,y=400)
	elif(f11<0.0 or f11>4.0):
		tk.Label(window,text="Error: old peak",font=("times",22,"bold"),relief="solid",bg="grey",fg="red").place(x=400,y=400)
	elif(f12<0 or f12>2):
		tk.Label(window,text="Error: Slope",font=("times",22,"bold"),relief="solid",bg="grey",fg="red").place(x=400,y=400)
	elif(f13<0 or f13>4):
		tk.Label(window,text="Error: ca",font=("times",22,"bold"),relief="solid",bg="grey",fg="red").place(x=400,y=400)
	elif(f14<1 or f14>4):
		tk.Label(window,text="Error: Thal",font=("times",22,"bold"),relief="solid",bg="grey",fg="red").place(x=400,y=400)
	else:
		tk.Label(window,text = "Patient Test Report",fg="black",relief="solid",font=("times","16","bold")).place(x = 100,y = 10)
		tk.Label(window,text = "Patientid",fg="black",font=("times","12","bold")).place(x = 50,y = 40)
		tk.Label(window,text = "Age:",fg="black",font=("times","12","bold")).place(x = 50,y = 80)
		tk.Label(window,text = "Sex:",fg="black",font=("times","12","bold")).place(x = 50,y = 120)
		tk.Label(window,text = "Chest Pain:",fg="black",font=("times","12","bold")).place(x = 50,y =160) 
		tk.Label(window,text = "Trestbps:",fg="black",font=("times","12","bold")).place(x = 50,y =200)
		tk.Label(window,text = "Cholestrol:",fg="black",font=("times","12","bold")).place(x = 50,y =240)
		tk.Label(window,text = "Fasting Blood sugar:",fg="black",font=("times","12","bold")).place(x = 50,y=280)
		tk.Label(window,text = "Restecg:",fg="black",font=("times","12","bold")).place(x = 50,y = 320)
		tk.Label(window,text = "Thalach: ",fg="black",font=("times","12","bold")).place(x = 50,y =360)
		tk.Label(window,text = "Exang:",fg="black",font=("times","12","bold")).place(x = 50,y = 400)
		tk.Label(window,text = "Oldpeak:",fg="black",font=("times","12","bold")).place(x = 50,y =440)
		tk.Label(window,text = "Slope:",fg="black",font=("times","12","bold")).place(x = 50,y = 480)
		tk.Label(window,text = "Ca:",fg="black",font=("times","12","bold")).place(x = 50,y =520)
		tk.Label(window,text = "Thal:",fg="black",font=("times","12","bold")).place(x =50,y =560) 
		#for appearing entry values
		tk.Label(window,text =nameid.get(),fg="black",font=("times","12","bold")).place(x=200,y=40)
		tk.Label(window,text=age.get(),fg="black",font=("times","12","bold")).place(x=200,y=80)
		if(sex.get()=='1'):
			tk.Label(window,text="Male",fg="black",font=("times","12","bold")).place(x=200,y=120)
		else:
			tk.Label(window,text="Female",fg="black",font=("times","12","bold")).place(x=200,y=120)
		tk.Label(window,text =chest.get(),fg="black",font=("times","12","bold")).place(x=200,y=160) 
		tk.Label(window,text =bps.get(),fg="black",font=("times","12","bold")).place(x=200,y=200)
		tk.Label(window,text =ch.get(),fg="black",font=("times","12","bold")).place(x=200,y=240)
		tk.Label(window,text =fbs.get(),fg="black",font=("times","12","bold")).place(x=200,y=280)
		tk.Label(window,text =rest.get(),fg="black",font=("times","12","bold")).place(x=200,y=320)
		tk.Label(window,text =tha.get(),fg="black",font=("times","12","bold")).place(x=200,y=360)
		tk.Label(window,text =ex.get(),fg="black",font=("times","12","bold")).place(x=200,y=400)
		tk.Label(window,text =op.get() ,fg="black",font=("times","12","bold")).place(x=200,y=440)
		tk.Label(window,text =slop.get(),fg="black",font=("times","12","bold")).place(x=200,y=480)
		tk.Label(window,text =ca.get(),fg="black",font=("times","12","bold")).place(x=200,y=520)
		tk.Label(window,text=thl.get(),fg="black",font=("times","12","bold")).place(x=200,y=560)  
		#Defining the reqirments
		tk.Label(window,text = "Reference Values",fg="black",relief="solid",font=("times","20","bold")).place(x =850 ,y = 50)
		tk.Label(window,text = "Chest Pain Type",fg="black",font=("times","12","bold")).place(x = 800,y = 130)
		tk.Label(window,text = "Value-1:typical angina",fg="black",font=("times","12","bold")).place(x = 820,y = 150)
		tk.Label(window,text = "Value-2:atypical angina",fg="black",font=("times","12","bold")).place(x = 820,y = 170)
		tk.Label(window,text = "Value-3:non-anginal pain",fg="black",font=("times","12","bold")).place(x = 820,y = 190)
		tk.Label(window,text = "Resting Blood pressure(mm/Hg)",fg="black",font=("times","12","bold")).place(x = 800,y = 220)
		tk.Label(window,text = "Serum cholostroel(mg/dl)",fg="black",font=("times","12","bold")).place(x = 800,y =250)
		tk.Label(window,text = "Fasting Blood Sugar",fg="black",font=("times","12","bold")).place(x = 800,y =280)
		tk.Label(window,text = "Resting ElectroCardiocResults",fg="black",font=("times","12","bold")).place(x = 800,y =310)  
		tk.Label(window,text = "Maximum Heart Rate Achieved",fg="black",font=("times","12","bold")).place(x = 800,y =340)  
		tk.Label(window,text = "Exercised Induced Angina",fg="black",font=("times","12","bold")).place(x = 800,y =370)   
		tk.Label(window,text = "ST depression induced by exercie relative to rest",fg="black",font=("times","12","bold")).place(x = 800,y =400)
		tk.Label(window,text = "slope of the peak exercise ST segment",fg="black",font=("times","12","bold")).place(x = 800,y =430)
		tk.Label(window,text = "number of major vessels(0-3)coloured by flourosopy",fg="black",font=("times","12","bold")).place(x = 800,y =460)
		tk.Label(window,text = "Thalassemia",fg="black",font=("times","12","bold")).place(x = 800,y =490)
		# tk.Label(window,text = ,fg="black",font=("times","12","bold")).place(x = 800,y =520)

		#Range values
		tk.Label(window,text="(Normal-120/80mmHg",fg="black",font=("times","12","bold")).place(x=280,y=160)
		tk.Label(window,text="High-120/80mmHg)",fg="black",font=("times","12","bold")).place(x=460,y=160)
		tk.Label(window,text ="(Normal:120-239mg/dl",fg="black",font=("times","12","bold")).place(x=280,y=240)
		tk.Label(window,text ="High:>=240mg/dl)",fg="black",font=("times","12","bold")).place(x=460,y=240)
		tk.Label(window,text ="(0-(Low)<=120mg/dl ",fg="black",font=("times","12","bold")).place(x=280,y=280)
		tk.Label(window,text ="1-(High)>=120mg/dl)",fg="black",font=("times","12","bold")).place(x=460,y=280)
		tk.Label(window,text ="(0-normal,1-having ST-T wave abnormality,2-left ventricular hyperthrophy)",fg="black",font=("times","12","bold")).place(x=240,y=320)
		#tk.Label(window,text =rest.get(),fg="black",font=("times","12","bold")).place(x=200,y=320)
		#tk.Label(window,text =rest.get(),fg="black",font=("times","12","bold")).place(x=200,y=320)

		#machine learning code from here
		from sklearn import tree
		from sklearn.naive_bayes import GaussianNB
		from sklearn import svm
		from sklearn import neighbors
		from sklearn.metrics import accuracy_score
		import pandas as pd
		import numpy as np
		train_val = pd.read_csv("heart.csv")
		train_target = train_val.iloc[:,-1].values
		train_data = train_val.iloc[:,:-1].values
		# test_data = train_digit.iloc[:,:].values
		# test_idx = [170]
		# test_data=train_data[test_idx]
		test_data=[[f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14]]
		# clf1 = tree.DecisionTreeClassifier()
		# clf1.fit(train_data,train_target)
		# print("DecisionTree",clf1.predict(test_data))

		clf2 = GaussianNB()
		clf2.fit(train_data,train_target)
		r=clf2.predict(test_data)
		if(r==1):
			l=tk.Label(window,text="Heart Disease Present",font=("times",22,"bold"),relief="solid",fg="black").place(x=220,y=600)
			
		else:
			l=tk.Label(window,text="No Heart Disease Present",font=("times",22,"bold"),relief="solid",fg="black").place(x=220,y=600)
			
		# clf3 = neighbors.KNeighborsClassifier()
		# clf3.fit(train_data,train_target)
		# print("kneighbor",clf3.predict(test_data))

		# clf4 = svm.SVC(gamma="scale")
		# clf4.fit(train_data,train_target)
		# print("svm",clf4.predict(test_data))
		#l.pack()
		# tk.Label(window,text="lets check",font=("time","12","bold")).place(x=10,y=10)
		# btn=tk.Button(window,text ="result",font=("times","14","bold"),bg="black",fg="white").place(x =150,y=150)




def pop_window(p,s,l):
    p.destroy()
    main_window(s,l)

def popupBonus(signup_window,login_window):
    
    popup_window=tk.Frame(login_window,background="grey")
    popup_window.place(x=380,y=180,width = 250, height = 100)
    
    #popupBonusWindow.wm_title("Window")
    labelBonus = Label(popup_window, text="Account Creation Successful",font="times 14",fg="white",bg="black")
    labelBonus.place(x=10,y=10)
    #labelBonus.grid(row=0, column=0)
    B1 = tk.Button(popup_window, text="Okay", command= lambda:pop_window(popup_window,signup_window,login_window))
    B1.place(x=110,y=50)

def login_database(fr,login_window,e1,e2):
    if e1.get()!="" and e2.get()!="":
        conn=sqlite3.connect("patients.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM test WHERE email=? AND password=?",(e1.get(),e2.get()))
        row=cur.fetchall()
        conn.close()
        if row!=[] and e1.get()!="" and e2.get()!="":
            submit_gui(login_window)
        else:
            l4=tk.Label(fr,text="User not found!!",font="times 14",bg='white',fg='red')
            l4.place(x=150,y=120)
    else:
        l4=tk.Label(fr,text="Fill Both Fields",font="times 14",bg='white',fg='red')
        l4.place(x=150,y=120)





def signup(frame2,login_window):
        def signup_database():
            if name.get()!="" and em.get()!="" and pwd.get()!="":
                conn=sqlite3.connect("patients.db")
                cur=conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text, password text)")
                cur.execute("INSERT INTO test Values(Null,?,?,?)",(name.get(),em.get(),pwd.get()))
                #l4=tk.Label(signup_window,text="Account created",font="times 15",bg="green")
                #l4.place(x=200,y=340)
                conn.commit()
                conn.close()
                popupBonus(signup_window,login_window)
            else:
                l4=tk.Label(signup_window,text="All fields Required",font="times 15",bg='white',fg='red')
                l4.place(x=210,y=150)
        frame2.destroy()
        #signup window
        signup_window=tk.Frame(login_window,background="white")
        signup_window.place(x=70,y=150,width = 450, height = 230)
        l1=tk.Label(signup_window,text="Name :",font="times 20",bg="white")
        l1.place(x=12,y=10)
        l2=tk.Label(signup_window,text="E-Mail :",font="times 20",bg="white")
        l2.place(x=12,y=60)
        l3=tk.Label(signup_window,text="Password :",font="times 20",bg="white")
        l3.place(x=12,y=110)
        name_text=tk.StringVar()
        name=tk.Entry(signup_window,textvariable=name_text,font="times 14",fg="black",bg="white")
        name.place(x=210,y=10,width=200,height=30)
        email_text=tk.StringVar()
        em=tk.Entry(signup_window,textvariable=email_text,font="times 14",fg="black",bg="white")
        em.place(x=210,y=60,width=200,height=30)
        password_text=tk.StringVar()
        pwd=tk.Entry(signup_window,textvariable=password_text,font="times 14",fg="black",bg="white")
        pwd.place(x=210,y=110,width=200,height=30)

        b1=tk.Button(signup_window,text="Create Account",width=20,command=lambda:signup_database())
        b1.place(x=100,y=190,width=120,height=25)
        b2=tk.Button(signup_window,text="Login",width=20,command= lambda : main_window(signup_window,login_window))
        b2.place(x=280,y=190,width=120,height=25)


#login window
def main_window(fr,login_window):
    fr.destroy()
    fr=tk.Frame(login_window,background="white")
    fr.place(x=95,y=150,width=400,height=200)
    l1=tk.Label(fr,text="Email :",font="times 20",bg="white")
    l1.place(x=20,y=20)
    l2=tk.Label(fr,text="Password :",fg="black",font="times 20",bg="white")
    l2.place(x=20,y=80)
    email_text=tk.StringVar()
    e1=tk.Entry(fr,textvariable=email_text,font="times 14",fg="black",bg="white")
    e1.place(x=160,y=20,height=28,width=180)
    password_text=tk.StringVar()
    e2=tk.Entry(fr,textvariable=password_text,show="*",font="times 14",fg="black",bg="white")
    e2.place(x=160,y=80,height=28,width=180)
    b1=tk.Button(fr,text="Login",width=25,command=lambda: login_database(fr,login_window,e1,e2))
    b1.place(x=50,y=150,height=28,width=120)
    b2=tk.Button(fr,text="Signup",width=25,command=lambda : signup(fr,login_window))
    b2.place(x=220,y=150,height=28,width=120)
    login_window.mainloop()

if __name__=="__main__":
    login_window= tk.Tk()
    login_window.title("")
    login_window.resizable(0,0)
    C = Canvas(login_window,  height=500, width=1000)
    filename = PhotoImage(file = 'test.png')
    background_label = Label(login_window, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()
    tk.Label(login_window,text="Prediction Of Heart Disease\nUsing Machine Learning",font=("Berlin Sans FB",30),fg="red",bg='white').place(x=60,y=20)
    fr=tk.Frame()
    main_window(fr,login_window)

