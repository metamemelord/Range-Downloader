import sys
import os
from lib import *

def main():
    try:
        if len(sys.argv)  < 5:
            exit("""\nPlease provide <start_index (integer)> <end_index (integer)> <base_url> <extension> <optional: index_to_skip_1> <optional: index_to_skip_2> ...\n\nExample: python %project_root%/main.py 1 5 Something-I-Want-To-Download.com/this jpg 3 4\n\nThis will try to download:
            %project_root%/this/this1.jpg
            %project_root%/this/this2.jpg
            %project_root%/this/this5.jpg""")
        do = DownloadObject()
        do.start = int(sys.argv[1])
        do.end = int(sys.argv[2])
        do.url = sys.argv[3]
        do.extension = sys.argv[4]
        if len(sys.argv) > 5:
            do.skip = set(int(arg) for arg in sys.argv[5:])
        final_directory = do.url.split("/")[-1]
        rce = RestCallExecuter()
        rce.download_object = do
        found = 0
        for data in rce.execute():
            if data != None:
                fs = FileSaver()
                print(fs.save(data, final_directory))
                found = 1
            else:
                print("Call failed")
        if found:
            print("\nDownloaded files saved in %s"%(os.path.realpath(os.path.join(os.getcwd(), "Downloads", final_directory))))
    except KeyboardInterrupt:
        print("\nAborted by user")
    except Exception as e:
        print(e)

main()