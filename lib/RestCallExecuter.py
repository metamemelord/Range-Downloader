import requests
from .File import File

class RestCallExecuter(object):
    def __init__(self):
        self.__download_object = None
    @property
    def download_object(self):
        return self.__download_object
    @download_object.setter
    def download_object(self, download_object):
        self.__download_object = download_object

    def execute(self):
        try:
            if self.download_object == None:
                raise ValueError("Resources not set")
            for idx in range(self.download_object.start, self.download_object.end + 1):
                if idx in self.download_object.skip:
                    continue
                final_url = self.download_object.url + str(idx) + "." + self.download_object.extension
                filename = final_url.split('/')[-1].split(".")
                if len(self.download_object.string_to_append):
                    filename[0] += "-" + self.download_object.string_to_append
                filename = ".".join(filename)
                res = requests.get(final_url)
                if res.status_code == 200:
                    print("Downloaded %s"%filename)
                    yield File(filename, res.content)
                else:
                    print("Error while retrieving %s"%final_url)
                    yield None

        except ValueError as ve:
            print(ve)
            yield None
        except Exception as e:
            print(e)
            yield None