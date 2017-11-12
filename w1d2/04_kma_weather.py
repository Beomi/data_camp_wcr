import requests
from bs4 import BeautifulSoup as bs

req = requests.get('http://www.kma.go.kr/index.jsp')

html = req.text
soup = bs(html, 'lxml')

# 우선 '아이콘 설명'부분까지 가져오고
weather_info_list = soup.select(
    '#subcontainer > div.weather_area_0930.ML22 > dl.region_weather_e'
)

# 빈 dict를 하나 만들어 준 후
now_weather_dict = {}

# enumerate() 내장 함수를 통해 리스트 값 뿐만 아니라
# 리스트의 인덱스를 가져옵니다.
for index, weather in enumerate(weather_info_list):
    # 첫번째 값(0번 index 인 경우)을 버립니다.
    # (continue는 for문의 다음 loop로 넘어가도록 만듭니다.)
    if index == 0:
        continue
    # 우선 정보 앞뒤와 중간의 공백/엔터들을 없애줍니다.
    weather_info = weather.text.replace('\n',' ').strip()
    # 지역과 정보 사이에 스페이스 하나가 있으므로 스페이스를 기준으로 앞뒤로 쪼개줍니다.
    split_by_blank = weather_info.split(' ')
    # 이제 위에서 만들어 준 dict에 값을 넣어줍니다.
    now_weather_dict[split_by_blank[0]] = float(split_by_blank[1])

print(now_weather_dict)

# dict는 아래와 같이 .items()를 이용해 키와 값을 동시에 사용할 수 있습니다.
for key, value in now_weather_dict.items():
    print(key, value)
