# cpm

castis package manager.

(Yes, inspired by npm.)

## Install

```
$ wget -O - https://raw.githubusercontent.com/castisdev/cpm/master/install.sh --no-check-certificate | bash
```

## Example Usage

```bash
# install
$ wget -O - https://raw.githubusercontent.com/castisdev/cpm/master/install.sh --no-check-certificate | bash
installing cpm...
...
...done.

# get help message 
$ cpm help

Usage: cpm <command>
where <command> is one of:
    help, info, init, install, list, remove, update

# show list of installed packages
$ cpm list
/home/mnpk/.cpm/src
└──  cpm@0.1.0

# install ctail package
$ cpm install ctail
...
installed ctail at: /home/mnpk/.cpm/src/ctail

$ cpm list
/home/mnpk/.cpm/src
├──  ctail@0.1.0
└──  cpm@0.1.0
```
