# Pinit (Project Initializer)

Pinit is an efficient and easy-to-use tool for
starting a new project, as it creates all the
necessary files that you'd probably create anyway.

![Screenshot](photos/CreateGif.gif)

## Installation

``` bash
git clone https://github.com/nikkelarsson/Pinit.git
```

## Requirements

* python >= 3

* Add other requirements here...

## Getting started

You can run Pinit as is with the Python interpreter
every time you want to use it.

However, this is not the most efficient way of using it.

A better way of using Pinit is by compiling it and then
putting the binary somewhere appropriate.

For this, Python module called `nuitka` comes in.

What `nuitka` does is it transforms the python code
into c code, and then compiles the c code.

You could also create a `bin` folder somewhere, add
that folder to your `PATH` and use Pinit that way.
Obviously the name isn't important – you can name
the folder what ever you want, `programs` for example,
but `bin` is usually quite recognizable name thus
a good choice for this.
This way you don't have to put the binary somewhere
you don't know. You can add the `bin` into your
`PATH` by adding the following either in .bashrc *or*
.zshrc:

``` bash
export PATH="path/to/your/bin/folder:$PATH"
```

For your knowledge, there is an installation script
that compiles Pinit for you. So, if you don't want to
do the compiling yourself, just use the install script!

### Compile manually

``` bash
python3 -m nuitka -o pinit --remove-output main.py
```

Using the `--remove-output` nuitka will not produce
the `build` directory it usually would after compiling;
this is just to avoid extra cleaning.

### Install using the installation script

``` bash
chmod +x install.sh
```

``` bash
./install.sh
```

And that should do it!  
Now you have the binary, `pinit`.
You can test that it works by invoking:

``` bash
./pinit
```

It should print the usage message for you.

Now you can create the `bin` folder, add it to your
`PATH` and either *move the binary*  or *symlink it* there, either way will work though symlinking is maybe
smarter solution as you don't have to move files around.

### Symlink

``` bash
ln -s pinit /path/to/your/bin/folder/
```

And... done! Now you can start using Pinit!

## Usage

This is the basic usage.

``` bash
pinit [OPTIONS] create <PROJECT_NAME>
```
