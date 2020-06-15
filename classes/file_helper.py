from google.cloud import storage
import base64, traceback
from pathlib import Path
from tempfile import TemporaryFile

class temp_helper(object):
    def get_content(self):
        file_data = None
        file_name = str(Path(__file__).resolve().parents[1]) + '/static/cecytec.jpg'
        try:
            print('File: ', file_name)
            with open(file_name, "rb") as file_content:
                print('Archivo leido')
                file_data = base64.b64encode(file_content.read()).decode('utf-8')
        except Exception as e:
            traceback.print_exc()
        return file_data

class file_helper(object):
    pk_bucket_name = ''

    def __init__(self, bucket_name):
        self.pk_bucket_name = bucket_name

    def add_file(self):
        client = storage.Client()
        bucket = client.bucket(self.pk_bucket_name)
        content = temp_helper().get_content()
        temp = TemporaryFile()
        try:
            data = base64.b64decode(content)
            temp.write(data)
            temp.seek(0)
            print('Dir: ', temp.name)
        except Exception as e:
            traceback.print_exc()

fh = file_helper('files-example')
fh.add_file()