import urllib.request
import zipfile
import os

def update():
    url = 'https://g400-59.is.oit.ac.jp/minecraft/python.zip'
    with urllib.request.urlopen(url) as u:
        with open('python.zip', 'bw') as o:
            o.write(u.read())

def unzip():
    with zipfile.ZipFile('python.zip') as zip_f:
        zip_f.extractall('.')
    os.remove('python.zip')

if __name__ == '__main__':
    update()
    unzip()