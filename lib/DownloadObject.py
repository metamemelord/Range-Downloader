class DownloadObject(object):
    def __init__(self):
        self.__start = 0
        self.__end = 1
        self.__url = ""
        self.__extension = ""
        self.__string_to_append = ""
        self.__skip = set()

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

    @property
    def extension(self):
        return self.__extension
    @extension.setter
    def extension(self, extension):
        self.__extension = extension

    @property
    def string_to_append(self):
        return self.__string_to_append
    @string_to_append.setter
    def string_to_append(self, string_to_append):
        self.__string_to_append = string_to_append