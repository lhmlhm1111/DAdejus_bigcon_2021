import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://www.weather.go.kr/weather/observation/currentweather.jsp'
res = requests.get(url)
text = res.text
soup = BeautifulSoup(text,'html.parser')

for tr in soup.select('#content_weather > table > tbody > tr'):
    tds = tr.select('td')
    if not tds:
        continue
    city = tds[0].text #지점
    weather_1 = tds[1].text #날씨 (현재일기)
    weather_2 = tds[2].text #날씨 (시정 km)
    weather_3 = tds[3].text #날씨 (운량 1/10)
    weather_4 = tds[4].text #날씨 (중하운량)
    temperature_1 = tds[5].text #기온(℃) (현재 기온)
    temperature_2 = tds[6].text #기온(℃) (이슬점 온도)
    temperature_3 = tds[7].text #기온(℃) (불쾌 지수)
    precipitation_1 = tds[8].text #강수 (일강수 mm)
    precipitation_2 = tds[9].text #강수 (습도 %)
    wind_1 = tds[10].text #바람 (풍향)
    wind_2 = tds[11].text #바람 (풍속 km/h)
    atmospheric_pressure_1 = tds[12].text #기압(hPa) (해면 기압)

    print(city, weather_1, weather_2, weather_3, weather_4, temperature_1, temperature_2, temperature_3,
          precipitation_1, precipitation_2, wind_1, wind_2, atmospheric_pressure_1)
'''
서울 구름많음 20 이상 8 8 26.5 13.5 73 16.5 45 동북동 1.6 1010.0
백령도 맑음 20 이상 2 2 21.1 14.7 68 2.9 67 남남동 5.0 1009.4
인천 구름많음 17.5 8 8 24.2 15.9 72 1.3 60 북서 4.1 1009.8
수원 구름많음 20 이상 8 8 25.6 14.0 72 0.3 49 동남동 3.5 1010.4
동두천   20 이상     23.6 12.8 70 4.3 51 동북동 2.1 1010.8
파주   9.7     24.4 15.5 72 0.1 58 북북동 2.0 1010.5
강화   18.3     23.9 16.6 72 3.0 64 서 1.9 1010.3
양평   20 이상     25.8 10.7 72 0.5 39 동남동 2.3 1010.6
이천   20 이상     23.9 10.8 70 0.7 44 동남동 3.3 1010.9
북춘천 구름조금 20 이상 5 5 22.6 10.0 68 0.1 45 동북동 4.6 1012.1
북강릉 구름많음 19.9 8 8 17.7 12.1 63   70 동남동 2.6 1014.9
울릉도 구름많음 20 이상 7 3 15.9 10.6 60 0.0 71 북동 6.9 1014.0
속초   20 이상     18.0 14.4 64 1.3 80 남동 2.1 1015.0
철원   20 이상     22.5 12.7 69 0.2 54 동북동 4.2 1011.4
대관령   17.7     11.6 10.3 53 0.7 92 동북동 3.3 1014.8
춘천   13.8     22.7 12.0 69 0.0 51 북동 4.6 1012.2
강릉   20 이상     19.0 12.7 65   67 동 3.3 1015.0
동해   20 이상     17.6 13.1 63   75 북동 1.6 1014.8
원주   20 이상     24.2 9.3 70 0.0 39 북북동 3.3 1010.3
영월         22.7 10.4 68   46 북북동 3.4 1010.8
인제   20 이상     19.1 11.1 65 0.5 60 북동 1.5 1013.4
홍천   20 이상     23.7 11.3 70 3.0 46 북동 4.0 1011.5
태백   20 이상     15.7 10.0 60 0.0 69 북동 3.2 1012.5
정선군   20 이상     19.4 8.9 65   51 남남동 3.7 1013.0
서산   20 이상     25.4 12.9 72   46 북동 2.9 1010.0
청주 구름조금 20 이상 3 1 25.5 10.1 71   38 동 3.0 1009.7
대전 맑음 20 이상 0 0 26.3 13.4 73   45 동 4.1 1010.1
충주   20 이상     27.0 10.2 73   35 동 2.0 1010.5
추풍령   20 이상     21.5 9.7 67   47 동 4.6 1010.7
홍성 흐림 20 이상 9 9 25.2 16.3 73   58 북동 1.8 1009.0
제천   20 이상     22.7 10.1 68   45 북동 3.2 1010.2
보은   20 이상     24.3 10.9 70   43 동남동 3.3 1010.4
천안   20 이상     24.1 10.0 70 2.1 41 동 4.0 1009.9
보령   18.1     25.4 18.8 74   67 서남서 1.0 1009.3
부여   19.4     26.3 11.9 72   41 북북동 2.0 1009.4
금산   19.9     24.4 11.0 70   43 동북동 3.1 1009.4
전주 구름많음 20 이상 6 6 25.9 16.9 74   58 북북동 3.3 1008.1
광주 구름많음 20 이상 7 7 26.8 15.1 74   49 북동 1.9 1008.2
목포 구름조금 17.3 5 5 24.8 18.0 73   66 북서 5.9 1009.0
여수 맑음 20 이상 0 0 22.1 16.3 70   70 동남동 4.3 1009.9
흑산도 맑음 19.7 0 0 22.1 19.4 71 0.0 85 남 3.0 1009.6
군산   16.9     25.9 16.9 74   58 서북서 2.6 1008.9
완도   19.1     23.6 15.6 71   61 남동 5.6 1009.3
고창   17.1     25.8 17.7 74   61 북서 6.0 1008.7
순천   13.2     24.2 14.0 71   53 남서 3.6 1008.5
진도(첨찰산)         22.5 15.5 70   65 서남서 3.3 1008.4
부안   20 이상     27.7 14.6 75   45 북 2.9 1008.9
임실   16.8     26.0 12.4 72   43 남남동 1.8 1008.1
정읍   19.4     27.3 16.8 75   53 북북동 3.2 1008.2
남원   20 이상     25.3 11.8 71   43 북북동 4.5 1008.6
장수   19.3     23.5 12.4 70   50 북동 3.7 1008.1
고창군   20 이상     25.9 13.7 73   47 북북동 3.3 1007.9
영광군   20 이상     25.5 15.2 73   53 북 4.7 1008.8
순창군   17.8     27.1 14.4 74   46 동 2.2 1008.4
보성군   20 이상     25.4 14.8 73   52 남남동 3.2 1009.9
강진군   11.9     25.2 16.0 73   57 남남서 4.3 1009.5
장흥   20 이상     25.1 15.6 73   56 남남동 4.0 1008.8
해남   20 이상     24.5 13.9 71   52 남동 3.8 1009.1
고흥   18.9     22.3 15.1 69   64 남남동 3.0 1009.5
광양시   18.2     24.2 14.5 71   55 동북동 3.9 1009.4
진도군   19.2     23.9 15.3 71   59 남남서 2.4 1008.7
제주 구름조금 20 이상 4 4 23.2 15.2 70   61 동 4.7 1009.6
고산         23.2 18.7 72   76 북서 7.0 1008.0
성산   17.3     20.4 15.8 67   75 북동 4.7 1010.2
서귀포   19.5     22.1 18.2 70   79 동북동 5.2 1008.7
안동 구름조금 20 이상 5 5 21.7 10.8 67   50 남동 5.4 1012.1
포항 구름많음 20 이상 8 8 19.4 14.2 66   72 북동 5.1 1013.6
대구 구름많음 20 이상 6 6 21.4 10.8 67   51 동남동 6.1 1011.9
울산 흐림 20 이상 9 9 19.3 13.9 65   71 북북동 3.4 1012.3
창원 구름조금 20 이상 3 3 22.8 13.5 69   56 북동 3.6 1010.2
부산 구름많음 19.6 7 7 21.4 13.3 68   60 북동 3.2 1011.0
울진   19.8     18.1 12.7 64   71 북북동 2.7 1014.8
상주   11.1     25.2 10.6 71   40 동 1.8 1011.2
통영   19.9     24.4 15.5 72   58 남남동 1.8 1010.4
진주   20 이상     24.5 11.0 70   43 동북동 3.3 1010.1
김해시   10.4     21.7 12.5 68   56 남서 1.8 1011.8
북창원   20 이상     23.1 12.6 69   52 동북동 2.9 1010.6
양산시   16.0     21.6 13.9 68   62 동북동 4.4 1012.5
의령군   20 이상     24.8 12.3 71   46 북북동 1.8 1010.3
함양군   20 이상     24.5 13.6 71   51 북동 2.3 1009.7
봉화   20 이상     20.8 9.0 66   47 동남동 2.7 1011.7
영주   20 이상     22.7 9.4 68   43 남동 1.5 1011.2
문경   20 이상     22.6 9.3 68 0.0 43 동남동 3.9 1011.2
청송군   20 이상     17.8 12.0 63 0.0 69 북동 2.4 1013.2
영덕   20 이상     19.5 13.6 66   69 북북동 5.7 1014.0
의성   20 이상     22.6 10.0 68   45 동 4.7 1012.3
구미   20 이상     23.8 12.4 70   49 동북동 2.8 1011.2
영천   18.1     20.6 11.2 66   55 동 3.7 1012.5
경주시   20 이상     19.4 12.8 65   66 북동 5.0 1012.9
거창   20 이상     22.3 12.2 68   53 동북동 1.6 1009.2
합천   20 이상     24.1 9.2 70   39 동북동 4.1 1010.6
밀양   20 이상     23.2 8.8 69   40 북북동 3.1 1011.3
산청   20 이상     23.6 11.9 70   48 동북동 2.7 1009.7
거제   20 이상     22.7 15.7 70   65 동남동 3.9 1010.6
남해   13.2     24.8 15.1 72   55 동 2.4 1009.9
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://www.weather.go.kr/weather/observation/currentweather.jsp'
res = requests.get(url)
text = res.text
soup = BeautifulSoup(text,'html.parser')

l = []
for tr in soup.select('#content_weather > table > tbody > tr'):
    tds = tr.select('td')
    if not tds:
        continue
    city = tds[0].text #지점
    weather_1 = tds[1].text #날씨 (현재일기)
    weather_2 = tds[2].text #날씨 (시정 km)
    weather_3 = tds[3].text #날씨 (운량 1/10)
    weather_4 = tds[4].text #날씨 (중하운량)
    temperature_1 = tds[5].text #기온(℃) (현재 기온)
    temperature_2 = tds[6].text #기온(℃) (이슬점 온도)
    temperature_3 = tds[7].text #기온(℃) (불쾌 지수)
    precipitation_1 = tds[8].text #강수 (일강수 mm)
    precipitation_2 = tds[9].text #강수 (습도 %)
    wind_1 = tds[10].text #바람 (풍향)
    wind_2 = tds[11].text #바람 (풍속 km/h)
    atmospheric_pressure_1 = tds[12].text #기압(hPa) (해면 기압)

    print(city, weather_1, weather_2, weather_3, weather_4, temperature_1, temperature_2, temperature_3,
          precipitation_1, precipitation_2, wind_1, wind_2, atmospheric_pressure_1)
    l.append([city, weather_1, weather_2, weather_3, weather_4, temperature_1, temperature_2, temperature_3,
          precipitation_1, precipitation_2, wind_1, wind_2, atmospheric_pressure_1])
'''
서울 구름많음 20 이상 8 8 26.5 13.5 73 16.5 45 동북동 1.6 1010.0
백령도 맑음 20 이상 2 2 21.1 14.7 68 2.9 67 남남동 5.0 1009.4
인천 구름많음 17.5 8 8 24.2 15.9 72 1.3 60 북서 4.1 1009.8
수원 구름많음 20 이상 8 8 25.6 14.0 72 0.3 49 동남동 3.5 1010.4
동두천   20 이상     23.6 12.8 70 4.3 51 동북동 2.1 1010.8
파주   9.7     24.4 15.5 72 0.1 58 북북동 2.0 1010.5
강화   18.3     23.9 16.6 72 3.0 64 서 1.9 1010.3
양평   20 이상     25.8 10.7 72 0.5 39 동남동 2.3 1010.6
이천   20 이상     23.9 10.8 70 0.7 44 동남동 3.3 1010.9
북춘천 구름조금 20 이상 5 5 22.6 10.0 68 0.1 45 동북동 4.6 1012.1
북강릉 구름많음 19.9 8 8 17.7 12.1 63   70 동남동 2.6 1014.9
울릉도 구름많음 20 이상 7 3 15.9 10.6 60 0.0 71 북동 6.9 1014.0
속초   20 이상     18.0 14.4 64 1.3 80 남동 2.1 1015.0
철원   20 이상     22.5 12.7 69 0.2 54 동북동 4.2 1011.4
대관령   17.7     11.6 10.3 53 0.7 92 동북동 3.3 1014.8
춘천   13.8     22.7 12.0 69 0.0 51 북동 4.6 1012.2
강릉   20 이상     19.0 12.7 65   67 동 3.3 1015.0
동해   20 이상     17.6 13.1 63   75 북동 1.6 1014.8
원주   20 이상     24.2 9.3 70 0.0 39 북북동 3.3 1010.3
영월         22.7 10.4 68   46 북북동 3.4 1010.8
인제   20 이상     19.1 11.1 65 0.5 60 북동 1.5 1013.4
홍천   20 이상     23.7 11.3 70 3.0 46 북동 4.0 1011.5
태백   20 이상     15.7 10.0 60 0.0 69 북동 3.2 1012.5
정선군   20 이상     19.4 8.9 65   51 남남동 3.7 1013.0
서산   20 이상     25.4 12.9 72   46 북동 2.9 1010.0
청주 구름조금 20 이상 3 1 25.5 10.1 71   38 동 3.0 1009.7
대전 맑음 20 이상 0 0 26.3 13.4 73   45 동 4.1 1010.1
충주   20 이상     27.0 10.2 73   35 동 2.0 1010.5
추풍령   20 이상     21.5 9.7 67   47 동 4.6 1010.7
홍성 흐림 20 이상 9 9 25.2 16.3 73   58 북동 1.8 1009.0
제천   20 이상     22.7 10.1 68   45 북동 3.2 1010.2
보은   20 이상     24.3 10.9 70   43 동남동 3.3 1010.4
천안   20 이상     24.1 10.0 70 2.1 41 동 4.0 1009.9
보령   18.1     25.4 18.8 74   67 서남서 1.0 1009.3
부여   19.4     26.3 11.9 72   41 북북동 2.0 1009.4
금산   19.9     24.4 11.0 70   43 동북동 3.1 1009.4
전주 구름많음 20 이상 6 6 25.9 16.9 74   58 북북동 3.3 1008.1
광주 구름많음 20 이상 7 7 26.8 15.1 74   49 북동 1.9 1008.2
목포 구름조금 17.3 5 5 24.8 18.0 73   66 북서 5.9 1009.0
여수 맑음 20 이상 0 0 22.1 16.3 70   70 동남동 4.3 1009.9
흑산도 맑음 19.7 0 0 22.1 19.4 71 0.0 85 남 3.0 1009.6
군산   16.9     25.9 16.9 74   58 서북서 2.6 1008.9
완도   19.1     23.6 15.6 71   61 남동 5.6 1009.3
고창   17.1     25.8 17.7 74   61 북서 6.0 1008.7
순천   13.2     24.2 14.0 71   53 남서 3.6 1008.5
진도(첨찰산)         22.5 15.5 70   65 서남서 3.3 1008.4
부안   20 이상     27.7 14.6 75   45 북 2.9 1008.9
임실   16.8     26.0 12.4 72   43 남남동 1.8 1008.1
정읍   19.4     27.3 16.8 75   53 북북동 3.2 1008.2
남원   20 이상     25.3 11.8 71   43 북북동 4.5 1008.6
장수   19.3     23.5 12.4 70   50 북동 3.7 1008.1
고창군   20 이상     25.9 13.7 73   47 북북동 3.3 1007.9
영광군   20 이상     25.5 15.2 73   53 북 4.7 1008.8
순창군   17.8     27.1 14.4 74   46 동 2.2 1008.4
보성군   20 이상     25.4 14.8 73   52 남남동 3.2 1009.9
강진군   11.9     25.2 16.0 73   57 남남서 4.3 1009.5
장흥   20 이상     25.1 15.6 73   56 남남동 4.0 1008.8
해남   20 이상     24.5 13.9 71   52 남동 3.8 1009.1
고흥   18.9     22.3 15.1 69   64 남남동 3.0 1009.5
광양시   18.2     24.2 14.5 71   55 동북동 3.9 1009.4
진도군   19.2     23.9 15.3 71   59 남남서 2.4 1008.7
제주 구름조금 20 이상 4 4 23.2 15.2 70   61 동 4.7 1009.6
고산         23.2 18.7 72   76 북서 7.0 1008.0
성산   17.3     20.4 15.8 67   75 북동 4.7 1010.2
서귀포   19.5     22.1 18.2 70   79 동북동 5.2 1008.7
안동 구름조금 20 이상 5 5 21.7 10.8 67   50 남동 5.4 1012.1
포항 구름많음 20 이상 8 8 19.4 14.2 66   72 북동 5.1 1013.6
대구 구름많음 20 이상 6 6 21.4 10.8 67   51 동남동 6.1 1011.9
울산 흐림 20 이상 9 9 19.3 13.9 65   71 북북동 3.4 1012.3
창원 구름조금 20 이상 3 3 22.8 13.5 69   56 북동 3.6 1010.2
부산 구름많음 19.6 7 7 21.4 13.3 68   60 북동 3.2 1011.0
울진   19.8     18.1 12.7 64   71 북북동 2.7 1014.8
상주   11.1     25.2 10.6 71   40 동 1.8 1011.2
통영   19.9     24.4 15.5 72   58 남남동 1.8 1010.4
진주   20 이상     24.5 11.0 70   43 동북동 3.3 1010.1
김해시   10.4     21.7 12.5 68   56 남서 1.8 1011.8
북창원   20 이상     23.1 12.6 69   52 동북동 2.9 1010.6
양산시   16.0     21.6 13.9 68   62 동북동 4.4 1012.5
의령군   20 이상     24.8 12.3 71   46 북북동 1.8 1010.3
함양군   20 이상     24.5 13.6 71   51 북동 2.3 1009.7
봉화   20 이상     20.8 9.0 66   47 동남동 2.7 1011.7
영주   20 이상     22.7 9.4 68   43 남동 1.5 1011.2
문경   20 이상     22.6 9.3 68 0.0 43 동남동 3.9 1011.2
청송군   20 이상     17.8 12.0 63 0.0 69 북동 2.4 1013.2
영덕   20 이상     19.5 13.6 66   69 북북동 5.7 1014.0
의성   20 이상     22.6 10.0 68   45 동 4.7 1012.3
구미   20 이상     23.8 12.4 70   49 동북동 2.8 1011.2
영천   18.1     20.6 11.2 66   55 동 3.7 1012.5
경주시   20 이상     19.4 12.8 65   66 북동 5.0 1012.9
거창   20 이상     22.3 12.2 68   53 동북동 1.6 1009.2
합천   20 이상     24.1 9.2 70   39 동북동 4.1 1010.6
밀양   20 이상     23.2 8.8 69   40 북북동 3.1 1011.3
산청   20 이상     23.6 11.9 70   48 동북동 2.7 1009.7
거제   20 이상     22.7 15.7 70   65 동남동 3.9 1010.6
남해   13.2     24.8 15.1 72   55 동 2.4 1009.9
'''

df = pd.DataFrame(l, columns=['city', 'weather_1', 'weather_2', 'weather_3', 'weather_4', 'temperature_1', 'temperature_2', 'temperature_3',
           'precipitation_1', 'precipitation_2', 'wind_1', 'wind_2', 'atmospheric_pressure_1'])
df.to_csv('weather.csv', index=False)
