# coding: UTF-8
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

# アクセスするURL
url = "https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E3%83%86%E3%83%AC%E3%83%93%E3%82%A2%E3%83%8B%E3%83%A1%E4%BD%9C%E5%93%81%E4%B8%80%E8%A6%A7_(2010%E5%B9%B4%E4%BB%A3_%E5%BE%8C%E5%8D%8A)"
# https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E3%83%86%E3%83%AC%E3%83%93%E3%82%A2%E3%83%8B%E3%83%A1%E4%BD%9C%E5%93%81%E4%B8%80%E8%A6%A7_(1970%E5%B9%B4%E4%BB%A3)
# https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E3%83%86%E3%83%AC%E3%83%93%E3%82%A2%E3%83%8B%E3%83%A1%E4%BD%9C%E5%93%81%E4%B8%80%E8%A6%A7_(1980%E5%B9%B4%E4%BB%A3)
# https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E3%83%86%E3%83%AC%E3%83%93%E3%82%A2%E3%83%8B%E3%83%A1%E4%BD%9C%E5%93%81%E4%B8%80%E8%A6%A7_(1990%E5%B9%B4%E4%BB%A3)
# https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E3%83%86%E3%83%AC%E3%83%93%E3%82%A2%E3%83%8B%E3%83%A1%E4%BD%9C%E5%93%81%E4%B8%80%E8%A6%A7_(2000%E5%B9%B4%E4%BB%A3_%E5%89%8D%E5%8D%8A)
# https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E3%83%86%E3%83%AC%E3%83%93%E3%82%A2%E3%83%8B%E3%83%A1%E4%BD%9C%E5%93%81%E4%B8%80%E8%A6%A7_(2000%E5%B9%B4%E4%BB%A3_%E5%BE%8C%E5%8D%8A)
# https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E3%83%86%E3%83%AC%E3%83%93%E3%82%A2%E3%83%8B%E3%83%A1%E4%BD%9C%E5%93%81%E4%B8%80%E8%A6%A7_(2010%E5%B9%B4%E4%BB%A3_%E5%89%8D%E5%8D%8A)
# https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E3%83%86%E3%83%AC%E3%83%93%E3%82%A2%E3%83%8B%E3%83%A1%E4%BD%9C%E5%93%81%E4%B8%80%E8%A6%A7_(2010%E5%B9%B4%E4%BB%A3_%E5%BE%8C%E5%8D%8A)


# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
html = urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

# 取得したいテーブルのclassを指定して取得　今回はwikitable
tables = soup.findAll("table",{"class":"wikitable"})

# 一応コマンドラインにも出力する
print(tables)

# 取得したデータを保管するためのcsvファイルを開ける
csvFile = open("anime_all_2018after.csv", 'at', encoding = 'utf-8')
    
writer = csv.writer(csvFile)

# 
try:
  for table in tables:
      csvRow = []
      for cell in table.findAll(['td']):
          csvRow.append(cell.get_text())
      writer.writerow(csvRow)
finally:
    csvFile.close()





