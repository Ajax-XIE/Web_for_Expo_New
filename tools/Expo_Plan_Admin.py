import pandas as pd
import streamlit as st
import os
import base64
import requests
from openpyxl import load_workbook

# expo_url = 'https://github.com/Ajax-XIE/Web_for_Expo/raw/main/Expo_Plan.xlsx'

# try:
#     expo_activity_change = pd.read_excel(expo_url)
# except:


def add_info(mode):
    if mode == 'dev':
        expo_activity_change = pd.read_excel("C:\\Users\\ajax3\\Documents\\GitHub\\Web_for_Expo\\data\\Expo_Plan.xlsx")

    if mode == 'prod':
        expo_url = 'https://github.com/Ajax-XIE/Web_for_Expo/raw/main/data/Expo_Plan.xlsx'
        expo_activity_change = pd.read_excel(expo_url)

    if "Add" not in st.session_state:
        st.session_state.Add = False

    def switch_add_state():
        st.session_state.Add = True
        st.session_state.Del = False

    if "submitAdd" not in st.session_state:
        st.session_state.submitAdd = False

    def switch_submitAdd():
        st.session_state.submitAdd = True

    if "Del" not in st.session_state:
        st.session_state.Del = False

    def switch_del_state():
        st.session_state.Del = True
        st.session_state.Add = False

    if "submitDel" not in st.session_state:
        st.session_state.submitDel = False

    def switch_submitDel():
        st.session_state.submitDel = True

    add_button, delete_button = st.columns(2)

    with add_button:
        
        st.button("添加活动信息",on_click=switch_add_state)

    if st.session_state.Add:
        
        property = st.selectbox("请选择活动性质:",["大型漫展","小型活动"])
        year = st.selectbox("请选择活动年份:",[2025,2026])
        month = st.selectbox("请选择活动月份:", [1,2,3,4,5,6,7,8,9,10,11,12])
        day = st.text_input("请输入活动具体日（或输入待定）:")
        date = False
        expo = st.text_input("请输入活动展会/地点:")
        theme = st.text_input("请输入活动IP主题:")
        progress = st.selectbox("请选择当前进程:",["已完结","招募中","规划中"])
        area = st.selectbox("请选择招募对象:",["内外","内部"])

        if property and year and month and day and expo and theme and progress and area:
            try:
                int_day = int(day)
                date = str(month) + "月" + str(day) + "日"
            except Exception:
                if day != "待定":
                    st.write("提交日期有误，请重新提交")
                else:
                    date = str(month) + "月"
        
        if property and year and month and day and expo and theme and progress and area and date:
            st.button("确认提交",on_click=switch_submitAdd)
            if st.session_state.submitAdd:
                st.write("提交成功")
            if property == "大型漫展":
                property = "Expo"
            else:
                property = "Activity"

            add_df = pd.DataFrame({
                "Property": [property],
                "Date": [str(date)],
                "Expo": [expo],
                "Theme": [theme],
                "Progress": [progress],
                "Range": [area],
                "Month": [month],
                "Year": [year]
                })
        
        if st.session_state.submitAdd:

            expo_activity_change = pd.concat([expo_activity_change, add_df]).drop_duplicates()
            expo_activity_change = expo_activity_change.sort_values(["Property","Year","Month"],ascending=[False, True, True])

            if mode == 'dev':
                expo_activity_change.to_excel("C:\\Users\\ajax3\\Documents\\GitHub\\Web_for_Expo\\data\\Expo_Plan.xlsx",index=False)
            if mode == 'prod':
                df_to_git(expo_activity_change,expo_url)
                expo_activity_change.to_excel(expo_url,index=False)
        
    with delete_button:

        st.button("删除活动信息",on_click=switch_del_state)

    if st.session_state.Del:
        
        del_info = [expo_activity_change['Date'][i] + expo_activity_change['Expo'][i] for i in range(len(expo_activity_change))]
        date = st.selectbox("请选择要删除的活动日期:",del_info)
        st.button("确认提交",on_click=switch_submitDel)

        if date and st.session_state.submitDel:

            expo_activity_change['ID'] = expo_activity_change.apply(lambda x: x['Date']+x['Expo'], axis=1)
            expo_activity_change = expo_activity_change[expo_activity_change['ID']!=date].reset_index().iloc[:,1:]

            if mode == 'dev':
                expo_activity_change.to_excel("C:\\Users\\ajax3\\Documents\\GitHub\\Web_for_Expo\\data\\Expo_Plan.xlsx",index=False)
            if mode == 'prod':
                expo_activity_change.to_excel(expo_url,index=False)
                df_to_git(expo_activity_change,expo_url)
            st.write("删除成功")

def df_to_git(dataframe, file_path):
    file_path = "data/Expo_Plan.xlsx"
    repo_owner = "Ajax-XIE"
    repo_name = "Web_for_Expo"
    branch = "main"
    token = os.getenv("GITHUB_TOKEN")

    headers = {"Authorization":f"token {token}"}
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}?ref={branch}"
    response = requests.get(api_url, headers=headers)
    file_data = response.json()
    current_sha = file_data["sha"]

    output_path = "temp_modified.xlsx"
    dataframe.to_excel(output_path, index=False, engine="openpyxl")

    # 3. 读取修改后的内容并Base64编码
    with open(output_path, "rb") as f:
        new_content = base64.b64encode(f.read()).decode("utf-8")

    # 4. 通过API推送更新
    payload = {
        "message": "Auto-update raw_data.xlsx",
        "content": new_content,
        "sha": current_sha,  # 必须提供原SHA
        "branch": branch
    }

    update_response = requests.put(api_url, headers=headers, json=payload)
    if update_response.status_code == 200:
        print("✅ Excel文件更新成功！")
    else:
        print(f"❌ 错误: {update_response.json()}")