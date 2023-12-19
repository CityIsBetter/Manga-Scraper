from settings import *
from stringHelpers import *
import requests
import shutil
import os

def send_request(url, binary=False):
    try:
        request = requests.get(url, stream=binary)
    except:
        print(REQUEST_ERROR)
        exit()

    return request

def not_released_yet(seriesName, chpNum):
    manga_url = get_url(seriesName, chpNum)
    html = send_request(manga_url).text

    return NOT_RELEASED_MSG in html

def download_img(url, download_path, pgNum):
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    img_name = add_zeros(str(pgNum)) + FILE_EXT
    img_path = download_path + img_name

    request = send_request(url, True)

    with open(img_path, 'wb') as file_path:
        request.raw.decode_content = True
        shutil.copyfileobj(request.raw, file_path)

    print(DOWNLOADING_MSG + str(pgNum))
