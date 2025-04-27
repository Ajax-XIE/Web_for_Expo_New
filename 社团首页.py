import streamlit as st
import sys

mode = ["prod","dev"]
mode = mode[0]

if mode == 'dev':
    sys.path.append('C:\\Users\\ajax3\\Documents\\GitHub\\Web_for_Expo\\tools')
if mode == 'prod':
    sys.path.append('https://github.com/Ajax-XIE/Web_for_Expo/raw/main/tools')
