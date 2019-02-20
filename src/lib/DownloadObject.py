class DownloadObject(object):
    def __init__(self):
        self.__start = 0
        self.__end = 1
        self.__skip = []
        self.__url = ""

    @property
    def start(self):
        return self.__start
    @start.setter
    def start(self, start):
        self.__start = start
    
    @property
    def end(self):
        return self.__end
    @end.setter
    def end(self, start):
        self.__end = start
    
    @property
    def skip(self):
        return self.__skip
    @skip.setter
    def skip(self, skip):
        self.__skip = skip
    
    @property
    def url(self):
        return self.__url
    @url.setter
    def url(self, url):
        self.__url = url