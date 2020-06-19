# Program extracting first column 
import xlrd 
import firebase_admin
from firebase_admin import db,credentials
config = {
    "apiKey": "AIzaSyDKEM_8Sy3DT_dw2BJSyqkGWcpOIZSo6Ks",
    "authDomain": "elearner-4fd02.firebaseapp.com",
    "databaseURL": "https://elearner-4fd02.firebaseio.com",
    "projectId": "elearner-4fd02",
    "storageBucket": "elearner-4fd02.appspot.com",
    "messagingSenderId": "933344165579",
    "appId": "1:933344165579:web:3f1137f53e8c971708e54e",
    "measurementId": "G-QW0SBXKZ3D"
}
cred = credentials.Certificate("static/elearner-4fd02-firebase-adminsdk-7kgbh-79bee47e37.json")
try:
    firebase_admin.initialize_app(cred,{"databaseURL": "https://elearner-4fd02.firebaseio.com",
    "storageBucket": "elearner-4fd02.appspot.com"})
except ValueError:
    print("Already Called")
    
loc = ("Question_Set.xlsx") 

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 
questions = []
optionsA = []
optionsB = []
optionsC = []
optionsD = []
answer = []
for i in range(1,sheet.nrows):
        questions.append(sheet.cell_value(i, 0))
        optionsA.append(sheet.cell_value(i, 1))
        optionsB.append(sheet.cell_value(i, 2))
        optionsC.append(sheet.cell_value(i, 3))
        optionsD.append(sheet.cell_value(i, 4))
        answer.append(sheet.cell_value(i, 5))
subject = input("enter the subject name")
textname = input("enter the test name")
user_ref = db.reference('/Tests/'+subject+'/'+textname)
for i in range(len(optionsA)):
    user_ref.child('q_'+str(i+1)).set({
        'question': questions[i],
        'optionsA': optionsA[i],
        'optionsB' : optionsB[i],
        'optionsC': optionsC[i],
        'optionsD': optionsD[i], 
        'answer': answer[i],      
    })
print("Done")
