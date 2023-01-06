import streamlit as st
import numpy as np
from PIL import Image
import torch
import torchvision.transforms as transforms

st.title("1차시 : 동물들을 생김새를 이용하여 분류할 수 있을까?")

st.header(":grey_question: AI 학습에는 잘 분류된 데이터가 필요할까?")
image_url = "images/image01.jpg"
youtube_url = "https://www.youtube.com/watch?v=_Js2GVyKELk"
st.image(image_url, use_column_width=True)
st.markdown(f"[자료1. 동물의 특징으로 분류하기]({youtube_url})")
st.header(":grey_exclamation: 이번 시간의 목표 ")
st.write(":white_circle: 다양한 동물들의 특징을 찾아보고, 컴퓨터가 인식할 수 있는 특징으로 동물들을 분류할 수 있다.")

st.header(":one: 활동 1")

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

st.write(":white_circle: 각 동물의 특징을 적어보자")
st.write(":white_circle: 동물들을 분류할 수 있는 특징을 찾아보자.")
st.write(":white_circle: 특징으로 동물을 분류해보자.")

st.header(":two: 활동 2")
st.write("컴퓨터가 이미지를 어떻게 숫자로 인식하는지 알아보자")
fac = st.slider("1부터 255사이 숫자를 고르세요", min_value = 1 , max_value = 255)
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
st.write(":white_circle: 컴퓨터는 이미지를 픽셀로 나눠서 인식함을 이해한다.")
st.write(":white_circle: 각 픽셀은 숫자로 표현하여 인식함을 이해한다. ")

st.header(":three: 컴퓨터가 인식할 수 있는 동물의 특징을 알아보자")
st.write(":white_circle: 위의 특징들 중 컴퓨터가 인식할 수 있는 특징과 아닌 특징을 구분해 본다.")
st.write(":white_circle: 컴퓨터가 인식할 수 있는 특징은 생김새와 관련된 특징임을 인식한다.")
st.write(":white_circle: 활동(1)에서 찾는 특징 중 생김새와 관련된 특징을 찾아보고, 생김새와 관련된 추가적인 특징을 찾아본다.")  

st.header(":book: 정리하기")
st.write(":white_circle: 컴퓨터가 이미지를 인식하는 방법을 이해할 수 있다.")
st.write(":white_circle: 컴퓨터가 인식할 수 있는 특징으로 동물을 분류할 수 있다.")  

st.subheader(":question: 다음차시)동물들의 이미지 데이터는 어떻게 수집할 수 있을까? ")