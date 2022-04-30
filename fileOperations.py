import sys

class FileManager():

    file = None

    def __init__(self, file):
        self.file = file
    
    def write(self, text):
        f = open(self.file, 'a')
        f.write(text)
        f.close()
    
    def read(self):
        r = open(self.file, 'r')
        return r.read()

file_name = sys.argv[1]

if len(file_name) > 0:
    manager = FileManager(file_name)
    text = raw_input('Write some text: ')
    manager.write(text)
    content = manager.read()
    print("File content: {}".format(content))