## 크롤링 슬랙 알림봇

python으로 제작한 크롤링 슬랙 알림봇 

### 사용 스택
|분야|스택|
|------|---|
|언어|Python|
|스케쥴러|Crontab|
|배포|Docker|
|배포|AWS lightsail|
|크롤링|Selenium|

### 프로젝트 설명
* 30초 마다 새 글을 크롤링합니다.
* 크롤링후 새로운 글이 존재한다면 슬랙 메세지를 전송합니다.
* aws lightsail 환경에서 Selenium을 사용하기위해 Dockerfiie을 통해 Chrome앱 설치합니다.
  ``` docker
  RUN apt-get install -yqq unzip
  RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
  RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin
  ``` 

