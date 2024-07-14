'''
Created on Feb 1, 2022

@author: Eduardo Grana
'''
import os
import lucidity_files

if os.name == 'posix':
    ROOT = '/home/eduardograna/work/test'
else:
    ROOT = 'C:\\test\\Xfolder'


def getTemplatesPaths():
    return [os.path.join(os.path.dirname(__file__), 'templates')]


def getTemplateByName(name):
    ''' get templates in a Lucidity fashion '''
    templates = lucidity_files.discover_templates(paths=getTemplatesPaths())  # @UndefinedVariable
    return lucidity_files.get_template(name, templates)


def touch(path):
    dirname = os.path.dirname(path)
    os.makedirs(dirname, exist_ok=True)
    with open(path, 'w'):
        pass
    print('touched {}'.format(path))


def mkdir(dirname):
    os.makedirs(dirname, exist_ok=True)
    print('created dir {}'.format(dirname))
