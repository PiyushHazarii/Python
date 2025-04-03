import os

# Specify the directory path
directory_path = '/'

# Get the list of all files and directories in the specified directory
entries = os.listdir(directory_path)

# Print the list
print(f"Contents of '{directory_path}':")
for entry in entries:
    print(entry)
