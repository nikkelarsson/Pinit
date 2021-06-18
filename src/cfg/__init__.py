
"""
 *  File: __init__.py
 *  Desc: Basic configurations.
 *  Auth: Niklas Larsson
"""

# NOTE: I'm not sure do I want to keep this config
# stuff in src/cfg forever... It would make more
# sense to keep this stuff in the src instead?

# New name suggestion => pyinit
# Why? Because this going to be initializer for
# python projects, thus the new suggestion.
NAME: str = "pinit"
VERSION: str = "0.0"
LANGUAGE: str = "fi"

if NAME == "":
	raise ValueError("’NAME’ needs a valid, non empty value; default should be ’pinit’.")
if VERSION == "":
	raise ValueError("’VERSION’ needs a valid, non empty value.")
if LANGUAGE == "":
	raise ValueError("’LANGUAGE’ needs a valid, non empty value, like ’eng’.")
