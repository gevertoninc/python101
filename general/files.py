READ = 'r'
APPEND = 'a'
OVERWRITE = 'w'
LINE_BUFFERING = 1
UTF8 = 'utf8'

file = open('../util/file', OVERWRITE, LINE_BUFFERING, UTF8)
file.write('Create file\n')
file.write('Create line\n')

print('\tfile.readable()')
print(file.readable())

file = open('../util/file')

print('\tfile.readline()')
print(file.readline())

file = open('../util/file')

print('\tfile.readlines()[1]')
print(file.readlines()[1])

file = open('../util/file', OVERWRITE, LINE_BUFFERING, UTF8)
file.write('Dobby is not free\n')
file = open('../util/file', READ, LINE_BUFFERING, UTF8)

print('\tfile.readlines()')
print(file.readlines())

file = open('../util/file', APPEND, LINE_BUFFERING, UTF8)
file.write('Dobby is free\n')
file = open('../util/file', READ, LINE_BUFFERING, UTF8)

print('\tfile.read()')
print(file.read())
