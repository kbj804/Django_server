# Manual Feature 추출

import pandas as pd 
import re


# 데이터 워드카운트 할까..?
# 아님. 일단 목차랑 Title로 카운팅 할까 



if __name__ == "__main__":
    df = pd.read_excel(r"./server_project/search_app/doc_data/Manual_QnA_Data.xlsx")