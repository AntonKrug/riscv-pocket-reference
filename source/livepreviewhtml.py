#!/usr/bin/env python

from livereload import Server, shell
import formic

sourcedir = './'
builddir = '../build/'

def previewHtml():
    server = Server()

    for filepath in formic.FileSet(include=sourcedir, exclude=[sourcedir +"/*_generated/**"]):
        print("Watching: " + filepath)
        server.watch(filepath, 'make html')

    server.serve(root=builddir+'html',open_url=False,host='0.0.0.0')

 