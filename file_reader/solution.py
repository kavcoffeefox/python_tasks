class FileReader:
    """This class for read file"""

    def __init__(self, file_path):
        self._file_path = file_path

    def read(self):
        try:
            fl = open(self._file_path)
            return fl.read()
        except IOError as err:
            return ""


reader = FileReader("example.txt")
print(reader.read())
