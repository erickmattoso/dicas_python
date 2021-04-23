# # list files on directory
# importing os module
import os

# Get the list of all files and directories in the root directory
path = os.getcwd()#"/"
dir_list = os.listdir(path)

print("Files and directories in '", path, "':")

# print the list
(dir_list)
"""
Files and directories in ' c:\Users\emattoso\projetos\pytricks\scripts\os_system_py ':
['os_system_py.ipynb']
"""



# # current directory
import os
# Get the current working directory (CWD)
cwd = os.getcwd()
# Print the current working directory (CWD)
print("Current working directory:", cwd)
"""Current working directory: c:\Users\emattoso\projetos\pytricks\scripts\os_system_py"""



# # create folder
# importing os module
import os

# Get the current working directory (CWD)
cwd = os.getcwd()

# Print the current working directory (CWD)
print("Current working directory:", cwd)

# Directory
directory = "GeeksforGeeks"

# Parent Directory path
parent_dir = cwd

# Path
path = os.path.join(parent_dir, directory)

# Create the directory 'GeeksForGeeks' in '/home / User / Documents'
os.mkdir(path)
print("Directory '% s' created" % directory)
"""
Current working directory: c:\Users\emattoso\projetos\pytricks\scripts\os_system_py
Directory 'GeeksforGeeks' created
"""



# # delete folder

# importing os module
import os

# Directory name
directory = "GeeksforGeeks"

# Parent Directory
parent_dir = cwd

# Path
path = os.path.join(parent_dir, directory)

# Remove the Directory
# "Geeks"
os.rmdir(path)




# # Join paths
# importing os module
import os

# File name
file = "utils.py"

# File location
location = os.getcwd()

# Path
path = os.path.join(location, file)

# os.remove(path)
print(path)
"""c:\Users\emattoso\projetos\pytricks\scripts\os_system_py\utils.py"""

# # rename files

print("Original: ",[i for i in os.listdir(os.getcwd()) if i.startswith("utils")])

import os
print("Original: ",[i for i in os.listdir(os.getcwd()) if i.startswith("utils")])

os.rename("utils.py",'utils1.py')
print("rename 1: ",[i for i in os.listdir(os.getcwd()) if i.startswith("utils")])

os.rename("utils1.py",'utils2.py')
print("rename 2: ",[i for i in os.listdir(os.getcwd()) if i.startswith("utils")])

os.rename("utils2.py",'utils.py')
print("rename 3: ",[i for i in os.listdir(os.getcwd()) if i.startswith("utils")])


