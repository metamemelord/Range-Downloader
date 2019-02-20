from requests import *

class RestCallExecuter(object):
    def __init__(self):
        self.__download_object = None
    @property
    def download_object(self):
        return __download_object
    @download_object.setter
    def download_object(self, download_object):
        self.__download_object = download_object

    def execute(self):
        if self.download_object == None:
            raise ValueError("Resources not set")
            exit(1)

        for idx in range(self.download_object.start, self.download_object.end + 1):
            final_url = self.download_object.start + str(idx)
            res = request.get(final_url)
            if res.status_code == 200:
                print("Downloaded %s"%final_url)
                yield res.body
            else:
                print("Error while retrieving %s"%final_url)