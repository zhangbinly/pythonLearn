from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copy %r --> %r" %(from_file,to_file)

input = open(from_file)
indata = input.read()
print "the input length: %d" %len(indata)

print "Does the output file exist? %r" % exists(to_file)

raw_input()

output = open(to_file, 'w')
output.write(indata)

print "all Done"

output.close
input.close

