import streamlit as st

st.title("2차시 :나만의 분류 기준으로 동물 이미지를 수집할 수 있을까?")

st.header(":rainbow: 지난 시간 내용 복습")
st.write(":white_circle: 동물 이미지를 보고 동물의 특징을 구분할 수 있었다")
st.write(":white_circle: 컴퓨터는 이미지를 숫자로 이해한다. 컴퓨터는 이미지를 통해 동물의 특징을 인식한다.")
st.write(":sparkles: 동영상을 보면서 지난 시간에 학습한 내용을 복습해보자!")
image_url = "images/image08.jpg"
youtube_url = "https://www.youtube.com/watch?v=_Js2GVyKELk"
st.image(image_url, use_column_width=True)
st.markdown(f"[자료1. 동물의 생김새로 구분하기]({youtube_url})")

st.header("흥미 유발 :video_game: Garbage In, Garbage Out!")
st.write("인공지능이 학습을 잘하려면 어떤 데이터가 필요할까? 게임을 통해 알아보자!")
st.image("images/image09.jpg", use_column_width=True)
garbage_url = "https://studio.code.org/s/oceans/lessons/1/levels/2"
st.markdown(f"[자료1. 동물의 생김새로 구분하기]({garbage_url})")
st.write(":sparkles: 인공지능 학습에는 잘 분류된 데이터가 필요하다.")

st.header(":grey_exclamation: 이번 시간의 목표 ")
st.write(":white_circle: 생김새로 구분할 수 있는 동물을 정하여, 이미지 데이터를 수집한다.")

st.header(":one: 활동1 : 나만의 동물 분류 기준을 적어봅시다!")
st.write(":white_circle: 아래는 여러 조류, 포유류, 파충류 동물들의 사진입니다.")
image2_url = "images/image12.png"
st.image(image2_url, use_column_width=True)
st.write(":white_circle: 다른 종류들과 구별되는 조류만의 특징은 무엇이 있을까요?")
st.write(":white_circle: 다른 종류들과 구별되는 포유류만의 특징은 무엇이 있을까요?")
st.write(":white_circle: 다른 종류들과 구별되는 파충류만의 특징은 무엇이 있을까요?")
st.write(":white_circle: 위에서 생각한 특징들 중 인공지능도 구별해낼 수 있는 특징들은 무엇이 있을까요?") 

st.header(":two: 활동2 : 이미지를 수집하는 방법(캐글 & 구글 크롤링)")
st.write("본격적으로 이미지를 수집하기 전! 어떻게 이미지를 수집할 수 있는지 대표적인 두 가지 방법을 알아봅시다")
st.subheader("캐글을 이용해서 이미지를 수집하는 방법")
st.write("캐글은 인공지능 학습용 데이터가 올라와 있는 사이트입니다. 내가 수집하고 싶은 이미지와 연관된 검색어를 통해 알맞은 이미지를 수집할 수 있습니다. 링크를 들어가 수집하고 싶은 동물 이름을 검색해서 이미지를 수집해봅시다.")
kaggle_url = "https://kaggle.com"
st.image("images/image10.jpg", use_column_width=True)
st.markdown(f"[자료3. 캐글]({kaggle_url})")
st.subheader("구글 크롤링을 이용해서 이미지를 수집하는 방법")
st.write("구글은 엄청난 양의 데이터를 검색할 수 있는 사이트입니다. 구글에 검색을 하면 여러 장의 관련 사진들을 확인할 수 있습니다. 크롤링이란 검색을 하고 사진을 다운로드 받는 과정을 코드를 통해 자동화시켜주는 작업입니다. 선생님이 주신 코드를 통해 키워드 검색으로 이미지를 수집해봅시다. 사용방법이 궁금하다면 선생님에게 물어보거나 아래의 링크 속 동영상을 시청해주세요.")
googlec_url = "https://youtu.be/cqM4gC2RU-k"
st.image("images/image11.jpg", use_column_width=True)
st.markdown(f"[자료3. 캐글]({googlec_url})")

st.header(":three: 활동 3: 도전! 이미지 수집하기")
st.write("활동2를 통해서 이미지를 수집하는 방법을 학습했습니다. 캐글과 구글 크롤링 중 어떤 방법이 마음에 드시나요?? 원하는 방법으로 이미지를 수집하여 :file_folder: 폴더에 정리해봅시다. :exclamation: 활동1에서 정한 분류 기준에 맞게 이미지를 수집하였나요?")
st.write(":open_mouth: 친구들과 수집한 데이터를 비교해봅시다.")
st.write("캐글을 통한 방법과 구글 크롤링을 통한 방법의 장단점은 무엇일까요?.")
st.write("**캐글** :grey_question: 양질의 풍부한 데이터를 수집할 수 있지만 완벽하게 목적에 부합하는 데이터를 찾기 어렵다")
st.write("**구글 크롤링** :grey_question: 키워드 검색을 통해 목적에 부합하는 데이터를 찾기 쉽지만 양질의 풍부한 데이터를 수집하기는 어렵다.")

st.header(":book: 오늘 배운 내용 정리하기")
st.write(":white_circle: 인공지능 학습에서 데이터 수집이 얼마나 중요한지 알 수 있다")  
st.write(":white_circle: 나만의 분류 기준을 만들고 캐글 혹은 구글 크롤링을 통해 동물 이미지를 수집할 수 있다.")  

st.subheader(":question: 다음차시)내가 모은 데이터를 인공지능도 분류할 수 있을까? ")
