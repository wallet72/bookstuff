#!/usr/bin/python

# my first python program
# will take ARGV[0] as the starting directory and will begin to process the contents.
#
# if file then decide if epub or mobi or txt or pdf
#   then add full path to html file that will give access to file
# if dir then navigate into dir
#   and process
#
# long term, would like to pull ebook info and add it to database
# with a web interface to pull book out of 'library'
#
# but we walk before we attempt a marathon :)
#
# and I hate the way Python uses indentation for loops and shit,
# how hard is it to just use something to actually close a loop?
#
#

# import stuff here..
import sys
import os
import ebooklib
#import pypdf2
from PyPDF2 import PdfFileReader

MOBI_FILE = "mobi_list.html"
EPUB_FILE = "epub_list.html"
PDF_FILE = "pdf_list.html"
TXT_FILE = "txt_list.html"
BIG_FILE = "big_list.html"
HUH_FILE = "unknown_list.html"



# number of arguments
if len(sys.argv) < 2:
    sys.exit("I don't think you specified a directory")

PATH = sys.argv[1]

# lazy sanity check for starting directory
if len(PATH) < 3:
    #print "Your starting directory is..." + PATH
    sys.exit("I don't think your starting directory is right")


# open all the files for writing.
# this will wipe the existing files.

MOBI = open(MOBI_FILE,'w')
EPUB = open(EPUB_FILE,'w')
PDF = open(PDF_FILE,'w')
TXT = open(TXT_FILE,'w')
BIG = open(BIG_FILE,'w')
HUH = open(HUH_FILE,'w')



# defs goes here

# so should we/how can we use a def to handle writing to files


# so what kind of file is it?
def check_file(name):

    # just need the last bit of the filename, using that to decide how
    # to get the metadata
    stuff = name.split(".")
    doctype = stuff[-1]

    # loop de loop de loop
    if doctype == 'pdf':
        book = PdfFileReader(open(name, 'rb'))
        dict = book.getDocumentInfo()
        print "Found book: " + dict.title + " - " + name
        PDF.write(dict.title)


        #TODO: write to html file for pdf docs

    elif doctype == 'epub':
        book = ebooklib.epub.read_epub(name)
        print "Found book: " + book.read_title + " - " + name
        EPUB.write(book.read_title)


        #TODO: write to html for epub docs


    elif doctype == 'mobi':
        book = ebooklib.epub.read_mobi(name)
        print "Found book: " + book.read_title + " - " + name
        MOBI.write(book.read_title)

        #TODO: write to html file for mobi docs


    elif doctype == 'txt':

        print "Found book: " + name + " - " + name
        TXT.write(name)

        #TODO: write to html file for txt docs

    else:

        print "Found book: " + name + " - " + name

        #TODO: write to other html file

    # dump the filename to file
    HUH.write(name)

    #end def check_file


# is it a file or a directory?
def check_target(name,recurse):
    for item in os.listdir(name):
        FULLPATH = os.path.join(name,item)

        if os.path.isfile(FULLPATH):
            check_file(FULLPATH)

        elif os.path.isdir(FULLPATH):
            check_target(FULLPATH,recurse)

# end def check_target






# start here
check_target(PATH,0)

