
"""
 *  File: globs.py
 *  Desc: Some global variables.
 *  Auth: Niklas Larsson
"""
 
import cfg
import cmds
import string

# The scandinavian letters are here 'just in case'.
ASCII_LOWERCASE_LETTERS: str = string.ascii_lowercase
SCANDINAVIAN_LOWERCASE_LETTERS: str = 'öäåø'
LETTERS_LOWERCASE: str = ASCII_LOWERCASE_LETTERS + SCANDINAVIAN_LOWERCASE_LETTERS

SETTINGS: dict = {
		"program": cfg.NAME,
		"version": cfg.VERSION,
		"language": cfg.LANGUAGE
		}

# Initialize descriptions.
def init_descriptions() -> object:
	if cfg.LANGUAGE == 'fi':
		descriptions = cmds.help.Finnish(cfg.NAME, cfg.VERSION)
	elif cfg.LANGUAGE == 'eng':
		descriptions = cmds.help.English(cfg.NAME, cfg.VERSION)
	return descriptions


descriptions = init_descriptions()
