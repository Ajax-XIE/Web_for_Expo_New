import streamlit as st

def sidebar_chinese():

    st.sidebar.empty()

    with st.sidebar:
        st.title("导航菜单")

        page = st.radio("选择页面",options = ['社团简介','近期活动概览','管理员模式'])

        if page == '社团简介':
            st.switch_page("C:\\Users\\ajax3\\Documents\\GitHub\\Web_for_Expo\\index.py")
        if page == '近期活动概览':
            st.switch_page("C:\\Users\\ajax3\\Documents\\GitHub\\Web_for_Expo\\pages\\PersonalWeb.py")
        if page == '管理员模式':
            st.switch_page("C:\\Users\\ajax3\\Documents\\GitHub\\Web_for_Expo\\pages\\AccessControl.py")