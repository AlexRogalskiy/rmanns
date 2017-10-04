import os
import time
import sys

PDF = '.pdf'

# Annotations
SITES = ''.join([
    '-e "s/www.it-ebooks.info/ /" ',
    '-e "s/www.allitebooks.com/ /" ',
])


def install_pdftk():
    """
    If sys.platform is linux then install pdftk using apt.
    """
    os.system('sudo apt update')
    os.system('sudo apt install pdftk')


def clean(file_name):
    """
    Correctify name of file for pdftk.
    """
    file_name = file_name.replace(' ', '_') \
        .replace('(', '') \
        .replace(')', '') \
        .replace(',', '') \
        .replace('-', '-') \
        .replace('!', '')

    return file_name


def rename(path):
    """
    Rename file.
    """
    for file in os.listdir(path):
        if file.endswith(PDF):
            if ' ' in file:
                os.rename(file, clean(file))


def finalize(file):
    os.remove('{file}'.format(file=file))
    os.remove('{file}1'.format(file=file))
    os.system('pdftk {file}2 output {file} compress'.format(file=file))
    os.remove('{file}2'.format(file=file))
    print('\033[92mAnnotations removed from file\033[0m: \033[33m{0}\033[0m.'.format(file))


def remove_annots(path):
    """
    Remove annotations from file.
    """
    rename(path)
    cmd = 'pdftk {file} output {file}1 uncompress'
    cmd_sed = 'sed {sites} {file}1 > {file}2'

    for file in os.listdir(path):
        if file.endswith(PDF):
            os.system(cmd.format(file=file))
            os.system(cmd_sed.format(file=file, sites=SITES))

            time.sleep(0.5)
            finalize(file)


if __name__ == '__main__':
    aw = input('Are you sure? [y/n]: ')
    if aw.lower() in ['y', 'yes']:

        if sys.platform == 'linux':
            # install_pdftk()
            pass

        remove_annots(os.curdir)
