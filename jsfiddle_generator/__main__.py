#!/usr/bin/env python
"""generate jsfiddle files: `demo.css`, `demo.js`, `demo.html`, `demo.details`"""
# -*- coding: utf-8 -*-
import click
import os
import jsfiddle_generator

MODULE_NAME = "jsfiddle_generator"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s path ...' % MODULE_NAME


@click.command()
@click.argument('paths', nargs=-1, required=True)
def _cli(paths):
    cwd = os.getcwd()
    for path in list(set(paths)):
        os.chdir(cwd)
        if os.path.exists(path) and os.path.isfile(path):
            path = os.path.dirname(path)
        if not os.path.exists(path):
            os.makedirs(path)
        os.chdir(path)
        jsfiddle_generator.JSFiddle().create()


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
