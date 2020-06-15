'''
From:
    - https://stackoverflow.com/questions/44328277/how-to-auth-to-google-cloud-using-service-account-in-python
    - https://cloud.google.com/storage/docs/uploading-objects?hl=es#storage-upload-object-python
'''

import base64, traceback, os
from google.cloud import storage
from google.oauth2 import service_account
from pathlib import Path
from datetime import datetime

class temp_helper(object):
    def get_content(self):
        file_data = None
        file_name = str(Path(__file__).resolve().parents[1]) + '/flask/static/cecytec.jpg'
        try:
            with open(file_name, "rb") as file_content:
                file_data = base64.b64encode(file_content.read()).decode('utf-8')
        except Exception as e:
            traceback.print_exc()
        return file_data

class file_helper(object):
    pk_bucket_name = ''

    def __init__(self, bucket_name):
        self.pk_bucket_name = bucket_name

    def add_file(self):
        key_path = str(Path(__file__).resolve().parents[1]) + '/private/secret.json'
        print('Key: ', key_path)
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path
        
        content = temp_helper().get_content()
        try:
            client = storage.Client()
            bucket = client.bucket(self.pk_bucket_name)
            blob = bucket.blob("images/{}.jpg".format(str(datetime.now().timestamp())))
            blob.upload_from_string(base64.b64decode(content), 'image/jpg')
            print("El archivo {} se ha guardado en: {}.".format(blob.name, self.pk_bucket_name.upper()))
        except Exception as e:
            traceback.print_exc()