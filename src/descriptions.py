#from settings import name, version, language
import sys

name = 'ytbd'
language = 'fi'
version = '0.0'

'''
All descriptions for commands are defined here.

Update this catalog as you add new commands.
'''

formattedName = '{}{}'.format(name[0].upper(), name[1:])
version = '{} {}'.format(formattedName, version)

if language == 'us':
  usage = '''Usage: {} [OPTIONS] <COMMAND>'''.format(name)
  description = '''Create projects efficiently any where with {}!'''.format(name)
  help_messages = '''
  Get help:
    -h,  --help                       Print this help message
    -V,  --version                    Print program version
    
  Project creation:
    create NAME                       Create new project as NAME.
                                      Markdown files like README and
                                      CHANGES will be created as well.
    -c,  --capitalized-markdowns      Create the markdown files using
                                      all caps. (Off by default)

  Verbose mode:
    -v,  --verbose                    Be verbose when creating new project,
                                      listing it as it is being created.
                                      (Error messages are displayed always
                                      no matter if this flag was used or not)'''

elif language == 'fi':
  usage = '''Käyttö: {} [VALITSIMET] <KOMENTO>'''.format(name)
  description = '''Luo projekteja tehokkaasti missä vain hyödyntäen {} projektinluomis työkalua!'''.format(name)
  help_messages = '''
  Avun saanti:
    -h,  --help                       Tulosta tämä viesti
    -V,  --version                    Tulosta ohjelman versio
    
  Projektin luominen:
    create NIMI                       Luo uusi projekti nimellä NIMI.
                                      Markdown tiedostot kuten README
                                      ja CHANGES luodaan myös.
    -c,  --capitalized-markdowns      Luo markdown tiedostot käyttäen
                                      isoja kirjaimia. (Oletuksena pois
                                      päältä)

  Apuviestit:
    -v,  --verbose                    Listaa projektin nimi, kun sitä
                                      ollaan luomassa. (Virheviestit
                                      tulostetaan aina, käytettiin tätä
                                      valitsinta tai ei)'''

# If language specified in settings.py is not available, use english.
else:
  usage = '''Usage: {} [OPTIONS] <COMMAND>'''.format(name)
  description = '''Create projects efficiently any where with {}!'''.format(name)
  help_messages = '''
  Get help:
    -h,  --help                       Print this help message
    -V,  --version                    Print program version
    
  Create project:
    create NAME                       Create new project as NAME.
                                      Markdown files like README and
                                      CHANGES will be created as well.
    -c,  --capitalized-markdowns      Create the markdown files using
                                      all caps. (Off by default)

  Verbose mode:
    -v,  --verbose                    Be verbose when creating new project,
                                      listing it as it is being created.
                                      (Error messages are displayed always
                                      no matter if this flag was used or not)'''