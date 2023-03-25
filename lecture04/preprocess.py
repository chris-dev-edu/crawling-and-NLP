import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import urllib.request
from konlpy.tag import Okt
from tqdm import tqdm
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# 해당 링크에서 트레이닝용 ratings_train.txt 데이터와 테스트용 ratings_test.txt 데이터를 다운로드한다.
urllib.request.urlretrieve("https://raw.githubusercontent.com/chris-dev-edu/crawling-and-NLP/main/lecture04/ratings_train.txt", filename="ratings_train.txt")
urllib.request.urlretrieve("https://raw.githubusercontent.com/chris-dev-edu/crawling-and-NLP/main/lecture04/ratings_test.txt", filename="ratings_test.txt")

# 각 데이터를 train_data, test_data에 저장한다.
train_data = pd.read_table('ratings_train.txt')
test_data = pd.read_table('ratings_test.txt')

# 훈련용 데이터의 리뷰 개수와 상위 5개를 출력
print('훈련용 리뷰 개수 :', len(train_data))
print(train_data[:5])

# 테스트용 데이터의 리뷰 개수와 상위 5개를 출력
print('테스트용 리뷰 개수 :', len(test_data))
print(test_data[:5])

# review 열의 중복 제거
train_data.drop_duplicates(subset=['review'], inplace=True)
print('중복 제거 후 훈련용 리뷰 개수 :', len(train_data))
