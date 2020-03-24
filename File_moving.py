import os,shutil

from os.path import splitext

def createFolder(directory):

	if not os.path.exists(directory):
		os.makedirs(directory)
		print(directory + " Directory Created")
	else:
		print("The required Folder already exists")

createFolder('./C_programs/')
createFolder('./Cpp_programs/')
createFolder('./Python_programs/')

cf = 0
cppf = 0
pf = 0

cwd = os.getcwd()

for files in os.listdir(cwd):
	file_name, extension = splitext(files)
	if extension == '.c' or extension == '.save':
		shutil.move(files, 'C_programs')
		cf = cf + 1
	elif extension == '.cpp':
		shutil.move(files, 'Cpp_programs')
		cppf = cppf + 1
	elif extension == '.py':
		shutil.move(files, 'Python_programs')
		pf = pf + 1

print("No. of c files moved:",cf)
print("No. of cpp files moved:",cppf)
print("No. of cpp files moved:",pf)

