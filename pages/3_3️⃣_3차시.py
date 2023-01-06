import torch
from PIL import Image, ImageFilter
from scipy.stats import beta
import torchvision.transforms as transforms
import streamlit as st
import numpy as np
import pandas as pd

from model import AnimalClassifier

st.title("3차시 : 나만의 분류 기준을 인공지능이 학습할 수 있을까?")
st.header(":rainbow: 지난 시간에? 목적에 맞는 데이터를 수집했다!")

st.header(":grey_exclamation: 이번 시간의 목표 ")
st.write(":white_circle: 분류 기능으로써 인공지능의 유용성을 안다.")
st.write(":white_circle: 동물을 구별할 수 있는 유용한 특징들에 대하여 고민한다.")

model = AnimalClassifier()
model.load_state_dict(torch.load("week3.pt"))
model.eval()

label = {0 : "포유류", 1 : "새", 2 : "파충류", 3 : "어류"}
transform = transforms.Compose([transforms.PILToTensor()])

st.header(":one: 이미지 분류기")
file = st.file_uploader('이미지를 올려주세요', type = ['jpg','png'])
if file is None:
  st.text('이미지를 먼저 올려주세요.')
else : 
  image = Image.open(file)
  img_resized = image.resize((200,200)).convert("RGB")
col1, col2 = st.columns(2)
with col1 :
    if file is not None:        
        st.image(img_resized)

with col2 :
    if file is not None:  
        input = transform(img_resized)
        input = input / 255
        input = input.unsqueeze(dim=0)
        output = model(input).squeeze()
        target = torch.argmax(output)
        result = label[target.item()]
        nout = output.detach().numpy()
        st.write(pd.DataFrame({"확률" : nout}, index = ["포유류", "새", "파충류", "어류"]))
        # df = pd.DataFrame([nout[0], nout[1], nout[2], nout[3]], columns = ["포유류", "새", "파충류", "어류"])
        # st.bar_chart(df)
        st.success(result)

st.header(":two: 설명 가능한 인공지능")
col1, col2 = st.columns(2)
with col1 :
    if file is not None:        
        st.image(img_resized)
with col2 : 
    if file is not None:
        input = transform(img_resized)
        input = input / 255
        input = input.clone().detach().requires_grad_(True)
        input2 = input.unsqueeze(dim=0)
        output = model(input2)
        output2 = output.squeeze()
        target = torch.argmax(output2)
        output2[target.item()].backward()
        grads = torch.abs(input.grad)
        ones = torch.ones((1,200,200))
        Rgrad = grads[0,:,:]/torch.max(grads[0,:,:])
        Ggrad = grads[1,:,:]/torch.max(grads[1,:,:])
        Bgrad = grads[2,:,:]/torch.max(grads[2,:,:])
        ones = torch.ones((1,200,200))
        Rgrad = ones - Rgrad.unsqueeze(dim = 0)
        Ggrad = ones - Ggrad.unsqueeze(dim = 0)
        Bgrad = ones - Bgrad.unsqueeze(dim = 0)
        RGBgrad = torch.cat([Rgrad, Ggrad, Bgrad], dim = 0)
        RGBimage = transforms.ToPILImage()(RGBgrad)
        RGBimage = RGBimage.convert("L")
        hmap = RGBimage.filter(ImageFilter.GaussianBlur(7))
        img = np.array(img_resized)/255
        hmap = np.array(hmap)/255
        hmap = (hmap - hmap.min())/(hmap.max()-hmap.min()) # 0에서 1 사이로 조정
        hmap = beta.cdf(hmap, 2, 5) # heatmap의 구분이 잘 되도록 0과 1쪽으로 조정
        hmap.resize(200,200,1)
        img_new = 1 - (1-img)*(1-hmap)
        img_new = torch.tensor(img_new.transpose((2,0,1)))
        img_new = transforms.ToPILImage()(img_new)
        st.image(img_new)

st.header(":three: 인공지능 분류모델이 갖는 장단점을 지금까지 학습한 내용을 바탕으로 얘기해보자")

st.header(":book: 정리하기")
st.write(":white_circle: 인공지능을 활용하여 수집된 데이터에 대한 이미지 분류를 수행할 수 있다.")
st.write(":white_circle: 동물을 분류하기 위한 다양한 기준을 생각해낼 수 있다.")  