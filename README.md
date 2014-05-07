Snakefire for Ubuntu
===================================

[Snakefire](http://snakefire.org) is a desktop client for [Campfire](https://campfirenow.com/) that can run on Linux, and any other OS that has QT support.

It's based on [pyfire](https://github.com/mariano/pyfire), a Campfire API written in python.

This repo was built to create a binary package for **Ubuntu 14.04** (Trusty Tahr). It's a complete rewrite of the package building scripts, using newer [`debhelper`](http://manpages.ubuntu.com/manpages/trusty/man7/debhelper.7.html) version and [`dh_python2`](http://manpages.ubuntu.com/manpages/precise/man1/dh_python2.1.html) as replacement for [deprecated `python_support`](http://article.gmane.org/gmane.linux.debian.devel.python/6948).

This Snakefire version uses different [Snakefire forks](https://github.com/mariano/snakefire/network), like original [Mariano Snakefire](https://github.com/mariano/snakefire) and some CSS changes from [James Broadhead fork](https://github.com/jamesbroadhead/snakefire).


## Install

Open a terminal (`Ctrl+Alt+T`) and run:

```term
sudo apt-add-repository -y ppa:rael-gc/snakefire
sudo apt-get update
sudo apt-get install snakefire
```

If you're using **KDE** additionally install `snakefire-kde`:

```
sudo apt-get install snakefire-kde
```

### Spell checking

For spell checking, you now need to install the related `aspell` dictionary. 

For example, to install the english dictionary:

```term
sudo apt-get install aspell-en
```

## License

Snakefire and Pyfire are released under the [MIT License](LICENSE).
