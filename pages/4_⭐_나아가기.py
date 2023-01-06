import torch
from PIL import Image
import torchvision.transforms as transforms
import streamlit as st
from skimage import color
import numpy as np

from model import ECCVGenerator

st.title(":star: 나아가기")
st.write("인공지능은 이미지 분류만 할 수 있을까? 인공지능은 이미지 속 객체 인식, 흑백 이미지 색칠하기 등 여러가지 일을 할 수 있다. \n 우리가 모은 데이터를 바탕으로 만든 이미지 색칠 모델을 체험해보자!")
st.header(":one: 이미지 색칠 모델")

model = ECCVGenerator()
model.load_state_dict(torch.load("colorization.pt"))
model.eval()

file = st.file_uploader('이미지를 올려주세요', type = ['jpg','png'])

transform = transforms.Compose([transforms.PILToTensor()])
if file is not None:
    image = Image.open(file)
    img_resized = image.resize((256,256)).convert("RGB")

col1, col2 = st.columns(2)

with col1 :
    if file is not None:        
        st.image(img_resized)

with col2 :
    if file is not None:
        color_image = np.asarray(img_resized)
        image_lab = color.rgb2lab(color_image)
        input = image_lab[:,:,0]
        input = np.expand_dims(input, axis=-1)
        input = input.transpose((2,0,1))
        input = torch.tensor(input, dtype = torch.float32).unsqueeze(dim = 0)
        output = model(input)
        input = input.detach().cpu()
        output = output.detach().cpu()
        out_img = torch.cat((input,output),dim=1).squeeze().numpy()
        output = out_img.transpose((1,2,0))
        image_rgb = color.lab2rgb(output)
        img_new = torch.tensor(image_rgb.transpose((2,0,1)))
        img_new = transforms.ToPILImage()(img_new)
        st.image(img_new)    

st.header(":robot_face: 앞으로 인공지능은 얼마나 더 발전할까요??")