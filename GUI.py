from importlib.abc import ResourceLoader
import tkinter as ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
sns.set_style('whitegrid')

model = pd.read_pickle('Loan_approval_predictions.pickle')

app = ttk.Tk()
app.geometry('900x900')
app.title('Loan Approval Prediction')

#set window color
#app.configure(bg='#FAF7F0')

cols = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Rural', 'Semiurban', 'Urban']

# Gender
ttk.Label(app, text='Choose Gender', padx=20,pady=10).grid(row=0, column = 0)
genders = {
    'Male': 1,
    'Female': 0
}
genderVar = ttk.Variable(app)
genderVar.set(genders['Male'])
frame = ttk.Frame(app)
frame.grid(row = 0, column = 1)
for gender, genderValue in genders.items():
    ttk.Radiobutton(frame, text = gender, variable = genderVar, value = genderValue).pack(side=ttk.LEFT)



#Married
ttk.Label(app, text='Married', padx=20,pady=10).grid(row=1, column = 0)
status = {
    'Yes': 1,
    'No': 0
}
statusVar = ttk.Variable(app)
statusVar.set(status['Yes'])
frame = ttk.Frame(app)
frame.grid(row = 1, column = 1)
for status, statusValue in status.items():
    ttk.Radiobutton(frame, text = status, variable = statusVar, value = statusValue).pack(side=ttk.LEFT)


#Dependents
ttk.Label(app, text='Number of Dependents', padx=20,pady=10).grid(row=2, column = 0)
Dependents = {
    '0': 0,
    '1': 1,
    '2': 2,
    '+3': 3
}
dependentVar = ttk.Variable(app)
dependentVar.set(Dependents['0'])
frame = ttk.Frame(app)
frame.grid(row = 2, column = 1)
for dependent, dependentValue in Dependents.items():
    ttk.Radiobutton(frame, text = dependent, variable = dependentVar, value = dependentValue).pack(side=ttk.LEFT)


#Education
ttk.Label(app, text='Education Status', padx=20,pady=10).grid(row=3, column = 0)
educations = {
    'Graduate': 1,
    'Not Graduate': 0
}
eduVar = ttk.Variable(app)
eduVar.set(educations['Graduate'])
frame = ttk.Frame(app)
frame.grid(row = 3, column = 1)
for edu, eduValue in educations.items():
    ttk.Radiobutton(frame, text = edu, variable = eduVar, value = eduValue).pack(side=ttk.LEFT)


#Self_Employed
ttk.Label(app, text='Self Employed', padx=20,pady=10).grid(row=4, column = 0)
Selfs = {
    'Yes': 1,
    'No': 0
}
selfVar = ttk.Variable(app)
selfVar.set(Selfs['Yes'])
frame = ttk.Frame(app)
frame.grid(row = 4, column = 1)
for self, selfValue in Selfs.items():
    ttk.Radiobutton(frame, text = self, variable = selfVar, value = selfValue).pack(side=ttk.LEFT)


#ApplicantIncome
ApplicantIncome = ttk.Variable(app)
ApplicantIncome.set('0')
ttk.Label(app, text='ApplicantIncome', padx = 15, pady = 15).grid(row = 5, column = 0)
frame = ttk.Frame(app)
frame.grid(row = 0, column = 1)
ttk.Entry(app, textvariable=ApplicantIncome, width=10).grid(row=5, column =1)


#CoapplicantIncome
CoapplicantIncome = ttk.Variable(app)
CoapplicantIncome.set('0')
ttk.Label(app, text='CoapplicantIncome', padx = 15, pady = 15).grid(row = 6, column = 0)
frame = ttk.Frame(app)
frame.grid(row = 0, column = 1)
ttk.Entry(app, textvariable=CoapplicantIncome, width=10).grid(row=6, column =1)


#LoanAmount
LoanAmount = ttk.Variable(app)
LoanAmount.set('0')
ttk.Label(app, text='LoanAmount', padx = 15, pady = 15).grid(row = 7, column = 0)
frame = ttk.Frame(app)
frame.grid(row = 0, column = 1)
ttk.Entry(app, textvariable=LoanAmount, width=10).grid(row=7, column =1)


#Loan_Amount_Term
Loan_Amount_Term = ttk.Variable(app)
Loan_Amount_Term.set('0')
ttk.Label(app, text='Loan_Amount_Term', padx = 15, pady = 15).grid(row = 8, column = 0)
frame = ttk.Frame(app)
frame.grid(row = 0, column = 1)
ttk.Entry(app, textvariable=Loan_Amount_Term, width=10).grid(row=8, column =1)

#Credit_History
ttk.Label(app, text='Credit History (1.0 for YES, 0.0 for No)', padx=20,pady=10).grid(row=9, column = 0)
Credits = {
    '1.0': 1,
    '0.0': 0
}
creditVar = ttk.Variable(app)
creditVar.set(Credits['1.0'])
frame = ttk.Frame(app)
frame.grid(row = 9, column = 1)
for credit, creditValue in Credits.items():
    ttk.Radiobutton(frame, text = credit, variable = creditVar, value = creditValue).pack(side=ttk.LEFT)


##Option Menu 1
data = ['Rural', 'Semiurban', 'Urban']
ttk.Label(app, text='Property Area').grid(row = 10, column = 0)
col1 = ttk.Variable(app)
values = ['select']+list(data)
col1.set(values[0])
frame = ttk.Frame(app)
frame.grid(row = 10, column = 1)
ttk.OptionMenu(app, col1, *values).grid(row = 10, column = 1)



# Prediciton Button
prop = [0,0,0]
def find_survival():
    global model

    alpha = col1.get()

    if alpha == 'Rural':
        prop[0] = 1
        prop[1] = 0
        prop[2] = 0
    
    elif alpha == 'Semiurban':
        prop[0] = 0
        prop[1] = 1
        prop[2] = 0
    
    else :
        prop[0] = 0
        prop[1] = 0
        prop[2] = 1

    print(prop[0], prop[1], prop[2])


    query_df = pd.DataFrame({'Gender': [genderVar.get()], 'Married': [statusVar.get()], 'Dependents': [dependentVar.get()], 'Education': [eduVar.get()], 'Self_Employed':[selfVar.get()], 'ApplicantIncome':[ApplicantIncome.get()], 'CoapplicantIncome':[CoapplicantIncome.get()],'LoanAmount':[LoanAmount.get()], 'Loan_Amount_Term':[Loan_Amount_Term.get()], 'Credit_History':[creditVar.get()], 'Rural':[prop[0]], 'Semiurban':[prop[1]], 'Urban':[prop[2]]})

    pred = model.predict(query_df)
    if pred[0] == 1:
        resultVar.set('Might Get the Loan!')
    else:
        resultVar.set('Might NOT Get the Loan!')

ttk.Button(app, text='Check', command = find_survival, padx=20, pady=2).grid(row = 11, column=0, columnspan=2)


# Result
resultVar = ttk.Variable(app)
ttk.Label(app, textvariable=resultVar, font=('Times New Roman',20)).grid(row = 12, column=0, columnspan=2)
#main







app.mainloop()