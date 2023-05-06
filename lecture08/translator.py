import urllib.request
import json

client_id = "gpVtiW_B4N7w0T5wwnXY"
client_secret = 'GVIZ8CXVbE'

text = input("번역할 Text를 입력하세요: ")
data = "source=ko&target=en&text=" + text
url = "https://openapi.naver.com/v1/papago/n2mt"

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()

if(rescode == 200):
    response_body = response.read()
    response_body.decode('utf-8')
    data = json.loads(response_body)

    print('번역전:', text)
    print('번역후:', data['message']['result']['translatedText'])
else:
    print("Error Code" + rescode)