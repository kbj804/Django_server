from django.shortcuts import render
import json
# Create your views here.
# MVC 패턴에서 Conroller


# Create your views here.
# 클래스 기반 뷰로 API를 작성할 계획이며 GET Method를 통해 요청을 하면 parameter로 전달된 검색어에 해당하는 검색 결과를 응답하도록 해줍니다.

from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
  
from elasticsearch import Elasticsearch  
  

  
class SearchView(APIView):

    def get(self, request):
        es = Elasticsearch()
        search_word=''
        

        if request.query_params.get('search_title'):
            search_word = request.query_params.get('search_title')
            docs = es.search(index='manual',
                         doc_type='manual_datas',
                         body={
                             "query": {
                                 "multi_match": {
                                     "query": search_word,
                                     "fields": ["title", "main_title","sub_title"]
                                 }
                             }
                         })
            
        elif request.query_params.get('search_content'):
            search_word = request.query_params.get('search_content')
            docs = es.search(index='manual',
                         doc_type='manual_datas',
                         body={
                             "query": {
                                 "multi_match": {
                                     "query": search_word,
                                     #"data_type": "string",
                                     "fields": ["content"]
                                 }
                             }
                         })

        elif request.query_params.get('test_search'):
            search_word = request.query_params.get('test_search')
            docs = es.search(index='manual',
                         doc_type='manual_datas',
                         body={
                             "query": {
                                 "multi_match": {
                                     "query": search_word,
                                     "fields": ["index"]
                                 }
                             }
                         })


        if not search_word:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'search word param is missing'})

    
        # docs = es.search(index='manual',
        #                  doc_type='manual_datas',
        #                  body={
        #                      "query": {
        #                          "multi_match": {
        #                              "query": search_word,
        #                              "fields": ["title", "content"]
        #                          }
        #                      }
        #                  })

        data_list = docs['hits']
        #print(data_list['hits']['source'])

        return Response(data_list)
