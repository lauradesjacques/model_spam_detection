import streamlit as st

st.set_page_config(layout="wide")

st.title('Solution pour détecter les SPAMS')

with st.form("my_form"):
        expediteur = st.text_input("E-mail de l'expéditeur", max_chars=250)
        objet = st.text_input("Objet", max_chars=300)
        message = st.text_input("Message", max_chars=1000)

formulaire = {
    expediteur: expediteur,
    objet: objet,
    message: message,
}
