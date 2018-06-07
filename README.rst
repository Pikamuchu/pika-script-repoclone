================
Repository Clone
================


.. image:: https://img.shields.io/pypi/v/repoclone.svg
        :target: https://pypi.python.org/pypi/repoclone

.. image:: https://travis-ci.org/pikamachu/pika-script-repoclone.svg?branch=master
        :target: https://travis-ci.org/pikamachu/pika-script-repoclone

.. image:: https://api.codacy.com/project/badge/Grade/e4a158fab8ee46b790529ad8169e9b96
        :target: https://www.codacy.com/app/antonio.marin.jimenez/pika-jwt-services-gateway?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=pikamachu/pika-jwt-services-gateway&amp;utm_campaign=Badge_Grade

.. image:: https://readthedocs.org/projects/repoclone/badge/?version=latest
        :target: https://repoclone.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

Script for repository clone and update (origin pull).


* Free software: MIT license
* Documentation: https://repoclone.readthedocs.io.


Features
--------

Python script for batch git clone and update (origin pull) from bitbucket and github repositories.

Installation
------------
pip install repoclone

Usage
-----

Usage: repoclone [OPTIONS] HOST

  Console script for repoclone.

Options:
  -u, --user TEXT       Repository user
  -p, --password TEXT   Repository password
  -d, --clone_dir TEXT  Repository clone directory
  --help                Show this message and exit.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
