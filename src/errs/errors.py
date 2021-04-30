class Error():
    '''Error class containing various methods for giving error messages.'''

    def __init__(self, language='eng'):
        self.language = language

    def invalid_command(self, cmd, retrn=False):
        '''Return an error when encountered with invalid command on command line.'''

        self.cmd = cmd

        if self.language == 'fi':
            self.msg = 'Virhe: tuntematon argumentti ”{}”'.format(self.cmd)
        elif self.language == 'eng':
            self.msg = 'Error: unrecognized argument ”{}”'.format(self.cmd)
        
        if retrn == False:
            print(self.msg)
        else:
            return self.msg

    def invalid_name(self, name, retrn=False):
        '''Error given when a file is created with ”invalid” name:
        ”-” as a prefix in filename is one of these ”invalid” cases.'''

        self.name = name
        
        if self.language == 'fi':
            self.msg = 'Virhe: huono nimeämiskäytäntö ”{}”'.format(self.name)
        elif self.language == 'eng':
            self.msg = 'Error: bad naming convention ”{}”'.format(self.name)

        if retrn == False:
            print(self.msg)
        else:
            return self.msg

    def missing_name(self, retrn=False):
        '''Error given when no name for project is given.'''

        if self.language == 'fi':
            msg = 'Virhe: <nimi> puuttuu'
        elif self.language == 'eng':
            msg = 'Error: <name> missing'

        if retrn == False:
            print(msg)
        else:
            return msg

    def file_exists(self, name, retrn=False):
        '''Error given when trying to create a file with a name, that
        matches already existing file's name.'''

        if self.language == 'fi':
            msg = 'Virhe: tiedosto ”{}” on jo olemassa'.format(name)
        elif self.language == 'eng':
            msg = 'Error: file ”{}” already exists'.format(name)

        if retrn == False:
            print(msg)
        else:
            return msg