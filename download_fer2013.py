import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi


def download_and_extract_dataset():
    api = KaggleApi()
    api.authenticate()

    dataset_url = 'https://www.kaggle.com/datasets/msambare/fer2013'
    dataset_name = 'msambare/fer2013'
    local_path = './data/fer2013.zip'

    if not os.path.exists('./data'):
        os.makedirs('./data')

    print(f'Dataset URL: {dataset_url}')

    api.dataset_download_files(dataset_name, path='./data', unzip=False)

    print(f'Dataset downloaded to {local_path}')

    with zipfile.ZipFile(local_path, 'r') as zip_ref:
        zip_ref.extractall('./data/fer2013')

    print('Dataset downloaded and extracted successfully.')


if __name__ == '__main__':
    download_and_extract_dataset()
