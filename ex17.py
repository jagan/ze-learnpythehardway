from sys import argv
from os.path import exists

script, from_file, to_file = argv

text = open(from_file).read()

print '%s file exists already? %s' % (to_file, exists(to_file))
raw_input('About to copy file. Press ENTER to continue or Ctrl C to abort.')

writer = open(to_file, 'w')
writer.write(text)

print 'File copied!'

writer.close()

