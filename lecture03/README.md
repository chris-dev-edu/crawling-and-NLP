# Lecture 03

## `pandas` package 설치
- PyCharm 하단 `Python Packages` 클릭
- pandas 검색 후 우측 `Install package` 클릭

## `pandas` package를 활용하여 크롤링한 데이터를 파일로 저장하기
```python
import pandas
data = ['apple', 'banana', 'grape', 'orange']
data_frame = pandas.DataFrame(data, columns=['fruit'])
data_frame.to_csv('fruit.csv', index=False)
```
- 4개의 과일 이름을 csv 파일로 저장
- 열 이름: `fruit`
- 파일 이름: `fruit.csv` 처럼 확장자 정의 필요
- index: [`True` | `False`] 1번째 열에 인덱스를 넣을지 여부 결정
- 위 코드를 실행시키면 `fruit.csv` 파일이 해당 python 파일과 같은 디렉토리 내에 생성되어있는 것을 확인할 수 있다.
- csv 파일 열기
   - Window: 엑셀 또는 [Extreme CSV 다운로드](https://www.microsoft.com/store/productId/9P160VLCR0ZC)
   - Mac: `Numbers`, `TableTools` 등의 App 활용
```python
import pandas

data = [
    ['apple', 15000],
    ['banana', 12000],
    ['grape', 9000],
    ['orange', 10000]
]

data_frame = pandas.DataFrame(data, columns=['fruit', 'price'])
data_frame.to_csv('fruit-and-price.csv', index=False)
```
- 4개의 과일 이름과 가격을 csv 파일로 저장
- data 내에 [fruit, price] 형태로 2개의 데이터가 저장되어 있기 때문에, columns에도 두 열의 이름을 정의한다.
```python
import pandas

fruits = ['apple', 'banana', 'grape', 'orange']
data_frame = pandas.DataFrame(fruits, columns=['fruits'])
data_frame['price'] = [15000, 12000, 9000, 10000]
data_frame.to_csv('fruit-and-price.csv', index=False)
```
- 위 코드 처럼 한 열의 데이터로 `data_frame`을 정의하고, 추가로 새로운 열과 열 이름을 지정해줄 수 있다.