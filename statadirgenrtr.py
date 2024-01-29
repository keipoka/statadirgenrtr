''' This is a simple command line application which generates a directory for STATA programs. This helps
people keep their outputs organised in folders and saves them time when generating them each time! '''

import os
import sys

root_path = os.path.dirname(os.path.abspath(sys.argv[0]))

project_folder = input("enter the name of your project folder here: ")

root_path = os.path.join(root_path, project_folder)

folder_names = ['dofiles', 'datafiles', 'logfiles', 'tables', 'graphs', 'documentation']

for items in folder_names:
	path = os.path.join(root_path, items)
	os.makedirs(path, exist_ok=True)

sys.exit()