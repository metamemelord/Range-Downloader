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
            if self.__download_object == None:
                raise ValueError("Resources not set")
                exit(1)
            for idx in range(self.__download_object.start, self.__download_object.end + 1):
                final_url = self.__download_object.url + str(idx) + "." + self.download_object.extension
                filename = final_url.split('/')[-1]
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