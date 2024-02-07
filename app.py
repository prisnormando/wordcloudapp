import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


st.title('Simple Streamlit App')

st.markdown("""
This app performs Word Cloud
* **Need to cantact: ** [1msdigital.com](https://app.1msdigital.com/contact-us/).
""")

st.set_option('deprecation.showPyplotGlobalUse', False)
#file_bytes = st.file_uploader("Upload a file", type="csv")

#if file_bytes is not None:
st.sidebar.header("Select Link")
links = ["https://www.paho.org/pt/noticias/6-2-2024-eliminacao-da-tuberculose-brasil-recebe-37a-reuniao-do-conselho-da-stop-tb",
        "https://www.paho.org/pt/noticias/19-12-2023-opas-governo-pernambuco-e-ministerio-da-saude-do-brasil-reforcam-parceria-para",
        "https://www.paho.org/pt/noticias/12-12-2023-opas-e-ebserh-firmam-parceria-para-fortalecer-integracao-entre-hospitais",
        "https://seaportai.com/covid-19/https://www.paho.org/pt/noticias/7-12-2023-inca-ministerio-da-saude-opas-sociedades-cientificas-e-ongs-do-brasil-reforcam",
        "https://www.paho.org/pt/noticias/1-2-2024-carga-global-cancer-aumenta-em-meio-crescente-necessidade-servicos"]
URL = st.sidebar.selectbox('Link', links)
st.sidebar.header("Select No.of words you want to display")
words = st.sidebar.selectbox("No.of Words", range(10,1000,10))
if URL is not None:
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('div', attrs = {'id':'main-content'})
    text = table.text
    cleaned_text = re.sub('\t', "", text)
    cleaned_texts = re.split('\n', cleaned_text)
    cleaned_textss = "".join(cleaned_texts)
    #st.write(cleaned_textss)
    st.write("Word Cloud Plot")
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(background_color="white", max_words=words,
                          stopwords=stopwords).generate(cleaned_textss)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    st.pyplot()



