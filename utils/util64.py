

import base64
from pathlib import Path
import sys

for arg in sys.argv:
    path = Path(str(arg))
    if path.exists() and path.is_file():
        with open(path.absolute(), 'rb') as source_file:
            print('Codificando: '.format(path.name))
            encoded = base64.b64encode(source_file.read())
            print('Gudardando')
            text_file = open("{}.txt".format(source_file.name), "w")
            text_file.write(encoded.decode('utf-8'))
            text_file.close()
            print('Guardado en: {}'.format(text_file.name))
    else:
        print('El archivo indicado no existe o está vacío.')
