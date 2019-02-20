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

    def save(self, data, directory):
        if self.filename == None or self.extension == None:
            raise ValueError("Filename or extension not set")
        try:
            download_folder = os.path.realpath(os.path.join(os.getcwd(), "..", "..", "Downloads"))
            final_path = os.path.join(download_folder, directory)
            if not os.path.isdir(download_folder):
                os.makedirs(download_folder)
            if not os.path.isdir(final_path):
                os.makedirs(final_path)
            print(os.path.join(final_path, self.filename + "." + self.extension), data)
            with open(os.path.join(final_path, self.filename + "." + self.extension), 'wb') as f:
                f.write(data)
            return "Ok"
        except ValueError:
            return "Could not save the data"
        except PermissionError:
            return "Operation not permitted by OS"
        except OSError:
            return "Operation not permitted by OS"
        except Exception as e:
            return e