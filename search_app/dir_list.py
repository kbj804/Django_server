import base64
import os
import glob
import zipfile

import shutil
from os import rename


# ./server_project/search_app/doc_data
def generate_file_list(path):
    pathList= os.listdir(path)
    print(pathList)
    resultList=[]
    for path in pathList:
        if 'docx' in path:
            resultList.append(path)
    return resultList

#print(generate_file_list('./server_project/search_app/doc_data'))

def export_json_file():
    pass

def mecab_Test():
    from eunjeon import Mecab
    mecab = Mecab()
    print(mecab.morphs('영등포구청역에 있는 맛집 좀 알려주세요.'))


mecab_Test()