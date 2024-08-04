import os

# Path to the dataset
data_path = './data/fer2013/'

# Check if the train and test directories exist
train_path = os.path.join(data_path, 'train')
test_path = os.path.join(data_path, 'test')

if os.path.exists(train_path) and os.path.exists(test_path):
    print(f'Train directory found with {len(os.listdir(train_path))} classes.')
    print(f'Test directory found with {len(os.listdir(test_path))} classes.')
else:
    print('Train or Test directories do not exist. Please check the download and extraction process.')
