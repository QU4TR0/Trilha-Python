import requests
import streamlit as st

BASE_URL = "https://api.github.com"

def user(username):
    url = f"{BASE_URL}/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        return print(response.json())
    else:
        return None


def ui():
    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">', unsafe_allow_html=True)

    st.title('Consulta Github')


ui()