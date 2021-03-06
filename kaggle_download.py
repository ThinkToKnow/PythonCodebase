import requests
import getpass


def download_and_unzip_data():
    username = input("Enter Kaggle username: ")
    pwd = getpass.getpass("Enter Kaggle password: ")

    # The direct link to the Kaggle data set
    data_urls = [
                 'https://www.kaggle.com/c/dogs-vs-cats/download/sampleSubmission.csv',
                 'https://www.kaggle.com/c/dogs-vs-cats/download/test1.zip',
                 'https://www.kaggle.com/c/dogs-vs-cats/download/train.zip',
                 ]

    for data_url in data_urls:
        print('Download %s' % data_url)
        # The local path where the data set is saved.
        local_filename = data_url.split('/')[-1]

        # Kaggle Username and Password
        kaggle_info = {'UserName': username, 'Password': pwd}

        # Attempts to download the CSV file. Gets rejected because we are not logged in.
        r = requests.get(data_url)

        # Login to Kaggle and retrieve the data.
        r = requests.post(r.url, data=kaggle_info)

        # Writes the data to a local file one chunk at a time.
        f = open('./Data/' + local_filename, 'w')
        for chunk in r.iter_content(chunk_size=512 * 1024):  # Reads 512KB at a time into memory
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
        f.close()
        print('Done')



if __name__ == '__main__':
    download_and_unzip_data()