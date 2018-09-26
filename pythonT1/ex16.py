from sys import argv

script, filename = argv
print "Open the file ..."
txt = open(filename,'w')

txt.truncate()

line1 = raw_input("line1:")
line2 = raw_input("line2:")

txt.write(line1)
txt.write(line2)

print txt.read().decode('utf-8')

txt.close