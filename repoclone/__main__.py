# -*- coding: utf-8 -*-
"""Allow repoclone to be executable through `python -m repoclone`."""
from __future__ import absolute_import

from .cli import main

if __name__ == "__main__":  # pragma: no cover
    main()
