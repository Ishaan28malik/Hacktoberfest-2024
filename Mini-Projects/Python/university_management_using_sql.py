class Clas:
        total_stu = 0
        def __init__(self,first,last,mother,father,roll,clas,phone,mail):
                self.first=first
                self.last=last
                self.mother=mother.capitalize()
                self.father=father.capitalize()
                self.roll=roll
                self.clas=clas
                self.phone=phone
                self.mail=mail.capitalize()
                Clas.total_stu +=1
        def fullname(self):
                 return self.first.capitalize()+" "+self.last.capitalize()


import psycopg2
db=psycopg2.connect(database='student',user='postgres',host='127.0.0.1',password='12345678',port=5432)
cur=db.cursor()
#os=Clas()
#a=os.fullname()
#cur.execute('Create table class(name varchar(20),mother varchar(20),father varchar(20),roll bigint,clas varchar(20), phone bigint, mail varchar(40),datetime varchar(35))')
#db.commit()
#state="""INSERT INTO class (name,mother,father,roll,clas,phone,mail) VALUES('%s','%s','%s',%d,'%s',%d,'%s')"""%(a,os.mother,os.father,os.roll,os.clas,os.phone,os.mail)
#cur.execute("insert into class values(%s,%s,%s,%d,%s,%d,%s)"%(os.fullname(),os.mother,os.father,os.roll,os.clas,os.phone,os.mail))
#db.commit()
#cur.execute(state)
#cur.execute('ALTER TABLE class ALTER COLUMN "clas" TYPE varchar(10)')
#db.commit()
def _():
        a = [77, 97, 100, 101, 32, 98, 121, 32, 58, 45, 45, 79, 36, 45, 45]
        print("-" * 20, end="")
        for x in range(len(a)):
            print(chr(a[x]), end="")
        print("-" * 20)
def dbs():
    db=psycopg2.connect(database='student',user= 'postgres',host='127.0.0.1',password='12345678',port=5432)
    cur=db.cursor()
    print("!Please Enter your enteries correctly. =")
    print("-"*55)
    a=input("Enter your first name    = ")
    b=input("Enter your last name     = ")
    c=input("Enter your mother's name = ")
    d=input("Enter your Ftaher's name = ")
    print("The roll no. should be of 5 digits")
    e=int(input("Enter your Rollno    ="))
    m=str(e)
    while len(m)!=5:
        print("Try again")
        e=int(input("Enter your Rollno Again      ="))
        m=str(e)
    f=input("Enter your class         =")
    g=input("Enter your phone no      =")
    p=str(g)
    while len(p)!=10:
        print("Try again with correct format of phone no.")
        g=input("Enter your phone no      =")
        p=str(g)
    h=input("Enter your mail id       =")
    t=dt()
    os=Clas(a,b,c,d,e,f,g,h)
    state="""INSERT INTO class (name,mother,father,roll,clas,phone,mail,datetime) VALUES('%s','%s','%s',%d,'%s',%s,'%s','%s')"""%(os.fullname(),os.mother,os.father,os.roll,os.clas,os.phone,os.mail,t)
    cur.execute(state)
    db.commit()
    i=input("do u want to add more enteries (yes/no)")
    return i

def repeat(self,i): 
    if (i=="yes" or i=="y"):
        dbs()
    else:
        print("Thanks for using dbs system")
def l(ro): 
    return(" "*(35-len(str(ro))))
def dt():
        import datetime
        now = datetime.datetime.now()
        return str(now.strftime("%Y-%m-%d %H:%M:%S"))
def check_details():
    k=int(input("Enter the roll no = "))
    cur.execute("select * from class where roll=%d"%(k))  
    ro=cur.fetchall()
    for row in ro :
        print("Here is your details of given roll no = ",k)
        print("-"*55)
        print("Name          = ",row[0])
        print("Mother's name = ",row[1])
        print("Father's name = ",row[2])
        print("Roll no       = ",row[3])
        print("Class         = ",row[4])
        print("Phone         = ",row[5])
        print("Mail id       = ",row[6])
        print("_"*55)
        _()

def count_len_of_table():
    cur.execute("select *from class")
    gh=cur.fetchall()
    rs=len(gh)
    return rs
print("Welcome to the Database Management System  ")
print("1. Admin")
print("2. Student")
print("3. Teacher")
print("4. Know About Developer")
import datetime
now = datetime.datetime.now()
 
i=int(input("Enter your choice = "))
if (i==1):
    print("-----Welcome to Admin Department------")
    print("1. Check Total no. of students ")
    print("2. Check student details")
    i=int(input("Enter your choice = "))
    if (i==1):
        print("Total no. of students are in University is = ",count_len_of_table())
    elif(i==2):
        k=int(input("Enter the roll no = "))
        cur.execute("select * from class where roll=%d")%(k)  
        row=cur.fetchall()
        print(row)
elif(i==2):
    print("1. Check your details")
    print("2. Generate id card")
    i=int(input("Enter your choice = "))
    if (i==2):
        i=int(input("Please Enter the Roll no = "))
        j=input("Enter your name = ")
        import time
        import sys
        s = '.'
        print("\n","\n","\n","\n",)
        sys.stdout.write( ' Please wait While loading ' )
        for z in range(3):
            sys.stdout.write( s )
            sys.stdout.flush()
            time.sleep(0.4)
        print("\r")
        cur.execute("select * from class where roll=%d"%(i))
        record=cur.fetchall()
        for row in record:
            q=str(now.year)
            ro=str(row[3])
            ri=str(cur.rowcount+000)
            li=len(q)+len(ro)+len(ri)
            print("|"+"-"*55+"|")
            print("|","              SOL(School of open learning )           "+"|")
            print("|"+"-"*55+"|")
            print("|"+"                     Identity card                    "+" |")
            print("|","                   -----------------                  "+"|")
            print("| ","Reg. Date/Time : %s"%(row[7]),l(row[7])+"|")
            print("| ","Reg. Id        : SOl-%s-%s-%s"%(q,ri,ro)," "*(28-li),"|")
            print("|"+" "*55+"|")
            print("| ","Name          = ",row[0],l(row[0])+"|")
            print("| ","Mother's name = ",row[1],l(row[1])+"|")
            print("| ","Father's name = ",row[2],l(row[2])+"|")
            print("| ","Roll no       = ",row[3],l(row[3])+"|")
            print("| ","Class         = ",row[4],l(row[4])+"|")
            print("| ","Phone         = ",row[5],l(row[5])+"|")
            print("| ","Mail id       = ",row[6],l(row[6])+"|")
            print("|"+"-"*55+"|")
            print("_"*55)
            _()

            
            
            
    elif(i==1):
        k=int(input("Enter the roll no = "))
        cur.execute("select * from class where roll=%d"%(k))  
        ro=cur.fetchall()
        for row in ro :
            print("Here is your details of given roll no = ",k)
            print("-"*55)
            print("Name          = ",row[0])
            print("Mother's name = ",row[1])
            print("Father's name = ",row[2])
            print("Roll no       = ",row[3])
            print("Class         = ",row[4])
            print("Phone         = ",row[5])
            print("Mail id       = ",row[6])
            print("_"*55)
            _()
            
elif(i==3):
    print("1. Add new student in class.")
    print("2. Check Total no. of students are in University.")
    print("3. Modify/Update student details.")
    print("4. Delete an student data")
    i=int(input("Enter the choice = " ))
    if(i==1):
        i=dbs()
        while i=="yes":
            dbs()
            i=input("Enter the input (yes /no)")
            if i =="yes":
                pass
            else:
                quit()
    elif(i==2):
        print("Total no. of students are in University is = ",count_len_of_table())
    elif(i==3):
        udb=int(input("Enter the student roll no. = "))
        cur.execute("select * from class where roll=%d"%(udb))  
        ro=cur.fetchall()
        for row in ro :
            print("Here is your details of given roll no = ",udb)
            print("-"*55)
            print("1. Name          = ",row[0])
            print("2. Mother's name = ",row[1])
            print("3. Father's name = ",row[2])
            print("4. Roll no       = ",row[3])
            print("5. Class         = ",row[4])
            print("6. Phone         = ",row[5])
            print("7. Mail id       = ",row[6])
            print("-"*55)
            k=int(input("Select the field you want to update = "))
            if k==1:
                print("You have selected name =%s for change"%(row[0]))
                k=input("Enter the new name with you want to replace the existing name = ")
                cur.execute("update class set name = '%s' where name='%s'"%(k.capitalize(),row[0]))
                db.commit()
                print("Record Updated successfully")
                k=input("Do you want to check the updated record?")
                if k=="yes" or k=="y":
                    check_details()
                else:
                    print("-"*55)
                    print("Thanks for using Database system...")
                    print("_"*55)
                    _()
            elif(k==2):
                print("You have selected Mother's name = %s for change"%(row[1]))
                k=input("Enter the new name with you want to replace the existing name = ")
                cur.execute("update class set mother = '%s' where mother='%s'"%(k.capitalize(),row[1]))
                db.commit()
                print("Record Updated successfully")
                k=input("Do you want to check the updated record?")
                if k=="yes" or k=="y":
                    check_details()
                else:
                    print("-"*55)
                    print("Thanks for using Database system...")
            elif k==3:
                print("You have selected Father's name  =%s for change"%(row[2]))
                k=input("Enter the new name with you want to replace the existing name = ")
                cur.execute("update class set father = '%s' where father='%s'"%(k.capitalize(),row[2]))
                db.commit()
                print("Record Updated successfully")
                k=input("Do you want to check the updated record?")
                if k=="yes" or k=="y":
                    check_details()
                else:
                    print("-"*55)
                    print("Thanks for using Database system...")
            elif k==4:
                print("You have selected Roll no.   =%d for change"%(row[3]))
                k=int(input("Enter the new Roll no. with you want to replace the existing Roll no. = "))
                cur.execute("update class set roll = %d where roll=%d"%(k,row[3]))
                db.commit()
                print("Record Updated successfully")
                k=input("Do you want to check the updated record?")
                if k=="yes" or k=="y":
                    check_details()
                else:
                    print("-"*55)
                    print("Thanks for using Database system...")
            elif k==5:
                print("You have selected Class  =%s for change"%(row[4]))
                k=input("Enter the new class with you want to replace the existing class = ")
                cur.execute("update class set clas = '%s' where clas='%s'"%(k,row[4]))
                db.commit()
                print("Record Updated successfully")
                k=input("Do you want to check the updated record?")
                if k=="yes" or k=="y":
                    check_details()
                else:
                    print("-"*55)
                    print("Thanks for using Database system...")
            elif k==6:
                print("You have selected Phone no.  =%d for change"%(row[5]))
                k=int(input("Enter the new phone no. with you want to replace the existing phone no. = "))
                cur.execute("update class set phone = %d where phone=%d"%(k,row[5]))
                db.commit()
                print("Record Updated successfully")
                k=input("Do you want to check the updated record?")
                if k=="yes" or k=="y":
                    check_details()
                else:
                    print("-"*55)
                    print("Thanks for using Database system...")
            elif k==7:
                print("You have selected Email-id =%s for change"%(row[6]))
                k=input("Enter the new mail id with you want to replace the existing mail id = ")
                cur.execute("update class set mail = '%s' where mail='%s'"%(k.capitalize(),row[6]))
                db.commit()
                print("Record Updated successfully")
                k=input("Do you want to check the updated record?")
                if k=="yes" or k=="y":
                    check_details()
                else:
                    print("-"*55)
                    print("Thanks for using Database system...")
                    print("_"*55)
                    _()
elif(i==4):
    print("_"*55)
    print("Name      = Orendra singh")
    print("Phone no. = 7503408348")
    print("Email-id  = Orendrasingh@gmail.com")
    print('Follow me on fb "www.facebook.com/orendra.singh"')
    print('Follow me on Instagram "www.instagram.com/orendrasingh"')
    print("_"*55)
    
    _()

else:
    print("Wrong input")
    

        
    
#i=dbs()
#while i=="yes":
#    dbs()
#    i=input("Enter the input (yes /no)")
#    if i =="yes":
#        pass
#    else:
#        quit()

