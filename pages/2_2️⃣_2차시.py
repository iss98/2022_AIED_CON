import streamlit as st

st.title("2차시 :나만의 분류 기준으로 동물 이미지 데이터를 수집할 수 있을까?")

st.header(":rainbow: 지난 시간에? 생김새로 동물을 구분할 수 있다")
image_url = "images/image08.jpg"
youtube_url = "https://www.youtube.com/watch?v=_Js2GVyKELk"
st.image(image_url, use_column_width=True)
st.markdown(f"[자료1. 동물의 생김새로 구분하기]({youtube_url})")

st.header(":video_game: Garbage In, Garbage Out!")
st.write("AI 학습에는 잘 분류된 데이터가 필요하다")
st.image("images/image09.jpg", use_column_width=True)
garbage_url = "https://studio.code.org/s/oceans/lessons/1/levels/2"
st.markdown(f"[자료1. 동물의 생김새로 구분하기]({garbage_url})")

st.header(":grey_exclamation: 이번 시간의 목표 ")
st.write(":white_circle: 생김새로 구분할 수 있는 동물을 정하여, 그 이미지 데이터를 모을 수 있다.")

st.header(":one: 나만의 동물 분류 기준을 적어봅시다!")
st.write(":white_circle: 내가 정한 동물들")
st.write(":white_circle: 왜 이 동물들로 정했나요")
st.write(":white_circle: 이 동물들은 어떻게 분류할 수 있나요?")
st.write(":white_circle: 인공지능도 이 동물을 구분할 수 있을지 생각해봅시다.") 

st.header(":two: 이미지데이터를 몹는 방법(Kaggle & 구글 크롤링)")
st.subheader("캐글을 이용해서 데이터를 몹는 방법")
kaggle_url = "https://kaggle.com"
st.image("images/image10.jpg", use_column_width=True)
st.markdown(f"[자료3. 캐글]({kaggle_url})")
st.subheader("구글 크롤링을 이용하여 몹는방법")
st.write("검색할 키워드를 골라서 크롤링을 해보자! \n 크롤링할때 사용가능한 코드는 선생님이 주실 예정!")
code = '''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


#아래의 세 개의 변수를 바꿔주면서 셀을 반복해서 돌리면 데이터를 수집할 수 있다.
#keyword : 구글에 검색할 keyword
#path : 이미지를 저장할 폴더명(mammal, reptile, bird, fish)
#max_num : 저장할 이미지의 개수
#count : image를 덮어씌우지 않게 지금까지 저장한 count로 계속 수정해주면서 저장장

keyword = "개구리"
path = "reptile"
max_num = 20
count = 1

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', options=options)
# 로컬 환경에서는 위의 코드를 주석처리하고 아래의 코드를 사용
# 로컬 환경에서 활용하면 크롤링을 시각적으로 확인할 수 있음
# driver = webdriver.Chrome('chromedriver')
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element(By.NAME, "q")
elem.send_keys(keyword)
elem.send_keys(Keys.RETURN)

images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
#최대 개수만큼만 이미지 뽑기. 최대 개수보다 이미지 개수가 적은 경우 이미지 개수만큼 추출
if len(images) > max_num :
    images = images[:max_num]
    
for image in images:
#찾은 이미지들 저장하기, 저작권 문제로 이미지 저장이 안되는 경우 그냥 넘기기기
    try : 
        image.click()
        time.sleep(3)
        imageURL = driver.find_element(By.CSS_SELECTOR, ".n3VNCb.KAlRDb").get_attribute("src")
        urllib.request.urlretrieve(imageURL, "labeleddata/"+path+"/"+str(count)+".jpg")
        count +=1
    except:
          pass
'''
st.code(code, language="python")

st.header(":three: 도전! 이미지 데이터 모으기")
st.write("원하는 방법으로 이미지 데이터를 수집하여 :file_folder: 폴더별로 정리한다.")

st.header(":book: 정리하기")
st.write(":white_circle: 나만의 분류 기준을 만들고 동물 이미지 데이터를 수집할 수 있다.")
st.write(":white_circle: 친구들과 수집한 데이터를 비교해봅시다.")  

st.subheader(":question: 다음차시)내가 모은 데이터를 인공지능도 분류할 수 있을까? ")