from elasticsearch import Elasticsearch
import json

es = Elasticsearch()

with open(r"./server_project/search_app/manual_data.json", encoding='utf-8') as json_file:
    json_data = json.loads(json_file.read())

es.indices.create(
    index='manual',
    #doc_type='manual_datas',
    body={
        "settings": {
            "index": {
                "analysis": {
                    "analyzer": {
                        "my_analyzer": {
                            "type": "custom",
                            "tokenizer": "nori_tokenizer"
                            ,"filter":["lowercase"]
                        }
                    },
                    "normalizer":{
                        "lowercase_normalizer":{
                            "type":"custom",
                            #"char_filter":[],
                            "filter":["lowercase"]
                        }
                    }
                }                
            }
        },
        "mappings": {
            "manual_datas": {
                "properties": {
                    "data_type": {
                        "type": "text"
                    },
                    "main_title": {
                        "type": "text"
                        ,"analyzer": "my_analyzer"
                        #,"normalizer": "lowercase_normalizer"
                    },
                    "sub_title": {
                        "type": "text"
                        ,"analyzer": "my_analyzer"
                        #,"normalizer": "lowercase_normalizer"
                    },
                    "title": {
                        "type": "text"
                        ,"analyzer": "my_analyzer"
                        #,"normalizer": "lowercase_normalizer"
                    },
                    "content": {
                        "type": "text",
                        "analyzer": "my_analyzer"
                        #,"normalizer": "lowercase_normalizer"
                    }
                }
            }
        }
    }
)

body =""
for i in json_data:
    body = body + json.dumps({"index": {"_index": "manual", "_type": "manual_datas"}}) + '\n'
    body = body + json.dumps(i, ensure_ascii=False) + '\n'
print(body)
es.bulk(body)
