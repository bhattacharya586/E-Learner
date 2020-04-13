from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from flask import Flask,render_template,request
import firebase_admin
from firebase_admin import db,credentials
from datetime import datetime
import xlrd




app = Flask(__name__)
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
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
# =====================LOGIN========================
import auth
def get_labels():
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])
@app.route('/')
@app.route('/login')
def login_page_request():
    return render_template("index.html")

@app.route('/adminlogindetails',methods=['GET','POST'])
def admin_login_page_handle():
    return render_template("index.html")

@app.route('/logindetails',methods=['GET','POST'])
def login_page_handle():
    return "Error"

# =====================DATABASE========================
@app.route('/opendatabase/<id>')
def opendatabase(id):
    if(id == "employersinformationdatabase"):
        ref = db.reference('/UserDB/Faculty')
        data = dict(ref.get())
        return render_template("databases/employersinformationdatabase.html",data=data)
    
    elif(id == "employerslogininformationdatabase"):
        ref = db.reference('/UserDB/Student')
        data = dict(ref.get())
        return render_template("databases/employerslogininformationdatabase.html",data=data)
    
    elif(id == "studentinformationdatabase"):
        ref = db.reference('/UserDB/Student')
        data = dict(ref.get())
        return render_template("databases/studentinformationdatabase.html",data=data)
    
    elif(id == "studentlogininformationdatabase"):
        ref = db.reference('/UserDB/Student')
        data = dict(ref.get())
        return render_template("databases/studentlogininformationdatabase.html",data=data)
    
    elif(id == "studentperformancedatabase"):
        ref = db.reference('/UserDB/Student')
        data = dict(ref.get())
        return render_template("databases/studentperformancedatabase.html",data=data)
    
    elif(id == "studentsassignmentdatabase"):
        ref = db.reference('/Assignments')
        data = dict(ref.get())
        return render_template("databases/studentsassignmentdatabase.html",data=data)
    
    elif(id == "theorydatabase"):
        ref = db.reference('/Theory')
        data = dict(ref.get())
        return render_template("databases/theorydatabase.html",data=data)
    
    elif(id == "videodatabase"):
        ref = db.reference('/Videos')
        data = dict(ref.get())
        return render_template("databases/videodatabase.html",data=data)
    
    elif(id == "whatsappdatabase"):
        ref = db.reference('/Blogs')
        data = dict(ref.get())
        return render_template("databases/whatsappdatabase.html",data=data)
    
    elif(id == "commentsdatabase"):
        ref = db.reference('/UserDB/Student')
        data = dict(ref.get())
        return render_template("databases/commentsdatabase.html",data=data)
    
    else:
        return "Error"

# =====================DATABASE========================

# =====================REGISTER========================
@app.route('/register')
def register_page_request():
    class_l = ['A','B','C','D','E','F','G','H','I','IT']
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
    
    return render_template("register.html",security=security_q,class_l=class_l)
def sabu_mail(towhom,subject,mail_msg):
    SCOPES = 'https://mail.google.com/'
    CLIENT_SECRET_FILE = 'credentials.json'
    APPLICATION_NAME = 'Gmail API Python Quickstart'
    authInst = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
    credentials = authInst.get_credentials()

    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    import send_email

    sendInst = send_email.send_email(service)
    message = sendInst.create_message_with_attachment('amazonaniruddha123@gmail.com',towhom,subject,mail_msg, 'image.jpg' )
    sendInst.send_message('me',message)

@app.route('/student_registration_request',methods=['GET','POST'])
def student_registration_request():
    typeofuser = request.form["typeofuser"]
    print(typeofuser)
    sabu_mail('coolsamrat586@gmail.com','Hi Aniruddha','Hi Aniruddha')
    
    return render_template("otp.html")
    return "Error"

@app.route('/adminregisterdetails',methods=['GET','POST'])
def admin_register_page_handle():
    return render_template("register.html")

@app.route('/otp')
def otp():
    return render_template("otp.html")

@app.route('/registerdetails',methods=['GET','POST'])
def register_page_handle():
    typeofuser = request.form["typeofuser"]
    if(typeofuser=="Faculty"):
        # need to check id with same is already present or not

        # -
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email_id = request.form["email_id"]
        phone_no = request.form["phone_no"]
        security_ques = request.form["security_ques"]
        solution = request.form["solution"]
        faculty_id = request.form["faculty_id"]
        password = request.form["password"]
        subjects = request.form["subjects"]
        faculty_id = "GEF-"+faculty_id
        user_ref = db.reference('/UserDB/Faculty')
        user_ref.child(faculty_id).set({
            'email': email_id,
            'phone': phone_no,
            'name': firstname + " " + lastname,
            'password': password,
            'security_question': security_ques,
            'solution': solution,
            'faculty_id': faculty_id,
            'subjects': subjects,
        })
        return render_template("index.html")
        # need to check id with same is already present or not

        # -
        
    #user_ref = db.reference('/UserDB/Admin')
    #user_ref.child(emp_id).set({
    #    'email': "coolsamrat586@gmail.com",
    #    'phone': "7983648067",
    #    'name': "Aniruddha"+"Bhattacharya",
    #    'password': "University@99",
    #    'security_question': "What is the name of your first school?",
    #    'solution': "Montfort Senior Secondary School",
    #    'emp_id': emp_id,
    #})
    
    return "Error"

# =====================BLOGS========================

@app.route('/blogs_entry')
def blogs_page_request():
    return render_template("user-blog.html")

# ==================ADMIN===PRIVILEDGES======================

@app.route('/admin-dashboard')
def admin_dashboard():
    return render_template("admin/admin_main.html")

@app.route('/intermediate/<typeurl>')
def intermediate(typeurl):
    return render_template("admin/intermediate-admin.html",typeurl=typeurl)

@app.route('/upload-theory/<id>')
def intermediate_upload_theory(id):
    return render_template("admin/admin_upload_theory.html",id=id,msg="not triggered")

@app.route('/upload-theory-handler',methods=['GET',"POST"])
def theory_handler():
    unitname = request.form["unitname"]
    titlename = request.form["titlename"]
    subject = request.form["subject"]
    contentdata = request.form["contentdata"]

    path = 'F:/Learner-20200402T142116Z-001/Learner/theory/'+subject 
    newpath=""
    try:  
        os.mkdir(path)  
        os.chdir(path)
        newpath = path+"/"+titlename+".txt"
        f = open(newpath, "w")
        f.write(contentdata)
        f.close()
    except OSError as error:  
        newpath = path+"/"+titlename+".txt"
        f = open(newpath, "w")
        f.write(contentdata)
        f.close()
    user_ref = db.reference('/Theory/'+subject)
    
    today = datetime.now()
    d4 = today.strftime("%b-%d-%Y")
    t4 = today.strftime("%H:%M:%S")
    user_ref.child(titlename).set({
        'Title': titlename,
        'URL': newpath,
        'Time': t4,
        'Date': d4,
        'Faculty_Id': "GEF-897878",
        'Unit_Name': unitname,
    })
    return render_template("admin/index.html")

@app.route('/upload-video/<id>')
def admin_upload_video(id):
    return render_template("admin/admin_upload_video.html",id=id,msg="not triggered")

@app.route('/upload-video-handler/<message>')
def video_handler(message):
    return render_template("admin/message.html",message=message)

@app.route('/upload-assignments/<id>')
def admin_upload_assignment(id):
    return render_template("admin/admin_upload_assignment.html",id=id,msg="not triggered")

@app.route('/upload-assignments-handler/<message>')
def assignments_handler(message):
    return render_template("admin/message.html",message=message)

@app.route('/upload-blogs')
def admin_upload_blogs():
    return render_template("admin/admin_upload_blogs.html")

@app.route('/upload-blogs-handler',methods=['GET','POST'])
def blogs_handler():
    title = request.form["titlename"]
    content =   request.form["content"]
    username = "coolsamrat586" 
    author = ""
    ref = db.reference('/Blogs')
    m = ref.get()
    if(m!=None):
        data = dict(m)
        for key,value in data.items():
            for k,v in value.items():
                if(v["title"]==title):
                    return "Title Taken"
    ref = db.reference('/UserDB/Student')
    data = dict(ref.get())
    for key,value in data.items():
        if(value["username"]==username):
            author = value["name"]  
    title = title.replace(" ","")
    title = title.replace(":","")
    path = 'F:/Learner-20200402T142116Z-001/Learner/blogs/'+username 
    newpath=""
    try:  
        os.mkdir(path)  
        newpath = path+"/"+title+".txt"
        f = open(newpath, "w")
        f.write(content)
        f.close()
    except OSError as error:  
        newpath = path+"/"+title+".txt"
        f = open(newpath, "w")
        f.write(content)
        f.close()
    user_ref = db.reference('/Blogs/'+username)
    
    today = datetime.now()
    d4 = today.strftime("%b-%d-%Y")
    t4 = today.strftime("%H:%M:%S")
    user_ref.child(title).set({
        'title': title,
        'URL': newpath,
        'time': t4,
        'date': d4,
        'author': author,
    })
    return render_template("admin/admin.html")

@app.route('/mails')
def mails():
    ref = db.reference('/UserDB/Student')
    m = ref.get()
    data = dict(m)
    names = []
    phones = []
    emails = []
    courses = []
    sections = []
    urolls = []
    for key,value in data.items():
        names.append(value["name"])
        phones.append(value["phone"])
        emails.append(value["email"])
        courses.append(value["class"])
        sections.append(value["section"])
        urolls.append(value["university_roll_no"])
            

    return render_template("admin/admin-mails.html",names=names,
                                              phones=phones,
                                              emails=emails,
                                              courses=courses,
                                              sections=sections,
                                              urolls=urolls,lengu=len(urolls))

@app.route('/send_mails/<mail>')
def send_per_mails(mail):
    return render_template("admin/admin_mail.html",mail=mail)

@app.route('/send_mails_handler/<message>')
def send_mails_handler(message):
    return render_template("admin/message.html",message=message)

@app.route('/send_all_mails')
def send_all_mails():
    return render_template("admin/send_all_mail.html")

# =============================================
@app.route('/student-home')
def student_home():
    return render_template("student/student_home.html")
@app.route('/student-theory')
def student_theory():
    return render_template("student/student_theory.html")
@app.route('/student-video')
def student_video():
    return render_template("student/student_video.html")
@app.route('/student-blog')
def student_blog():
    return render_template("student/student_blogs.html")
@app.route('/student-tests')
def student_tests():
    return render_template("student/student_tests.html")
# =============================================
@app.route('/test-portal')
def student_test_portal():
    loc = (r"C:/Users/cools/Desktop/Question_Set.xlsx") 
    questions = ['']
    optionA = ['']
    optionB = ['']
    optionC = ['']
    optionD = ['']
    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0) 
    sheet.cell_value(0, 0) 
    
    for i in range(1,sheet.nrows): 
        questions.append(sheet.cell_value(i, 0).lstrip())
        optionA.append(sheet.cell_value(i, 1).lstrip())
        optionB.append(sheet.cell_value(i, 2).lstrip())
        optionC.append(sheet.cell_value(i, 3).lstrip())
        optionD.append(sheet.cell_value(i, 4).lstrip())

    return render_template("tes/index.html",lengu=len(questions),questions=questions,
                                            optionA=optionA,
                                            optionB=optionB,
                                            optionC=optionC,
                                            optionD=optionD)
@app.route('/testsol',methods=['GET','POST'])
def testsol():
    email  = request.form["name"]
    subject = request.form["subject"]
    questions_list = []
    solutions_list = ["","","","","","","","","","","","","","","","","","","",""]
    sols = 0
    for i,v in request.form.items():
        if "solution" in i:
            sols = int(i.split("-")[1])
            solutions_list[sols] = v
        if "question" in i:
            questions_list.append(v)
    #Read solutions
    loc = (r"C:/Users/cools/Desktop/Question_Set.xlsx") 
    solutions_real = ['']
    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0) 
    sheet.cell_value(0, 0) 
    
    for i in range(1,sheet.nrows): 
        solutions_real.append(sheet.cell_value(i, 5).lstrip())
    print(solutions_real)
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
    batch = ""
    enrollment = ""
    name = ""
    ref = db.reference('/UserDB/Student/')
    data = ref.get()
    data = dict(data)
    for key, value in data.items():
        if(value["email"]==email):
            name = value["name"]
            batch = value["class"]
            enrollment = value["university_roll_no"]
            
    Marks = ((correct*3)+(incorrect*(-1)))

    user_ref = db.reference('/Performance/'+batch+'/'+subject)
    
    user_ref.child(enrollment).set({
        'Name': name,
        'Email': email,
        'Batch': batch,
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
        'Answer_1': solutions_list[1],
        'Answer_2': solutions_list[2],
        'Answer_3': solutions_list[3],
        'Answer_4': solutions_list[4],
        'Answer_5': solutions_list[5],
        'Answer_6': solutions_list[6],
        'Answer_7': solutions_list[7],
        'Answer_8': solutions_list[8],
        'Answer_9': solutions_list[8],
        'Answer_10': solutions_list[10],
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
    return "hello"
# =============================================

if __name__ == '__main__':
    app.run(debug=True)