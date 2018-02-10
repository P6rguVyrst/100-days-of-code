# -*- coding: utf-8 -*-

"""Console script for testingapp."""

import click


@click.command()
def main(args=None):
    """Console script for testingapp."""
    click.echo("Replace this message by putting your code into "
               "testingapp.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


if __name__ == "__main__":
    main()
