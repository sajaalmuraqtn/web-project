# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from form.py")

def Hellow():
    students = db.executesql("SELECT * FROM students", as_dict=True)
    return dict(students= students)
# ---- example login page ----
def login():
    return locals()


# ---- example register page ----
def register():
    
    return locals()
    
# ---- example addregister query ----
def addregister():
    if request.vars['FirstName']:
        first_name = request.vars['FirstName']
        last_name = request.vars['LastName']
        email = request.vars['email']
        password = request.vars['password']
        reset_password_key = request.vars['resetPassword']

        db.executesql("INSERT INTO students (first_name, last_name, email,password,reset_password_key) VALUES (%s, %s, %s, %s,%s)", placeholders=(first_name,last_name, email,password,reset_password_key))
    else:
        redirect(URL('register'))

    return locals()

