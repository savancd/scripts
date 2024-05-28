#
#
# Creating folder structure
#
#

# Importing modules
import os
from functools import partial

# Asking user input to enter the name of the directory that
#  will be created
directory = input("Enter the name of root folder: ")

# Asking user for input where to save the project
# and to create directory folder
parent_dir = input("Enter the path to create directory: ")

# Concatenate the previous two user inputs
path = os.path.join(parent_dir, directory)

# Making the path to the directory created
os.mkdir(path)
# Printing succesfull confirmation 
print("Directory '% s' created" % directory)

# List of subfolders created inside main directory
list = (
	"documents",
	"documents/personal",
	"documents/photos",
	"documents/notes",

	"documents/work",
	"documents/work/projects",
	"documents/work/reports",
	"documents/work/meeting_notes",
	"documents/work/references",
	
	"learning",
	"learning/linux",
	"learning/coding",
	"learning/coding/python",
	"learning/coding/c++",

	"downloads",
	"downloads/documents",
	"download/images",
	"download/software",

	"projects",
	"projects/personal_projects",
	"projects/github",

	"code",
	"code/python",
	"code/c++",
)


# Taking the current path to the directory
current_folder = path

concat_root_path = partial(os.path.join, current_folder)
make_directory = partial(os.makedirs,  exist_ok=True)

for path_items in map(concat_root_path, list):
	make_directory(path_items)
