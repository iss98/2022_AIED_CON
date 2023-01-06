
import streamlit as st

st.set_page_config(
  page_title = "2022_AIED_CON",
  layout = "wide",
)

st.title("인공지능으로 동물들의 생김새 파악하기")
st.write("**팀원** : 수학교육과 김래영, 송무호, 신인섭, 이준수")
st.write("**대상 학년** : 초등학교 3학년")
st.write("**관련 교과** : 인공지능 기초, 과학")
st.header(":school: 관련 성취기준")
col1, col2 = st.columns(2)

with col1 : 
  st.subheader(":male-scientist: 과학")
  st.write(":pencil2: 여러 가지 동물을 관찰하여 특징에 따라 동물을 분류할 수 있다.")
  st.write(":pencil2: 동물의 생김새와 생활 방식이 환경과 관련되어 있음을 설명할 수 있다.")

with col2 : 
  st.subheader(":female-scientist: 인공지능 기초")
  st.write(":pencil2: 이미지 인식, 컴퓨터 비전의 활용 분야를 탐색하고, 컴퓨터 비전의 한계를 인간의 시각처리와 비교하여 설명한다.")
  st.write(":pencil2: 분류 모델의 개념을 이해하고, 분류 모델이 적용되는 사례를 탐색한다.")
  st.write(":pencil2: 인공지능을 활용하여 해결할 수 있는 문제와 그렇지 않은 문제를 구분한다.")
  st.write(":pencil2: 문제 해결에 필요한 데이터를 선정하고, 핵심 속성을 추출한다.")

st.header(":female-teacher: 수업 구성 의도")
st.write(":pencil2: 나만의 분류 기준을 만들고 기준에 따라 이미지 데이터를 수집하는 과정을 통해, 문제를 선정하고 문제 해결에 필요한 데이터를 수집하는 절차를 체험할 수 있도록 하였다.")
st.write(":pencil2: 다양한 특징을 기준으로 동물을 분류해보고 컴퓨터가 인식할 수 있는 특징과 그렇지 않은 특징을 구분하는 과정을 통해, 컴퓨터의 시각 인식에 대한 기초적인 이해를 돕고 인공지능을 활용하여 해결할 수 있는 문제와 그렇지 않은 문제를 구분할 수 있도록 하고자 하였다.")
st.write(":pencil2: Saliency map 동물을 분류하는 모델의 분류결과 뿐 아니라 모델의 해석가능성을 체험할 수 있게 구성하였다. 나만의 분류 기준과 인공지능의 분류 기준을 비교하여 인공지능의 장단점을 인식할 수 있게 하였고, 인공지능이 절대적인 정답을 주는 것이 아니라 문제 상황에서 활용할 수 있는 도구임을 인식하도고 하고자 하였다.")

st.header(":female-teacher: 지도 상의 유의점")
st.write(":pencil2: 컴퓨터가 인식할 수 있는 특징과 그렇지 않은 특징을 포함하여, 다양한 기준으로 동물을 분류해보도록 지도한다.")
st.write(":pencil2: 동물을 구분하는 여러 특징 중 컴퓨터의 시각 인식 원리를 고려하여 생김새에 대한 특징을 자연스럽게 선택할 수 있도록 지도한다.")
st.write(":pencil2: 데이터를 수집할 때, 저작권을 침해하지 않도록 지도한다")
st.write(":pencil2: 크롤링 기법이나 분류 모델의 원리와 세부 코드는 지도하지 않는다.")
st.write(":pencil2: 인공지능 모델의 결과가 동물 분류의 절대적인 기준은 아님을 인지할 수 있도록 지도한다.")

st.header(":exclamation: 학생들이 모은 데이터로 모델을 학습시키는 방법")
st.write(":one: 아래의 github 페이지에서 :file_folder: contents를 다운로드 받고 개인 구글 드라이브로 옮긴다.")
github_url = "https://github.com/iss98/2022_AIED_CON"
st.markdown(f"[github 링크]({github_url})")
st.write(":two: 학생들이 모은 데이터를 :file_folder:labeleddata 폴더에 넣는다.")
st.write(":three: 차시에 맞는 :page_with_curl: .ipynb파일에 들어가서 제공된 코드를 이용해 모델을 학습시킨다.")
st.write(":four: :file_folder:save폴더에 저장된 모델을 복제한 github repo에 넣어주면 끝!")