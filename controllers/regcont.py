
def addSchedule():

	form = SQLFORM(db.courseschedules)

	if form.process().accepted:
		response.flash = 'form accepted'
	elif form.errors:
		response.flash = 'form has errors'
	else:
		response.flash = 'please fill out the form'

	return dict(form=form)

def schedules():

	grid = SQLFORM.grid(db.courseschedules, csv=False)

	return dict(grid=grid)


def addcourses():

	form = SQLFORM(db.courses)

	if form.process().accepted:
		response.flash = 'form accepted'
	elif form.errors:
		response.flash = 'form has errors'
	else:
		response.flash = 'please fill out the form'

	return dict(form=form)

def showcourses():

	grid = SQLFORM.grid(db.courses)

	return dict(grid=grid)