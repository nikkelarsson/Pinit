# Changelog

All changes to Pinit will be documented in this file.

## [Unreleased] – 2021

### Added

- `create` as a base command to create new
  projects.  It creates (by default) all useful
  files (readme.md, changes.md, gitignore) in
  the location specified.  Also, the readme +
  changes will be populated with a template
  every time you create a project, so you don't
  have to write everything from scratch.

- Ability to create a project to custom
  location by providing a path.

- `-v` and `--verbose` to be informative, when
  creating files.

- `-c` and `--capitalized-markdowns` to create
  markdown files using all caps. The idea
  behind this feature is to give option to
  users that prefer markdown files written in
  all caps.

### Changed

- Parsing command line args from `argparse` to
  manually written parsing.

### Removed

- `--add-readme, --silent, --add-gitignore`
  because it made a lot more sense to
  automatically include these files in the init
  process - you'd probably create them anyway.
  Also, `--silent` is no longer needed, because
  Pinit is now ”silent” by default.

## [0.3.0] – 2020-12-26

### Added

- `--add-gitignore` to create gitignore during init.

## [0.2.0] – 2020-12-25

### Added

- `--silent` to silence stdout, except errors.

## [0.1.0] – 2020-12-21

### Added

- Project creation / init functionality.

- `--add-readme` to create readme.md during init.

- `--silent` to silence stdout, except errors.
