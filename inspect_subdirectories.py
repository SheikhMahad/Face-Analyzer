import os

train_directory = './data/fer2013/train'
test_directory = './data/fer2013/test'

# Function to list files in a directory
def list_files(directory):
    if os.path.exists(directory):
        files = os.listdir(directory)
        if files:
            print(f'Files in {directory}:')
            for file in files:
                print(file)
        else:
            print(f'No files found in {directory}.')
    else:
        print(f'Directory {directory} does not exist.')

# Inspect train and test directories
print("Inspecting train directory:")
list_files(train_directory)

print("\nInspecting test directory:")
list_files(test_directory)
