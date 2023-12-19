from settings import *

def dashes(seriesName):
    return "_".join(seriesName.split(" ")).lower()

def add_zeros(pgNum):
    digits = len(pgNum)
    zeros = "0" * (EST_MAX_DIGITS - digits)
    return zeros + pgNum

def get_url(seriesName, chpNum, pgNum = 1):
    return PROVIDER + dashes(seriesName) + "/" + dashes(seriesName) + "_" + str(chpNum) + "/" +  dashes(seriesName) + "_" + str(chpNum) + "_" + str(pgNum) #https://images.mangafreak.net/mangas/jujutsu_kaisen/jujutsu_kaisen_245/jujutsu_kaisen_245_2.jpg

def get_download_path(seriesName, chpNum):
    return LOCAL_PATH + seriesName + "\\" + str(chpNum) + "\\"   
