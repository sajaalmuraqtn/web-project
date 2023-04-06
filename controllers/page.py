# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from page.py")

# ---- example home page ----
def home():
    students = db.executesql("SELECT * FROM students", as_dict=True)
    return dict(students= students)

def Hellow():
    students = db.executesql("SELECT * FROM students", as_dict=True)
    return dict(students= students)


#add courses page

def addcourses(): 
	return dict(message="hello from page.py")

#show courses page
def showcourses(): 
	return dict(message="hello from page.py")

