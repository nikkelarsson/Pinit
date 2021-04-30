
'''
file : create.py  
desc : File creation handling.
'''

import getpass
import os

# NOTE: pass arguments for ”*files” as a list!
# This is, because files() tries to parse the *files
# argument as a list: giving *files just a single variable
# as an argument would make create() work unexpectedly.
def files(*files, language='eng', verbose=False, project_type='python', gitrepo=False):
	'''Create the files that make the project, like the root dir etc.'''

    count = 0
    fwd_slashes = 0
	username = getpass.getuser()

	for new_file in files:
        if count == 0:

            # Allow using the ”~/” abbreviation: it's nicer to write less.
            if new_file[0][0:1] == '~/':
                new_file.replace('~/', '/Users/{}/'.format(username))

            # To avoid problems, prohibit the use of ”-” as a prefix in filenames.
            if new_file[0][0] == '-':
                return 'INVALID_FILENAME_USED'

            elif new_file[0][0:1] == '-':
                return 'INVALID_FILENAME_USED'

            if os.path.exists(new_file[0]):
                return 'FILE_ALREADY_EXISTS'

			# NOTE: WHAT THIS SECTION BELOW EVEN DOES?
			# ----------------------------------------
            # Check whether project was created to cwd or else.
            # Reason: When we create a project in cwd, we get the
            # project's name straight away. But when we create a
            # project somewhere else, the actual name of the project
            # is the last word in the path -> path/to/myproject ->
			# ”myproject” and that is the word we need to extract
			# from the path.
            for filename in new_file:
                letters = filename[0:].split()
                for letter in letters:
                    if letter == '/':
                        fwd_slashes += 1
            return letters

            # When a project is created in a location other than the current working directory,
            # extract the name used for the project from the path.
            # Reason: As we create the ”source code” directory inside the project directory,
            # we're going to name it with the same name that the project directory was named with.
            # if fwd_slashes >= 1:
            #     for start_point in file:
            #         if file[0][-2] == '/':
            #             name_extracted = ''

            # Its a good convention to name directories and files using lowercase letters only.
            # project = file[0].lower()

            # try:
            #     os.mkdir(project) # This will be the root directory.
            # except FileNotFoundError:
            #     return 'FILE_NOT_FOUND'

            # with open('{}/README.md'.format(project), 'w', encoding='utf-8') as f:
            #     f.write('# {}'.format(project))
            # with open('{}/CHANGELOG.md'.format(project), 'w', encoding='utf-8') as f:
            #     f.write('# Changelog')
            # os.mkdir('{}/src'.format(project)) # And this will be the src dir.

            # return 'OK.'
            #count += 1

        # if count == 1:
        #     if language == 'fi':
        #         msg = 'Luotiin ”{}” onnistuneesti.'.format(project)
        #     elif language == 'eng':
        #         msg = 'Created ”{}” successfully.'.format(project)
        #     if verbose == True:
        #         return msg
