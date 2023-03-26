import pandas as pd
import numpy as np
from konlpy.tag import Okt
from tqdm import tqdm
from keras.preprocessing.text import Tokenizer

# 데이터를 data에 저장한다.
data = pd.read_csv('ratings_test.csv')

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

# 형태소 분석기 KoNLP의 Okt 활용
okt = Okt()
print(okt.morphs('와 이런 것도 영화라고 차라리 뮤직비디오를 만드는 게 나을 뻔', stem=True))

# stopwords = 불용어
stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']

# 형태소별 토큰화를 진행하고, 불용어를 제거하여 X_train 리스트에 추가
X_train = []
for sentence in tqdm(data['review']):
    tokenized_sentence = okt.morphs(sentence, stem=True) # 토큰화
    stopwords_removed_sentence = [word for word in tokenized_sentence if not word in stopwords] # 불용어 제거
    X_train.append(stopwords_removed_sentence)

# 토크나이저 사용
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_train)
print(tokenizer.word_index)

threshold = 3
total_cnt = len(tokenizer.word_index) # 단어의 수
rare_cnt = 0 # 등장 빈도수가 threshold보다 작은 단어의 개수를 카운트
total_freq = 0 # 훈련 데이터의 전체 단어 빈도수 총 합
rare_freq = 0 # 등장 빈도수가 threshold보다 작은 단어의 등장 빈도수의 총 합

# 단어와 빈도수의 쌍(pair)을 key와 value로 받는다.
for key, value in tokenizer.word_counts.items():
    total_freq = total_freq + value

    # 단어의 등장 빈도수가 threshold보다 작으면
    if(value < threshold):
        rare_cnt = rare_cnt + 1
        rare_freq = rare_freq + value

print('단어 집합(vocabulary)의 크기 :', total_cnt)
print('등장 빈도가 %s번 이하인 희귀 단어의 수: %s' %(threshold - 1, rare_cnt))
print("단어 집합에서 희귀 단어의 비율:", (rare_cnt / total_cnt)*100)
print("전체 등장 빈도에서 희귀 단어 등장 빈도 비율:", (rare_freq / total_freq)*100)

vocab_size = total_cnt - rare_cnt + 1
print('단어 집합의 크기 :', vocab_size)

tokenizer = Tokenizer(vocab_size)
tokenizer.fit_on_texts(X_train)
X_train = tokenizer.texts_to_sequences(X_train)

print(X_train[:3])
y_train = np.array(data['label'])