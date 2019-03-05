import sys
import os
from datetime import datetime
from lib import *

success = 0
failed_tasks = set()
do = DownloadObject()
idx = -1
exit_message = """\nPlease provide required arguments <base_url> <file_extension> <start_index (integer)> <end_index (integer)> 
Optional arguments: <string to append to filenames> <index_to_skip_1 (integer)> <index_to_skip_2 (integer)> ...\n\nExample: python %project_root%/main.py https://Something-I-Want-To-Download.com/this jpg 1 5 test 3 4\n\nThis will try to download:
            https://Something-I-Want-To-Download.com/this1.jpg
            https://Something-I-Want-To-Download.com/this2.jpg
            https://Something-I-Want-To-Download.com/this5.jpg

And will save the files as: 
            %project_root%/Downloads/this/this1-test.jpg
            %project_root%/Downloads/this/this2-test.jpg
            %project_root%/Downloads/this/this5-test.jpg"""
            
def main():
    try:
        if len(sys.argv)  < 5:
            exit(exit_message)
        global do
        global success
        global failed_tasks
        global idx
        do.start = int(sys.argv[3])
        do.end = int(sys.argv[4])
        do.url = sys.argv[1]
        do.extension = sys.argv[2]
        if len(sys.argv) >= 6:
            do.string_to_append = sys.argv[5] if len(sys.argv[5]) else ""
        if len(sys.argv) > 6:
            do.skip = set(int(arg) for arg in sys.argv[6:])
        final_directory = do.url.split("/")[-1]
        rce = RestCallExecuter()
        rce.download_object = do
        idx = do.start
        for data in rce.execute():
            if data != None:
                fs = FileSaver()
                print(fs.save(data, final_directory))
                success += 1
            else:
                failed_tasks.add(idx)
                print("Call failed")
            idx += 1
        if success:
            result_path = os.path.realpath(os.path.join(os.getcwd(), "Downloads", final_directory))
            Report.generate(result_path, do.url, do.extension, success, failed_tasks, do.skip)
            
    except KeyboardInterrupt:
        print("\nAborted by user")
        if success:
            result_path = os.path.realpath(os.path.join(os.getcwd(), "Downloads", final_directory))
            Report.generate(result_path, do.url, do.extension, success, failed_tasks, do.skip, idx)
    except Exception as e:
        print(e)

main()