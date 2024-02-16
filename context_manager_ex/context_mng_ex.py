import os
from contextlib import contextmanager


f = open('sample. txt', 'w')
f.write('This is test.')
f. close()

with open('sample.txt', 'w') as f:
    f.write('This is test.')


class OpenFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def _enter__(self):
        self. file = open(self. filename, self .mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self. file. close()


with OpenFile('sample.txt', 'W') as f:
    f.write('Testing')

print(f.closed)


@contextmanager
def open_file(file, mode):
    f = open(file, mode)
    yield f
    f.close()


with open_file('sample.txt', 'w') as f:
    f.write('This is test.')

print(f.closed)


cwd = os.getcwd()   # get current working directory
os.chdir('directory_1')  # changing directory
print(os.listdir())     # listing files
os.chdir(cwd)   # changing directory back to current

cwd = os.getcwd()
os.chdir('directory_2')
print(os.listdir())
os.chdir(cwd)


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir('directory_1'):
    print(os.listdir())
with change_dir('directory_2'):
    print(os.listdir())
