import streamlit as st

st.set_page_config(     # 페이지 설정
    page_title="텍스트와 미디어", # 페이지 Tab의 타이틀
    page_icon="🔤",     # 페이지 Tab의 아이콘
    layout="wide",  # 페이지 레이아웃
    initial_sidebar_state="auto", # 사이드바 초기 상태
)

'# 🚗: 일반 텍스트'
st.write('# 마크다운 H1 : st.write()')
st.write('### 마크다운 H3 : st.write()')
st.write('') # 빈 줄 추가

st.title('제목 : st.title()')
st.header('헤더 : st.header()')
st.subheader('서브헤더 : st.subheader()')
st.text('본문 텍스트 : st.text()')
st.write('')

st.markdown('## 마크다운 : st.markdown()')
st.markdown(
    '''
    # 마크다운 헤더1
    - 마크다운 목록1. **굵게** 표시
    - 마크다운 목록2. *기울임* 표시
        - 마크다운 목록2-1
        - 마크다운 목록2-2

    ## 마크다운 헤더2
    - [네이버](https://naver.com)
    - [구글](https://google.com)

    ### 마크다운 헤더3
    일반 텍스트
    '''
)

st.divider()  # 👈 구분선

'# 🚗: 형식이 있는 텍스트'

st.caption('캡션(작고 흐린 글씨로 표현됨) : st.caption()')

st.write('##### 코드 블록: st.code()')
st.code('print("Hello, World!")', language='python')
st.code('print("Hello, World!")', language='python', line_numbers=True)

st.write('##### 코드 블록: Markdown')
st.write(
    '''
    ```python
    print("Hello, World!")
    ```
    '''
)

st.write('##### 코드+결과: st.echo()')
with st.echo():
    # 이 블록의 코드와 결과를 출력
    name = 'Chunghun Ha'
    st.write("Hello, Streamlit!", name)


st.write('##### Latex 수식 작성: st.latex()')
st.latex('\int_a^b f(x)dx')

st.write('##### Latex 수식 작성: Markdown')
st.write('$$\int_a^b f(x)dx$$')

'''# 👑 Magic 적용
1. ordered item
    - 강조: **unordered item**
    - 기울임: *unordered item*
2. ordered item
3. ordered item
'''

'''#### 텍스트 색상 변경
- :red[빨간색 텍스트]
- :blue[파란색 텍스트]
- :green[초록색 텍스트]
- :orange[주황색 텍스트]
- :gray[회색 텍스트]
'''

'# 🎥: 이미지와 동영상'

'#### :orange[이미지: st.image()]'
st.image("./data/python.png", caption="파이썬 로고", width=500)

'#### :orange[오디오: st.audio()]'
st.audio("./data/After_You.mp3", format="audio/mpeg", loop=True)

'#### :orange[동영상: st.video()]'
# 'rb' : 바이너리 모드로 파일 열기
video_file = open("./data/stars.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes)

st.divider()  # 👈 구분선

'# 📚: 콜아웃'

'#### :orange[정보: st.info()]'
st.info(
    icon="ℹ️",
    body='''
    - :red[빨간색 텍스트]
    - :blue[파란색 텍스트]
    - :green[초록색 텍스트]
    - :orange[주황색 텍스트]''')

'#### :orange[경고: st.warning()]'
st.warning('This is a warning message', icon="⚠️")

'#### :orange[에러: st.error()]'
st.error('This is an error message', icon="🚫")

'#### :orange[성공: st.success()]'
st.success('This is a success message', icon="✅")


