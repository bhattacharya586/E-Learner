import csv
import firebase_admin
from firebase_admin import db,credentials
import random
import string
def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
names = []
fnames = []
security_q = [
        "What was your childhood nickname?",
        "In what city did you meet your spouse/significant other?",
        "What is the name of your favorite childhood friend?",
        "What street did you live on in third grade?",
        "What is your oldest sibling’s birthday month and year? (e.g., January 1900)",
        "What is the middle name of your youngest child?",
        "What is your oldest sibling's middle name?",
        "What school did you attend for sixth grade?",
        "What was your childhood phone number including area code? (e.g., 000-000-0000)",
        "What is your oldest cousin's first and last name?",
        "What was the name of your first stuffed animal?",
        "In what city or town did your mother and father meet?",
        "Where were you when you had your first kiss?",
        "What is the first name of the boy or girl that you first kissed?",
        "What was the last name of your third grade teacher?",
        "In what city does your nearest sibling live?",
        "What is your youngest brother’s birthday month and year? (e.g., January 1900)",
        "What is your maternal grandmother's maiden name?",
        "In what city or town was your first job?",
        "What is the name of the place your wedding reception was held?",
        "What is the name of a college you applied to but didn't attend?",
        "Where were you when you first heard about 9/11?"]
email = []
operation = ['@gmail.com','@yahoo.com','@hotmail.com','@amazon.com','@redit.com']
phone = []
strt = ['99','98','78','94','75','80','85','92','62','79']
lawyers = ['Personal Injury Lawyer','Estate Planning Lawyer','Bankruptcy Lawyer','Intellectual Property Lawyer',
 'Employment Lawyer','Corporate Lawyer','Immigration Lawyer','Criminal Lawyer',
 'Medical Malpractice Lawyer','Tax Lawyer','Family Lawyer','Workers Compensation Lawyer',
 'Contract Lawyer','Social Security Disability Lawyer','Civil Litigation Lawyer','General Practice Lawyer']
count=-1
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
mnames = ['Bhagirathi','Meghna','Anjali','Prachi','Aarti','Bharti','Vaishali','Harshita','Isha','Komal','Richa','Sakshi','Riddhi','Tanya','Lopamudra','Shreya','Bidisha','Bipasha','Shreyoshi','Modhumita','Snigdha','Shashwati','Madhumita','Aishwarya','Bhashati','Anuradha','Kareena','Kaitrina','Hema','Rekha','Rakhi','Jaya','Kriti','Sridevi','Juhi','Shraddha','Amrita']
mn = []

print(len(mnames))
print("Information Creating Started")
with open(r'DOLA_List_of_Advocate_Uttar_Pradesh-dec-2016.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if(count==10000):
            break
        count=count+1
        if(count==0):
            continue
        if(row[2]!='NA'):
            
            names.append(row[1])
            fnames.append(row[2])
            mother = mnames[random.randint(0,36)].upper() + " " +row[2].split(" ")[-1]
            mn.append(mother)
            op = row[1].replace(" ","").lower()+str(count)+operation[random.choice([0,1,2,3,4])]
            email.append(op)

tenth = []
twelth = []
psk=[]
class_ = ['BTech_1st_Year','BTech_2nd_Year','BTech_3rd_Year','BTech_4th_Year']
section = ['A','B','C','D','E']
secA = []
secB = []
secC = []
secD = []
secE = []

cc = []
cs = []
cq = []
start = 2015000
csol = []
urolls = []
crolls = [] 

while(len(phone)!=1000 and len(crolls)!=1000):
    r1 = random.randint(10205048, 98542301)
    tt = round(random.uniform(2.2,10.0), 1)
    tenth.append(tt)
    if tt>=9.0:
        twelth.append(round(random.uniform(70.0,100.0), 2))
    if tt>5.0 and tt<9.0:
        twelth.append(round(random.uniform(50.0,100.0), 2))
    else:
        twelth.append(round(random.uniform(20.0,100.0), 2))
    cla = "BTech_3rd_Year" #class_[random.choice([0,1,2,3])]
    cc.append(cla) #class
    sec = "D"#section[random.choice([0,1,2,3])]
    cs.append(sec) # section
    #cl = random.randint(1, 100)
    #if(sec == 'A'):
    #    if cl not in secA:
    #        secA.append(cl)
    #if(sec == 'B'):
    #    if cl not in secB:
    #        secB.append(cl)
    #if(sec == 'C'):
    #    if cl not in secC:
    #        secC.append(cl)
    #if(sec == 'D'):
    #    if cl not in secD:
    #        secD.append(cl)
    #if(len(secA)<=100):
    #    crolls.append(cl)
    cq.append(security_q[random.randint(0, 21)]) 
    csol.append(randomString(8))
    psk.append(randomString(8))
    phone_no = strt[random.choice([0,1,2,3,4,5,6,7,8,9])]+str(r1)
    if(len(phone)<=1000):
       if phone_no not in phone:
            phone.append(phone_no)
    rl = "GES-"+ str(start)#str(random.randint(2012001, (2012001+1000)))
    if rl not in urolls:
        urolls.append(rl)
    print(cla,sec,urolls)
    start = start + 1
    
print("Information Creating Done")

print(crolls)
print(secA)
print(secB)
print(secC)
print(secD)
n = 0
user_ref = db.reference('/UserDB/Student')
for i in range(300,400):
    print(n+1," ",urolls[n]," ",'D'," ",names[i])
    user_ref.child(str(urolls[n])).set({
        'email': email[i],
        'phone': str(phone[n]),
        'name' : names[i].lower().capitalize(),
        'fname': fnames[i],
        'mname': mn[i],
        'password': psk[n],
        'class': cc[n],
        'section':'D',
        'class_roll_no': str(n+1),
        'security_question': cq[n],
        'solution': csol[n],
        'university_roll_no': str(urolls[n]),
        '10th_CGPA': str(tenth[n]),
        '12th_Percentage': str(twelth[n])
    })
    n+=1

    #print(tenth[i]," => ",twelth[i]," => ",cc[i]," => ",cs[i]," => ",cq[i]," => ",csol[i])
    #print(names[i]," => ",fnames[i]," => ",mn[i]," => ",email[i])
#print("Insertion Started into Database")
        


print("Done")
