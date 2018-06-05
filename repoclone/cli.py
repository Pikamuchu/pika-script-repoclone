# -*- coding: utf-8 -*-

"""Console script for repoclone."""

import sys
import click

from .repoclone import repoclone
from .exceptions import (
    RepocloneException,
    RepositoryCloneFailed
)

@click.command()
@click.argument(u'host')
@click.option(
    u'-u', u'--user',
    help=u'Repository user',
)
@click.option(
    u'-p', u'--password',
    help=u'Repository password',
)
@click.option(
    u'-d', u'--clone_dir',
    help=u'Repository clone directory',
)
def main(host=None, user=None, password=None, clone_dir=None):
    """Console script for repoclone."""

    click.secho("**** Running repoclone ****", fg="green")

    click.echo("* host = " + host)
    if not user is None:
        click.echo("* user = " + user)

    if not clone_dir is None:
        click.echo("* clone_dir = " + clone_dir)

    click.echo("")

    try:
        repoclone(type=type, host=host, user=user, password=password,
                clone_dir=clone_dir)
    except (RepocloneException,
            RepositoryCloneFailed) as e:
        click.secho("Error: " + str(e), fg="red")
        return 1

    click.echo("")
    click.secho("**** Repoclone finish succesfully!! ****", fg="green")

    return 0

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
