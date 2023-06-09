import streamlit as st
import pandas as pd
import numpy as np
import joblib
# Importing all required modules 
import webbrowser as wb
import requests
from bs4 import BeautifulSoup
import googletrans
from googletrans import Translator
from datetime import datetime

# -- Set page config
apptitle = 'Predict VN30-index crawl data'
st.set_page_config(page_title=apptitle, 
                   layout="wide",
                   page_icon="🧊",
                   initial_sidebar_state="expanded")
#                  page_icon="chart_with_upwards_trend")
# Get the URL from the user using a text input widget
url = st.text_input('Enter a URL')
# st.button('Get')
# Extract the href attribute from the link using requests and BeautifulSoup
if st.button('Get'):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a')
    hrefs = [link.get('href') for link in links]

    # Display the extracted href attributes using a write widget
    st.write('Extracted href attributes:')
    link_list = set(list(hrefs))
    else_list = []
    for href in link_list:
      if ("https://" in href) and ('-' in href):
        else_list.append(href)
    st.write(else_list)  
    title_list = []
    for i in else_list:
      response_2 = requests.get(i)
      soup_2 = BeautifulSoup(response_2.content, 'html.parser')
    # Extract the data you want to display
      title = soup_2.title.string
      title_list.append(title)  
    df = pd.DataFrame(title_list,columns=['Title'],index = [i for i in range(0,len(title_list))])
#     st.write(df)
    
    translator = Translator()
    en_lst = []
    time_lst = []
    
    for j in range(len(df.Title)):
      trans = translator.translate(df.Title.iloc[j], src='vi', dest='en')
      en_lst.append(trans.text)
      
      dt_obj = datetime.fromtimestamp(df.index[j]).strftime('%y - %m - %d')
      time_lst.append(dt_obj)
      
    df_2 = pd.DataFrame(en_lst,columns=['Title'],index = time_lst)
    
    st.write(df_2)


    
response_test = requests.get("https://vnexpress.net/khoi-ngoai-lien-tiep-mua-rong-co-phieu-4579445.html")
soup_test = BeautifulSoup(response_test.content, 'html.parser')
span_element = soup_test.find('date', {'xpath': '/html/body/section[5]/div/div[2]/div[1]/span'})
# Get the text content of the span element
span_text = span_element.text
st.write(span_text)
