import base64, traceback
from pathlib import Path

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