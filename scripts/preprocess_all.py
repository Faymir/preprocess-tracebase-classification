import os

path = './tracebase/incomplete/'
for file in os.listdir(path):
    current = os.path.join(path, file)
    if os.path.isdir(current) and file != '..' and file != '.':
        print('python scripts/preprocess_device.py ' + file + ' 0')
        os.system('python scripts/preprocess_device.py ' + file + ' 0')