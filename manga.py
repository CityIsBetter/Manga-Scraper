from settings import *
from request import *
from stringHelpers import *


def download_chp(seriesName, chpNum):
    current_pg = INITAL_PAGE
    download_path = get_download_path(seriesName, chpNum)

    if not_released_yet(seriesName, chpNum):
        print(NOT_RELEASED_MSG)
        return None
    while True:
        pg_url = get_url(seriesName, chpNum, current_pg)
        request = send_request(pg_url)

        if request.status_code == 404:
            print(DOESNT_EXIST)
            global isThere
            isThere = 0
            break

        download_img(pg_url, download_path, current_pg)

        current_pg += 1

manga = input("Enter Manga name:")
while True:
    c = int(input("Enter do you want to\n1. Download entire manga \n2. Download range of chapters(ex: 2-21) \n3. Download single chapter \nEnter your choice:"))
    if c == 1:
        chp = 1
        while isThere != 0:
            download_chp(manga, chp)
            chp += 1
        break
    elif c == 2:
        start, end = input("Enter multiple values: ").split("-")
        for i in range(int(start), int(end)+1):
            download_chp(manga, i)
        break
    elif c == 3:
        chp = input("Enter chapter number:")
        download_chp(manga, chp)

        break
    else:
        print("Enter valid choice")