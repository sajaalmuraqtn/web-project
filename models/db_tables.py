import datetime


db.define_table('courses',
	Field('code', 'string', required=True, notnull=True),
	Field('name', 'string'),
	Field('description', 'string'),
	Field('prerequisites', 'string', 'reference courses',
		requires=IS_IN_DB(db, 'courses.code', '%(name)s'),notnull=False),
	Field('instructor', 'string'),
	Field('capacity', 'integer'),
	Field('scheduleId', 'integer', 
		'reference courseschedules', 
		requires=IS_IN_DB(db, 'courseschedules.id', '%(days)s: %(startTime)s - %(endTime)s')),
	primarykey=['code']
	)

db.define_table('rooms',
	Field('code', 'string', required=True, notnull=True),
	primarykey=['code'])


db.define_table('courseschedules',
	Field('id', 'integer'),
	Field('days', 'string'),
	Field('startTime', 'time', default=datetime.time(0,0)),
	Field('endTime', 'time', default=datetime.time(0,0)),
	Field('RoomNo', 'string', 'reference rooms', requires=IS_IN_DB(db, 'rooms.code', '%(code)s') )
	)

