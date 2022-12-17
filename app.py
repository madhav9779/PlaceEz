from flask import Flask, render_template, request, session, url_for, redirect,flash
# from logging import exception
from werkzeug.utils import secure_filename
import pymysql  
import os
from datetime import date, datetime
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import os
from flask_mail import Mail
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
from logging import DEBUG

app = Flask(__name__)
app.logger.setLevel(DEBUG)

global final_labels

UPLOAD_FOLDER = 'static/upload/'
UPLOAD_FOLDER1 = 'static/company_img/'
UPLOAD_FOLDER2 = 'static/logo/'
UPLOAD_FOLDER3 = 'static/upload_resume/'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER1'] = UPLOAD_FOLDER1
app.config['UPLOAD_FOLDER2'] = UPLOAD_FOLDER2
app.config['UPLOAD_FOLDER3'] = UPLOAD_FOLDER3
app.secret_key = 'random string'

def dbConnection():
    try:
        connection = pymysql.connect(
            host="localhost", user="root", password="root", database="003placement", charset="utf8")
        return connection
    except:
        print("Something went wrong in database Connection")


def dbClose():
    try:
        dbConnection().close()
    except:
        print("Something went wrong in Close DB Connection")
        
dbConnection()
################################################################################################################################
#                                           Deadline Notification
################################################################################################################################
def DeadlineMail(studentMail,cmpName,JobTitle,JobType,RemainDays):   
    fromaddr = "madhavbansal9779@gmail.com"
    toaddr = studentMail
   
    #instance of MIMEMultipart 
    msg = MIMEMultipart() 
  
    # storing the senders email address   
    msg['From'] = fromaddr 
  
    # storing the receivers email address  
    msg['To'] = toaddr 
  
    # storing the subject  
    msg['Subject'] = "Last "+ str(RemainDays)+" days to apply for job"
  
    # string to store the body of the mail 
    body = "Hello! students, Posted job deadlie is near don't miss your dream jobs,Please login and check all the details \n\nNote: that after deadline you can't apply for this jobs \n\nCompany Name: "+str(cmpName)+" \nJob Profile: "+str(JobTitle)+" \nDeadline: "+str(JobType)
  
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
  
    # open the file to be sent  
    # filename = filetosend
    # attachment = open(filetosend, "rb") 
  
    # # instance of MIMEBase and named as p 
    # p = MIMEBase('application', 'octet-stream') 
  
    # # To change the payload into encoded form 
    # p.set_payload((attachment).read()) 
  
    # # encode into base64 
    # encoders.encode_base64(p) 
   
    # p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
    # # attach the instance 'p' to instance 'msg' 
    # msg.attach(p) 
  
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
  
    # start TLS for security 
    s.starttls() 
  
    # Authentication 
    s.login(fromaddr, "jpvsfigjbcnagvir") 
  
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
  
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
  
    # terminating the session 
    s.quit() 
   


def deadlineNotif():
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute("select companyName,jobTitle,jobType,datediff(ApplicationDeadline, curdate()) as days_remaining from jobinfo;")
    res = cursor.fetchall()

    cursor.execute("select email from userdetails;")
    res2 = cursor.fetchall()



    companyName = [i[0] for i in res]
    jobTitle = [i[1] for i in res]
    jobType = [i[2] for i in res]
    days_remaining = [i[3] for i in res]
    studentMail = [i[0] for i in res2]

    # print(companyName,jobTitle, jobType, days_remaining)
    allData = zip(studentMail,companyName,jobTitle, jobType, days_remaining)

    for studentMail,cmpName,JobTitle,JobType,RemainDays in allData:
        if RemainDays==3:
            DeadlineMail(studentMail,cmpName,JobTitle,JobType,RemainDays)

# deadlineNotif()
################################################################################################################################
#                                           After Deadline job gets deleted
################################################################################################################################
def deadline2(branch):
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute("select companyName,Salary,jobTitle,jobType,datediff(ApplicationDeadline, curdate()) as days_remaining,logo,jobLoc,OtherBenifits,jobId from jobinfo where branches=%s;",(branch))
    res = cursor.fetchall()

    companyName = [i[0] for i in res]
    Salary = [i[1] for i in res]
    jobTitle = [i[2] for i in res]
    jobType = [i[3] for i in res]
    days_remaining = [i[4] for i in res]
    logo = [i[5] for i in res]
    jobLoc = [i[6] for i in res]
    OtherBenifits = [i[7] for i in res]
    jobid = [i[8] for i in res]

    # print(companyName,jobTitle, jobType, days_remaining)
    allData = zip(companyName,Salary,jobTitle, jobType,logo,jobLoc,OtherBenifits,jobid,days_remaining)

    for companyName,Salary,jobTitle, jobType,logo,jobLoc,OtherBenifits,jobId,RemainDays in allData:
        if int(RemainDays)<=0:
            print()
            print("jobid")
            print(jobId)
            print(type(jobId))
            sql1 = "INSERT INTO deadline_over SELECT * FROM jobinfo WHERE jobId = %s;"
            val1 = (int(jobId))
            cursor.execute(sql1,val1)

            sql2 = "DELETE from jobinfo where jobId=%s;"
            val2 = (int(jobId))
            cursor.execute(sql2,val2)
            con.commit()

    cursor.execute("select companyName,Salary,jobTitle,jobType,logo,jobLoc,OtherBenifits,jobId from deadline_over where branches=%s;",(branch))
    res2 = cursor.fetchall()

    companyName = [i[0] for i in res2]
    Salary = [i[1] for i in res2]
    jobTitle = [i[2] for i in res2]
    jobType = [i[3] for i in res2]
    logo = [i[4] for i in res2]
    jobLoc = [i[5] for i in res2]
    OtherBenifits = [i[6] for i in res2]
    jobid = [i[7] for i in res2]

    finalData = zip(companyName,Salary,jobTitle, jobType,logo,jobLoc,OtherBenifits)
    return finalData

# deadlineNotif()
################################################################################################################################
#                                           Student login page
################################################################################################################################
@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try:
            # session.pop('user', None)
            studEmail = request.form.get("email")
            studpass = request.form.get("pass")
            studrole = request.form.get("role")

            print(studEmail, studpass, studrole)
            con = dbConnection()
            cursor = con.cursor()
            res_count = cursor.execute('SELECT * FROM userdetails WHERE email = %s AND pass = %s AND Department = %s', (studEmail, studpass, studrole))
            result = cursor.fetchone()
            print(res_count)
            if res_count>0:
                session['user'] = result[1]
                session['userlname'] = result[2]
                session['userid'] = result[0]
                session['email'] = studEmail
                session['branch'] = studrole
                print("hii in if")
                return redirect(url_for('index'))
            else:
                print("hii in else")
                msg = "Sorry, your Email/Password/Department was incorrect. Please double-check your Email/Password/Department."
                msg2 = "error"
                return render_template('login.html',msg=msg,msg2=msg2)
        except Exception as e:
            print(e)
            print("Exception occured at login")
            return render_template('login.html')
        finally:
            dbClose()
    return render_template('login.html')
################################################################################################################################
#                                           Student login page
################################################################################################################################
@app.route('/forget', methods=["GET", "POST"])
def forget():
    return render_template('forget.html')

################################################################################################################################
#                                           Placement Head login page
################################################################################################################################
@app.route('/head_login', methods=["GET", "POST"])
def head_login():
    msg = ''
    if request.method == "POST":
        try:
            session.pop('user', None)
            print(request.form)
            headEmail = request.form.get("email")
            password = request.form.get("pass")
            role = request.form.get("role")

            print(headEmail, password,role)
            con = dbConnection()
            cursor = con.cursor()
            cursor.execute('SELECT * FROM company WHERE email = %s AND pass = %s AND role=%s', (headEmail, password,role))
            result = cursor.fetchone()
            print(result)
            if result:
                session['user'] = result[1]
                session['userlname'] = result[2]
                session['userid'] = result[0]
                session['email'] = headEmail
                session['branch'] = role
                return redirect(url_for('cmpindex'))
            else:
                return render_template('head_login1.html')
        except Exception as e:
            print(e)
            print("Exception occured at login")
            return render_template('head_login1.html')
        finally:
            dbClose()
    # return redirect(url_for('index'))
    return render_template('head_login1.html')
################################################################################################################################
#                                           Logout
################################################################################################################################
@app.route('/logout')
def logout():
    session.pop('user')
    session.pop('userlname')
    session.pop('userid')
    session.pop('email')
    session.pop('branch')
    return redirect(url_for('login'))

@app.route('/logout2')
def logout2():
    session.pop('user')
    session.pop('userlname')
    session.pop('userid')
    session.pop('email')
    session.pop('branch')
    return redirect(url_for('head_login'))
################################################################################################################################
#                                           User home page
################################################################################################################################
@app.route('/index', methods=["GET", "POST"])
def index():
    print("hii before session")
    # if 'user' in session:
    print("hii after session")
    branch = session.get("branch")
    print("branch")
    print(branch)
    con = dbConnection()
    cursor = con.cursor()
    
    deadlineover = deadline2(branch)

    cursor.execute("select companyName,Salary,jobTitle,jobType,logo,jobLoc,OtherBenifits from jobinfo where branches=%s",(branch))
    res = cursor.fetchall()
    res = list(res)
    print(res)

    print()
    print("res")
    print(res)

    deadlinecompanyName = []
    deadlinesalary = []
    deadlinejobTitle = []
    deadlinejobType = []
    deadlinejoblogo = []
    deadlinejobloc = []
    deadlinejobperks = []

    for companyName,Salary,jobTitle, jobType,logo,jobLoc,OtherBenifits in deadlineover:
        # print()
        # print("companyName")
        # print(companyName)
        deadlinecompanyName.append(companyName)
        deadlinesalary.append(Salary)
        deadlinejobTitle.append(jobTitle)
        deadlinejobType.append(jobType)
        deadlinejoblogo.append(logo)
        deadlinejobloc.append(jobLoc)
        deadlinejobperks.append(OtherBenifits)
        for i in res:
            if companyName == i[1]:
                res.remove(i)


    companyName = [i[0] for i in res]
    salary = [i[1] for i in res]
    jobTitle = [i[2] for i in res]
    jobType = [i[3] for i in res]
    logo = [i[4] for i in res]
    jobLoc = [i[5] for i in res]
    jobperks = [i[6] for i in res]

    lst = zip(companyName,salary,jobTitle,jobType,logo,jobLoc,jobperks)
    # print(deadlinecompanyName,deadlinejobTitle,deadlinejobType,logo)
    deadlineovr = zip(deadlinecompanyName,deadlinesalary,deadlinejobTitle,deadlinejobType,deadlinejoblogo,deadlinejobloc,deadlinejobperks)
    return render_template('index.html', lst=lst,deadlineovr=deadlineovr)
    # return render_template('login.html')
################################################################################################################################
#                                           Company home page
################################################################################################################################
@app.route('/cmpindex')
def cmpindex():
    uname = session.get('user')
    headBranch = session.get('branch')
    con = dbConnection()
    cursor = con.cursor()

    deadlineover = deadline2(headBranch)

    cursor.execute("select companyName,Salary,jobTitle,jobType,logo,jobLoc,OtherBenifits from jobinfo where branches=%s",(headBranch))
    res = cursor.fetchall()
    res = list(res)
    print(res)

    deadlinecompanyName = []
    deadlinesalary = []
    deadlinejobTitle = []
    deadlinejobType = []
    deadlinejoblogo = []
    deadlinejobloc = []
    deadlinejobperks = []

    for companyname,Salary,jobtitle, jobtype,cmplogo,jobloc,OtherBenifits in deadlineover:
        # print()
        # print("companyName")
        # print(companyName)
        deadlinecompanyName.append(companyname)
        deadlinesalary.append(Salary)
        deadlinejobTitle.append(jobtitle)
        deadlinejobType.append(jobtype)
        deadlinejoblogo.append(cmplogo)
        deadlinejobloc.append(jobloc)
        deadlinejobperks.append(OtherBenifits)
        for i in res:
            if companyname == i[1]:
                res.remove(i)

    companyName = [i[0] for i in res]
    salary = [i[1] for i in res]
    jobTitle = [i[2] for i in res]
    jobType = [i[3] for i in res]
    logo = [i[4] for i in res]
    jobLoc = [i[5] for i in res]
    jobperks = [i[6] for i in res]

    lst = zip(companyName,salary,jobTitle,jobType,logo,jobLoc,jobperks)

    deadlineovr = zip(deadlinecompanyName,deadlinesalary,deadlinejobTitle,deadlinejobType,deadlinejoblogo,deadlinejobloc,deadlinejobperks)
    return render_template('cmpindex.html', lst=lst,deadlineovr=deadlineovr)
################################################################################################################################
#                                           admin view job description page
################################################################################################################################
@app.route('/singlejob')
def singlejob():
    cmpname = request.args.get('cmp_name')
    jbTitle = request.args.get('jbTitle')
    print(cmpname)

    if cmpname == None:
        cmpname=session.get('cmpname')

    con = dbConnection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM jobinfo WHERE companyName=%s AND jobTitle=%s", (cmpname,jbTitle))
    res = cursor.fetchall()
    res = list(res)
    companyName = [i[1] for i in res]
    logo = [i[2] for i in res]
    jobTitle = [i[3] for i in res]
    jobLoc = [i[4] for i in res]
    jobType = [i[5] for i in res]
    publishedOn = [i[6] for i in res]
    salary = [i[7] for i in res]
    applicationDeadline = [i[8] for i in res]
    branch = [i[14] for i in res]
    studInfo1 = [i[15] for i in res]
    JobDescription = ""
    Responsibilities = ""
    Education_Experience = ""
    OtherBenifits = ""
    jobdesc1 = ""
    jobdesc2 = ""
    jobdesc3 = ""
    jobdesc4 = ""
    jobdesc5 = ""
    jobques1 = ""
    jobques2 = ""
    jobques3 = ""
    jobques4 = ""
    jobques5 = ""

    for i in res:
        JobDescription += i[9]

        Responsibilities += i[10]

        Education_Experience += i[11]

        OtherBenifits += i[12]

        jobdesc1 += i[16]
        jobdesc2 += i[17]
        jobdesc3 += i[18]
        jobdesc4 += i[19]
        jobdesc5 += i[20]
        jobques1 += i[21]
        jobques2 += i[22]
        jobques3 += i[23]
        jobques4 += i[24]
        jobques5 += i[25]


    print()
    print("studInfo")
    print(studInfo1)

    labledict = {"fname":"First Name"," fname":"First Name","lname":"Last Name"," lname":"Last Name","fathername":"Father Name","mothername":"Mother Name",
                "curntLoc":"Current Location","Hometwn":"HomeTown","Hometown":"HomeTown",
                "certif":"Certificates","cgpa":"Current CGPA","cgpa7":"Current CGPA","clgname":"Collage Name","rolno":"Roll No.","pEmail":"Personal Email",
                "phnno":"Phone No.","brnch":"Branch","degre":"Degree","percent10":"10th Percentage",
                "percent12":"12th Percentage","actbacklog":"Active Backlog"}

    
    studInfo = []
    for i in studInfo1:
        a = i.replace("'","")
        a = a.replace("[","")
        a = a.replace("]","")
        asdf = a.split(",")
        studInfo.append(asdf)
    
    inp_lables = []
    for i in studInfo[0]:
        a = i.replace(" ","")
        print()
        print("printing a")
        print(a)
        print()
        a = labledict[a]
        inp_lables.append(a)

    OtherBenifits = OtherBenifits.split("|")
    JobDescription = JobDescription.split("|")
    Responsibilities = Responsibilities.split("|")
    Education_Experience = Education_Experience.split("|")
    
    jobdesc1 = jobdesc1.split("|")
    jobdesc2 = jobdesc2.split("|")
    jobdesc3 = jobdesc3.split("|")
    jobdesc4 = jobdesc4.split("|")
    jobdesc5 = jobdesc5.split("|")
    jobques1 = jobques1.split("|")
    jobques2 = jobques2.split("|")
    jobques3 = jobques3.split("|")
    jobques4 = jobques4.split("|")
    jobques5 = jobques5.split("|")

    print(OtherBenifits)
    print()
    print(JobDescription)
    print()
    print(Responsibilities)
    print()
    print(Education_Experience)


    usrname = session.get('user')
    userlname = session.get('userlname')
    usrbranch = session.get('branch')
    usrmail = session.get('email')

    
    
    # cursor.execute("SELECT status FROM applycmp WHERE fname=%s and lname=%s", (usrname,userlname))
    # res2 = list(cursor.fetchone())
    # print()
    # print("len res2")
    # print(len(res2))
    # print(studInfo)

    # if len(res2)==0:
    #     res2 = ["not selected"]
    # else:
    #     res2 = list(res2[0])

    # final_studinfo = []
    # for i in studInfo[0]:
    #     # print()
    #     # print("printing i")
    #     # print(i)
    #     # print()
    #     cursor.execute("select "+i+" from studentinfo where fname=%s AND cEmail=%s AND brnch=%s;",(usrname,usrmail,usrbranch))
    #     res = list(cursor.fetchall())
    #     print(res)
    #     final_studinfo.append(res[0][0])

    print()
    print("studInfo")
    print(studInfo[0])
    print()
    print(jobdesc1,jobdesc2,jobdesc3,jobdesc4,jobdesc5)
    print(jobques1,jobques2,jobques3,jobques4,jobques5)

    lst = zip(companyName, logo, jobTitle, jobLoc, jobType, publishedOn,
              salary, applicationDeadline, JobDescription, Responsibilities, Education_Experience, OtherBenifits,
              jobdesc1,jobdesc2,jobdesc3,jobdesc4,jobdesc5,jobques1,jobques2,jobques3,jobques4,jobques5)

    lst2 = zip(logo,jobTitle,companyName,jobLoc,jobType)

    return render_template('cmp_view.html', lst=lst,studInfo=inp_lables)
################################################################################################################################
#                                           admin view job description page
################################################################################################################################
@app.route('/studsinglejob')
def studsinglejob():
    global final_labels

    cmpname = request.args.get('cmp_name')
    jbTitle = request.args.get('jbTitle')
    print("cmpname, jbTitle")
    print(cmpname, jbTitle)

    if cmpname == None:
        cmpname=session.get('cmpname')

    con = dbConnection()
    cursor = con.cursor()
    sql = "SELECT * FROM jobinfo WHERE companyName=%s AND jobTitle=%s"
    val = (cmpname,jbTitle)
    cursor.execute(sql,val)
    res = cursor.fetchall()
    res = list(res)
    companyName = [i[1] for i in res]
    logo = [i[2] for i in res]
    jobTitle = [i[3] for i in res]
    jobLoc = [i[4] for i in res]
    jobType = [i[5] for i in res]
    publishedOn = [i[6] for i in res]
    salary = [i[7] for i in res]
    applicationDeadline = [i[8] for i in res]
    branch = [i[14] for i in res]
    studInfo1 = [i[15] for i in res]
    JobDescription = ""
    Responsibilities = ""
    Education_Experience = ""
    OtherBenifits = ""
    jobdesc1 = ""
    jobdesc2 = ""
    jobdesc3 = ""
    jobdesc4 = ""
    jobdesc5 = ""
    jobques1 = ""
    jobques2 = ""
    jobques3 = ""
    jobques4 = ""
    jobques5 = ""

    print()
    print("studInfo")
    print(studInfo1)
    
    studInfo = []
    for i in studInfo1:
        a = i.replace("'","")
        a = a.replace("[","")
        a = a.replace("]","")
        asdf = a.split(",")
        studInfo.append(asdf)

    for i in res:
        JobDescription += i[9]

        Responsibilities += i[10]

        Education_Experience += i[11]

        OtherBenifits += i[12]

        jobdesc1 += i[16]
        jobdesc2 += i[17]
        jobdesc3 += i[18]
        jobdesc4 += i[19]
        jobdesc5 += i[20]
        jobques1 += i[21]
        jobques2 += i[22]
        jobques3 += i[23]
        jobques4 += i[24]
        jobques5 += i[25]
    

    OtherBenifits = OtherBenifits.split("|")
    JobDescription = JobDescription.split("|")
    Responsibilities = Responsibilities.split("|")
    Education_Experience = Education_Experience.split("|")
    
    jobdesc1 = jobdesc1.split("|")
    jobdesc2 = jobdesc2.split("|")
    jobdesc3 = jobdesc3.split("|")
    jobdesc4 = jobdesc4.split("|")
    jobdesc5 = jobdesc5.split("|")
    jobques1 = jobques1.split("|")
    jobques2 = jobques2.split("|")
    jobques3 = jobques3.split("|")
    jobques4 = jobques4.split("|")
    jobques5 = jobques5.split("|")

    print(OtherBenifits)
    print()
    print(JobDescription)
    print()
    print(Responsibilities)
    print()
    print(Education_Experience)


    usrname = session.get('user')
    userlname = session.get('userlname')
    usrbranch = session.get('branch')
    usrmail = session.get('email')

    
    
    res_count = cursor.execute("SELECT status FROM applycmp WHERE fname=%s and lname=%s", (usrname,userlname))

    if res_count==0:
        res2 = ["not selected"]
    else:
        res2 = list(cursor.fetchone())
        print()
        print("len res2")
        print(len(res2))
        print(res2)
        res2 = list(res2[0])

    labledict = {"fname":"First Name"," fname":"First Name","lname":"Last Name"," lname":"Last Name","fathername":"Father Name","mothername":"Mother Name",
                "curntLoc":"Current Location","Hometwn":"HomeTown","Hometown":"HomeTown",
                "certif":"Certificates","cgpa":"Current CGPA","cgpa7":"Current CGPA","clgname":"Collage Name","rolno":"Roll No.","pEmail":"Personal Email",
                "phnno":"Phone No.","brnch":"Branch","degre":"Degree","percent10":"10th Percentage",
                "percent12":"12th Percentage","actbacklog":"Active Backlog"}

    print()
    print("usrname,usrmail,usrbranch")
    print(usrname,usrmail,usrbranch)
    print(studInfo)
    final_studinfo = []
    final_labels = []
    for i in studInfo[0]:
        print(i)
        cursor.execute("select "+i+" from studentinfo where fname=%s AND cEmail=%s AND brnch=%s;",(usrname,usrmail,usrbranch))
        res = list(cursor.fetchone())
        print()
        print("final_studinfo")
        print(res)
        print()
        # final_studinfo.append(res[0][0])
        final_studinfo.append(res[0])
        a = i.replace(" ","")
        final_labels.append(labledict[a])

    print()
    print("final_studinfo")
    print(final_studinfo)
    print(type(final_studinfo))
    print(studInfo)

    lst = zip(companyName, logo, jobTitle, jobLoc, jobType, publishedOn,
              salary, applicationDeadline, JobDescription, Responsibilities, Education_Experience, OtherBenifits,
              jobdesc1,jobdesc2,jobdesc3,jobdesc4,jobdesc5,jobques1,jobques2,jobques3,jobques4,jobques5)

    lst2 = zip(logo,jobTitle,companyName,jobLoc,jobType)

    formfields = zip(final_labels,final_studinfo)
    return render_template('stud_view.html', lst=lst,lst2=lst2,formfields=formfields,res2=res2)
################################################################################################################################
#                                           View applied jobs
################################################################################################################################
@app.route('/historyjob')
def historyjob():
    global final_labels

    cmpname = request.args.get('cmp_name')
    jbTitle = request.args.get('jbTitle')
    print("cmpname, jbTitle")
    print(cmpname, jbTitle)

    if cmpname == None:
        cmpname=session.get('cmpname')

    con = dbConnection()
    cursor = con.cursor()
    sql = "SELECT * FROM jobinfo WHERE companyName=%s AND jobTitle=%s"
    val = (cmpname,jbTitle)
    cursor.execute(sql,val)
    res = cursor.fetchall()
    res = list(res)
    companyName = [i[1] for i in res]
    logo = [i[2] for i in res]
    jobTitle = [i[3] for i in res]
    jobLoc = [i[4] for i in res]
    jobType = [i[5] for i in res]
    publishedOn = [i[6] for i in res]
    salary = [i[7] for i in res]
    applicationDeadline = [i[8] for i in res]
    branch = [i[14] for i in res]
    studInfo1 = [i[15] for i in res]
    JobDescription = ""
    Responsibilities = ""
    Education_Experience = ""
    OtherBenifits = ""
    jobdesc1 = ""
    jobdesc2 = ""
    jobdesc3 = ""
    jobdesc4 = ""
    jobdesc5 = ""
    jobques1 = ""
    jobques2 = ""
    jobques3 = ""
    jobques4 = ""
    jobques5 = ""

    print()
    print("studInfo")
    print(studInfo1)
    
    studInfo = []
    for i in studInfo1:
        a = i.replace("'","")
        a = a.replace("[","")
        a = a.replace("]","")
        asdf = a.split(",")
        studInfo.append(asdf)

    for i in res:
        JobDescription += i[9]

        Responsibilities += i[10]

        Education_Experience += i[11]

        OtherBenifits += i[12]

        jobdesc1 += i[16]
        jobdesc2 += i[17]
        jobdesc3 += i[18]
        jobdesc4 += i[19]
        jobdesc5 += i[20]
        jobques1 += i[21]
        jobques2 += i[22]
        jobques3 += i[23]
        jobques4 += i[24]
        jobques5 += i[25]
    

    OtherBenifits = OtherBenifits.split("|")
    JobDescription = JobDescription.split("|")
    Responsibilities = Responsibilities.split("|")
    Education_Experience = Education_Experience.split("|")
    
    jobdesc1 = jobdesc1.split("|")
    jobdesc2 = jobdesc2.split("|")
    jobdesc3 = jobdesc3.split("|")
    jobdesc4 = jobdesc4.split("|")
    jobdesc5 = jobdesc5.split("|")
    jobques1 = jobques1.split("|")
    jobques2 = jobques2.split("|")
    jobques3 = jobques3.split("|")
    jobques4 = jobques4.split("|")
    jobques5 = jobques5.split("|")

    print(OtherBenifits)
    print()
    print(JobDescription)
    print()
    print(Responsibilities)
    print()
    print(Education_Experience)


    usrname = session.get('user')
    userlname = session.get('userlname')
    usrbranch = session.get('branch')
    usrmail = session.get('email')

    
    
    res_count = cursor.execute("SELECT status FROM applycmp WHERE fname=%s and lname=%s", (usrname,userlname))

    if res_count==0:
        res2 = ["not selected"]
    else:
        res2 = list(cursor.fetchone())
        print()
        print("len res2")
        print(len(res2))
        print(res2)
        res2 = list(res2[0])

    labledict = {"fname":"First Name"," fname":"First Name","lname":"Last Name"," lname":"Last Name","fathername":"Father Name","mothername":"Mother Name",
                "curntLoc":"Current Location","Hometwn":"HomeTown","Hometown":"HomeTown",
                "certif":"Certificates","cgpa":"Current CGPA","cgpa7":"Current CGPA","clgname":"Collage Name","rolno":"Roll No.","pEmail":"Personal Email",
                "phnno":"Phone No.","brnch":"Branch","degre":"Degree","percent10":"10th Percentage",
                "percent12":"12th Percentage","actbacklog":"Active Backlog"}

    print()
    print("usrname,usrmail,usrbranch")
    print(usrname,usrmail,usrbranch)
    print(studInfo)
    final_studinfo = []
    final_labels = []
    for i in studInfo[0]:
        print(i)
        cursor.execute("select "+i+" from studentinfo where fname=%s AND cEmail=%s AND brnch=%s;",(usrname,usrmail,usrbranch))
        res = list(cursor.fetchone())
        print()
        print("final_studinfo")
        print(res)
        print()
        # final_studinfo.append(res[0][0])
        final_studinfo.append(res[0])
        a = i.replace(" ","")
        final_labels.append(labledict[a])

    print()
    print("final_studinfo")
    print(final_studinfo)
    print(type(final_studinfo))
    print(studInfo)

    lst = zip(companyName, logo, jobTitle, jobLoc, jobType, publishedOn,
              salary, applicationDeadline, JobDescription, Responsibilities, Education_Experience, OtherBenifits,
              jobdesc1,jobdesc2,jobdesc3,jobdesc4,jobdesc5,jobques1,jobques2,jobques3,jobques4,jobques5)

    lst2 = zip(logo,jobTitle,companyName,jobLoc,jobType)

    formfields = zip(final_labels,final_studinfo)
    return render_template('stud_viewhistory.html', lst=lst,lst2=lst2,formfields=formfields,res2=res2)

################################################################################################################################
#                                           Apply to job
################################################################################################################################
@app.route('/applyjob',methods=["GET","POST"])
def applyjob():
    global final_labels
    if 'user' in session:
        if request.method=="POST":
            
            studinfo = []
            for i in final_labels:
                aplyinfo = request.form.get(i)
                studinfo.append(aplyinfo)
            
            jobques1 = request.form.get("ques1")
            jobques2 = request.form.get("ques2")
            jobques3 = request.form.get("ques3")
            jobques4 = request.form.get("ques4")
            jobques5 = request.form.get("ques5")
            
            aplycompanyName = request.form.get("companyName")
            aplyjobTitle = request.form.get("jobTitle")
            resumfile = request.files["stud_resume"]

            resume_filename = secure_filename(resumfile.filename)
            resumfile.save(os.path.join(app.config['UPLOAD_FOLDER2'], resume_filename))

            resumefile_path = "static/upload_resume/"+resume_filename

            print()
            print("student info")
            print(studinfo)
            print()
            print("resume file path")
            print(resumefile_path,aplycompanyName,aplyjobTitle)
            print()
            print("questions")
            print(jobques1,type(jobques2),type(jobques3),jobques4,jobques5)
            print()

            conn = dbConnection()
            cur = conn.cursor()

            fname = session.get("user")
            lname = session.get("userlname")


            # studinfo.remove(fname)
            # studinfo.remove(lname)
            status = "applied"
            catlst = ['catt1','catt2','catt3','catt4','catt5','catt6','catt7','catt8','catt9']
            for i in range(len(catlst)):
            #     print(i)
                if len(studinfo)!=len(catlst):
                    studinfo.append("Unavailable")
                else:
                    c = catlst

            cat1 = "Unavailable"
            cat2 = "Unavailable"
            cat3 = "Unavailable"
            cat4 = "Unavailable"
            cat5 = "Unavailable"
            cat6 = "Unavailable"
            cat7 = "Unavailable"
            cat8 = "Unavailable"
            cat9 = "Unavailable"

            if jobques1 is None or jobques1=='':
                jobques1 = "Not needed"
            if jobques2 is None or jobques2=='':
                jobques2 = "Not needed"
            if jobques3 is None or jobques3=='':
                jobques3 = "Not needed"
            if jobques4 is None or jobques4=='':
                jobques4 = "Not needed"
            if jobques5 is None or jobques5=='':
                jobques5 = "Not needed"


            sql1 = "insert into applycmp (cmpName,Jobtitle,resume,fname,lname,cat1,cat2,cat3,cat4,cat5,cat6,cat7,cat8,cat9,ques1,ques2,ques3,ques4,ques5,status) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            val1 = (aplycompanyName,aplyjobTitle,str(resumefile_path),fname,lname,cat1,cat2,cat3,cat4,cat5,cat6,cat7,cat8,cat9,jobques1,jobques2,jobques3,jobques4,jobques5,status)
            cur.execute(sql1,val1)
            conn.commit()
            
            sql2 = "update applycmp SET cat1=%s ,cat2=%s,cat3=%s,cat4=%s,cat5=%s,cat6=%s,cat7=%s,cat8=%s,cat9=%s where cmpName=%s AND Jobtitle=%s AND resume=%s AND fname=%s AND lname=%s AND status=%s;"
            val2 = (str(studinfo[0]),str(studinfo[1]),str(studinfo[2]),str(studinfo[3]),str(studinfo[4]),str(studinfo[5]),str(studinfo[6]),str(studinfo[7]),str(studinfo[8]),aplycompanyName,aplyjobTitle,str(resumefile_path),fname,lname,status)
            cur.execute(sql2,val2)
            conn.commit()

            # msg = "Congratulations! you have successfully applied to this profile."
            # flash(msg)
            session['cmpname']=aplycompanyName
            # return redirect(url_for("index"))
            return "success"
        return render_template('stud_view.html')
    return render_template('login.html')
################################################################################################################################
#                                           Display Selected Students
################################################################################################################################
@app.route('/placed')
def placed():
    if 'user' in session:
        con = dbConnection()
        cursor = con.cursor()
        cursor.execute("SELECT applyId,fname, lname, cmpName, Jobtitle FROM applycmp where status='Selected';")
        res = cursor.fetchall()
        res = list(res)
        print(res)

        Id = [i[0] for i in res]
        fname = [i[1] for i in res]
        lname = [i[2] for i in res]
        cmpname = [i[3] for i in res]
        jobprof = [i[4] for i in res]

        lst = zip(Id,fname, lname,  cmpname, jobprof)
        return render_template('selectionResult.html', lst=lst)
    return render_template('login.html')
################################################################################################################################
#                                           Display Selected Students
################################################################################################################################
@app.route('/cmpplaced', methods=["GET", "POST"])
def cmpplaced():
    if 'user' in session:
        con = dbConnection()
        cursor = con.cursor()
        headbranch = session.get("branch")

        cursor.execute("SELECT companyName FROM jobinfo where branches=%s;",(headbranch))
        result = cursor.fetchall()
        res = list(result)
        
        allcmps = [i[0] for i in res]
        print("res")
        print(allcmps)
        # shdbfhfb



        if request.method=="POST":
            cmpname = request.form.get("cmpName")
            cursor.execute("SELECT * FROM applycmp where cmpName=%s and status='Selected';",(cmpname))
            # res = cursor.fetchall()
            # res = list(res)
            # print("res")
            # print(res)

            columns = cursor.description 
            result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
            print("result of Newly Launched",result)
            df = pd.DataFrame.from_dict(result)
            print()
            print("dataframe")
            print(df)
            df = df.drop(columns=df.columns[(df == 'Unavailable').any()])
            # dff = df.drop(columns=df.columns[(df == '').any()])
            dff = df.drop(columns=df.columns[(df == 'Not needed').any()])
            
            dfcolumns = list(dff)
            print("dfcolumns")
            print(dfcolumns)
            print(dff.values.tolist())
            if 'resume' in dfcolumns:
                dff = dff.drop(['resume'], axis=1)

            dff.to_csv("static/company_img/Selected_student_information.csv")

            lst2=dff.values.tolist()
            lst = zip(dfcolumns,lst2)


            # Id = [i[0] for i in res]
            # fname = [i[1] for i in res]
            # lname = [i[2] for i in res]
            # email = [i[3] for i in res]
            # cmpname = [i[4] for i in res]
            # jobprof = [i[5] for i in res]

            # lst = zip(Id,fname, lname, email, cmpname, jobprof)
            return render_template('cmp_result.html', tables=[dff.to_html(header="true", classes='table table-stripped')], titles=dff.columns.values)
        return render_template('cmp_result1.html',allcmps=allcmps)
    return render_template('login.html')
################################################################################################################################
#                                           Update information
################################################################################################################################
@app.route('/updateinfo', methods=["GET", "POST"])
def updateinfo():
    if 'user' in session:
        if request.method=="POST":
            fileinput = request.files['infofile']
            filenaming = secure_filename(fileinput.filename)
            # fName = filenaming.split(".")
            
            fileinput.save(os.path.join(app.config['UPLOAD_FOLDER'], filenaming))
            
            if ".csv" in filenaming:
                df = pd.read_csv("static/upload/"+filenaming)
            else:
                df = pd.read_excel("static/upload/"+filenaming)
            
            Fname = df["First name"]
            Lname = df["Last name"]
            Fathername = df["Father Name"]
            Mothername = df["Mother Name"]
            curntLoc = df["Current Location"]
            Hometwn = df["Hometown Location"]
            certif = df["Certification Courses"]
            cgpa = df["CGPA"]
            clgname = df["College Name"]
            rolno = df["Roll Number"]
            pEmail = df["Personal Email"]
            cEmail = df["College Email"]
            Paswrd = df["Password"]
            phnno = df["Phone Number"]
            brnch = df["Branch"]
            degre = df["Degree"]
            percent10 = df["10th Percentage"]
            percent12 = df["12th Percentage"]
            actbacklog = df["Active Backlogs"]

            studinfo = zip(Fname,Lname,Fathername,Mothername,curntLoc,Hometwn,certif,cgpa,clgname,
            rolno,cEmail,pEmail,phnno,brnch,degre,percent10,percent12,actbacklog)

            userdetailzip = zip(Fname,Lname,phnno,cEmail,Paswrd,brnch)

            conn = dbConnection()
            curs = conn.cursor()


            for Fname,Lname,phnno,cEmail,Paswrd,brnch in userdetailzip:
                res_count = curs.execute("SELECT * from userdetails where fname=%s and email=%s;",(Fname,cEmail))
                if res_count>0:
                    curs.execute("UPDATE userdetails set fname=%s , lname=%s , mob=%s , email=%s , pass=%s , Department=%s where fname=%s and email=%s;",(Fname,Lname,phnno,cEmail,Paswrd,brnch,Fname,cEmail,))
                    conn.commit()
                else:
                    sql1 = "INSERT into userdetails (fname,lname,mob,email,pass,Department) values (%s,%s,%s,%s,%s,%s);"
                    val1 = (Fname,Lname,phnno,cEmail,Paswrd,brnch)
                    curs.execute(sql1,val1)
                    conn.commit()

            for Fname,Lname,Fathername,Mothername,curntLoc,Hometwn,certif,cgpa,clgname,rolno,cEmail,pEmail,phnno,brnch,degre,percent10,percent12,actbacklog in studinfo:
                res_count = curs.execute("SELECT * from studentinfo where fname=%s and Lname=%s and pEmail=%s and brnch=%s and cEmail=%s;",(Fname,Lname,pEmail,brnch,cEmail))
                if res_count>0:
                    curs.execute('''UPDATE studentinfo set fname=%s , lname=%s , fathername=%s , mothername=%s , curntLoc=%s , Hometown=%s , certif=%s, cgpa=%s , clgname=%s , rolno=%s , cEmail=%s, pEmail=%s , phnno=%s , brnch=%s , degre=%s , percent10=%s , percent12=%s , actbacklog=%s where fname=%s and Lname=%s and pEmail=%s and brnch=%s AND cEmail=%s;''',(Fname,Lname,Fathername,Mothername,curntLoc,Hometwn,certif,round(cgpa,3),clgname,rolno,cEmail,pEmail,phnno,brnch,degre,percent10,percent12,actbacklog,Fname,Lname,pEmail,brnch,cEmail))
                    conn.commit()
                else:
                    print()
                    print(df)
                    print()
                    print("printing sql2 data")
                    print(Fname,Lname,Fathername,Mothername,curntLoc,Hometwn,certif,round(cgpa,3),clgname,rolno,pEmail,phnno,brnch,degre,percent10,percent12,actbacklog)
                    print()
                    sql2 = '''INSERT into studentinfo (fname,lname,fathername,mothername,curntLoc,Hometown,certif,cgpa,clgname,rolno,cEmail,pEmail,phnno,brnch,degre,percent10,percent12,actbacklog) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''       
                    val2 = (Fname,Lname,Fathername,Mothername,curntLoc,Hometwn,certif,round(cgpa,3),clgname,rolno,cEmail,pEmail,phnno,brnch,degre,percent10,percent12,str(actbacklog))
                    curs.execute(sql2,val2)
                    conn.commit()
            
            msg = "Student Data Updated successfully!"
            return render_template('updateinfo.html',msg=msg)
        return render_template('updateinfo.html')
    return render_template('login.html')
################################################################################################################################
#                                           Company Post job page
################################################################################################################################
def sendemailtouser(usertoaddress,companyName,jobProfile,deadLine):   
    fromaddr = "madhavbansal9779@gmail.com"
    toaddr = usertoaddress
   
    #instance of MIMEMultipart 
    msg = MIMEMultipart() 
  
    # storing the senders email address   
    msg['From'] = fromaddr 
  
    # storing the receivers email address  
    msg['To'] = toaddr 
  
    # storing the subject  
    msg['Subject'] = "New job posted on portal"
  
    # string to store the body of the mail 
    body = "Hello! student, we posted a new job,Please login and check all the details \n Company Name: "+companyName+" \n Job Profile: "+jobProfile+" \n Deadline: "+deadLine
  
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
  
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
  
    # start TLS for security 
    s.starttls() 
  
    # Authentication 
    s.login(fromaddr, "jpvsfigjbcnagvir") 
  
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
  
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
  
    # terminating the session 
    s.quit()    


@app.route('/postjob', methods=["GET", "POST"])
def postjob():
    msg1 = 12
    print("printing hi before post method")
    headbranch = session.get("branch")
    if request.method == "POST":
        print("printing hi after post method")
        logo = request.files['logo']
        filename_secure2 = secure_filename(logo.filename)
        logo.save(os.path.join(app.config['UPLOAD_FOLDER2'], filename_secure2))
        print("[info]: company logo saved")

        jtitle = request.form.get("jtitle")
        jloc = request.form.get("jloc")
        jobType = request.form.get("jobType")
        jd = request.form.get("jd")
        Salary = request.form.get("Salary")
        deadline = request.form.get("deadline")
        cmpname = request.form.get("cmpname")
        resp = request.form.get("resp")
        eduexp = request.form.get("eduexp")
        benif = request.form.get("benif")
        branch = request.form.get('branch')
        studinfo = request.form.getlist('studinfo')
        jobdesc1 = request.form.get('desc1')
        jobdesc2 = request.form.get('desc2')
        jobdesc3 = request.form.get('desc3')
        jobdesc4 = request.form.get('desc4')
        jobdesc5 = request.form.get('desc5')
        jobques1 = request.form.get('ques1')
        jobques2 = request.form.get('ques2')
        jobques3 = request.form.get('ques3')
        jobques4 = request.form.get('ques4')
        jobques5 = request.form.get('ques5')
        print()
        print("studinfo")
        print(studinfo,jobdesc1,jobdesc2,jobdesc3,jobdesc4,jobdesc5)
        print(jobques1,jobques2,jobques3,jobques4,jobques5)
        
        filename_secure2 = "../static/logo/"+filename_secure2
        publishedOn = str(date.today())

        uname = session.get("user")

        if jobdesc1 is None:
            jobdesc1 = "Not needed"
        if jobdesc2 is None:
            jobdesc2 = "Not needed"
        if jobdesc3 is None:
            jobdesc3 = "Not needed"
        if jobdesc4 is None:
            jobdesc4 = "Not needed"
        if jobdesc5 is None:
            jobdesc5 = "Not needed"

        if jobques1 is None:
            jobques1 = "Not needed"
        if jobques2 is None:
            jobques2 = "Not needed"
        if jobques3 is None:
            jobques3 = "Not needed"
        if jobques4 is None:
            jobques4 = "Not needed"
        if jobques5 is None:
            jobques5 = "Not needed"


        con = dbConnection()
        cursor = con.cursor()
        sql = "INSERT INTO jobinfo (companyName, logo, jobTitle, jobLoc, jobType, publishedOn, salary, applicationDeadline, JobDescription, Responsibilities, Education_Experience, OtherBenifits,uname,branches,studentInfo,desc1,desc2,desc3,desc4,desc5,ques1,ques2,ques3,ques4,ques5) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        val = (cmpname, str(filename_secure2), jtitle, jloc,jobType, str(publishedOn), Salary, str(deadline), jd, resp, eduexp, benif,uname,branch,str(studinfo),jobdesc1,jobdesc2,jobdesc3,jobdesc4,jobdesc5,jobques1,jobques2,jobques3,jobques4,jobques5)
        # print(cmpname, str(filename_secure2), str(filename_secure1), email, jtitle, jloc,jobType, str(publishedOn), Vacancy, exp, Salary, str(deadline), jd, resp, eduexp, benif,uname,branch,str(studinfo))
        # cursor.execute("INSERT INTO jobinfo (companyName, logo, email, jobTitle, jobLoc, jobType, publishedOn, vacancy, Experience, salary, applicationDeadline, JobDescription, Responsibilities, Education_Experience, OtherBenifits,uname,branches,studentInfo) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"(cmpname, str(filename_secure2), str(filename_secure1), email, jtitle, jloc,jobType, str(publishedOn), Vacancy, exp, Salary, str(deadline), jd, resp, eduexp, benif,uname,branch,str(studinfo)))
        cursor.execute(sql,val)
        con.commit()
        
        cursor.execute("SELECT pEmail from studentinfo")
        res = cursor.fetchall()
        result = list(res)

        # for i in result:
        #     sendemailtouser(i[0],cmpname,jtitle,deadline) 
        
        # msg = "job added successfully!"

        return "success"

    msg = "Post a job for any profile"
    return render_template('post-job.html', msg=msg, headbranch=headbranch)

################################################################################################################################
#                                           Students get hired
################################################################################################################################
def SelectedMailToUser(usertoaddress,companyName,jobProfile):   
    fromaddr = "madhavbansal9779@gmail.com"
    toaddr = usertoaddress
   
    #instance of MIMEMultipart 
    msg = MIMEMultipart() 
  
    # storing the senders email address   
    msg['From'] = fromaddr 
  
    # storing the receivers email address  
    msg['To'] = toaddr 
  
    # storing the subject  
    msg['Subject'] = "Congatulations! You have been selected by "+companyName
  
    # string to store the body of the mail 
    body = "Congratulations! student you have been seleted by "+companyName+" For "+jobProfile+" Please contact to placement cell for further process.", 
  
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
  
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
  
    # start TLS for security 
    s.starttls() 
  
    # Authentication 
    s.login(fromaddr, "jpvsfigjbcnagvir") 
  
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
  
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
  
    # terminating the session 
    s.quit()    

@app.route('/emp', methods=["GET", "POST"])
def emp():
    uname = session.get("user")
    print(uname)
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute("SELECT * from applycmp")
    result = cursor.fetchall()
    result = list(result)
    print(result)

    cmpName = [i[1] for i in result]
    Jobtitle = [i[2] for i in result]
    resume = [i[3] for i in result]
    fname = [i[4] for i in result]
    lname = [i[5] for i in result]
    cat1 = [i[6] for i in result]
    cat2 = [i[7] for i in result]
    cat3 = [i[8] for i in result]
    cat4 = [i[9] for i in result]
    cat5 = [i[10] for i in result]
    cat6 = [i[11] for i in result]
    cat7 = [i[12] for i in result]
    cat8 = [i[13] for i in result]
    cat9 = [i[14] for i in result]
    ques1 = [i[15] for i in result]
    ques2 = [i[16] for i in result]
    ques3 = [i[17] for i in result]
    ques4 = [i[18] for i in result]
    ques5 = [i[19] for i in result]
    status = [i[20] for i in result]

    lst2 = zip(cmpName,Jobtitle,fname,lname,cat1,cat2,cat3,cat4,cat5,cat6,cat7,cat8,cat9,ques1,ques2,ques3,ques4,ques5,status)

    return render_template('hireemp.html',lst2=lst2)


@app.route('/hiring', methods=["GET", "POST"])
def hiring():
    con = dbConnection()
    cursor = con.cursor()

    uname = session.get("user")
    print(uname)
    studFname = request.args.get('Fname')
    studLname = request.args.get('Lname')
    CmpName = request.args.get('CmpName')
    jobProfile = request.args.get('jobProfile')
    Status = "Selected"
    print(studFname,studLname,CmpName,jobProfile)

    cursor.execute("select cEmail,pEmail from studentinfo where fname=%s and lname=%s",(studFname,studLname))
    result = cursor.fetchall()
    res = list(result)
    for i in res[0]:
        print(i)
    # SelectedMailToUser(i,CmpName,jobProfile)

    uname = session.get("user")
    print(uname)
    
    cursor.execute("UPDATE applycmp set status=%s where fname=%s and lname=%s and cmpName=%s and Jobtitle=%s",(Status,studFname,studLname,CmpName,jobProfile))
    con.commit()
    
    # cursor.execute("SELECT * from applycmp")
    # result = cursor.fetchall()
    # result = list(result)
    # print(result)

    # cmpName = [i[1] for i in result]
    # Jobtitle = [i[2] for i in result]
    # resume = [i[3] for i in result]
    # fname = [i[4] for i in result]
    # lname = [i[5] for i in result]
    # cat1 = [i[6] for i in result]
    # cat2 = [i[7] for i in result]
    # cat3 = [i[8] for i in result]
    # cat4 = [i[9] for i in result]
    # cat5 = [i[10] for i in result]
    # cat6 = [i[11] for i in result]
    # cat7 = [i[12] for i in result]
    # cat8 = [i[13] for i in result]
    # cat9 = [i[14] for i in result]
    # ques1 = [i[15] for i in result]
    # ques2 = [i[16] for i in result]
    # ques3 = [i[17] for i in result]
    # ques4 = [i[18] for i in result]
    # ques5 = [i[19] for i in result]
    # status = [i[20] for i in result]

    # lst2 = zip(cmpName,Jobtitle,fname,lname,cat1,cat2,cat3,cat4,cat5,cat6,cat7,cat8,cat9,ques1,ques2,ques3,ques4,ques5,status)


    # lst2 = zip(ufname,ulname,email,mobno,prev_post,exp,cmpName,jobpos,status)

    # return render_template('hireemp.html',lst2=lst2)

    return redirect(url_for(emp))
################################################################################################################################
#                                           Company Post job page
################################################################################################################################
@app.route('/jobhistory', methods=["GET", "POST"])
def jobhistory():
    uname = session.get("user")
    print(uname)
    con = dbConnection()
    cursor = con.cursor()

    studName = session.get("user")
    studlname = session.get("userlname")
    studbranch = session.get("branch")

    cursor.execute("SELECT cmpName, Jobtitle from applycmp where fname=%s and lname=%s and status='applied'",(studName,studlname))
    result = cursor.fetchall()
    res = list(result)
    allcmpname = [i[0] for i in res]
    alljobtitle = [i[1] for i in res]
    cmplst = zip(allcmpname, alljobtitle)

    reslst = []
    for i,j in cmplst:
        res_count = cursor.execute("select companyName,Salary,jobTitle,jobType,logo,jobLoc,OtherBenifits from jobinfo where branches=%s and companyName=%s and jobTitle=%s",(studbranch,i,j))
        res = cursor.fetchall()
        res = list(res)
        # print(res)
        reslst.append(res)
        if res_count==0:
            cursor.execute("select companyName,Salary,jobTitle,jobType,logo,jobLoc,OtherBenifits from jobinfo where branches=%s and companyName=%s and jobTitle=%s",(studbranch,i,j))
            res2 = cursor.fetchall()
            res2 = list(res2)
            # print(res)
            reslst.append(res2)

    print()
    print("reslst")
    print(reslst)
    print()
    companyName = [i[0] for i in res]
    print()
    print("companyName")
    print(companyName)
    print()
    salary = [i[1] for i in res]
    jobTitle = [i[2] for i in res]
    jobType = [i[3] for i in res]
    logo = [i[4] for i in res]
    jobLoc = [i[5] for i in res]
    jobperks = [i[6] for i in res]

    print("companyName,salary,jobTitle,jobType,logo,jobLoc,jobperks")
    print(companyName,salary,jobTitle,jobType,logo,jobLoc,jobperks)
    lst = zip(companyName,salary,jobTitle,jobType,logo,jobLoc,jobperks)

    return render_template('history.html',lst=lst)

################################################################################################################################
#                                           Testing
################################################################################################################################
@app.route('/test', methods=["GET", "POST"])
def testing():
    if request.method == "POST":

        jtitle = request.form.get("jtitle")
        jobType = request.form.get("jobType")
        test1 = request.form.get("test1")
        test2 = request.form.get("test2")
        test3 = request.form.get("test3")
        test4 = request.form.get("test4")

        print(jtitle,jobType,test1,test2,test3,test4)

        if test3 is None:
            print()
            print("getting none")
        else:
            print()
            print("getting some value")


        return render_template('test.html')
    return render_template('test.html')




if __name__ == '__main__':
    app.run(debug=True)
    # app.run('0.0.0.0')
