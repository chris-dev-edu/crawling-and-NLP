# Lecture 01 ~ 02 정리

## 01. 크롤링과 크롤러
### 크롤링
- 웹 페이지를 가져와서 데이터를 추출하는 행위
### 크롤러
- 크롤링을 하는 프로그램

## 02. 크롤링을 위한 웹 기본 개념
### HTML
- Hyper Text Markup Language의 약자
- 웹에 표현되는 요소들과 Text들을 Tag 형태로 가지고 있음
- 각 Tag는 Element 라고도 하며, 일반적으로 ClassName 또는 ID를 속성으로 가지고있을 수  있음
### CSS
- Cascading Style Sheets의 약자
- 스타일시트 언어로, 웹에 스타일을 부여하는 역할
### Javascript
- 웹 사이트 내 동적인 요소를 구현하는 언어

## 03. 크롤링을 위한 기본 Package
### Package란?
- 특정 기능을 가진 프로그램
### Selenium
- 웹사이트 테스트를 위한 도구로 , 브라우저 동작을 자동화할 수 있음
### BeautifulSoup4
- HTML에서 원하는 데이터를 가져오기 쉽게 parsing 해주는 도구
### webdriver manager
- Python 환경에서 브라우저 동작을 가능하게 해주는 도구

## 04. 크롤링 패키지 활용하기
### Selemium (with. webdriver manager)
- 웹 드라이버 정의
```python
# selenium에서 webdriver import
from selenium import webdriver

# 크롬 드라이버 사용
driver = webdriver.Chrome()

# 엣지 드라이버 사용
driver = webdriver.Edge()

# 접속할 URL 정의
url = "https://www.naver.com"

# 드라이버를 활용하여 URL에 접속
driver.get(url)

# 드라이버 종료
driver.close()
```
- 웹 드라이버 기능: [lecture01/driver_util.py 확인](https://github.com/chris-dev-edu/crawling-and-NLP/blob/main/lecture01/driver_util.py)
### Selenium으로 특정 element 가져오기
```python
# 필요한 package 기능 import
from selenium import webdriver
from selenium.webdriver.common.by import By

# 엣지 드라이버 정의
driver = webdriver.Edge()

# 접속할 URL 정의
url = "https://www.naver.com"

# 드라이버를 활용하여 URL에 접속
driver.get(url)

# 아래처럼 by, value에 값을 전달하여
# 클래스이름, 아이디, 태그이름 등으로 element를 가져올 수 있음
driver.find_element(by=By.CLASS_NAME, value='클래스 이름')
driver.find_element(by=By.ID, value='아이디 값')
driver.find_element(by=By.TAG_NAME, value='div')

# element는 해당 조건에 만족하는 첫번째 단일 요소를
# elements는 해당 조건에 만족하는 모든 요소를 List형태로 가져오게 됨
element = driver.find_element(by=By.CLASS_NAME, value='클래스 이름')
elements = driver.find_elements(by=By.CLASS_NAME, value='클래스 이름')

# List 형태: [요소1, 요소2, 요소3, ... ] 같은 형태로 N개의 요소를 가지고 있음
# index를 활용하여 List내의 개별 요소를 가져올 수 있으며,
# 요소1은 0번, 요소 N은 n-1번 index에 위치하게 됨
element1 = elements[0]
element5 = elements[4]
```

### BeautifulSoup4 활용하기
```python
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Edge()
url = "https://www.naver.com"
driver.get(url)

# 웹 드라이버를 활용하여 접속한 웹 사이트의 html문서를 그대로 가져옴
html = driver.page_source

# html 문서를 BeautifulSoup에서 Parsing(구문 분석)
soup = BeautifulSoup(html, 'html.parser')

# 클래스명이 'class_name'인 element를 가져옴
soup.select('.class_name')

# 아이디가 'id_value'인 element를 가져옴
soup.select('#id_value')

# 태그명이 'tag_name'인 element를 가져옴
soup.select('tag_name')

# 조건에 맞는 단일 element 가져오기
element = soup.select_one('.class_name')

# 조건에 맞는 다중 element를 List형태로 가져오기
elements = soup.select('.class_name')

# element의 html내 text를 가져옴 (일반적으로 우리가 가져오고싶은 정보는 여기에 담겨있음)
text = element.get_text()
```

## 05. 크롤링에 유용한 Python 기능
### Comment 처리
```python
# Comment는 주석이라고도 한다.
# 주석처리된 line은 코드로 인식하지 않는다.
# 일반적으로 학습, 협업, 유지보수 등을 위해 작성한 코드의 설명이나 사용법 등을 적는다.

# 단일 문장 주석은 앞에 '#'을 붙인다.

"""
다중 문장 주석은
큰 따옴표 3개로 시작한 지점부터
큰 따옴표 3개로 끝낸 지점 사이의
모든 Text를 주석으로 인식한다.
"""
```
### `time` package
```python
import time

# 아무 동작도 하지않고, 2초 대기
time.sleep(2)
```
- 웹 브라우저가 url에 접속하여 우리가 가져오고자하는 html 문서를 모두 Load 하도록 기다릴때 사용
- 우리가 작성한 코드가 의도한대로 동작하는지 단계별 디버깅(테스트)하기 위해 사용
### List
```python
number_list = [1, 2, 4, 8, 16]

# number_list의 0번째 index값 출력: 1
print(number_list[0])

# number_list의 3번째 index값 출력: 8
print(number_list[3])
```
### `For` loop
```python
# i가 0부터 시작하여 5보다 작을 때 까지 for 구문 안의 코드를 반복
for i in range(5):
    print(i)
"""출력 결과
0
1
2
3
4
"""

# word에 my_list 내의 element가 순차적으로 선언된다.
# word 대신 다른 변수 이름을 사용해도 무방하다.
my_list = ['apple', 'banana', 'cherry', 'delicious']
for word in my_list:
    print("word:", word)
"""출력 결과
word: apple
word: banana
word: cherry
word: delicious
"""
```