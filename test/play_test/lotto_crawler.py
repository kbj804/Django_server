import re
import psycopg2

from selenium import webdriver
from bs4 import BeautifulSoup
 
#문자열에서 숫자을 찾아 return
def getNumberFrom(str):
    return int("".join(re.findall("\\d+", str)))
 
coptions = webdriver.ChromeOptions()
coptions.add_argument('headless')
coptions.add_argument('window-size=1920x1080')
coptions.add_argument("disable-gpu")
coptions.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
 
driver = webdriver.Chrome('D:\\chromedriver.exe', options=coptions)
 
# 동행복권url
url = "https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo="
driver.get(url)
html = driver.page_source
 
soup = BeautifulSoup(html, 'html.parser')
 
# 현재회차 lotto 번호
lastLottoNo = getNumberFrom(soup.select("div.win_result > h4 > strong")[0].get_text())
 
# db 접속
conn = psycopg2.connect(host="localhost", user="postgres", password="1234", dbname='postgres')
 
curs = conn.cursor()
 
try :
    # 1회차부터 마지막회차까지 정보 가져오기
    for i in range(1, lastLottoNo+1):
        lottoData=[] # 로또정보
        lottoMoneyDatas = [] # 로또당첨금정보
        lottoWinNumbers = [] # 로또당첨번호정보
     
        driver.get("https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo=%d" % i)
        html = driver.page_source
     
        soup = BeautifulSoup(html, 'html.parser')
     
        lottoNo = getNumberFrom(soup.select("div.win_result > h4 > strong")[0].get_text())
        lottoData.append( lottoNo )
     
        #총판매금액
        totMoney = soup.select("ul.list_text_common > li > strong")[0].get_text()
        nos = soup.select("span.ball_645")
        winNo = ""
        bonus= ""
        idx = 0
     
        for no in nos:
            lottoWinNumber = []
            isBonus = "N"
            if idx == len(nos)-1:
                winNo = no.get_text()
                isBonus = "Y"
            else :
                winNo = no.get_text()
     
            lottoWinNumber.append(lottoNo)
            lottoWinNumber.append(getNumberFrom(winNo))
            lottoWinNumber.append(isBonus)
            lottoWinNumbers.append(lottoWinNumber)       
     
            idx = idx+1          
     
        ranks = soup.select("table.tbl_data > tbody > tr")
        for rank in ranks:
            lottoMoneyData = []
            lottoMoneyData.append( lottoNo )
            lottoMoneyData.append(getNumberFrom(rank.select("td:nth-of-type(1)")[0].get_text())) # 등수
            lottoMoneyData.append(getNumberFrom(rank.select("td:nth-of-type(2)")[0].get_text())) # 등수별 총 당첨금
            lottoMoneyData.append(getNumberFrom(rank.select("td:nth-of-type(3)")[0].get_text())) # 당첨자수
            lottoMoneyData.append(getNumberFrom(rank.select("td:nth-of-type(4)")[0].get_text())) # 개별당첨금액
     
            if(len(rank.select("td")) == 6):
                gameInfo = re.sub("\\s+", "", re.sub("\\n", "^", rank.select("td:nth-of-type(6)")[0].text)) # 당첨유형
                winAuto = 0
                winSemiAuto = 0
                winManual = 0
     
                infos = gameInfo.split("^")
                for info in infos:
                    if info == "":
                        continue
                    elif info.startswith("자동"):
                        winAuto = getNumberFrom(info)
                    elif info.startswith("반자동"):
                        winSemiAuto = getNumberFrom(info)   
                    elif info.startswith("수동"):
                        winManual = getNumberFrom(info)
     
            lottoMoneyDatas.append(lottoMoneyData)
     
        pickDate = getNumberFrom(soup.select("div.win_result > p.desc")[0].get_text())
        lottoData.extend( [getNumberFrom(totMoney), winAuto, winSemiAuto, winManual, pickDate] )
          
        sql = """insert into lotto.lotto ( lotto_no, tot_money, wintp_auto, wintp_semiauto, wintp_manual, pick_date, wdate )
        values (%s, %s, %s, %s, %s, %s, now())"""
        curs.execute(sql, lottoData)
     
        lottoWinNumberSql = """insert into lotto.lotto_win_number ( lotto_no, win_no, is_bonus, wdate)
        values (%s, %s, %s, now())"""
        curs.executemany(lottoWinNumberSql, lottoWinNumbers)
     
        lottoMoneySql = """insert into lotto.lotto_money ( lotto_no, rank, rank_tot_money, win_cnt, money, wdate)
        values (%s, %s, %s, %s, %s, now())"""
        curs.executemany(lottoMoneySql, lottoMoneyDatas)
     
        print("%d회 정보 입력완료\n" % lottoNo)
        if lottoNo % 50 == 0:
            conn.commit()       
 
finally:   
    conn.commit()
    curs.close()
    conn.close()  


