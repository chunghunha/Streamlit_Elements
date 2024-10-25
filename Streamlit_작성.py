import streamlit as st

st.set_page_config(     # 페이지 설정
    page_title="Hello", # 페이지 Tab의 타이틀
    page_icon="👋",     # 페이지 Tab의 아이콘
    layout="wide",  # 페이지 레이아웃: centered, wide
    initial_sidebar_state="expanded", # 사이드바 초기 상태: auto, collapsed, expanded
    menu_items={        # 페이지 오른쪽 상부의 메뉴에 추가할 메뉴 항목: Get help, Report a bug, About
        'Get help': 'https://docs.streamlit.io',
        'About': "# 이것은 헤더. \n - 마크다운 문법 지원 \n - [네이버](https://naver.com)"
    }
)

st.write("# Streamlit World에 오신 것을 환영합니다.! 👋")   # st.write()를 이용한 헤더 작성

st.sidebar.success("위의 목록에서 Demo를 선택하시오.")  # 사이드바에 success 메시지 출력

st.markdown(   # st.markdown()을 이용한 본문 작성
    """
    **Streamlit**을 활용하여 _웹 어플리케이션_을 만들어 봅시다.  
    **👈 왼쪽의 사이드바**에서 원하는 데모를 선택하세요.
    
    ### Streamlit에 대하여 더 알고싶으신가요?
    - [홈페이지](https://streamlit.io)
    - [공식문서](https://docs.streamlit.io)
    - [커뮤니티 포럼](https://discuss.streamlit.io)

    ### 더 복잡한 데모를 보고 싶으신가요?
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)


