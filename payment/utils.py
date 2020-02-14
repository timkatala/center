import datetime
MONTHS = ['Yanvar',
	'Fevral',
	'Mart',
	'Aprel',
	'May', 
	'Iyun',
	'Iyul',
	'Avgust',
	'Sentyabr',
	'Oktyabr',
	'Noyabr',
	'Dekabr',
	]

def timer():
	return f'{MONTHS[datetime.datetime.now().month-1]} {datetime.datetime.now().year}'


def timer1():
	if datetime.datetime.now().month-2<0:
		return f'{MONTHS[datetime.datetime.now().month-2]} {datetime.datetime.now().year-1}'
	return f'{MONTHS[datetime.datetime.now().month-2]} {datetime.datetime.now().year}'