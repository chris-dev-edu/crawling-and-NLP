import pandas
import numpy as np

# 데이터를 data에 저장한다.
data = pandas.read_csv('ratings_train.csv')

# 훈련용 데이터의 리뷰 개수와 상위 5개를 출력
print('훈련용 리뷰 개수 :', len(data))
print(data[:5])

# review 열의 중복 제거
data.drop_duplicates(subset=['review'], inplace=True)
print('중복 제거 후 훈련용 리뷰 개수 :', len(data))

# label값 분포 확인
print(data.groupby('label').size().reset_index(name='count'))

# Null값을 가진 데이터가 있는지 확인
print(data.isnull().values.any())

# Null값을 가진 데이터의 수 확인
print(data.isnull().sum())

# Null값을 가진 데이터의 위치 확인
print(data.loc[data.review.isnull()])

# Null값을 가진 데이터 삭제(drop)
data = data.dropna(how='any')
print('Null 제거 후 훈련용 리뷰 개수 :', len(data))

# 한글과 공백을 제외하고 모두 제거 (정규표현식 활용)
print(data[:5])
data['review'] = data['review'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")
print(data[:5])

# 공백으로 이루어진 review를 Null로 변경
data['review'] = data['review'].str.replace('^ +', "")
data['review'].replace('', np.nan, inplace=True)

# 변경 후 상위 5개 데이터 및 Null 값의 개수 확인
print(data[:5])
print(data.isnull().sum())

# Null값을 가진 데이터 제거 후 개수 출력
data = data.dropna(how='any')
print('전처리 후 훈련용 리뷰 개수 :', len(data))
