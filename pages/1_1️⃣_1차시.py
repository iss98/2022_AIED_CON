import streamlit as st
import numpy as np
from PIL import Image
import torch
import torchvision.transforms as transforms

st.title("1차시 : 생김새를 동물들을 이용하여 분류할 수 있을까?")

st.header("생각해보기 :grey_question: AI 학습에는 잘 분류된 데이터가 필요할까?")
image_url = "images/image01.jpg"
youtube_url = "https://www.youtube.com/watch?v=_Js2GVyKELk"
st.image(image_url, use_column_width=True)
st.markdown(f"[자료1. 동물의 특징으로 분류하기]({youtube_url})")
st.header(":grey_exclamation: 이번 시간의 목표 ")
st.write(":white_circle: 다양한 동물들의 특징을 찾아보고, 컴퓨터가 인식할 수 있는 특징으로 동물들을 분류할 수 있다.")

st.header(":one: 활동 1 : 이미지를 통해 동물들의 특징을 찾아보자")
st.write("아래에는 참새, 곰, 여우, 금붕어, 오리, 돌고래의 이미지가 있다. 두 마리의 동물을 골라서 특징을 비교해보자. 나아가 모든 동물들의 특징을 비교해보자.")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/image02.jpg", use_column_width=True)
    st.image("images/image05.jpg", use_column_width=True)

with col2:
    st.image("images/image03.jpg", use_column_width=True)
    st.image("images/image06.jpg", use_column_width=True)

with col3:
    st.image("images/image04.jpg", use_column_width=True)
    st.image("images/image07.jpg", use_column_width=True)


st.write(f":white_circle: 참새와 금붕어의 특징을 적어보자.")
st.write(f":white_circle: 참새와 금붕어의 공통된 특징을 적어보자.")
st.write(f":white_circle: 참새와 금붕어의 다른 특징을 적어보자.")
st.write(":white_circle: 6마리의 동물들을 분류할 수 있는 특징을 찾아보자.")
st.write(":white_circle: 위에서 생각한 특징들로 동물을 분류해보자.")

st.header(":two: 활동 2 : 컴퓨터가 이미지를 이해하는 방법")
st.write("컴퓨터는 숫자를 통해 이미지를 이해한다. 이때, 픽셀이란 단위를 통해 이미지를 이해하고 각 픽셀은 숫자를 갖는다. \n 숫자가 작아지면 이미지가 어두워지고, 숫자가 커지면 이미지가 밝아진다.")
fac = st.slider("사이드바를 움직여보며 밝기의 변화를 관찰해보자.", min_value = 1 , max_value = 255)
img = Image.open("images/image03.jpg")
img = img.resize((600,600)).convert("RGB")
fade = torch.tensor(1 - np.ones((3,600,600)) * fac)
img_new = transforms.ToPILImage()(fade)
col1, col2 = st.columns(2)
with col1 :
    st.image(img, use_column_width=True)
with col2 :
    blendimage = Image.blend(img, img_new, alpha = 0.8)
    st.image(blendimage, use_column_width=True)

st.header(":three: 활동3 : 컴퓨터가 인식할 수 있는 동물의 특징을 알아보자")
st.write(":white_circle: 컴퓨터가 인식할 수 있는 특징과 인식할 수 없는 특징을 구분해보자.")
st.write(":white_circle: 컴퓨터가 인식할 수 있는 특징의 공통점은 무엇일까?")
if st.button("공통점은?"):
	st.write("동물의 생김새가 아닐까!")
st.write(":white_circle: 활동(1)에서 찾는 특징 중 생김새와 관련된 특징을 찾아보자. 나아가 생김새와 관련된 추가적인 특징을 찾아본다.")  

st.header(":book: 오늘 배운 내용 정리하기")
st.write(":white_circle: 컴퓨터는 이미지를 숫자로 인식한다.")
st.write(":white_circle: 컴퓨터는 동물의 생김새 차이를 인식한다.")  

st.subheader(":question: 다음차시)동물들의 이미지 데이터는 어떻게 수집할 수 있을까? ")
