"""server_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


#url의 설정한 부분까지 잘라내고 남은 문자열 부분의 후속 처리를 위해 search_app의 urls.py와 연결해줍니다.
# 이제 Django는 http://127.0.0.1:8000/로 들어오는 모든 접속 요청을 search_app.urls로 전송해 추가 명령을 찾을 것입니다.
from django.conf.urls import include, url
  
urlpatterns = [  
    #path('admin/', admin.site.urls),  
    path('search_app/', include('search_app.urls')),  # include 함수는 다른 URLconf를 참조할 수 있도록 도와줌
    url(r'^chat/', include('chat.urls')),
    url(r'^admin/', admin.site.urls),
    

]