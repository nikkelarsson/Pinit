
'''
File : create.py  
Desc : File creation procedures.
'''

import getpass
import os

# NOTE: pass arguments for ”*files” as a list or as a tuple!
# This is, because files() tries to parse the *files
# argument as a list (or tuple): giving *files just a single variable
# as an argument would make create() work unexpectedly.
def files(
		*files       : tuple,
		language     : str  = 'eng',
		verbose      : bool = False,
		project_type : str  = 'python',
		git          : bool = False
		) -> str:

	'''Create the files that make the project, like the root dir etc.'''

	count       : int = 0
	username    : str = getpass.getuser()
	fwd_slashes : int = 0

	# TODO: 1. Make sure filename is valid. [CHECK]
	# TODO: 2. If creating in other location than cwd make sure that the location actually exists.
	# TODO: 3. Finally make sure, that no file with the same name exists in the location.
	for new_file in files:
		if count == 0:

			# Allow using the ”~/” abbreviation: it's nicer to write less.
			if new_file[0][0:1] == '~/':
				new_file.replace('~/', '/Users/{}/'.format(username))

			# To avoid problems, prohibit the use of ”-” as a prefix in filenames.
			if new_file[0][0] == '-':
				return 'INVALID_FILENAME'

			# I dunno is this even needed, as the expression above
			# kind of already considers a filename an error, if
			# just the first letter is a dash?
			elif new_file[0][0:1] == '-':
				return 'INVALID_FILENAME'

			# Check if file is created in location other than cwd.
			# This is unfinished.
			if fwd_slashes >= 1:
				for final_fwd_slash in new_file:
					if final_fwd_slash:
						pass

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
			# for filename in new_file:
			# 	letters = filename[0:].split()
			# 	for letter in letters:
			# 		if letter == '/':
			# 			fwd_slashes += 1
			# return letters


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
