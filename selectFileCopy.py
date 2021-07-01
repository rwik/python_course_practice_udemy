import os
from os import path
import shutil

src = "/home/rwik/Desktop/src"
dst = "/home/rwik/Desktop/dest"
my_file = open("/home/rwik/Desktop/src/inp.txt", "r")
content_list= my_file.read().splitlines()
print(content_list)
files = [i for i in content_list if path.isfile(path.join(src, i))]
for f in files:
    shutil.copy(path.join(src, f), dst)
