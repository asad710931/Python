import os

file_path=os.path.abspath(__file__)
BASE_DIR=os.path.dirname(file_path)
#Full_dir=os.path.dirname(BASE_DIR)
myfiles = os.path.join(BASE_DIR,"files","mytext.txt")
text=""
with open(myfiles,mode='r') as f:
    text=f.read()
print(text.format(name='maria'))
