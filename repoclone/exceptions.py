# -*- coding: utf-8 -*-

"""
repoclone.exceptions
-----------------------

All exceptions used in the Cookiecutter code base are defined here.
"""

class RepocloneException(Exception):
    """
    Base exception class. All Cookiecutter-specific exceptions should subclass
    this class.
    """

class RepositoryCloneFailed(RepocloneException):
    """Raised when a repoclone template can't be cloned."""

