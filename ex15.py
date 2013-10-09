from sys import argv

script, file_name = argv

txt = open(file_name)

print 'Here are the contents of "%s":' % file_name,
print txt.read()