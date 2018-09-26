# -- coding: utf-8 --
from sys import argv

script, filename = argv

txt = open(filename)

print "file: %r", filename

print txt.read().decode('utf-8')

file_again = raw_input(">")

txt_again = open(file_again)

print "---------------------------------------",txt_again.readline()

txt.close()
txt_again