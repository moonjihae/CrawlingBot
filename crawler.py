from selenium import webdriver
import time
from send_messages import send_message_to_slack
import config

def crawling(id, pw):
    options = webdriver.ChromeOptions()
    # 새 화면창 없이 크롤링 실행
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('disable-gpu')
    driver = webdriver.Chrome("chromedriver.exe", chrome_options=options)

    driver.get(
        "https://logins.daum.net/accounts/loginform.do?status=-401&url=http%3A%2F%2Fm.cafe.daum.net%2F_myAlimis%2Fnewarticle%3Fnull")

    driver.find_element_by_css_selector(".login_account >a").click()

    time.sleep(2)
    # 로그인
    daum_id = driver.find_element_by_class_name("tf_g.tf_email")
    daum_id.clear()
    daum_id.send_keys(id)

    daum_pw = driver.find_element_by_id("id_password_3")
    daum_pw.clear()
    daum_pw.send_keys(pw)

    driver.find_element_by_class_name("btn_g.btn_confirm.submit").click()
    time.sleep(3)

    while True:
        f = open("latest_num.txt", "r+")
        latest_num = f.read()
        driver.get("https://m.cafe.daum.net/_myAlimis/newarticle")
        driver.find_element_by_xpath("""//*[@id="daumHead"]/nav/ul/li[4]/a[1]""").click()
        post_num = driver.find_element_by_id("alim_count").text
        if latest_num != post_num:
            url = driver.find_element_by_css_selector(
                "#myNewsList > li.my-news__item.my-news__item--start > a").get_attribute('href')
            driver.find_element_by_css_selector("#myNewsList > li.my-news__item.my-news__item--start > a").click()
            title = driver.find_element_by_class_name("tit_subject").text
            message = {"text": "<" + url + "|" + title + ">"}
            f.seek(0)
            f.write(post_num)
            f.close()
            # 메세지 전송
            send_message_to_slack(message)

        # 30초마다 크롤링 진행
        time.sleep(30)


if __name__ == "__main__":
    crawling(config.id,config.pw )  # 유저의 id,pw 입력
