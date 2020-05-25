from docx2python import docx2python


def generate_table(doc_body, doc_len):
    # 테이블 처리
    table_list=[]
    
    for i in range(doc_len):
        filed_list=[]
        for k in range(len(doc_body[i])):
            filed_list.append(doc_body[i][k][0])
        table_list.append(filed_list)
    #table_dic = make_table_dic(table_list)

    return table_list


doc_result = docx2python(r"./server_project/search_app/in.docx")

for j in range(1,len(doc_result.body)):
    doc_body = doc_result.body[j]
    doc_len = len(doc_body)

    if doc_len == 1:
            # 문서 스플릿
            pass
    else:
        print('ID = {0}'.format(str(j)))
        # 테이블
        table = generate_table(doc_body, doc_len)
        print(table)


  