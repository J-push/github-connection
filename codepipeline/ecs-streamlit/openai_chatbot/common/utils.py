import os 
import boto3
import streamlit as st

@st.cache_data # 데이터를 caching 처리 
def __set_openai_api_key():
  OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', None)
  
  if not OPENAI_API_KEY:
    ssm = boto3.client('ssm')
    #streamlit 파라미터(aws에서 만든거) name 입력
    parameter = ssm.get_parameter(Name='/TEST/CICD/STREAMLIT/OPENAI_API_KEY', WithDecryption=True)
    os.environ['OPENAI_API_KEY'] = parameter['Parameter']['Value']


def init_chatbot():
  __set_openai_api_key()

  if "messages" not in st.session_state:
    st.session_state.messages = []



