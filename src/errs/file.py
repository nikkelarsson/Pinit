
'''
file : file.py  
desc : File operation related errors.
'''

def exists(name, language='eng'):
    '''Error given when trying to create a file or a directory
    with a name, that matches already existing file's or directorys name.'''

    if language == 'fi':
        msg = 'Virhe: ”{}” on jo olemassa'.format(name)
    elif language == 'eng':
        msg = 'Error: ”{}” already exists'.format(name)
    print(msg)

def has_invalid_filename(name, language='eng'):
    '''Error given when attempted to create a file with a name
    that is invalid.'''
        
    if language == 'fi':
        msg = 'Virhe: Huono nimeämiskäytäntö ”{}”'.format(name)
    elif language == 'eng':
        msg = 'Error: Bad naming convention ”{}”'.format(name)
    print(msg)

def name_missing(language='eng'):
    '''Error given when file is missing a filename.'''

	if language == 'fi':
		msg = 'Virhe: <nimi> puuttuu'
	elif language == 'eng':
		msg = 'Error: <name> missing'
	print(msg)

def not_found(name, language='eng'):
    '''Error given when trying to, for example, create a file or a directory into
    location, that doesn't exist.'''

    if language == 'fi':
        msg = 'Virhe: Virheellinen polku ”{}”'.format(name)
    elif language == 'eng':
        msg = 'Error: Invalid path ”{}”'.format(name)
    print(msg)
