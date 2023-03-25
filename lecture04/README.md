# Lecture 04

## package 설치
`before Lecture 04.`
- selenium
- beautifulsoup4
- webdriver-manager
- pandas

`after Lecture 04`
- numpy
- konlpy
- tqdm
- tensorflow
- matplotlib
- keras
- transformers

## NLP 란?
- Natural Language Processing (자연어 처리)의 약자
- Natural Language란 인간이 일상에서 사용하는 언어이다.
- 즉, NLP(자연어처리)란 기계가 자연어를 이해하고 처리할 수 있도록 하는 과정을 말한다.

## NLP 활용 분야
`텍스트 분류(Text Classification)`
- 텍스트가 특정 분류, 카테고리에 속하는 것을 예측하는 기법. 
- ex) 스팸 메일 분류나 뉴스 기사의 내용을 기반으로 연애/정치/사회/문화 중 어떤 카테고리에 속하는지 자동으로 분류해주는 프로그램.

`감성 분석(Sentiment Analysis)`
- 텍스트에 나타나는 감정/기분 등의 주관적 요소를 분석하는 기법. 
- ex) SNS의 글을 분석하여 글쓴이의 감정을 분석하는 것, 영화 및 제품의 리뷰를 분석하는 것 등

`텍스트 요약(Summarization)`
- 텍스트에서 중요한 주제를 추출하여 요약하는 기법. 
- ex) 토픽 모델링(Topic Modeling)

`텍스트 군집화(Clustering)와 유사도 측정`
- 비슷한 유형의 텍스트에 대해 군집화하는 기법. 

`기계 번역(Translation)`
- 구글 번역기나 파파고와 같은 번역기

`대화 시스템 및 자동 질의 응답 시스템`
- 애플의 Siri, 삼성 갤럭시의 빅스비, Chat GPT 등의 챗봇

## NLP 과정
1. 텍스트 전처리(Text Preprocessing)
   - 대/소문자 변경, 특수문자 삭제, 이모티콘 삭제 등의 전처리 작업, 단어(Word) 토큰화 작업, 불용어(Stop word) 제거 작업, 어근 추출(Stemming/Lemmatization) 등의 텍스트 정규화 작업
 
2. 피처 벡터화 (Feature Vectorization)
   - 전처리된 텍스트에서 피처를 추출하고 여기에 벡터 값을 할당

3. 머신러닝 모델링
   - 피처 벡터화된 데이터에 대하여 모델을 수립하고 학습/예측

## 텍스트 전처리
- 라벨링: 준비한 데이터의 각 요소에 특정 기준을 토대로 값을 부여
- 중복 제거: 같은 data를 가진 요소들을 하나만 남기고 삭제
- 특수문자, 이모티콘 등 불필요한 내용 제거
- Null 값을 가진 데이터를 제거 (Null: 값이 존재하지 않는 상태)
- 불용어 제거: 한글의 `[은, 는, 이, 가, ...]` 등의 자체적인 의미가 없는 단어 제거
- 단어 토큰화: 단어를 형태소(의미를 가지는 가장 작은 말의 단위)단위로 나누는 것