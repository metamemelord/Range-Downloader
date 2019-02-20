import os

class FileSaver(object):
    def save(self, data, directory):
        print("Saving file...")
        try:
            download_folder = os.path.realpath(os.path.join(os.getcwd(), "Downloads"))
            final_path = os.path.join(download_folder, directory)
            if not os.path.isdir(download_folder):
                os.makedirs(download_folder)
            if not os.path.isdir(final_path):
                os.makedirs(final_path)
            with open(os.path.join(final_path, data.filename), 'wb') as f:
                f.write(data.content)
            return "Saved"
        except ValueError:
            return "Could not save the data"
        except PermissionError:
            return "Operation not permitted by OS"
        except OSError:
            return "Operation not permitted by OS"
        except Exception as e:
            return e