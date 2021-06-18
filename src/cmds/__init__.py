
"""
 *  File: __init__.py  
 *  Desc: Catalog of available commands and flags.
 *  Auth: Niklas Larsson
"""

#
# Description information.
#
# < Commands >
# 1. create..........Create new project.
#
#
# < Flags >
# 1. help............Print command's and flag's descriptions.
# 2. version.........Print program's version.
# 3. silent..........Don't print any output, except errors.
# 4. summary.........Print a summary what was created.

# Imports here are sorted alphabetically.
import cmds.create
import cmds.help
import cmds.version

# Available commands and flags. Maybe sort them here alphabetically too?
commands: dict = {}
flags: dict = {}

# Commands
commands["create"] = {"long" : "create"}

# Flags
flags["git"] = {"long" : "--init-as-git"}
flags["help"] = {"short" : "-h", "long" : "--help"}
flags["version"] = {"short" : "-V", "long" : "--version"}
flags["silent"] = {"short" : "-s", "long" : "--silent"}
flags["summary"] = {"short" : "-S", "long" : "--summary"}
