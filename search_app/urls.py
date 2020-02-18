from django.urls import path
from django.conf.urls import url
from search_app import views
  
urlpatterns = [  
    path('', views.SearchView.as_view()),
   # url(r'^$', views.SearchView.as_view()),

]