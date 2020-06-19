from __future__ import print_function
import httplib2
import os
import random 
import cgi
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import openpyxl
from flask import Flask,render_template,request,session,redirect,url_for,send_file
import firebase_admin
from firebase_admin import db,credentials
from datetime import datetime
import xlrd
import random

app = Flask(__name__)
app.secret_key = 'randowmjfnwejfnwkjdnwnfewkjnfkjwefnwjenfjwnefjwef'
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
subjects_semwise = {
            "BTech_1st_Year":    [
                                    {
                                        "Electronics Engg":
                                        ["https://previews.123rf.com/images/tuktukdesign/tuktukdesign1709/tuktukdesign170900071/85693436-network-icon-vector-symbol-group-of-people-and-teamwork-of-connected-business-person-in-glyph-pictog.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "Engg Maths-01":
                                        ["https://previews.123rf.com/images/tuktukdesign/tuktukdesign1709/tuktukdesign170900071/85693436-network-icon-vector-symbol-group-of-people-and-teamwork-of-connected-business-person-in-glyph-pictog.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "Chemistry":
                                        ["https://previews.123rf.com/images/tuktukdesign/tuktukdesign1709/tuktukdesign170900071/85693436-network-icon-vector-symbol-group-of-people-and-teamwork-of-connected-business-person-in-glyph-pictog.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "Intro to C Prog":
                                        ["https://previews.123rf.com/images/tuktukdesign/tuktukdesign1709/tuktukdesign170900071/85693436-network-icon-vector-symbol-group-of-people-and-teamwork-of-connected-business-person-in-glyph-pictog.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "Engg Mech":
                                        ["https://previews.123rf.com/images/tuktukdesign/tuktukdesign1709/tuktukdesign170900071/85693436-network-icon-vector-symbol-group-of-people-and-teamwork-of-connected-business-person-in-glyph-pictog.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "AutoCAD":
                                        ["https://previews.123rf.com/images/tuktukdesign/tuktukdesign1709/tuktukdesign170900071/85693436-network-icon-vector-symbol-group-of-people-and-teamwork-of-connected-business-person-in-glyph-pictog.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "Prof Comm-01":
                                        ["https://thumbs.dreamstime.com/b/two-color-compiler-vector-icon-programming-concept-isolated-blue-sign-symbol-can-be-use-web-mobile-logo-eps-149163801.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "Elec Engg":
                                        ["https://previews.123rf.com/images/vectorhome/vectorhome1907/vectorhome190700579/127615654-devops-icon-vector.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "Engg Maths-02":
                                        ["https://cdn3.iconfinder.com/data/icons/action-vector-icons-set-2/512/121-512.png","Completed","Total Uploads"]
                                    },
                                    {
                                        "Physics":
                                        ["https://cdn3.iconfinder.com/data/icons/action-vector-icons-set-2/512/121-512.png","Completed","Total Uploads"]
                                    },
                                    {
                                        "Adv C Prog":
                                        ["https://cdn1.iconfinder.com/data/icons/human-resources-25/64/aptitude-test-human-resources-business-512.png","Completed","Total Uploads"]
                                    },
                                    {
                                        "Mech Engg":
                                        ["https://cdn1.iconfinder.com/data/icons/human-resources-25/64/aptitude-test-human-resources-business-512.png","Completed","Total Uploads"]
                                    },
                                    {
                                        "Prof Comm-02":
                                        ["https://cdn1.iconfinder.com/data/icons/human-resources-25/64/aptitude-test-human-resources-business-512.png","Completed","Total Uploads"]
                                    }
                                ],

            "BTech_2nd_Year":    [
                                    {
                                        "Intro to C++":
                                        ["https://previews.123rf.com/images/tuktukdesign/tuktukdesign1709/tuktukdesign170900071/85693436-network-icon-vector-symbol-group-of-people-and-teamwork-of-connected-business-person-in-glyph-pictog.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "Cloud Comp-01":
                                        ["https://previews.123rf.com/images/tuktukdesign/tuktukdesign1709/tuktukdesign170900071/85693436-network-icon-vector-symbol-group-of-people-and-teamwork-of-connected-business-person-in-glyph-pictog.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "Discrete Maths":
                                        ["https://previews.123rf.com/images/tuktukdesign/tuktukdesign1709/tuktukdesign170900071/85693436-network-icon-vector-symbol-group-of-people-and-teamwork-of-connected-business-person-in-glyph-pictog.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "Career Skills-01":
                                        ["https://previews.123rf.com/images/tuktukdesign/tuktukdesign1709/tuktukdesign170900071/85693436-network-icon-vector-symbol-group-of-people-and-teamwork-of-connected-business-person-in-glyph-pictog.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "Logic Design":
                                        ["https://previews.123rf.com/images/tuktukdesign/tuktukdesign1709/tuktukdesign170900071/85693436-network-icon-vector-symbol-group-of-people-and-teamwork-of-connected-business-person-in-glyph-pictog.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "Computer Org":
                                        ["https://previews.123rf.com/images/tuktukdesign/tuktukdesign1709/tuktukdesign170900071/85693436-network-icon-vector-symbol-group-of-people-and-teamwork-of-connected-business-person-in-glyph-pictog.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "CBNST":
                                        ["https://thumbs.dreamstime.com/b/two-color-compiler-vector-icon-programming-concept-isolated-blue-sign-symbol-can-be-use-web-mobile-logo-eps-149163801.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "Cloud Comp-02":
                                        ["https://previews.123rf.com/images/vectorhome/vectorhome1907/vectorhome190700579/127615654-devops-icon-vector.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "Career Skills-02":
                                        ["https://cdn3.iconfinder.com/data/icons/action-vector-icons-set-2/512/121-512.png","Completed","Total Uploads"]
                                    },
                                    {
                                        "JAVA Prog":
                                        ["https://cdn3.iconfinder.com/data/icons/action-vector-icons-set-2/512/121-512.png","Completed","Total Uploads"]
                                    },
                                    {
                                        "Finite Automata":
                                        ["https://cdn1.iconfinder.com/data/icons/human-resources-25/64/aptitude-test-human-resources-business-512.png","Completed","Total Uploads"]
                                    }
                                ],

            "BTech_3rd_Year":    [
                                    {
                                        "DBMS":
                                        ["https://previews.123rf.com/images/tuktukdesign/tuktukdesign1709/tuktukdesign170900071/85693436-network-icon-vector-symbol-group-of-people-and-teamwork-of-connected-business-person-in-glyph-pictog.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "OS":
                                        ["https://previews.123rf.com/images/tuktukdesign/tuktukdesign1709/tuktukdesign170900071/85693436-network-icon-vector-symbol-group-of-people-and-teamwork-of-connected-business-person-in-glyph-pictog.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "Career Skills-03":
                                        ["https://previews.123rf.com/images/tuktukdesign/tuktukdesign1709/tuktukdesign170900071/85693436-network-icon-vector-symbol-group-of-people-and-teamwork-of-connected-business-person-in-glyph-pictog.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "Machine Learning":
                                        ["https://previews.123rf.com/images/tuktukdesign/tuktukdesign1709/tuktukdesign170900071/85693436-network-icon-vector-symbol-group-of-people-and-teamwork-of-connected-business-person-in-glyph-pictog.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "Cloud Comp-03":
                                        ["https://previews.123rf.com/images/tuktukdesign/tuktukdesign1709/tuktukdesign170900071/85693436-network-icon-vector-symbol-group-of-people-and-teamwork-of-connected-business-person-in-glyph-pictog.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "Computer Networks":
                                        ["https://previews.123rf.com/images/tuktukdesign/tuktukdesign1709/tuktukdesign170900071/85693436-network-icon-vector-symbol-group-of-people-and-teamwork-of-connected-business-person-in-glyph-pictog.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "Compiler Design":
                                        ["https://thumbs.dreamstime.com/b/two-color-compiler-vector-icon-programming-concept-isolated-blue-sign-symbol-can-be-use-web-mobile-logo-eps-149163801.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "DevOps":
                                        ["https://previews.123rf.com/images/vectorhome/vectorhome1907/vectorhome190700579/127615654-devops-icon-vector.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "FS Web Dev":
                                        ["https://cdn3.iconfinder.com/data/icons/action-vector-icons-set-2/512/121-512.png","Completed","Total Uploads"]
                                    },
                                    {
                                        "Design Algorithms":
                                        ["https://cdn3.iconfinder.com/data/icons/action-vector-icons-set-2/512/121-512.png","Completed","Total Uploads"]
                                    },
                                    {
                                        "Career Skills-04":
                                        ["https://cdn1.iconfinder.com/data/icons/human-resources-25/64/aptitude-test-human-resources-business-512.png","Completed","Total Uploads"]
                                    }
                                ],
            "BTech_4th_Year":    [
                                    {
                                        "DBMS":
                                        ["https://previews.123rf.com/images/tuktukdesign/tuktukdesign1709/tuktukdesign170900071/85693436-network-icon-vector-symbol-group-of-people-and-teamwork-of-connected-business-person-in-glyph-pictog.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "OS":
                                        ["https://previews.123rf.com/images/tuktukdesign/tuktukdesign1709/tuktukdesign170900071/85693436-network-icon-vector-symbol-group-of-people-and-teamwork-of-connected-business-person-in-glyph-pictog.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "Career Skills-03":
                                        ["https://previews.123rf.com/images/tuktukdesign/tuktukdesign1709/tuktukdesign170900071/85693436-network-icon-vector-symbol-group-of-people-and-teamwork-of-connected-business-person-in-glyph-pictog.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "Machine Learning":
                                        ["https://previews.123rf.com/images/tuktukdesign/tuktukdesign1709/tuktukdesign170900071/85693436-network-icon-vector-symbol-group-of-people-and-teamwork-of-connected-business-person-in-glyph-pictog.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "Cloud Computing-03":
                                        ["https://previews.123rf.com/images/tuktukdesign/tuktukdesign1709/tuktukdesign170900071/85693436-network-icon-vector-symbol-group-of-people-and-teamwork-of-connected-business-person-in-glyph-pictog.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "Computer Networks":
                                        ["https://previews.123rf.com/images/tuktukdesign/tuktukdesign1709/tuktukdesign170900071/85693436-network-icon-vector-symbol-group-of-people-and-teamwork-of-connected-business-person-in-glyph-pictog.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "Compiler Design":
                                        ["https://thumbs.dreamstime.com/b/two-color-compiler-vector-icon-programming-concept-isolated-blue-sign-symbol-can-be-use-web-mobile-logo-eps-149163801.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "DevOps":
                                        ["https://previews.123rf.com/images/vectorhome/vectorhome1907/vectorhome190700579/127615654-devops-icon-vector.jpg","Completed","Total Uploads"]
                                    },
                                    {
                                        "FS Web Dev":
                                        ["https://cdn3.iconfinder.com/data/icons/action-vector-icons-set-2/512/121-512.png","Completed","Total Uploads"]
                                    },
                                    {
                                        "Design Algorithms":
                                        ["https://cdn3.iconfinder.com/data/icons/action-vector-icons-set-2/512/121-512.png","Completed","Total Uploads"]
                                    },
                                    {
                                        "Career Skills-04":
                                        ["https://cdn1.iconfinder.com/data/icons/human-resources-25/64/aptitude-test-human-resources-business-512.png","Completed","Total Uploads"]
                                    }
                                ]
        
        }
@app.route('/')
def blank():
    return render_template('index.html')
# ======================================LOGIN AND REGISTER=======================================================
# This section contains all routes of login and register function
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

# Admin login routes Starts
@app.route('/admin-login')
def admin_login_page_request():
    return render_template('admin/admin_login.html',msg="")

@app.route('/admin-login-details',methods =['GET','POST'])
def admin_login_page_response():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        if(email == "amazonaniruddha123@gmail.com" and password == "University@99"):
            session["student_session"] = email
            return redirect(url_for('admin_dashboard'))
        else:
            return render_template('admin/admin_login.html',msg="noaccount")
    else:
        return render_template('admin/admin_login.html',msg="Not Post")

# Admin login routes Ends

@app.route('/login')
def login_page_request():
    return render_template("login.html",msg="")

@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    if "student_session" in session:
        session.pop('student_session', None)
        return redirect(url_for('blank'))
    else:
        return redirect(url_for('blank'))

@app.route('/logoutstudent')
def logoutstudent():
    # remove the username from the session if it is there
    if "student_session" in session:
        session.pop('student_session', None)
        n_ref = db.reference('/LoginDB/Student')
        n_ref.child(email).set({
            'email': session["student_session"]["email"],
            'university_roll_no': session["student_session"]["university_roll_no"],
            'Status':'Deactive'
        })
        return redirect(url_for('blank'))
    else:
        return redirect(url_for('blank'))

@app.route('/logindetails',methods=['GET','POST'])
def login_page_handle():
    email = request.form["email"]
    password = request.form["password"]
    ref = db.reference('/UserDB/Student')
    m = ref.get()
    if m != None:
        data = dict(m)
        flag=False
        for key,value in data.items():
            if(email == value["email"] and password == value["password"]):
                urollno = value["university_roll_no"]
                phone = value["phone"]
                class_ad = value["class"]
                flag = True
                session['student_session'] = {  'email':email,
                                                'university_roll_no':urollno,
                                                'class':class_ad,
                                                'phone':phone }
                n_ref = db.reference('/LoginDB/Student')
                n_ref.child(email).set({
                    'email': email,
                    'university_roll_no': urollno,
                    'Status':'Active'
                })
                return redirect(url_for('student_home'))   
    else:
        return render_template("login.html",msg="Unknown Error")               
    if(flag==False):
        return render_template("login.html",msg="Not Registered")  
                        
    return render_template("login.html",msg="Unknown Error")

@app.route('/adminlogindetails',methods=['GET','POST'])
def admin_login_page_handle():
    return "Error"

@app.route('/forget')
def forget_page_request():
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
    return render_template("forget.html",security=security_q)

@app.route('/forget-handle',methods=['GET','POST'])
def forget_page_handle():
    email = request.form["email"]
    securityquestion = request.form["securityquestion"]
    solution = request.form["solution"]
    ref = db.reference('/UserDB/Student')
    data = dict(ref.get())
    flag=False
    for key,value in data.items():
        if(email == value["email"] and securityquestion == value["security_question"]
            and solution == value["solution"]):
            password = value["password"]
            Title_mail = "Your Password is : "
            otp = password
            msg ="""From: <amazonaniruddha123@gmail.com>
                To:  <"""+email+""">
                MIME-Version: 1.0
                Content-type: text/html
                Subject: SMTP HTML e-mail test
                This is an e-mail message to be sent in HTML format.
                <b>This is HTML message.</b>
                <h1>This is your password valid for the instance only : """+otp+"""</h1>
                """
            sabu_mail(email,Title_mail,msg) 
            return "password sent to mail" 
    if(flag==False):
        return "Not Registered"
                        
    return "error"

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
    print(credentials)
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
    if typeofuser == "Student":
        Email_add = request.form["email"]
        print(request.form)
        Title_mail = "Welcome to GEU-Terminal!!!Your Contents are safe."
        otp = random.randint(000000, 999999)
        otp = str(otp)
        msg ="""From: <amazonaniruddha123@gmail.com>
                To: To Person <"""+Email_add+""">
                MIME-Version: 1.0
                Content-type: text/html
                Subject: SMTP HTML e-mail test
                This is an e-mail message to be sent in HTML format.
                <b>This is HTML message.</b>
                <h1>This is your OTP valid for the instance only : """+otp+"""</h1>
                """
        sabu_mail(Email_add,Title_mail,msg) 
    return render_template("otp.html",result = request.form,otp = otp)
    return "Error"

@app.route('/adminregisterdetails',methods=['GET','POST'])
def admin_register_page_handle():
    return render_template("register.html")

@app.route('/otpverifier',methods=['GET','POST'])
def otp():
    typeofuser = request.form["typeofuser"]
    otpsent = request.form["otpsent"]
    otpwrite = request.form["otpwrite"]
    if(otpsent==otpwrite):

        ref = db.reference('/UserDB/Student')
        m = ref.get()
        if m != None:
            data = dict()
            email_i = []
            class_i = []
            section_i = []
            croll = []
            uroll = []
            for key,value in data.items():
                email_i.append(value["email"])
                class_i.append(value["class"])
                section_i.append(value["section"])
                croll.append(value["class_roll_no"])
                uroll.append(value["university_roll_no"])
        
            if(typeofuser=="Student"):
                firstname = request.form["firstname"]
                lastname = request.form["lastname"]
                fathername = request.form["fathername"]
                mothername = request.form["mothername"]
                urollno = request.form["urollno"]
                class_ad = request.form["class_ad"]
                classrollno = request.form["classrollno"]
                section = request.form["section"]
                tenthgrade = request.form["tenthgrade"]
                twelthgrade = request.form["twelthgrade"]
                email_id = request.form["email"]
                phone_no = request.form["phone"]
                security_ques = request.form["securityquestion"]
                solution = request.form["solution"]
                password = request.form["password"]
                urollno = "GES-"+urollno
                if(email_id in email_i or urollno in uroll):
                    return "Already Registered"
                for i in range(len(croll)):
                    if(croll[i]==classrollno and section_i[i]==section and class_i[i]==class_ad):
                        return "Already Registered"
                
                user_ref = db.reference('/UserDB/Student')
                user_ref.child(urollno).set({
                    'email': email_id,
                    'phone': phone_no,
                    'name' : firstname + " " + lastname,
                    'fname': fathername,
                    'mname': mothername,
                    'password': password,
                    'class':class_ad,
                    'section':section,
                    'class_roll_no': classrollno,
                    'security_question': security_ques,
                    'solution': solution,
                    'university_roll_no': urollno,
                    '10th_CGPA': tenthgrade,
                    '12th_Percentage': twelthgrade
                })
                session['student_session'] = { 'email':email_id,
                                        'university_roll_no':urollno,
                                        'class':class_ad,
                                        'phone':phone_no}
                n_ref = db.reference('/LoginDB/Faculty')
                n_ref.child(email).set({
                    'email': email,
                    'faculty_id': faculty_id,
                    'Status':'Active'
                })
                return redirect(url_for('student_home'))
            else:
                return "Not Student"
        else:
            if(typeofuser=="Student"):
                firstname = request.form["firstname"]
                lastname = request.form["lastname"]
                fathername = request.form["fathername"]
                mothername = request.form["mothername"]
                urollno = request.form["urollno"]
                class_ad = request.form["class_ad"]
                classrollno = request.form["classrollno"]
                section = request.form["section"]
                tenthgrade = request.form["tenthgrade"]
                twelthgrade = request.form["twelthgrade"]
                email_id = request.form["email"]
                phone_no = request.form["phone"]
                security_ques = request.form["securityquestion"]
                solution = request.form["solution"]
                password = request.form["password"]
                urollno = "GES-"+urollno
                user_ref = db.reference('/UserDB/Student')
                user_ref.child(urollno).set({
                    'email': email_id,
                    'phone': phone_no,
                    'name' : firstname + " " + lastname,
                    'fname': fathername,
                    'mname': mothername,
                    'password': password,
                    'class':class_ad,
                    'section':section,
                    'class_roll_no': classrollno,
                    'security_question': security_ques,
                    'solution': solution,
                    'university_roll_no': urollno,
                    '10th_CGPA': tenthgrade,
                    '12th_Percentage': twelthgrade
                })
                session['student_session'] = { 'email':email_id,
                                        'university_roll_no':urollno,
                                        'class':class_ad,
                                        'phone':phone_no}

                return redirect(url_for('student_home'))
            else:
                return "Not Student"
    else:
        return "Wrong OTP"
    return "Error"
    
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
# =======================END LOGIN and REGISTER===============================    
# ===============================DATABASE=====================================
# This contains all the database information and routes.
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

# ==========================END OF DATABASE================================
# ==============================BLOGS======================================
# I think this is the dummy section I'll check it at last
@app.route('/blogs_entry')
def blogs_page_request():
    return render_template("user-blog.html")
# ===========================END OF BLOGS==================================
# ===========================ADMIN SECTION=================================
# This is the section of ADMIN
@app.route('/admin-dashboard')
def admin_dashboard():
    if "student_session" in session:
        malik = session["student_session"]
        info = []
        for i,j in subjects_semwise.items():
            info = j
        print(info)
        ref = db.reference('/Theory/')
        mk = ref.get()
        topics_theory_list = []
        author_theory_list = []
        date_theory_list = []
        time_theory_list = []
        UN_theory_list = []
        URL_theory_list = []
        if mk != None:
            data = dict(mk)
            for i,j in data.items():
                for k,l in j.items():
                    topics_theory_list.append(l["Title"])
                    tref = db.reference('/UserDB/Faculty/'+l["Faculty_Id"])
                    ml = tref.get()
                    author_theory_list.append(ml["name"])
                    date_theory_list.append(l["Date"])
                    time_theory_list.append(l["Time"])
                    UN_theory_list.append(l["Unit_Name"])
                    URL_theory_list.append(l["URL"])
        ref = db.reference('/Videos/')
        mk = ref.get()
        topics_videos_list = []
        author_videos_list = []
        date_videos_list = []
        time_videos_list = []
        UN_videos_list = []
        URL_videos_list = []
        if mk != None:
            data = dict(mk)
            for i,j in data.items():
                for k,l in j.items():
                    topics_videos_list.append(l["Title"])
                    tref = db.reference('/UserDB/Faculty/'+l["Faculty_Id"])
                    ml = tref.get()
                    author_videos_list.append(ml["name"])
                    date_videos_list.append(l["Date"])
                    time_videos_list.append(l["Time"])
                    UN_videos_list.append(l["Unit_Name"])
                    URL_videos_list.append(l["URL"])
        ref = db.reference('/UserDB/Student/')
        mk = ref.get()
        student_list_detailedA = []
        student_list_detailedB = []
        student_list_detailedC = []
        student_list_detailedD = []
        if mk != None:
            data = dict(mk)
            for i,j in data.items():
                if j["class"] == "BTech_1st_Year":
                    student_list_detailedA.append([j["name"],int(j["class_roll_no"]),j["university_roll_no"],j["section"]])
                if j["class"] == "BTech_2nd_Year":
                    student_list_detailedB.append([j["name"],int(j["class_roll_no"]),j["university_roll_no"],j["section"]])
                if j["class"] == "BTech_3rd_Year":
                    student_list_detailedC.append([j["name"],int(j["class_roll_no"]),j["university_roll_no"],j["section"]])
                if j["class"] == "BTech_4th_Year":
                    student_list_detailedD.append([j["name"],int(j["class_roll_no"]),j["university_roll_no"],j["section"]])

        sorted(student_list_detailedA,key=lambda l:l[1])
        sorted(student_list_detailedB,key=lambda l:l[1])
        sorted(student_list_detailedC,key=lambda l:l[1])
        sorted(student_list_detailedD,key=lambda l:l[1])

        print(student_list_detailedA)

        
        return render_template("admin/admin_main.html",malik=malik,topics_theory_list=topics_theory_list,
                                author_theory_list=author_theory_list,
                                date_theory_list=date_theory_list,
                                time_theory_list=time_theory_list,
                                UN_theory_list=UN_theory_list,
                                URL_theory_list=URL_theory_list,
                                topics_videos_list=topics_videos_list,
                                author_videos_list=author_videos_list,
                                date_videos_list=date_videos_list,
                                time_videos_list=time_videos_list,
                                UN_videos_list=UN_videos_list,
                                URL_videos_list=URL_videos_list,info=info,
                                student_list_detailedA=student_list_detailedA,
                                student_list_detailedB=student_list_detailedB,
                                student_list_detailedC=student_list_detailedC,
                                student_list_detailedD=student_list_detailedD)
    else:
        return redirect(url_for('admin_login_page_request'))

@app.route('/admin-visuals')
def admin_visuals():
    if "student_session" in session:
        malik = session["student_session"]

        print('/Performance/BTech_3rd_Year'+"/OS")
        #ref = db.reference('/Performance/BTech_3rd_Year'+"/OS")
        #m = ref.get()
        da=[]
        dq=[]
        dc=[]
        dd=[]
        #if m != None:
        #    solutions_real = []
        #    data = dict(m)
            
        #    for i,j in data.items():
        #        u_ref = db.reference('UserDB/Student/'+i)
        #        mo = u_ref.get()
        #        section=mo["section"]

        #        if(section=="A"):
        #            da.append(j["Marks"])
        #        if(section=="B"):
        #            dq.append(j["Marks"])
        #        if(section=="C"):
        #            dc.append(j["Marks"])
        #        if(section=="D"):
        #            dd.append(j["Marks"])

        #    num_li = [kl for kl in range(1,len(da)+len(dq)+len(dc)+len(dd)+1)]
        kheerA = []
        kheerB = []
        kheerC = []
        kheerD = []
        rt = {'Aniruddha':[("Test 1","90"),("Test 2","70"),("Test 3","80")],
        'Isha':[("Test 1","20"),("Test 2","50"),("Test 3","60")]}

        for i in range(0,100):
            kheerA.append([i+1,random.randint(10,100)])
            kheerB.append([i+1,random.randint(10,100)])
            kheerC.append([i+1,random.randint(10,100)])
            kheerD.append([i+1,random.randint(10,100)])
        return render_template("admin/admin_visuals.html",
                                    malik=malik,
                                    das=da,
                                    dqs=dq,
                                    dcs=dc,
                                    dds=dd,
                                    kheerA=kheerA,kheerB=kheerB,
                                    kheerC=kheerC,kheerD=kheerD,rt=rt)
        #else:
        #    return render_template("admin/admin_main.html",
        #                            malik=malik,
        #                            das=da,
        #                            dbs=db,
        #                            dcs=dc,
        #                            dds=dd,
        #                            num_li=100)
    else:
        return redirect(url_for('admin_login_page_request'))

@app.route('/intermediate/<typeurl>')
def intermediate(typeurl):
    if "student_session" in session:
        malik = session["student_session"]
        return render_template("admin/intermediate-admin.html",typeurl=typeurl,malik=malik)
    else:
        return redirect(url_for('admin_login_page_request'))

@app.route('/upload-theory/<id>')
def intermediate_upload_theory(id):
    if "student_session" in session:
        malik = session["student_session"]
        return render_template("admin/admin_upload_theory.html",id=id,msg="not triggered",malik=malik)
    else:
        return redirect(url_for('admin_login_page_request'))

@app.route('/upload-theory-handler',methods=['GET',"POST"])
def theory_handler():
    if "student_session" in session:
        if request.method == 'POST':
            malik = session["student_session"]
            unitname = request.form["unitname"]
            titlename = request.form["titlename"]
            subject = request.form["subject"]
            contentdata = request.form["contentdata"]
            contentdata ="""
            <!doctype html>
            <html lang="en">
            <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <!-- Bootstrap CSS -->
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
            <title>"""+titlename+"""</title>
            </head>
            <body>
            <div class="container mt-5 mb-5">
            <h2 class="text-left">"""+unitname+"""</h2>
            <h5 class="text-center">"""+titlename+"""</h5>
            <p class="text-justify"><code>"""+contentdata+"""</code></p>
            </div>
            <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous">
            </script>
            <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous">
            </script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous">
            </script>
            </body>
            </html>"""
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
            return redirect(url_for('admin_dashboard'))
        else:
            return redirect(url_for('admin_dashboard'))
    else:
        return redirect(url_for('admin_login_page_request'))

@app.route('/upload-video/<id>')
def admin_upload_video(id):
    if "student_session" in session:
        malik = session["student_session"]
        return render_template("admin/admin_upload_video.html",id=id,msg="not triggered",malik=malik)
    else:
        return redirect(url_for('admin_login_page_request'))
    
@app.route('/upload-video-handler/<message>')
def video_handler(message):
    if "student_session" in session:
        return redirect(url_for('admin_dashboard'))
    else:
        return redirect(url_for('admin_login_page_request'))

@app.route('/upload-assignments/<id>')
def admin_upload_assignment(id):
    if "student_session" in session:
        malik = session["student_session"]
        return render_template("admin/admin_upload_assignment.html",id=id,msg="not triggered",malik=malik)
    else:
        return redirect(url_for('admin_login_page_request'))

@app.route('/upload-assignments-handler/<message>')
def assignments_handler(message):
    if "student_session" in session:
        return redirect(url_for('admin_dashboard'))
    else:
        return redirect(url_for('admin_login_page_request'))

#@app.route('/upload-blogs')
#def admin_upload_blogs():
#    return render_template("admin/admin_upload_blogs.html")

#@app.route('/upload-blogs-handler',methods=['GET','POST'])
#def blogs_handler():
#    title = request.form["titlename"]
#    content =   request.form["content"]
#    username = "coolsamrat586" 
#    author = ""
#    ref = db.reference('/Blogs')
#    m = ref.get()
#    if(m!=None):
#        data = dict(m)
#        for key,value in data.items():
#            for k,v in value.items():
#                if(v["title"]==title):
#                    return "Title Taken"
#    ref = db.reference('/UserDB/Student')
#    data = dict(ref.get())
#    for key,value in data.items():
#        if(value["username"]==username):
#            author = value["name"]  
#    title = title.replace(" ","")
#    title = title.replace(":","")
#    path = 'F:/Learner-20200402T142116Z-001/Learner/blogs/'+username 
#    newpath=""
#    try:  
#        os.mkdir(path)  
#        newpath = path+"/"+title+".txt"
#        f = open(newpath, "w")
#        f.write(content)
#        f.close()
#    except OSError as error:  
#        newpath = path+"/"+title+".txt"
#        f = open(newpath, "w")
#        f.write(content)
#        f.close()
#    user_ref = db.reference('/Blogs/'+username)
    
#   today = datetime.now()
#    d4 = today.strftime("%b-%d-%Y")
#    t4 = today.strftime("%H:%M:%S")
#    user_ref.child(title).set({
#        'title': title,
#        'URL': newpath,
#        'time': t4,
#        'date': d4,
#        'author': author,
#    })
#    return redirect(url_for('admin_dashboard'))

#============================MAIL SECTION=======================

@app.route('/sending_mail',methods=['GET','POST'])
def sending_mail():
    if "student_session" in session:
        if request.method == "POST":
            malik = session["student_session"]
            recieve = request.form["rcv"]
            print(recieve)
            subject = request.form["subject"]
            content = request.form["content"]
            msg ="""From: <amazonaniruddha123@gmail.com>
                To:  <"""+recieve+""">
                MIME-Version: 1.0
                Content-type: text/html
                Subject: """+subject+"""
                This is an e-mail message to be sent in HTML format.
                \n\n\n"""+content+"""
                """
            Title_mail = "You got a mail from GEU-Terminals : "
            sabu_mail(recieve,Title_mail,msg) 
            return redirect(url_for('mails'))
        else:
            return redirect(url_for('mails'))
    else:
        return redirect(url_for('admin_login_page_request'))

@app.route('/mails')
def mails():
    if "student_session" in session:
        malik = session["student_session"]
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
                                                urolls=urolls,lengu=len(urolls),malik=malik)
    else:
        return redirect(url_for('admin_login_page_request'))

@app.route('/send_mails/<mail>')
def send_per_mails(mail):
    if "student_session" in session:
        malik = session["student_session"]
        return render_template("admin/admin_mail.html",mail=mail,malik=malik)
    else:
        return redirect(url_for('admin_login_page_request'))
    
@app.route('/send_mails_handler/<message>')
def send_mails_handler(message):
    if "student_session" in session:
        malik = session["student_session"]
        return redirect(url_for('admin_dashboard'))
    else:
        return redirect(url_for('admin_login_page_request'))

@app.route('/send_all_mails')
def send_all_mails():
    if "student_session" in session:
        malik = session["student_session"]
        return render_template("admin/send_all_mail.html",malik=malik)
    else:
        return redirect(url_for('admin_login_page_request'))
    

# ==============================END OF ADMIN==============================
# ================================STUDENTS==============================
# This section contains the priviledges of the students
@app.route('/student-home')
def student_home():
    if "student_session" in session:
        session_info = session["student_session"]
        class_batch = session_info["class"]
        class_email = session_info["email"]
        class_phone = session_info["phone"]
        class_university_roll_no = session_info["university_roll_no"]
        info = []
        for i,j in subjects_semwise.items():
            if(i==class_batch):
                info = j
        print(info)
        ref = db.reference('/Theory/')
        mk = ref.get()
        topics_theory_list = []
        author_theory_list = []
        date_theory_list = []
        time_theory_list = []
        UN_theory_list = []
        URL_theory_list = []
        if mk != None:
            data = dict(mk)
            for i,j in data.items():
                for k,l in j.items():
                    topics_theory_list.append(l["Title"])
                    tref = db.reference('/UserDB/Faculty/'+l["Faculty_Id"])
                    ml = tref.get()
                    author_theory_list.append(ml["name"])
                    date_theory_list.append(l["Date"])
                    time_theory_list.append(l["Time"])
                    UN_theory_list.append(l["Unit_Name"])
                    URL_theory_list.append(l["URL"])
        classmates = []
        reref = db.reference('/UserDB/Student/'+class_university_roll_no)
        mj= reref.get()
        mysection = mj["section"]
        reref = db.reference('/UserDB/Student/')
        mj= reref.get()
        if mj != None:
            datan = dict(mj)
            for i,j in datan.items():
                if(mysection == j["section"]):
                    classmates.append([j["name"],j["class_roll_no"],j["university_roll_no"]])
        ref = db.reference('/Videos/')
        mk = ref.get()
        topics_videos_list = []
        author_videos_list = []
        date_videos_list = []
        time_videos_list = []
        UN_videos_list = []
        URL_videos_list = []
        if mk != None:
            data = dict(mk)
            for i,j in data.items():
                for k,l in j.items():
                    topics_videos_list.append(l["Title"])
                    tref = db.reference('/UserDB/Faculty/'+l["Faculty_Id"])
                    ml = tref.get()
                    author_videos_list.append(ml["name"])
                    date_videos_list.append(l["Date"])
                    time_videos_list.append(l["Time"])
                    UN_videos_list.append(l["Unit_Name"])
                    URL_videos_list.append(l["URL"])

        return render_template("student/student_home.html",info=info,
                                class_email=class_email,
                                topics_theory_list=topics_theory_list,
                                author_theory_list=author_theory_list,
                                date_theory_list=date_theory_list,
                                time_theory_list=time_theory_list,
                                UN_theory_list=UN_theory_list,
                                URL_theory_list=URL_theory_list,
                                topics_videos_list=topics_videos_list,
                                author_videos_list=author_videos_list,
                                date_videos_list=date_videos_list,
                                time_videos_list=time_videos_list,
                                UN_videos_list=UN_videos_list,
                                URL_videos_list=URL_videos_list,
                                classmates = classmates,mysection=mysection)
                    
    return "error"

@app.route('/student-theory/<subname>')
def student_theory(subname):
    if "student_session" in session:
        session_info = session["student_session"]
        class_batch = session_info["class"]
        class_email = session_info["email"]
        class_phone = session_info["phone"]
        class_university_roll_no = session_info["university_roll_no"]
        info = []
        for i,j in subjects_semwise.items():
            if(i==class_batch):
                info = j
        print(info)
        ref = db.reference('/Theory/'+subname)
        m = ref.get()
        chapters = []
        print("*"*150)
        if m != None:
            data = dict(m)
            for i,j in data.items():
                chapters.append(j["Unit_Name"])
        
        print("*"*150)
        chapters = set(chapters)
        return render_template("student/student_theory.html",chapters=chapters,subname=subname,class_email=class_email,info=info)
    return "error"

@app.route('/student-video/<subname>')
def student_video(subname):
    if "student_session" in session:
        session_info = session["student_session"]
        class_batch = session_info["class"]
        class_email = session_info["email"]
        class_phone = session_info["phone"]
        class_university_roll_no = session_info["university_roll_no"]
        info = []
        for i,j in subjects_semwise.items():
            if(i==class_batch):
                info = j
        print(info)
        ref = db.reference('/Videos/'+subname)
        m = ref.get()
        chapters = []
        print("*"*150)
        if m != None:
            data = dict(m)
            for i,j in data.items():
                chapters.append(j["Unit_Name"])
        
        print("*"*150)
        chapters = set(chapters)
        return render_template("student/student_video.html",chapters=chapters,subname=subname,class_email=class_email,info=info)
    return "error"

@app.route('/student-blog')
def student_blog():
    return render_template("student/student_blogs.html")

@app.route('/student-tests/<subname>')
def student_tests(subname):
    if "student_session" in session:
        session_info = session["student_session"]
        class_batch = session_info["class"]
        class_email = session_info["email"]
        class_phone = session_info["phone"]
        class_university_roll_no = session_info["university_roll_no"]
        info = []
        for i,j in subjects_semwise.items():
            if(i==class_batch):
                info = j
        print(info)
        #ref = db.reference('/Videos/'+subname)
        #m = ref.get()
        #chapters = []
        #print("*"*150)
        #if m != None:
        #    data = dict(m)
        #    for i,j in data.items():
        #        chapters.append(j["Unit_Name"])
        
        #print("*"*150)
        #chapters = set(chapters)
        
        ref = db.reference('/Tests/'+subname)
        m = ref.get()
        print("Test details", m)
        if m !=None:
            data = dict(m)
            print("Tests")
            print(data)
            return render_template("student/student_tests.html",subname=subname,class_email=class_email,info=info,data=data)
        else:
            return "No tests" 
    return "error"
# ========================END OF STUDENT SECTION==========================
# =========================TEST PORTAL SECTION============================
# This section contains information of test portal
@app.route('/test-portal/<subname>/<testname>')
def student_test_portal(subname,testname):
    if "student_session" in session:
        ref = db.reference('/Performance/'+session["student_session"]["class"]+'/'+subname+'/'+session["student_session"]["university_roll_no"])
        m = ref.get()
        flag=False
        if m != None:
            data = dict(m)
            if(data["Test_name"] == testname):
                flag=True
                uref = db.reference('/Tests/'+subname+'/'+testname)
                mo = uref.get()
                solutions_real = []
                if mo != None:
                    datax = dict(mo)
                    print(datax)
                    for ib,jb in datax.items():
                        solutions_real.append(jb["answer"].lstrip())
                print("Solution Real ",solutions_real)
                session_info = session["student_session"]
                class_batch = session_info["class"]
                class_email = session_info["email"]
                class_phone = session_info["phone"]
                class_university_roll_no = session_info["university_roll_no"]
                info = []
                for i,j in subjects_semwise.items():
                    if(i==class_batch):
                        info = j
                print(info)
                return render_template("tes/testrules.html",subject = subname
                ,data = data,msg="TestGivenAlready",solutions = solutions_real,info=info,class_email=class_email)
        if flag==False:
            #loc = (r"C:/Users/cools/Desktop/Question_Set.xlsx") 
            info = []
            questions = ['']
            optionA = ['']
            optionB = ['']
            optionC = ['']
            optionD = ['']
            #wb = xlrd.open_workbook(loc) 
            #sheet = wb.sheet_by_index(0) 
            #sheet.cell_value(0, 0) 
            
            #for i in range(1,sheet.nrows): 
            #    questions.append(sheet.cell_value(i, 0).lstrip())
            #    optionA.append(sheet.cell_value(i, 1).lstrip())
            #    optionB.append(sheet.cell_value(i, 2).lstrip())
            #    optionC.append(sheet.cell_value(i, 3).lstrip())
            #    optionD.append(sheet.cell_value(i, 4).lstrip())
            print(subname)
            print(testname)
            ref = db.reference('/Tests/'+subname+'/'+testname)
            m = ref.get()
            if m != None:
                data = dict(m)
                for i,j in data.items():
                    questions.append(j["question"])
                    optionA.append(j["optionsA"])
                    optionB.append(j["optionsB"])
                    optionC.append(j["optionsC"])
                    optionD.append(j["optionsD"])
                urr_ref = db.reference('/Performance/'+session["student_session"]["class"]+'/'+subname)
            
                urr_ref.child(session["student_session"]["university_roll_no"]).set({
                    'Correct':"0",
                    'Incorrect':"0",
                    'Not_Answered':"10",
                    'Test_name':testname,
                    'Subject':subname,
                    'Email': session["student_session"]["email"],
                    'Batch': session["student_session"]["class"],
                    'URollNo':session["student_session"]["university_roll_no"],
                    'Question_1': questions[1],
                    'Question_2': questions[2],
                    'Question_3': questions[3],
                    'Question_4': questions[4],
                    'Question_5': questions[5],
                    'Question_6': questions[6],
                    'Question_7': questions[7],
                    'Question_8': questions[8],
                    'Question_9': questions[9],
                    'Question_10': questions[10],
                    'Answer_1': "",
                    'Answer_2': "",
                    'Answer_3': "",
                    'Answer_4': "",
                    'Answer_5': "",
                    'Answer_6': "",
                    'Answer_7': "",
                    'Answer_8': "",
                    'Answer_9': "",
                    'Answer_10': "",
                    'Marks':"0"
                })
                session_info = session["student_session"]
                class_batch = session_info["class"]
                class_email = session_info["email"]
                class_phone = session_info["phone"]
                class_university_roll_no = session_info["university_roll_no"]
                return render_template("tes/index.html",lengu=len(questions),questions=questions,
                                                    optionA=optionA,
                                                    optionB=optionB,
                                                    optionC=optionC,
                                                    optionD=optionD,subname=subname,testname=testname,info=info,class_email=class_email)
            else:
                return "no tests"
    else:
        return redirect(url_for('admin_login_page_request'))
    
@app.route('/testsol',methods=['GET','POST'])
def testsol():
    if "student_session" in session:
        email  = session["student_session"]["email"]
        subject = request.form["subject"]
        testname = request.form["testname"]
        questions_list = []
        solutions_list = ["","","","","","","","","","","","","","","","","","","",""]
        sols = 0
        for i,v in request.form.items():
            print(i,v)
            if "solution" in i:
                sols = int(i.split("-")[1])
                solutions_list[sols-1] = v
            if "question" in i:
                questions_list.append(v)
        #Read solutions
        #loc = (r"C:/Users/cools/Desktop/Question_Set.xlsx") 
        #solutions_real = ['']
        #wb = xlrd.open_workbook(loc) 
        #sheet = wb.sheet_by_index(0) 
        #sheet.cell_value(0, 0) 
        
        #for i in range(1,sheet.nrows): 
        #    solutions_real.append(sheet.cell_value(i, 5).lstrip())
        print(solutions_list)
        print('/Tests/'+subject+'/'+testname)
        ref = db.reference('/Tests/'+subject+'/'+testname)
        m = ref.get()
        if m != None:
            solutions_real = []
            data = dict(m)
            for i,j in data.items():
                solutions_real.append(j["answer"].lstrip())
            print(solutions_real)
            correct = 0
            incorrect = 0
            notans = 0
            strop = []
            for myans,realans in zip(solutions_list,solutions_real):
                #print("Myans = ",myans," Realans = ",realans)
                if myans == realans and (myans!='' and realans!=''):
                    correct = correct + 1
                    strop.append(1)
                elif myans == "":
                    notans = notans + 1
                    strop.append(0)
                else:
                    incorrect = incorrect + 1
                    strop.append(-1)
            print("correct ",correct)
            print(strop)
            batch = session["student_session"]["class"]
            enrollment = session["student_session"]["university_roll_no"]       
                    
            Marks = ((correct*3)+(incorrect*(-1)))
            print('/Performance/'+batch+'/'+subject)
            wb_obj = openpyxl.load_workbook("DatasetGate.xlsx")
            source1 = wb_obj.get_sheet_by_name('Sheet1')  
            shic_ref = db.reference('UserDB/Student/'+session["student_session"]["university_roll_no"])
            mshic = shic_ref.get()
            dataschi = dict(mshic)
            student_Name = dataschi["name"]
            dataqw = (student_Name,enrollment,
                email,batch,
                subject,testname,strop[0],strop[1],
                strop[2],strop[3],strop[4],strop[5],
                strop[6],strop[7],strop[8],strop[9],correct,incorrect,notans,Marks) 
            
            
            
            source1.append(dataqw)  
            wb_obj.save('DatasetGate.xlsx') 

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
                'Marks':Marks
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
            ref = db.reference('/Performance/'+session["student_session"]["class"]+'/'+subject+'/'+session["student_session"]["university_roll_no"])
            md = ref.get()
            flag=False
            info = []
            if md != None:
                dataq = dict(md)
                if(dataq["Test_name"] == testname):
                    flag=True
                    uref = db.reference('/Tests/'+subject+'/'+testname)
                    mo = uref.get()
                    solutions_real = []
                    if mo != None:
                        datax = dict(mo)
                        print(datax)
                        for ib,jb in datax.items():
                            solutions_real.append(jb["answer"].lstrip())
                    print("Solution Real ",solutions_real)
                    session_info = session["student_session"]
                    class_batch = session_info["class"]
                    class_email = session_info["email"]
                    class_phone = session_info["phone"]
                    class_university_roll_no = session_info["university_roll_no"]
                    info = []
                    for i,j in subjects_semwise.items():
                        if(i==class_batch):
                            info = j
                    print(info)
                    return render_template("tes/testrules.html",subject = subject
                    ,data = dataq,msg="TestGivenAlready",solutions = solutions_real,info=info,class_email=class_email)
        else:
            return "no tests"
    else:
        return redirect(url_for('admin_login_page_request'))
    
@app.route('/testrules/<subname>/<titlename>')
def testrule(subname,titlename):
    path = 'F:/Learner-20200402T142116Z-001/Learner/theory/'+subname+'/'+titlename+".txt" 
    ip = open(path,"r")
    read_f = ip.read()
    
    return send_file(path, attachment_filename=titlename+".html")

#=======================READ GRAPHS========================
@app.route('/read-graph')
def graph():
    if "student_session" in session:
        import xlrd 
  
        loc = ("DatasetGate.xlsx") 
        
        wb = xlrd.open_workbook(loc) 
        sheet = wb.sheet_by_index(0) 
        sheet.cell_value(0, 0) 
        aniruddha_marks = []
        for i in range(sheet.nrows): 
            if  (sheet.cell_value(i, 3) ==  session["student_session"]["class"] and
                sheet.cell_value(i, 1) == session["student_session"]["university_roll_no"] and 
                sheet.cell_value(i, 2) == session["student_session"]["email"]):
                aniruddha_marks.append([sheet.cell_value(i, 4),sheet.cell_value(i, 16),sheet.cell_value(i, 17),sheet.cell_value(i, 18),sheet.cell_value(i, 19)])
        print(aniruddha_marks)
        session_info = session["student_session"]
        class_batch = session_info["class"]
        class_email = session_info["email"]
        class_phone = session_info["phone"]
        class_university_roll_no = session_info["university_roll_no"]
        info = []
        for i,j in subjects_semwise.items():
            if(i==class_batch):
                info = j
        print(info)
        return render_template("student/visual.html",aniruddha_marks=aniruddha_marks,info=info,class_email=class_email)
    else:
        return "mello"

# =======================SHARE SECTION======================
@app.route('/share-video',methods=["GET",'POST'])
def share_video():
    if "student_session" in session:
        if request.method=="POST":
            to = request.form["email_id_t"]
            subject_p = request.form["cur_subn"]
            sub = request.form["subject_r_t"]
            content_t_t = request.form["content_t"]
            Title_mail = session["student_session"]["email"]+" has shared a video with you..."
            msg ="""From: <amazonaniruddha123@gmail.com>
                To:  <"""+to+""">
                MIME-Version: 1.0
                Content-type: text/html
                Subject: """+sub+"""
                This is an e-mail message to be sent in HTML format.
                Link of the Video: """+content_t_t+""" 
                """
            sabu_mail(to,Title_mail,msg)
            return redirect(url_for('student_video',subname=subject_p))
        else:
            return "not in post"
    else:
        return "not in session"
    return "error"

@app.route('/share-theory',methods=["GET",'POST'])
def share_theory():
    if "student_session" in session:
        if request.method=="POST":
            to = request.form["email_id_t"]
            subject_p = request.form["cur_subn"]
            sub = request.form["subject_r_t"]
            content_t_t = request.form["content_t"]
            Title_mail = session["student_session"]["email"]+" has shared a video with you..."
            msg ="""From: <amazonaniruddha123@gmail.com>
                To:  <"""+to+""">
                MIME-Version: 1.0
                Content-type: text/html
                Subject: """+sub+"""
                This is an e-mail message to be sent in HTML format.
                Link of the Video: """+content_t_t+""" 
                """
            sabu_mail(to,Title_mail,msg)
            return redirect(url_for('student_theory',subname=subject_p))
        else:
            return "not in post"
    else:
        return "not in session"
    return "error"

# ===========================FACULTY SECTION==================
# Admin login routes Starts
@app.route('/faculty-login')
def faculty_login_page_request():
    return render_template('faculty/faculty_login.html',msg="")

@app.route('/faculty-login-handle',methods=['GET','POST'])
def faculty_login_handle():
    email = request.form["email"]
    password = request.form["password"]
    ref = db.reference('/UserDB/Faculty')
    m = ref.get()
    if m != None:
        data = dict(m)
        flag=False
        for key,value in data.items():
            if(email == value["email"] and password == value["password"]):
                faculty_id = value["faculty_id"]
                phone = value["phone"]
                name_ad = value["name"]
                flag = True
                session['student_session'] = {  'name_ad':name_ad,
                                                'email':email,
                                                'faculty_id':faculty_id,
                                                'phone':phone }
                n_ref = db.reference('/LoginDB/Faculty')
                n_ref.child(email).set({
                    'email': email,
                    'faculty_id': faculty_id,
                    'Status':'Active'
                })
                return redirect(url_for('faculty_home'))   
    else:
        return render_template("faculty/faculty_login.html",msg="Unknown Error")               
    if(flag==False):
        return render_template("faculty/faculty_login.html",msg="Not Registered")  
                        
    return render_template("faculty/faculty_login.html",msg="Unknown Error")

@app.route('/logoutfaculty')
def logoutfaculty():
    # remove the username from the session if it is there
    if "student_session" in session:
        session.pop('student_session', None)
        n_ref = db.reference('/LoginDB/Faculty')
        n_ref.child(email).set({
            'email': session["student_session"]["email"],
            'faculty_id': session["student_session"]["faculty_id"],
            'Status':'Deactive'
        })
        return redirect(url_for('blank'))
    else:
        return redirect(url_for('blank'))

@app.route('/faculty-home')
def faculty_home():
    if "student_session" in session:
        malik = session["student_session"]
        info = []
        for i,j in subjects_semwise.items():
            info = j
        print(info)
        ref = db.reference('/Theory/')
        mk = ref.get()
        topics_theory_list = []
        author_theory_list = []
        date_theory_list = []
        time_theory_list = []
        UN_theory_list = []
        URL_theory_list = []
        if mk != None:
            data = dict(mk)
            for i,j in data.items():
                for k,l in j.items():
                    if(l["Faculty_Id"]==session["student_session"]["faculty_id"]):
                        topics_theory_list.append(l["Title"])
                        tref = db.reference('/UserDB/Faculty/'+l["Faculty_Id"])
                        ml = tref.get()
                        author_theory_list.append(ml["name"])
                        date_theory_list.append(l["Date"])
                        time_theory_list.append(l["Time"])
                        UN_theory_list.append(l["Unit_Name"])
                        URL_theory_list.append(l["URL"])
        ref = db.reference('/Videos/')
        mk = ref.get()
        topics_videos_list = []
        author_videos_list = []
        date_videos_list = []
        time_videos_list = []
        UN_videos_list = []
        URL_videos_list = []
        if mk != None:
            data = dict(mk)
            for i,j in data.items():
                for k,l in j.items():
                    if(l["Faculty_Id"]==session["student_session"]["faculty_id"]):
                        topics_videos_list.append(l["Title"])
                        tref = db.reference('/UserDB/Faculty/'+l["Faculty_Id"])
                        ml = tref.get()
                        author_videos_list.append(ml["name"])
                        date_videos_list.append(l["Date"])
                        time_videos_list.append(l["Time"])
                        UN_videos_list.append(l["Unit_Name"])
                        URL_videos_list.append(l["URL"])
        ref = db.reference('/UserDB/Student/')
        mk = ref.get()
        student_list_detailedA = []
        student_list_detailedB = []
        student_list_detailedC = []
        student_list_detailedD = []
        if mk != None:
            data = dict(mk)
            for i,j in data.items():
                if j["class"] == "BTech_1st_Year":
                    student_list_detailedA.append([j["name"],int(j["class_roll_no"]),j["university_roll_no"],j["section"]])
                if j["class"] == "BTech_2nd_Year":
                    student_list_detailedB.append([j["name"],int(j["class_roll_no"]),j["university_roll_no"],j["section"]])
                if j["class"] == "BTech_3rd_Year":
                    student_list_detailedC.append([j["name"],int(j["class_roll_no"]),j["university_roll_no"],j["section"]])
                if j["class"] == "BTech_4th_Year":
                    student_list_detailedD.append([j["name"],int(j["class_roll_no"]),j["university_roll_no"],j["section"]])

        sorted(student_list_detailedA,key=lambda l:l[1])
        sorted(student_list_detailedB,key=lambda l:l[1])
        sorted(student_list_detailedC,key=lambda l:l[1])
        sorted(student_list_detailedD,key=lambda l:l[1])

        print(student_list_detailedA)

        return render_template("faculty/faculty_main.html",malik=malik,topics_theory_list=topics_theory_list,
                                author_theory_list=author_theory_list,
                                date_theory_list=date_theory_list,
                                time_theory_list=time_theory_list,
                                UN_theory_list=UN_theory_list,
                                URL_theory_list=URL_theory_list,
                                topics_videos_list=topics_videos_list,
                                author_videos_list=author_videos_list,
                                date_videos_list=date_videos_list,
                                time_videos_list=time_videos_list,
                                UN_videos_list=UN_videos_list,
                                URL_videos_list=URL_videos_list,info=info,
                                student_list_detailedA=student_list_detailedA,
                                student_list_detailedB=student_list_detailedB,
                                student_list_detailedC=student_list_detailedC,
                                student_list_detailedD=student_list_detailedD)
    else:
        return redirect(url_for('faculty_login_page_request'))

@app.route('/faculty-visuals')
def faculty_visuals():
    if "student_session" in session:
        malik = session["student_session"]
        print('/Performance/BTech_3rd_Year'+"/OS")
        #ref = db.reference('/Performance/BTech_3rd_Year'+"/OS")
        #m = ref.get()
        da=[]
        dq=[]
        dc=[]
        dd=[]
        #if m != None:
        #    solutions_real = []
        #    data = dict(m)
            
        #    for i,j in data.items():
        #        u_ref = db.reference('UserDB/Student/'+i)
        #        mo = u_ref.get()
        #        section=mo["section"]

        #        if(section=="A"):
        #            da.append(j["Marks"])
        #        if(section=="B"):
        #            dq.append(j["Marks"])
        #        if(section=="C"):
        #            dc.append(j["Marks"])
        #        if(section=="D"):
        #            dd.append(j["Marks"])

        #    num_li = [kl for kl in range(1,len(da)+len(dq)+len(dc)+len(dd)+1)]
        kheerA = []
        kheerB = []
        kheerC = []
        kheerD = []
        rt = {'Aniruddha':[("Test 1","90"),("Test 2","70"),("Test 3","80")],
        'Isha':[("Test 1","20"),("Test 2","50"),("Test 3","60")]}

        for i in range(0,100):
            kheerA.append([i+1,random.randint(10,100)])
            kheerB.append([i+1,random.randint(10,100)])
            kheerC.append([i+1,random.randint(10,100)])
            kheerD.append([i+1,random.randint(10,100)])
        return render_template("faculty/faculty_visuals.html",
                                    malik=malik,
                                    das=da,
                                    dqs=dq,
                                    dcs=dc,
                                    dds=dd,
                                    kheerA=kheerA,kheerB=kheerB,
                                    kheerC=kheerC,kheerD=kheerD,rt=rt)
        #else:
        #    return render_template("admin/admin_main.html",
        #                            malik=malik,
        #                            das=da,
        #                            dbs=db,
        #                            dcs=dc,
        #                            dds=dd,
        #                            num_li=100)
    else:
        return redirect(url_for('faculty_login_page_request'))

@app.route('/faculty_intermediate/<typeurl>')
def faculty_intermediate(typeurl):
    if "student_session" in session:
        malik = session["student_session"]
        return render_template("faculty/intermediate-faculty.html",typeurl=typeurl,malik=malik)
    else:
        return redirect(url_for('faculty_login_page_request'))

@app.route('/faculty_upload-theory/<id>')
def faculty_intermediate_upload_theory(id):
    if "student_session" in session:
        malik = session["student_session"]
        return render_template("faculty/faculty_upload_theory.html",id=id,msg="not triggered",malik=malik)
    else:
        return redirect(url_for('faculty_login_page_request'))

@app.route('/faculty_upload-theory-handler',methods=['GET',"POST"])
def faculty_theory_handler():
    if "student_session" in session:
        if request.method == 'POST':
            malik = session["student_session"]
            unitname = request.form["unitname"]
            titlename = request.form["titlename"]
            subject = request.form["subject"]
            contentdata = request.form["contentdata"]
            contentdata ="""
            <!doctype html>
            <html lang="en">
            <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <!-- Bootstrap CSS -->
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
            <title>"""+titlename+"""</title>
            </head>
            <body>
            <div class="container mt-5 mb-5">
            <h2 class="text-left">"""+unitname+"""</h2>
            <h5 class="text-center">"""+titlename+"""</h5>
            <p class="text-justify"><code>"""+contentdata+"""</code></p>
            </div>
            <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous">
            </script>
            <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous">
            </script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous">
            </script>
            </body>
            </html>"""
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
                'Faculty_Id': session["student_session"]["faculty_id"],
                'Unit_Name': unitname,
            })
            return redirect(url_for('faculty_home'))
        else:
            return redirect(url_for('faculty_home'))
    else:
        return redirect(url_for('faculty_login_page_request'))

@app.route('/faculty_upload-video/<id>')
def faculty__upload_video(id):
    if "student_session" in session:
        malik = session["student_session"]
        return render_template("faculty/faculty_upload_video.html",id=id,msg="not triggered",malik=malik)
    else:
        return redirect(url_for('faculty_login_page_request'))
    
@app.route('/faculty_upload-video-handler/<message>')
def faculty_video_handler(message):
    if "student_session" in session:
        return redirect(url_for('faculty_home'))
    else:
        return redirect(url_for('faculty_login_page_request'))

@app.route('/faculty_sending_mail',methods=['GET','POST'])
def faculty_sending_mail():
    if "student_session" in session:
        if request.method == "POST":
            malik = session["student_session"]
            recieve = request.form["rcv"]
            print(recieve)
            subject = request.form["subject"]
            content = request.form["content"]
            msg ="""From: <amazonaniruddha123@gmail.com>
                To:  <"""+recieve+""">
                MIME-Version: 1.0
                Content-type: text/html
                Subject: """+subject+"""
                This is an e-mail message to be sent in HTML format.
                \n\n\n"""+content+"""
                """
            Title_mail = "You got a mail from GEU-Terminals : "
            sabu_mail(recieve,Title_mail,msg) 
            return redirect(url_for('faculty_mails'))
        else:
            return redirect(url_for('faculty_mails'))
    else:
        return redirect(url_for('faculty_login_page_request'))

@app.route('/faculty_mails')
def faculty_mails():
    if "student_session" in session:
        malik = session["student_session"]
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
                

        return render_template("faculty/faculty-mails.html",names=names,
                                                phones=phones,
                                                emails=emails,
                                                courses=courses,
                                                sections=sections,
                                                urolls=urolls,lengu=len(urolls),malik=malik)
    else:
        return redirect(url_for('faculty_login_page_request'))

@app.route('/faculty_send_mails/<mail>')
def faculty_send_per_mails(mail):
    if "student_session" in session:
        malik = session["student_session"]
        return render_template("faculty/faculty_mail.html",mail=mail,malik=malik)
    else:
        return redirect(url_for('faculty_login_page_request'))
    
@app.route('/faculty_send_mails_handler/<message>')
def faculty_send_mails_handler(message):
    if "student_session" in session:
        malik = session["student_session"]
        return redirect(url_for('faculty_home'))
    else:
        return redirect(url_for('faculty_login_page_request'))

@app.route('/faculty_opendatabase/<id>')
def faculty_opendatabase(id):
    
    if "student_session" in session:
        if(id == "studentinformationdatabase"):
            ref = db.reference('/UserDB/Student')
            data = dict(ref.get())
            return render_template("faculty/studentinformationdatabase.html",data=data)
        
        elif(id == "theorydatabase"):
            ref = db.reference('/Theory')
            data = dict(ref.get())
            return render_template("faculty/theorydatabase.html",data=data)
        
        elif(id == "videodatabase"):
            ref = db.reference('/Videos')
            data = dict(ref.get())
            return render_template("faculty/videodatabase.html",data=data)
    else:
        return "not in session"
    


@app.route('/faculty-search',methods=["GET","POST"])
def faculty_search():
    if "student_session" in session:
        if request.method == "POST":
            message = request.form["message"]
            malik = session["student_session"]
            info = []
            for i,j in subjects_semwise.items():
                info = j
            print(info)
            ref = db.reference('/Theory/')
            m = ref.get()
            topics_theory_list = []
            author_theory_list = []
            date_theory_list = []
            time_theory_list = []
            UN_theory_list = []
            URL_theory_list = []
            if(m!=None):
                data = dict(m)
                for i,j in data.items():
                    for k,l in j.items():
                        if(message.lower() in l["Title"].lower() or message.lower() in l["Unit_Name"].lower()):
                            topics_theory_list.append(l["Title"])
                            tref = db.reference('/UserDB/Faculty/'+l["Faculty_Id"])
                            ml = tref.get()
                            author_theory_list.append(ml["name"])
                            date_theory_list.append(l["Date"])
                            time_theory_list.append(l["Time"])
                            UN_theory_list.append(l["Unit_Name"])
                            URL_theory_list.append(l["URL"])

            ref = db.reference('/Video/')
            m = ref.get()
            topics_videos_list = []
            author_videos_list = []
            date_videos_list = []
            time_videos_list = []
            UN_videos_list = []
            URL_videos_list = []
            if(m!=None):
                data = dict(m)
                for i,j in data.items():
                    for k,l in j.items():
                        if(message.lower() in l["Title"].lower() or message.lower() in l["Unit_Name"].lower()):
                            topics_videos_list.append(l["Title"])
                            tref = db.reference('/UserDB/Faculty/'+l["Faculty_Id"])
                            ml = tref.get()
                            author_videos_list.append(ml["name"])
                            date_videos_list.append(l["Date"])
                            time_videos_list.append(l["Time"])
                            UN_videos_list.append(l["Unit_Name"])
                            URL_videos_list.append(l["URL"])
            
            return render_template("faculty/search.html",malik=malik,topics_theory_list=topics_theory_list,
                                    author_theory_list=author_theory_list,
                                    date_theory_list=date_theory_list,
                                    time_theory_list=time_theory_list,
                                    UN_theory_list=UN_theory_list,
                                    URL_theory_list=URL_theory_list,
                                    topics_videos_list=topics_videos_list,
                                    author_videos_list=author_videos_list,
                                    date_videos_list=date_videos_list,
                                    time_videos_list=time_videos_list,
                                    UN_videos_list=UN_videos_list,
                                    URL_videos_list=URL_videos_list,info=info)
        else:
            return "not post"
    else:
        return redirect(url_for('faculty_login_page_request'))
        
# ==========================================================

if __name__ == '__main__':
    app.run(debug=True)