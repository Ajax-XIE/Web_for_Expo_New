import pandas as pd
import streamlit as st

mode = ["prod","dev"]
mode = mode[0]

if mode == 'dev':
    import sys
    sys.path.append('C:\\Users\\ajax3\\Documents\\GitHub\\Web_for_Expo\\tools')
if mode == 'prod':
    from tools import Expo_Plan_Admin from tools

def control_dashboard(mode):

    if 'login' not in st.session_state:
        st.session_state.login = False

    def admin_mode():
        st.session_state.login = True

    if 'clicked' not in st.session_state:
        st.session_state.clicked = False

    def clicked():
        st.session_state.clicked = True

    # st.button("管理员模式",on_click=clicked)
    st.session_state.clicked = True
    
    if st.session_state.clicked:
        pwd = st.text_input("请输入管理员密码:")
        if pwd:
            if pwd == "破产重组碎碎冰":
                admin_mode()
                st.write("管理员登陆成功")
            else:
                st.write("验证码校验失败")
                st.session_state.login = False

    if st.session_state.clicked and st.session_state.login:
        Expo_Plan_Admin.add_info(mode)

control_dashboard(mode)
