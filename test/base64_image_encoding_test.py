import base64
import os
import glob
import zipfile

import shutil
from os import rename

def generate_img_path_list(path, name):
    img_folder_path = path + name + '/word/media/'
    
    # 해당 경로의 파일명 리스트
    img_name_list = os.listdir(img_folder_path)

    # 경로 + 파일명 으로 각 파일 위치 인덱싱
    img_path_list=[]
    for img_name in img_name_list:
        img_path_list.append(img_folder_path + img_name)
    
    return img_path_list

def find_pngFile_using_zipfile(path):
    # glob 을 사용하면 png만 뽑아낼 수도 있고 아무튼 더 편리하긴함 근데 glob란 단어가 못생김 그래서 안씀
    file_list = glob.glob(path + '*')
    img_list_png = [file for file in file_list if file.endswith(".png")]

    return img_list_png

def generate_binary(img_list):
    # 이미지들의 바이너리 파일을 저장할 리스트 공간
    imgs_binary_list = []

    # 이미지를 base64 인코딩하여 바이너이 형태로 추출
    for img in img_list:
        with open(img, 'rb') as s_img:
            img_b64 = base64.b64encode(s_img.read())
            imgs_binary_list.append(img_b64)
    
    return imgs_binary_list

# docx -> zip 
def transform_docx_to_zip(docx_path, name):
    file_name = name + '{ext}'
    r_name = docx_path + file_name.format(ext='.docx')

    temp_path = docx_path + 'temp.docx'

    shutil.copy(r_name, temp_path)

    rename(temp_path, temp_path.replace('docx','zip'))

    return temp_path

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' + directory)


def unzip(zip_path, name):
    file_name = name + '{ext}'
    zip_file_path_name = zip_path + file_name.format(ext='.zip')

    createFolder(zip_path + name)

    fantasy_zip = zipfile.ZipFile(zip_file_path_name)

    fantasy_zip.extractall(zip_path + name)
    #fantasy_zip.extract('word/media/image1.png',  zip_path + name)
    fantasy_zip.close()



if __name__ == "__main__":
    # 이미지들이 있는 path 경로
    file_path = "./server_project/search_app/doc_data/"
    file_name = "rename_test"

    transform_docx_to_zip(file_path, file_name)
    unzip(file_path, 'temp')

    img_list = generate_img_path_list(file_path, 'temp')

    # 바이너리 리스트는 음... 그냥 나중에 뭐 저장을 하든 어쩌든 해야할듯
    binary_list = generate_binary(img_list)

    '''
    image_64_decode = base64.decodestring(binary_list[0]) 
    image_result = open(file_path + 'image1.gif', 'wb')
    # create a writable image and write the decoding result
    image_result.write(image_64_decode)
    '''

    # 이미지 바이너리 파일을 디코딩해서 사진파일을 추출
    image_64_decode = base64.decodestring(binary_list[0]) 
    with open(file_path + 'image1.png', 'wb') as img:
        img.write(image_64_decode)
    
    os.remove(file_path + 'temp.zip')
    shutil.rmtree(file_path + 'temp')






        






'''
# 바이너리 쓰기
data = [1, 2, 3, 4, 5]
with open("test.bin", "wb") as f:
    f.write(bytes(data))
 
# 바이너리 읽기
with open("test.bin", "rb") as f:
    content = f.read()   # 모두 읽음
    print(type(content)) # bytes class
    for b in content:
        print(b)
'''