import sys
import click
try:
    from .funcs import *
except ImportError:
    from funcs import *


@click.group()
@click.version_option("0.0.1")
def main():
    pass


@main.command()
def init(**kwargs):
    initialize()


@main.command()
@click.argument('name', required=True)
def run(**kwargs):
    name = kwargs.pop('name')
    while not name:
        name = input('Enter name of script to run')
    runScript(name)


@main.command()
@click.option('-n', '--name', 'name', required=False)
@click.option('-c', '--command', 'command', required=False)
def add(**kwargs):
    name = kwargs.pop('name')
    command = kwargs.pop('command')
    while not name:
        name = input('Enter name for script: ')
    while not command:
        command = input('Enter command for script: ')
    addScript(name, command)


@main.command()
def list(**kwargs):
    scripts = loadScripts()
    for name, command in scripts.items():
        print(f'{name} >>> {command}')


@main.command()
@click.option('-n', '--name', 'name', required=False)
def rm(**kwargs):
    name = kwargs.pop('name')
    while not name:
        name = input('Enter name of script to remove: ')
    removeScript(name)


if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("py-scripts")
    main()