# setup.py
from setuptools import setup

setup(
  name='aces_livealert',
  version='0.1.0',
  py_modules=['aces_livealert'],
  install_requires=[
    'typer',  # Using Typer for CLI
  ],
  entry_points='''
  [console_scripts]
  aces_livealert=aces_livealert:app
  ''',
)

