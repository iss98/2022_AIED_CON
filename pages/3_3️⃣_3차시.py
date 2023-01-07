import torch
from PIL import Image, ImageFilter
from scipy.stats import beta
import torchvision.transforms as transforms
import streamlit as st
import numpy as np
import pandas as pd

from model import AnimalClassifier

st.title("3차시 : 나만의 분류 기준을 인공지능이 학습할 수 있을까?")
st.header(":rainbow: 지난 시간 내용 복습")
st.write("지난 시간에 우리는 인공지능 학습에 잘 분류된 데이터가 필요하다는 것을 확인했습니다. 이미지를 수집하는 두 가지 방법을 배웠고, 인공지능 학습을 위해 이미지를 수집했습니다.")

st.header(":grey_exclamation: 이번 시간의 목표 ")
st.write(":exclamation: 선생님이 지난 시간에 여러분이 모은 이미지를 학습한 인공지능을 가지고 왔습니다! 우리가 모은 이미지로 학습한 인공지능이 동물들을 잘 분류하는지 동물의 특징을 잘 확인하는지 탐구해봅시다.")
st.write(":white_circle: 분류 기능으로써 인공지능의 유용성을 안다.")
st.write(":white_circle: 동물을 구별할 수 있는 유용한 특징들에 대하여 고민한다.")

model = AnimalClassifier()
model.load_state_dict(torch.load("week3.pt"))
model.eval()

label = {0 : "포유류", 1 : "조류", 2 : "파충류", 3 : "어류"}
transform = transforms.Compose([transforms.PILToTensor()])

st.header(":one: 활동 1 : 이미지 분류기")
st.write("여러 장의 이미지를 가지고 와서 학습한 인공지능이 동물들을 잘 분류하는지 확인해봅시다! 분류하기 쉬운 이미지부터 분류하기 어려운 이미지를 모두 넣어보고 어떤 결과가 나오는지 확인해봅시다.")
file = st.file_uploader('이미지를 올려주세요.', type = ['jpg','png'], key=0)
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
        nout = np.around(output.detach().numpy() * 100)/100
        st.write(pd.DataFrame({"확률" : nout}, index = ["포유류", "조류", "파충류", "어류"]))
        # df = pd.DataFrame([nout[0], nout[1], nout[2], nout[3]], columns = ["포유류", "조류", "파충류", "어류"])
        # st.bar_chart(df)
        st.success(result)

st.header(":two: 활동 2: 설명 가능한 인공지능")
st.write("설명 가능한 인공지능이란 인공지능이 분류를 한 기준을 시각화시켜주는 인공지능입니다. 활동1에서 했던 예시들을 다시 넣어보면서 왜 인공지능이 활동1에서 확인한 결과로 분류했는지 고민해봅시다.")
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
        
        
st.header(":three: 활동 3 : 합성된 이미지에 대한 결과")
st.write("두 동물들의 모습이 합성된 이미지를 입력하면 어떤 결과가 나올까요? 분류 결과 및 그 결과에 대한 인공지능의 근거를 확인해봅시다.")
st.write("이미지의 분류 결과")
file2 = st.file_uploader('이미지를 올려주세요.', type = ['jpg','png'], key = 1)
if file2 is None:
  st.text('이미지를 먼저 올려주세요.')
else : 
  image = Image.open(file2)
  img_resized = image.resize((200,200)).convert("RGB")
col1, col2 = st.columns(2)
with col1 :
    if file2 is not None:        
        st.image(img_resized)

with col2 :
    if file2 is not None:  
        input = transform(img_resized)
        input = input / 255
        input = input.unsqueeze(dim=0)
        output = model(input).squeeze()
        target = torch.argmax(output)
        result = label[target.item()]
        nout = np.around(output.detach().numpy() * 100)/100
        st.write(pd.DataFrame({"확률" : nout}, index = ["포유류", "조류", "파충류", "어류"]))
        # df = pd.DataFrame([nout[0], nout[1], nout[2], nout[3]], columns = ["포유류", "조류", "파충류", "어류"])
        # st.bar_chart(df)
        st.success(result)

st.write("인공지능이 분류를 한 기준에 대한 시각화입니다. 왜 인공지능이 합성된 사진을 위와 같이 분류했는지 고민해봅시다.")
col1, col2 = st.columns(2)
with col1 :
    if file2 is not None:        
        st.image(img_resized)
with col2 : 
    if file2 is not None:
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

st.header(":four: 활동 4: 우리가 만든 인공지능의 장단점을 토의해보자")
st.write(":thumbsup: 분류의 정확도가 높다. 인공지능이 기준을 가지고 분류한다.")
st.write(":thumbsdown: 인공지능이 완벽하지 않고, 인공지능이 세운 기준을 해석하는 것이 쉽지 않다.")
st.write(":question: 우리가 만든 인공지능을 우리의 실생활에서 사용할 수 있을까? 더 좋은 인공지능을 만드려면 데이터 수집 과정에서 어떻게 해야 할까? 동물을 분류하기 위해 다른 기준을 세울 수 있을까?")

st.header(":book: 오늘 배운 내용 정리하기")
st.write(":white_circle: 인공지능을 활용하여 수집된 데이터에 대한 이미지 분류를 수행할 수 있다.")
st.write(":white_circle: 동물을 분류하기 위한 다양한 기준을 생각해낼 수 있다.")  
