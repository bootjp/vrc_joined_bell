from distutils.core import setup
import py2exe

option = {
    'bundle_files': 1,
}

setup(
    options={
        'py2exe': option,
    },
    console=[
        {'script': 'vrc_joined_bell.py'}
    ],
    zipfile=None,
)