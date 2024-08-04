import os

def inspect_directory(path):
    print(f'Files in {path}:')
    for file_name in os.listdir(path):
        print(file_name)

if __name__ == '__main__':
    inspect_directory('./data/fer2013')
