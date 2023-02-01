import os
import shutil

source= "C:/Users/ME/Downloads/mydownloads"
to="C:/Users/ME/Downloadsmoveingfolder"

list_of_files = os.listdir(source)
print(list_of_files)

for i in list_of_files:
    name,extention=os.path.splitext(i)
    print(name)
    print(extention)

    