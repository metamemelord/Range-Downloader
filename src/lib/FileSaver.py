import os

class FileSaver(object):
    def __init__(self):
        self.__filename = None
        self.__extension = None
    
    @property
    def filename(self):
        return self.__filename
    
    @filename.setter
    def filename(self, filename):
        self.__filename = filename

    @property
    def extension(self):
        return self.__extension
    
    @extension.setter
    def extension(self, extension):
        self.__extension = extension

    def save(self, data):
        if self.filename == None:
            raise ValueError("Filename not set")
        try:
            with(os.path.join(__path__, "../downloads", self.filename, self.extension), 'wb') as f:
                f.write(data)
            return "Ok"
        except ValueError:
            return "Could not save the data"
        except Error as e:
            return e.message