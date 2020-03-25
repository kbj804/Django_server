import base64
import os
import glob

def generate_img_path(path):
    # 해당 경로의 파일명 리스트
    img_name_list = os.listdir(path)

    # 경로 + 파일명 으로 각 파일 위치 인덱싱
    img_path_list=[]
    for img_name in img_name_list:
        img_list.append(path + img_name)
    
    return img_path_list
    
def generate_binary(img_list):
    # 이미지들의 바이너리 파일을 저장할 리스트 공간
    imgs_binary_list = []

    # 이미지를 base64 인코딩하여 바이너이 형태로 추출
    for img in img_list:
        print(img)
        with open(img, 'rb') as s_img:
            img_b64 = base64.b64encode(s_img.read())
            imgs_binary_list.append(img_b64)
    
    return imgs_binary_list


# 이미지들이 있는 path 경로
path = "./server_project/search_app/doc_data/iXVDR_Manual_양식/word/media/*"

# glob 을 사용하면 png만 뽑아낼 수도 있고 아무튼 더 편리하긴함 근데 glob란 단어가 못생김
file_list = glob.glob(path)
print(file_list)
file_list_py = [file for file in file_list if file.endswith(".png")]
print(file_list_py)