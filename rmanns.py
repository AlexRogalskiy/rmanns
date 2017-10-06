import os
import time
import sys

PDF = '.pdf'

# Annotations
ANNOTATIONS = ''.join([
    '-e "s/www.it-ebooks.info/ /" ',
    '-e "s/www.allitebooks.com/ /" ',
    '-e "s/WWW.EBOOK777.COM/ /" ',
    '-e "s/www.ebook777.com/ /" ',
    '-e "s/free ebooks ==>/ /" ',
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
    os.remove('{file}2'.format(file=file))

    print(
        '\033[92m{msg}\033[0m: \033[33m{file}\033[0m.'.format(
            file=file,
            msg='Annotations removed from file')
    )


def remove_annots(path):
    """
    Remove annotations from file.
    """
    rename(path)
    cmd_uncompress = 'pdftk {file} output {file}1 uncompress'
    cmd_sed = 'sed {annotations} {file}1 > {file}2'
    cmd_compress = 'pdftk {file}2 output {file} compress'

    for file in os.listdir(path):
        if file.endswith(PDF):
            os.system(cmd_uncompress.format(file=file))
            os.system(cmd_sed.format(file=file, annotations=ANNOTATIONS))
            os.system(cmd_compress.format(file=file))

            time.sleep(0.1)
            finalize(file)


if __name__ == '__main__':
    aw = input('Are you sure? [y/n]: ')
    if aw.lower() in ['y', 'yes']:

        if sys.platform == 'linux':
            # install_pdftk()
            pass

        remove_annots(os.curdir)
