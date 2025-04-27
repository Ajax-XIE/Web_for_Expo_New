import pandas as pd
import streamlit as st
import sys
mode = ["prod","dev"]
mode = mode[0]

@st.cache_data
def load_data(mode):
    if mode == 'dev':
        sys.path.append('C:\\Users\\ajax3\\Documents\\GitHub\\Web_for_Expo_New\\tools')
        expo_activity_raw = pd.read_excel("C:\\Users\\ajax3\\Documents\\GitHub\\Web_for_Expo_New\\data\\Expo_Plan.xlsx")

    if mode == 'prod':
        expo_url = 'https://github.com/Ajax-XIE/Web_for_Expo_New/raw/main/data/Expo_Plan.xlsx'
        expo_activity_raw = pd.read_excel(expo_url)

    return expo_activity_raw

expo_activity_raw = load_data(mode)

expo_raw = expo_activity_raw[expo_activity_raw['Property']=="Expo"].reset_index().iloc[:,1:]
activity_raw = expo_activity_raw[expo_activity_raw['Property']=="Activity"].reset_index().iloc[:,1:]

expo_title = "### 大型漫展活动规划:  \n"
expo_info = [expo_title]

for i in range(len(expo_raw)):
    expo_activity = expo_raw["Date"][i] + " ----- 【" + expo_raw["Expo"][i] + "】" + expo_raw["Theme"][i] + "（" + expo_raw["Progress"][i] + "）"
    if expo_raw["Progress"][i] == "已完结":
        render_color = "red"
    elif expo_raw["Progress"][i] == "招募中":
        render_color = "green"
    else:
        render_color = "gray"
    expo_activity = ":{}[".format(render_color) + expo_activity + "]" + "  \n"

    expo_info.append(expo_activity)

activity_title = "  \n ### 小型团建活动规划:  \n"
activity_info = [activity_title]

for i in range(len(activity_raw)):
    activity_activity = activity_raw["Date"][i] + " ----- 【" + activity_raw["Expo"][i] + "】" + activity_raw["Theme"][i] + "（" + activity_raw["Progress"][i] + "）"
    if activity_raw["Progress"][i] == "已完结":
        render_color = "red"
    elif activity_raw["Progress"][i] == "招募中":
        render_color = "green"
    else:
        render_color = "gray"
    activity_activity = ":{}[".format(render_color) + activity_activity + "]" + "  \n"

    activity_info.append(activity_activity)

context = ""
for element in expo_info:
    context += element
for element in activity_info:
    context += element


context += "  \n 审核QQ群号：285266320"

st.title("近期活动汇总")

st.markdown(context)

if st.button("刷新数据"):
    st.cache_data.clear()
    expo_activity_raw = load_data(mode)