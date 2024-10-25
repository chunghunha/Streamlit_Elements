import streamlit as st

st.set_page_config(     # 페이지 설정
    page_title="레이아웃", # 페이지 Tab의 타이틀
    page_icon="⚖️",     # 페이지 Tab의 아이콘
    layout="centered",  # 페이지 레이아웃
    initial_sidebar_state="auto", # 사이드바 초기 상태
)

'# 📊 :blue[사이드바]'

'#### :orange[사이드바: st.sidebar]'
'👈 왼쪽의 사이드바를 확인하세요.'

st.sidebar.write('## 사이드바 텍스트')
st.sidebar.checkbox('체크박스 1')
st.sidebar.checkbox('체크박스 2')
st.sidebar.radio('라디오 버튼', ['radio 1', 'radio 2', 'radio 3'])
st.sidebar.selectbox('셀렉트박스', ['select 1', 'select 2', 'select 3'])

st.divider()  # 👈 구분선

'# 🧑🏻‍🚀 :blue[레이아웃]'
'#### :orange[컬럼: st.columns()]'
col_1, col_2, col_3 = st.columns([1,2,1]) # 컬럼 인스턴스 생성. 1:2:1 비율로 컬럼을 나눔

with col_1:
    st.write('## 1번 컬럼')
    st.checkbox('이것은 1번 컬럼에 속한 체크박스 1')
    st.checkbox('이것은 1번 컬럼에 속한 체크박스 2')

with col_2:
    st.write('## 2번 컬럼')
    st.radio('2번 컬럼의 라디오 버튼', ['radio 1', 'radio 2', 'radio 3'])  # 동일한 라디오 버튼을 생성할 수 없음
    # 사이드바에 이미 라디오 버튼이 생성되어 있기 때문에, 여기서는 라디오 버튼의 내용을 변경해야 오류가 발생하지 않음

col_3.write('## 3번 컬럼')
col_3.selectbox('3번 컬럼의 셀렉트박스', ['select 1', 'select 2', 'select 3'])
# 사이드바에 이미 셀렉트박스가 생성되어 있기 때문에, 여기서는 셀렉트박스의 내용을 변경해야 오류가 발생하지 않음

'#### :orange[탭: st.tabs()]'

# 탭 인스턴스 생성. 3개의 탭을 생성
tab_1, tab_2, tab_3 = st.tabs(['Python', 'R', 'Julia'])  
with tab_1:
    st.write(
        '''
        ```python
        import pandas as pd

        df = pd.DataFrame(
            {'id': [1, 2, 3], 
            'name': ['Alice', 'Bob', 'Charlie'],
            'age': [24, 34, 45]
            }
        )
        ```
        '''
    )

with tab_2:
    st.write(
        '''
        ```r
        df <- data.frame(
            id = c(1, 2, 3),
            name = c('Alice', 'Bob', 'Charlie'),
            age = c(24, 34, 45)
        )
        ```
        '''
    )

tab_3.write(
    '''
    ```julia
    using DataFrames

    df = DataFrame(
        id = [1, 2, 3],
        name = ["Alice", "Bob", "Charlie"],
        age = [24, 34, 45]
    )
    ```
    '''
)

'#### :orange[확장 레이아웃: st.expander()]'
with st.expander('🔍 확장 레이아웃'):
    st.write('이곳은 확장 레이아웃입니다.')
    st.write('확장 레이아웃은 특정 컨텐츠를 숨기거나 보여줄 때 사용됩니다.')
