import webbrowser

# webbrowser.open("https://www.daum.net")


## 1. 사용자의 입력을 받아 검색하기
# keyword = input('원하는 리그를 입력해 주세요: ')

## 2. 여러 페이지를 한번에 열기
url = 'https://sports.media.daum.net/sports/schedule/'

league = ['epl','bundesliga','primera','seriea','ligue1','eredivisie',
'uefacl','uefacup','eplcup','facup']

for l in league:
    webbrowser.open(url + l)









