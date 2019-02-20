import sys
from lib import RestCallExecuter
from lib import DownloadObject
from lib import FileSaver

def main():
    try:
        if len(sys.argv)  < 5:
            exit("""Please provide <start_index (integer)> <end_index (integer)> <base_url> <extension>\n\nExample: python main.py 1 5 Something-I-Want-To-Download.com/this jpg\n\nThis will try to download:
            Something-I-Want-To-Download.com/this1.jpg
            Something-I-Want-To-Download.com/this2.jpg
            Something-I-Want-To-Download.com/this3.jpg
            Something-I-Want-To-Download.com/this4.jpg
            Something-I-Want-To-Download.com/this5.jpg""")
        do = DownloadObject()
        do.start = int(sys.argv[1])
        do.end = int(sys.argv[2])
        do.url = sys.argv[3]
        do.extension = sys.argv[4]
        final_directory = do.url.split("/")[-1]
        rce = RestCallExecuter()
        rce.download_object = do
        for data in rce.execute():
            if data != None:
                fs = FileSaver()
                print(fs.save(data, final_directory))
            else:
                print("Call failed")
    except KeyboardInterrupt:
        print("\nAborted by user")

main()