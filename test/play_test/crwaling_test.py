from bs4 import BeautifulSoup
import requests

req = requests.get("http://" + 'naver.com' )
html = req.text

# 이렇게 하면 html 변수에 'naver.com'사이트에 대한 모든 HTML 정보가 들어오고
soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
# html 을 다루기 쉽도록 soup변수에 bs4를 넣어서 텍스트 데이터를 정규화를 하던 마음대로 다루시면 됩니다.

urls = soup.find_all('a', href=True)
print(urls)

# 이렇게 하면 urls 변수에 네이버 사이트에 있는 url들이 리스트 형태로 저장됩니다.