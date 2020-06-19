# 6th-Semester-Mini-Project
Develop a sharing e-learning platform using cloud computing. By Aniruddha Bhattacharya

# Introduction
पाठशाला is an online e-learning platform made by Aniruddha Bhattacharya in 2020, that offers the students and the instructors come to same platform to study and teach the students well respectively. It has been designed in a way that the students of Graphic Era Deemed to be University or any university can accommodate here to get the education provided by their faculties. 

I have got the idea of making e-Learning platform by observing the need of this kind of platform during the covid-19 pandemic lockdown. The students of Government schools are unable to study and wasted 3-4 months of time in this time because they don’t have any medium to study. And even in our university I have seen the faculties had suffered a lot  of problems like for taking the tests they have to take it on HackerEarth, for submission of assignments hey have to provide separate links of google forms on Whatsapp or Gdrive etc, leaving a chance that some students might not get it.

I have made a web-based application or website which has the capability to handle this kind of problems very easily without any error and much efforts. Here in my e-Learning platform the teachers can easily post the contents whether it is Videos, Theory/Text, Post tests and the assignment links and quickly check it too as the result is made quickly and send it to the mail id of the student.

# Features
Firstly, we will land to a landing page consisting of Admin Login, Faculty Login and the Student Login and Register options.

<b>Admin</b>
  1.	Upload Theory Content
  2.	Upload Video Content
  3.	Check Visual Performances of the Students (Categorized by Sections)
  4.	Can Check the Performance databases.
  5.	Admin can add the faculty details.
  6.	Has access to all the databases and has permission to manipulate the data or the information of the student, employers, videos, and theory contents.
  7.	Can check the student lists and the Active Users (Students and the Faculties) 
  8.	Can Mail to Faculty as well as the students.
  9.	A working Search bar which can search the relevant data present in the database.
  
<b>Faculty</b>

  1.	Upload Theory Content
  2.	Upload Video Content
  3.	Check Visual Performances of the Students (Categorized by Sections)
  4.	Can Check the Performance databases.
  5.	Has access to all the databases of the student and videos/theory contents uploaded by him and other faculties. 
  6.	Can Mail to students.
  7.	Has a software to push the questions of tests directly from the system to the cloud without uploading the file to server (security reasons).
  8.	A working Search bar which can search the relevant data present in the database.
  
<b>Student</b>

  1.	Access the Videos
  2.	Access the Theory Contents and the codes.
  3.	The Video and the theory content can be shared via email and hence feature has been added to share the videos and the theory content via email.
  4.	A working Search bar which can search the relevant data present in the database.
  5.	The shortcuts to go to the contents in the dashboard and the simplified navigation.
  6.	Real time tests with 30 minutes of timer and auto submission.
  7.	Proper report and result of the test and a detailed visual of how many marks the students is receiving in each test, and how many correct, incorrect and unanswered questions are there.

# Technology stacks that I have used to make this project are as following: -
<b>
  1.	HTML5, CSS3, JAVASCRIPT, AJAX, JQUERY, JINJA.
  2.	Python3, Flask-Framework.
  3.	Firebase Database, Firebase Storage.
  4.	AWS EC2 Ubuntu AMI, Load Balancing, Apache Server, WSGI Server.
  5.	GitBash, FileZilla.
</b>

# HTML5, CSS3, JAVACRIPT, AJAX, JQUERY, JINJA
  
  <b>HTML5</b>: HTML is heavily used for creating pages that are displayed on the world wide web. Every page contains a set of HTML tags including hyperlinks which are used for connecting to other pages. Every page that we witness, on the world wide web, is written using a version of HTML code.

  <b>CSS3</b>: CSS is the language for describing the presentation of Web pages, including colors, layout, and fonts. It allows one to adapt the presentation to different types of devices, such as large screens, small screens, or printers. CSS is independent of HTML and can be used with any XML-based markup language.

  <b>JAVASCRIPT</b>: Adding interactive behavior to web pages. JavaScript allows users to interact with web pages. And used for real time data authentication during the tine of login and registration.
  
  <b>AJAX, JQUERY</b>: Adding interactive behavior to web pages.
  
  <b>JINJA</b>: A Jinja template is simply a text file. Jinja can generate any text-based format (HTML, XML, CSV, LaTeX, etc.). ... A template contains variables and/or expressions, which get replaced with values when a template is rendered; and tags, which control the logic of the template.

# Python3, Flask-Framework

  <b>Python3</b>: Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.
  
  <b>Flask-Framework</b>: Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.
  
# Firebase: 

Firebase is a mobile and web application development platform developed by Firebase, Inc. in 2011, then acquired by Google in 2014. As of March 2020, the Firebase platform has 19 products, which are used by more than 1.5 million apps.

A Cloud Based Storage and Cloud based Database is provided by Google which is free of Cost. The Firebase database resembles the AWS RDS and the Firebase Storage resembles the AWS S3 Services.

<code>
  <script>
    var firebaseConfig = {
                            apiKey: "AIzaSyDKEM_8Sy3DT_dw2BJSyqkGWcpOIZSo6Ks",
                            authDomain: "elearner-4fd02.firebaseapp.com",
                            databaseURL: "https://elearner-4fd02.firebaseio.com",
                            projectId: "elearner-4fd02",
                            storageBucket: "elearner-4fd02.appspot.com",
                            messagingSenderId: "933344165579",
                            appId: "1:933344165579:web:3f1137f53e8c971708e54e",
                            measurementId: "G-QW0SBXKZ3D"
                        };
                        
   firebase.initializeApp(firebaseConfig);
   var database = firebase.database();

   function writeUserData(downloadURL, title, subject, unitname) {
        var today = new Date();
        var dd = String(today.getDate()).padStart(2, '0');
        var months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        var mm = (months[today.getMonth()]);
        var yyyy = today.getFullYear();
        var td = mm + '-' + dd + '-' + yyyy;

        var hr = today.getHours();
        var min = today.getMinutes();
        var sec = today.getSeconds();
        if (min < 10) {
            min = "0" + min;
        }
        var time = hr + ":" + min + ":" + sec;
        firebase.database().ref('Videos/' + subject + "/" + title).set({
            Date: td,
            Time: time,
            Faculty_Id: "GEF-123456",
            Title: title,
            URL: downloadURL,
            Unit_Name: unitname,
         });
     }
     
     var leadsRef = database.ref('users');
     leadsRef.on('value', function(snapshot) {
     snapshot.forEach(function(childSnapshot) {
     var childData = childSnapshot.val();
     console.log(childData.username);
     });
  });
  </script>
  </code>
# AWS EC2, Load Balancing

  <b>Amazon EC2</b>: Secure and resizable compute capacity in the cloud. Launch applications when needed without upfront commitments. Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers. Amazon EC2’s simple web service interface allows you to obtain and configure capacity with minimal friction. It provides you with complete control of your computing resources and lets you run on Amazon’s proven computing environment.

  <b>Load Balancing</b>: Elastic Load Balancing automatically distributes incoming application traffic across multiple targets, such as Amazon EC2 instances, containers, IP addresses, and Lambda functions. It can handle the varying load of your application traffic in a single Availability Zone or across multiple Availability Zones. Elastic Load Balancing offers three types of load balancers that all feature the high availability, automatic scaling, and robust security necessary to make your applications fault tolerant.

# Apache Web Server
  The Apache HTTP Server Project is an effort to develop and maintain an open-source HTTP server for modern operating systems including UNIX and Windows. The goal of this project is to provide a secure, efficient and extensible server that provides HTTP services in sync with the current HTTP standards.

# WSGI Server
  The Web Server Gateway Interface is a simple calling convention for web servers to forward requests to web applications or frameworks written in the Python programming language. The current version of WSGI, version 1.0.1, is specified in Python Enhancement Proposal 3333.
  
# GitBash and Git
  Git is a set of command line utility programs that are designed to execute on a Unix style command-line environment. Modern operating systems like Linux and macOS both include built-in Unix command line terminals. This makes Linux and macOS complementary operating systems when working with Git. Microsoft Windows instead uses Windows command prompt, a non-Unix terminal environment.
# FileZilla
  FileZilla is a free software, cross-platform FTP application, consisting of FileZilla Client and FileZilla Server. Client binaries are available for Windows, Linux, and macOS, server binaries are available for Windows only. Simply it is used to establish a FTP connection to our AMI.
