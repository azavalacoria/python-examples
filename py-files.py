
import os
import sys

from datetime import datetime
from pathlib import Path

if len(sys.argv) == 2:
    targetPath = os.path.join(Path.home(), sys.argv[1])
    content = os.listdir(targetPath)
    contentValues = {}
    contentData = {}
    
    for item in content:
        size = '{}'.format(len(item))
        if size not in contentValues:
            contentValues[size] = 1
            contentData[size] = []
        else:
            contentValues[size]+=1
            contentData[size].append(item)
    contentData = dict(sorted(contentData.items()))
    maxLength = int(sorted(contentValues.keys())[-1])
    
    print('Max len in filename is: ', maxLength)
    
    with open('outputs/{}.txt'.format(datetime.now()), 'w') as fp:
        for cd in contentData:
            fp.writelines('Name length: {:03d} of {:03d} - {}\n'.format(len(line), maxLength, str(line).rjust(maxLength)) for line in contentData['{}'.format(cd)])
else:
    print('error ')