import os
import subprocess


ascii_art = """

███╗   ███╗███████╗██████╗ ███╗   ██╗    ███████╗ ██████╗██████╗ ██╗██████╗ ████████╗
████╗ ████║██╔════╝██╔══██╗████╗  ██║    ██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝
██╔████╔██║█████╗  ██████╔╝██╔██╗ ██║    ███████╗██║     ██████╔╝██║██████╔╝   ██║   
██║╚██╔╝██║██╔══╝  ██╔══██╗██║╚██╗██║    ╚════██║██║     ██╔══██╗██║██╔═══╝    ██║   
██║ ╚═╝ ██║███████╗██║  ██║██║ ╚████║    ███████║╚██████╗██║  ██║██║██║        ██║   
╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   
                                                                                     
"""
                                                  
print(ascii_art)                                                 
# Get the folder name and location from user
folder_name = input("Enter the folder name: ")
folder_location = input("Enter the folder location: ")

# Create the main folder
os.makedirs(os.path.join(folder_location, folder_name))

# Change the working directory to the main folder
os.chdir(os.path.join(folder_location, folder_name))

print("##Creating client and server folders ...")  
# Create client and server folders
os.makedirs('client')
os.makedirs('server')

print("##Changing working directory to server...")  

# Change the working directory to server folder
os.chdir('server')

print("## Running npm install...")  

# Initialize npm and install express
subprocess.call(['C:\\Program Files\\nodejs\\npm.cmd', 'init', '-y'])
subprocess.call(['C:\\Program Files\\nodejs\\npm.cmd', 'install', 'express'])

# Get packages that user wants to install
packages = input("Enter the packages you want to install separated by space: ").split()
for package in packages:
    subprocess.call(['C:\\Program Files\\nodejs\\npm.cmd', 'install', package])

# Get MongoDB URL from user
mongodb_url = input("Enter the MongoDB URL: ")

# Write the MongoDB URL to a .env file in server folder
with open('.env', 'w') as f:
    f.write('MONGODB_URL=' + mongodb_url)

print("## Creating boilerplate code...")  

# Write the boilerplate code for index.js
index_js = """const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Hello World');
});

const port = process.env.PORT || 5000;
app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
"""

with open('index.js', 'w') as f:
    f.write(index_js)

server_directories = ['routes','common','config','middleware','models']

# create other folders
for directories in server_directories:
    os.makedirs(directories)


git_ignore = """node_modules
.env
 """

with open('.gitignore', 'w') as f:
    f.write('node_modules')




# Change the working directory to client folder
os.chdir('..')
os.chdir('client')


subprocess.call(['C:\\Program Files\\nodejs\\npx.cmd', 'create-react-app', '.','--no-git'])

os.chdir('..')

git_ignore1 = """client/node_modules
client/node_modules
server/node_modules
 """
with open('.gitignore', 'w') as f:
    f.write(git_ignore1)


print("## Initializing repository...")  

# init git repo
subprocess.call(['C:\Program Files\Git\cmd\git.exe', 'init'])

print("#### Successfully created ####")  
