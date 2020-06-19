import csv
import firebase_admin
from firebase_admin import db,credentials
import random
import string
def testsol(solutions_list,questions_list,batch,email,enrollment,subject,testname):
    #print("TestSol => ", questions_list)
    #print("TestSol => ", solutions_list)
    ref = db.reference('/Tests/'+'OS'+'/Deadlock')
    m = ref.get()
    if m != None:
        solutions_real = []
        data = dict(m)
        for i,j in data.items():
            solutions_real.append(j["answer"].lstrip())
    for i,j in zip(solutions_real,solutions_list):
        print(i,"\t\t\t",j)
    #print("TestSol => ", solutions_real)
    
    correct = 0
    incorrect = 0
    notans = 0
    for myans,realans in zip(solutions_list,solutions_real):
        #print("Myans = ",myans," Realans = ",realans)
        if myans == realans and (myans!='' and realans!=''):
            correct = correct + 1
        elif myans == "":
            notans = notans + 1
        else:
            incorrect = incorrect + 1
    print("Correct ",correct)   
    Marks = ((correct*5)+(incorrect*(-1)))
    user_ref = db.reference('/Performance/'+batch+'/'+subject)
            
    user_ref.child(enrollment).set({
        'Correct':correct,
        'Incorrect':incorrect,
        'Not_Answered':notans,
        'Test_name':testname,
        'Subject':subject,
        'Email': email,
        'Batch': batch,
        'URollNo':enrollment,
        'Question_1': questions_list[0],
        'Question_2': questions_list[1],
        'Question_3': questions_list[2],
        'Question_4': questions_list[3],
        'Question_5': questions_list[4],
        'Question_6': questions_list[5],
        'Question_7': questions_list[6],
        'Question_8': questions_list[7],
        'Question_9': questions_list[8],
        'Question_10': questions_list[9],
        'Answer_1': solutions_list[0],
        'Answer_2': solutions_list[1],
        'Answer_3': solutions_list[2],
        'Answer_4': solutions_list[3],
        'Answer_5': solutions_list[4],
        'Answer_6': solutions_list[5],
        'Answer_7': solutions_list[6],
        'Answer_8': solutions_list[7],
        'Answer_9': solutions_list[8],
        'Answer_10': solutions_list[9],
        'Marks':Marks,
    })
            
                #'Question_11': questions_list[10],
                #'Question_12': questions_list[11],
                #'Question_13': questions_list[12],
                #'Question_14': questions_list[13],
                #'Question_15': questions_list[14],
                #'Question_16': questions_list[15],
                #'Question_17': questions_list[16],
                #'Question_18': questions_list[17],
                #'Question_19': questions_list[19],
                #'Question_20': questions_list[19],
    
            
    
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
cred = credentials.Certificate("F:/cloud_learning/Admin_SIde/static/elearner-4fd02-firebase-adminsdk-7kgbh-79bee47e37.json")
try:
    firebase_admin.initialize_app(cred,{"databaseURL": "https://elearner-4fd02.firebaseio.com",
    "storageBucket": "elearner-4fd02.appspot.com"})
except ValueError:
    print("Already Called")
    
ref = db.reference('/Tests/OS')
m = ref.get()
#print("Test details", m)
if m !=None:
    data = dict(m)
    #print("Tests")
    #print(data)

questions = []
optionA = []
optionB = []
optionC = []
optionD = []

ref = db.reference('/Tests/OS'+'/'+"Deadlock")
m = ref.get()
if m != None:
    data = dict(m)
    for i,j in data.items():
        questions.append(j["question"])
        optionA.append(j["optionsA"])
        optionB.append(j["optionsB"])
        optionC.append(j["optionsC"])
        optionD.append(j["optionsD"])
print("*"*100)

ref = db.reference('/UserDB/Student')
m = ref.get()
if m != None:
    mails = []
    data = dict(m)
    for i,j in data.items():
        if(j["email"] in mails):
            print(j["email"]," ",j["university_roll_no"])
            dref = db.reference('/UserDB/Student/'+j["university_roll_no"])
            dref.delete()
        else:
            mails.append(j["email"])
            
            
print("Done")
