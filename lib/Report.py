from datetime import datetime
import os

class Report(object):
    @staticmethod
    def generate(result_path, url, extension, success, failed_tasks, skip, aborted_at = -1):
        try:
            log_file_path = os.path.join(result_path, "download.log")
            print("\nDownloaded files saved in %s"%(result_path))
            with open(log_file_path, "a") as f:
                f.write("Report generated at: %s\n\n"%(datetime.now()))
                f.write("Base URL: %s\n"%url)
                f.write("File extension: %s\n"%extension)
                f.write("Total: %d\n"% (success + len(failed_tasks)))
                f.write("Successful: %d\n"%success)
                f.write("Failed: %s\n"%len(failed_tasks))
                if len(failed_tasks):
                    f.write("These indices failed to download: [%s]\n"%(", ".join(str(value) for value in list(failed_tasks))))
                if len(skip):
                    f.write("Skipped indices: [%s]\n"%(", ".join(str(value) for value in skip)))
                if aborted_at != -1:
                    f.write("\nDownload aborted by user on index: %d\n"%aborted_at)
                f.write("-------------------------------------------------\n")
            print("\nLog file: %s"%(log_file_path))
            
        except Exception as e:
            print(e)