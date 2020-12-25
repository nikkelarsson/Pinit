## Pinit (Project Initializer)
Pinit is a command line tool that is intended to be used to improve your progamming workflow.
Basic use is `pinit [PROJECT] [OPTIONS]`

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
