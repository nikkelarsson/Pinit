
'''
File : file.py
Desc : File operation related errors.
'''

def exists(name, language='eng'):
	'''Give an error when trying to create a file
	with a name that matches already existing file's name.'''

	if language == 'fi':
		msg = 'Virhe: ”{}” on jo olemassa'.format(name)
	elif language == 'eng':
		msg = 'Error: ”{}” already exists'.format(name)
	print(msg)

def invalid_filename(name, language='eng'):
	'''Give an error when attempting to create file
	with invalid name.'''

	if language == 'fi':
		msg = 'Virhe: Huono nimeämiskäytäntö ”{}”'.format(name)
	elif language == 'eng':
		msg = 'Error: Bad naming convention ”{}”'.format(name)
	print(msg)

def name_missing(language='eng'):
	'''Give an error when file is missing a filename.'''

	if language == 'fi':
		msg = 'Virhe: <nimi> puuttuu'
	elif language == 'eng':
		msg = 'Error: <name> missing'
	print(msg)

def not_found(path, language='eng'):
	'''Give an error when trying to create files to location
	that doesn't exist.'''

	if language == 'fi':
		msg = 'Virhe: Virheellinen polku ”{}”'.format(path)
	elif language == 'eng':
		msg = 'Error: Invalid path ”{}”'.format(path)
	print(msg)