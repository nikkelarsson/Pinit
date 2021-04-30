import sys
import os
import time
import descriptions
import textwrap
import getpass
#from settings import version, name, language
from mdtemplates import readmetemplate, changestemplate

language = 'fi'

def printHelp():
	'''Print program help'''
	print('{}'.format(descriptions.usage))
	print()
	print('{}'.format(descriptions.description))
	print()
	print('{}'.format(textwrap.dedent(descriptions.help_messages).strip()))

def printProgramVersion():
	'''Print program version'''
	print('{}'.format(descriptions.version))

def createFiles(dirname, *additargs, initasgitrepo=False, capitalizedmarkdownfiles=False, readme='readme.md', changes='changes.md'):

	'''Create new project with desired files. README.md and CHANGES.md files are created by default.'''

	# Allow all caps when creating markdown files.
	if capitalizedmarkdownfiles == True:
		readme = 'README.md'
		changes = 'CHANGES.md'
	else:
		pass

	# When user wants to create project, say, to their home dir, allow the ”~/” abbreviation.
	if dirname[0:1] == '~/':
		dirname.replace('~/', '/Users/{}'.format(getpass.getuser()))

	# First lets create the root folder with readme, src folder etc.
	os.mkdir(dirname)
	os.chdir(dirname)
	os.mkdir('src')

	with open(readme, 'w', encoding='utf-8') as f:

		# First insert main heading using the name the project was created with
		dirnameFirstInitial = dirname[0].upper()
		dirnameRestOfChars = dirname[1:]
		dirname = dirnameFirstInitial + dirnameRestOfChars
		f.write('# {}'.format(dirname))
		f.write('')

		# Insert mdtemplates.py's ”readme” into contents, just to let you.
		contents = readmetemplate
		f.write(contents)
	
	with open(changes, 'w', encoding='utf-8') as f:

		# Insert mdtemplates.py's ”changes” into contents, just to let you.
		contents = changestemplate
		f.write(contents)

	# Also create .gitignore file according to the preference initasgitrepo has been set.
	if initasgitrepo == False:
		pass
	elif initasgitrepo == True:
		with open('.gitignore', 'w', encoding='utf-8') as f:
			f.write()

	# After basic files have been created we can additionally create more files into the src folder.
	if additargs:
		os.chdir('src')
		for arg in additargs:
			with open(arg, 'w', encoding='utf-8') as f:
				f.write()

def initDriver(goheadless=True):

	'''Initialize the Chrome driver'''

	from selenium import webdriver
	from selenium.webdriver.chrome.options import Options

	options = Options()
	options.add_argument('--headless')

	if goheadless == True:
		driver = webdriver.Chrome(
			executable_path=os.path.abspath('/Users/{}/Downloads/chromedriver'.format(getpass.getuser())),
			options=options)
		return driver
	else:
		driver = webdriver.Chrome(
			executable_path=os.path.abspath('/Users/{}/Downloads/chromedriver'.format(getpass.getuser())))
		return driver

def initAsGitRepo():

	'''Init project as git repository, as it is being created.'''

	# We need this stuff only when initializing as git repo;
	# I don't know if importing this stuff only here will make things
	# any faster etc. but lets give it a try.
	import requests
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.chrome.options import Options
	from selenium.webdriver.support import ui

	url = 'https://github.com/login'

	# Init the project first as git repo.
	#os.system('git init')
	#os.system('git branch -M main')

	driver = initDriver(goheadless=False)
	driver.get(url)
	wait = ui.WebDriverWait(driver, 6)
	githubLoginField = driver.find_element_by_id('login_field')
	githubPasswordField = driver.find_element_by_id('password')
	githubSignInButton = driver.find_element_by_name('commit')

	try:
		githubTokenField = driver.find_elements_by_xpath('//*[@id="login"]/div[5]/form/input[1]')
	except:
		driver.quit()

	if language == 'fi':
		print('Kirjaudu GitHubiin')
		username = input('Käyttäjätunnus tai sähköposti: ')

		# Using getpass here to hide the passwd while typing it.
		passwd = getpass.getpass('Salasana: ')

		# Input username and password into their own fields in GitHub.
		githubLoginField.send_keys(username)
		githubPasswordField.send_keys(passwd)
		# Reset passwd variable, just in case :O
		passwd = ''
		githubSignInButton.click()

		# Check if user uses 2-factor-authentication by waiting a moment.
		try:
			wait.until(
				lambda driver:
				driver.find_elements_by_xpath('//*[@id="login"]/div[5]/form/input[1]')
			)
			token = input('Todennusavain: ')
			githubTokenField.clear()
			githubTokenField.send_keys(token)
			githubTokenField.send_keys(Keys.RETURN)
		except:
			pass

	elif language == 'us':
		print('Login to GitHub')
	else:
		print('Login to GitHub')

	time.sleep(10)
	driver.quit()

def checkForSlashes(path):
	
	'''
	Check if user is creating a project in custom location.
	If yes, then extract the text that comes after the final forward slash ”/”.

	An example: user creates project in ~/Documents/HelloWorld  
	So, we should then extract the ”HelloWorld” from the path. Got it?

	The purpose of this function is to make sure, that the name user will use for the project
	is legit; as using --help or any valid flag as a name etc. is prohibited.
	'''

	count = 0

	for i in path:
		if i == '/':
			count += 1
	
	# If no ”/” were found, then just pass.
	if count == 0:
		return 1
	else:

		# Try to find the first letter after the ”/”
		if path[-2] == '/':
			theName = path[-1]
			return theName
		elif path[-3] == '/':
			theName = path[-2:]
			return theName
		elif path[-4] == '/':
			theName = path[-3:]
			return theName
		elif path[-5] == '/':
			theName = path[-4:]
			return theName
		elif path[-6] == '/':
			theName = path[-5:]
			return theName
		elif path[-7] == '/':
			theName = path[-6:]
			return theName
		elif path[-8] == '/':
			theName = path[-7:]
			return theName
		elif path[-9] == '/':
			theName = path[-8:]
			return theName
		elif path[-10] == '/':
			theName = path[-9:]
			return theName
		elif path[-11] == '/':
			theName = path[-10:]
			return theName

		# Also try to find the first letter after the ”/”.
		# This is just another, maybe more sophisticated method for doing that.
		# I've commented this section out because I trusted the method above more, although
		# it's a little more work done, whatever.

		#index = -3

		#for i in path:
		#	if path[index] == '/':
		#		theName = path[index:]
		#	index -= 1