import os

# Printing directories and sub directories

listOfDirs = []
listOfFiles = []
for dirname, dirnames, filenames in os.walk('.'):
    # print path to all subdirectories first.
    print('DIRS')
    for subdirname in dirnames:
        listOfDirs.append(os.path.join(dirname, subdirname))

    print('-------------------')

    # print path to all filenames.
    print('FILES')
    for filename in filenames:
        listOfFiles.append(os.path.join(dirname, filename))

print(listOfDirs)
print(listOfFiles)
