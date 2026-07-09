인크루트에서 python 검색

import requests
from bs4 import BeautifulSoup

keyword = "python"
url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}"

r = requests.get(url)
#print(r.text)

soup = BeautifulSoup(r.text, "html.parser")
result = soup.find_all("li", class_="c_col")
print(len(result))



인크루트에서 간호사 검색
import requests
from bs4 import BeautifulSoup

keyword = "python"
url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}"

r = requests.get(url)
#print(r.text)

soup = BeautifulSoup(r.text, "html.parser")
lis = soup.find_all("li", class_="c_col")

for li in lis:
    company=li.find("a",class_="cpname").text
    print(company)


경력
import requests
from bs4 import BeautifulSoup

keyword = "python"
url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}"

r = requests.get(url)
#print(r.text)

soup = BeautifulSoup(r.text, "html.parser")
lis = soup.find_all("li", class_="c_col")

for li in lis:
    company=li.find("a",class_="cpname").text
    title=li.find("div",class_="cell_mid").find("div",class_="cl_top").find("a").text
    print(title)


지역
import requests
from bs4 import BeautifulSoup

keyword = "python"
url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}"

r = requests.get(url)
#print(r.text)

soup = BeautifulSoup(r.text, "html.parser")
lis = soup.find_all("li", class_="c_col")

for li in lis:
    company=li.find("a",class_="cpname").text
    title=li.find("div",class_="cell_mid").find("div",class_="cl_top").find("a").text
    location=li.find("div",class_="cl_md").find_all("span")[0].text
    print(location)



해당공고링크
import requests
from bs4 import BeautifulSoup

keyword = "python"
url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}"

r = requests.get(url)
#print(r.text)

soup = BeautifulSoup(r.text, "html.parser")
lis = soup.find_all("li", class_="c_col")


for li in lis:
    company=li.find("a",class_="cpname").text
    title=li.find("div",class_="cell_mid").find("div",class_="cl_top").find("a").text
    location=li.find("div",class_="cl_md").find_all("span")[0].text
    link=li.find("div",class_="cell_mid").find("div",class_="cl_top").find("a").get("href")
    print(link)


app.py
#내 컴퓨터에서만 돌아가는 가상서버열기
#파일 실행하면 주소 출력됨.
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, python!'
#루트 추가. 주소에 /hello 추가하기
@app.route('/hello')
#def hello():
#    return "안녕하세요"

if __name__ == '__main__':
    app.run(debug=True)
#서버 닫기 : 터미널에서crtl+c