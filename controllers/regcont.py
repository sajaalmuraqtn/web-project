def addSchedule():

	form = SQLFORM(db.courseschedules)

	if form.process().accepted:
		response.flash = 'Schedule added'
	elif form.errors:
		response.flash = 'Schedule has errors'
	else:
		response.flash = 'please fill out the Schedule form'

	return dict(form=form)

def schedules():

	grid = SQLFORM.grid(db.courseschedules, csv=False,deletable=False,editable=False)

	return dict(grid=grid)


def addroom():


	form = SQLFORM(db.rooms)

	if form.process().accepted:
		response.flash = 'Room added'
	elif form.errors:
		response.flash = 'Room has Problem'
	else:
		response.flash = 'please fill out the Room form'

	return dict(form=form)



def addCourse():
	courseId = int(request.args(0))
	db.studentsRegs.insert(studentId=auth.user.id,courseId=courseId)
	msg=courseId
	redirect(URL('yourCourses'))
	return locals()
    

def addcourses():


	form = SQLFORM(db.courses)

	if form.process().accepted:
		response.flash = 'course added'
	elif form.errors:
		response.flash = 'course has Problem'
	else:
		response.flash = 'please fill out the course form'

	return dict(form=form)

def showcourses():
	grid = SQLFORM.grid(db.courses,csv=False,deletable=False,editable=False)
	return dict(grid=grid)

def delete():

    if request.vars['id']:
        id = request.vars['id']

        db.executesql("DELETE FROM studentsReg WHERE id=" + id)
    
    redirect(URL('coursesReg'))


def coursesReg():
    regcourses = db.executesql("SELECT r.id,r.studentId,r.courseId,c.name,c.instructor,c.scheduleid, s.startTime , s.endTime , s.RoomNo FROM (courses c  join studentsReg r ON c.code=r.courseId) join courseschedules s ON s.id=c.scheduleid ", as_dict=True)
    return dict(regcourses= regcourses)



def registercourses():

	form = SQLFORM(db.studentsreg)

	if form.process().accepted:
		response.flash = 'courses added to your schedual'
	elif form.errors:
		response.flash = 'course register has Problem'
	else:
		response.flash = 'please fill out the course register form'

	return dict(form=form)

