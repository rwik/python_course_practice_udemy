#!/usr/bin/env python3

import os

path = "/home/rwik/Desktop/vault"
folders = []

for param1 in os.scandir(path):
	try:
	    print(param1)
	    os.chdir(param1)
	    os.system("git status")
	    os.system("cd ..")
	    os.chdir(path)
	except NotADirectoryError:
	        pass
	except:
	        pass

