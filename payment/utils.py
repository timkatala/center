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