import pandas as pd
import streamlit as st

expo_activity_raw = pd.read_excel("Expo_Plan.xlsx")

expo_raw = expo_activity_raw[expo_activity_raw['Property']=="Expo"].reset_index().iloc[:,1:]
activity_raw = expo_activity_raw[expo_activity_raw['Property']=="Activity"].reset_index().iloc[:,1:]

expo_title = "### 大型漫展活动规划:  \n"
expo_info = [expo_title]

for i in range(len(expo_raw)):
    expo_activity = expo_raw["Date"][i] + " ----- 【" + expo_raw["Expo"][i] + "】" + expo_raw["Theme"][i] + "（" + expo_raw["Progress"][i] + "）"
    if expo_raw["Progress"][i] == "已完结":
        rendor_color = "red"
    elif expo_raw["Progress"][i] == "招募中":
        rendor_color = "green"
    else:
        rendor_color = "gray"
    expo_activity = ":{}[".format(rendor_color) + expo_activity + "]" + "  \n"

    expo_info.append(expo_activity)

activity_title = "  \n ### 小型团建活动规划:  \n"
activity_info = [activity_title]

for i in range(len(activity_raw)):
    activity_activity = activity_raw["Date"][i] + " ----- 【" + activity_raw["Expo"][i] + "】" + activity_raw["Theme"][i] + "（" + activity_raw["Progress"][i] + "）"
    if activity_raw["Progress"][i] == "已完结":
        rendor_color = "red"
    elif activity_raw["Progress"][i] == "招募中":
        rendor_color = "green"
    else:
        rendor_color = "gray"
    activity_activity = ":{}[".format(rendor_color) + activity_activity + "]" + "  \n"

    activity_info.append(activity_activity)

context = ""
for element in expo_info:
    context += element
for element in activity_info:
    context += element


context += "  \n 审核QQ群号：285266320"

st.title("近期活动汇总")

st.markdown(context)



