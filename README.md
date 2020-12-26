## Pinit (Project Initializer)
Pinit is a command line tool that is intended to be used to improve your progamming workflow.

Basic use is `pinit [PROJECT] [OPTIONS]`

## List of available flags
- `--add-readme` to create readme file during project initialization
- `--add-gitignore` to create gitignore file during init
- `NAME` to choose a name for the project that is going to be created

These are not all the available flags, but using `--help` or `-h` you get the full list
of available ones.

## Installation
**Clone**
```
git clone https://github.com/nikkelarsson/Pinit.git
```

## How to use Pinit
1. Either run it with `python3`
2. Or compile it and run as binary

**Run with python**
```
python3 main.py
```

**Compile and run as binary**
* First compile (`nuitka` works good for this)
```
python3 -m nuitka --follow-imports main.py
```

* After compiling you'll have `main.bin` (Mac) or just `main` (Linux)
* Then you can rename `main.bin` (or `main`) to `pinit` and use as is
```
./pinit
```

* Or move the binary somewhere more appropriate, like `usr/local/bin` and then run:
```
pinit
```

## Project creation
**Create a project with README.md**
```
pinit myproject --add-readme
```
or
```
pinit myproject --add-readme=yes
```

**Create a project without README.md**
```
pinit myproject
```
or
```
pinit myproject --add-readme=no
```

**Silence output**
```
pinit myproject --silent
```

**Create a project with .gitignore**
```
pinit myproject --add-gitignore
```

**Create a project with both README.md + .gitignore**
```
pinit myproject --add-gitignore --add-readme
```
