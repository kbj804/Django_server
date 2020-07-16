import base64
import os
import glob
import zipfile

import shutil
from os import rename
from search_app_configs import PathConfig

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


if __name__ == "__main__":
    path = PathConfig()
    manual_list = generate_file_list(path.MANUAL_PATH)

    for file_name in manual_list:
        print(path.MANUAL_PATH + file_name)