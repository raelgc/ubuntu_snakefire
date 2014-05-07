Snakefire for Ubuntu
===================================

[Snakefire](http://snakefire.org) is a desktop client for [Campfire](https://campfirenow.com/) that can run on Linux, and any other OS that has QT support.

It's based on [pyfire](https://github.com/mariano/pyfire), a Campfire API written in python.

This repo was built to create a running version for **Ubuntu 14.04** (Trusty Tahr).

This Snakefire version uses different Snakefire forks, like original [Mariano Snakefire](https://github.com/mariano/snakefire) and some CSS changes from [James Broadhead fork](https://github.com/jamesbroadhead/snakefire) of Snakefire.


# Install

Open a terminal (`Ctrl+Alt+T`) and run:

```term
sudo apt-add-repository -y ppa:rael-gc/snakefire
sudo apt-get update
sudo apt-get install snakefire
```

## Spell checking

For spell checking, you now need to install the related aspell dictionary. 

For example, to install the english dictionary:

```term
sudo apt-get install aspell-en
```

# License

Snakefire and Pyfire are released under the [MIT License](LICENSE).
