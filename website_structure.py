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
	"app",
	"app/console",
	"app/exceptions",

	"app/https",
	"app/https/controlers",
	"app/https/middleware",

	"app/models",
	"app/providers",

	"bootstrap",
	"bootstrap/cache",

	"config",
	"database",
	"database/factories",
	"database/migrations",
	"database/seeders",

	"public",
	"public/js",
	"public/img",
	"public/CSS",

	"resources",
	"resources/css",
	"resources/js",
	"resources/lang",
	"resources/views",

	"routes",
	"routes/channels.php",
	"routes/console.php",
	"routes/web.php",

	"storage",
	"storage/storage",
	"storage/app",
	"storage/app/public",
	"storage/framework",
	"storage/logs",
)


# Taking the current path to the directory
current_folder = path

concat_root_path = partial(os.path.join, current_folder)
make_directory = partial(os.makedirs,  exist_ok=True)

for path_items in map(concat_root_path, list):
	make_directory(path_items)
